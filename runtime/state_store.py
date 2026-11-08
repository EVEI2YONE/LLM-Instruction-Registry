"""Local SQLite reference store for durable contexts and artifacts.

Not an authentication, secret store, hosted gateway or deployed agent service.
The caller must enforce project/tenant identity and permission checks.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path


def canonical(payload: dict) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class ConflictError(Exception):
    pass


class StateStore:
    def __init__(self, path: str | Path):
        self.db = sqlite3.connect(str(path))
        self.db.execute("PRAGMA foreign_keys = ON")
        self.db.execute("PRAGMA busy_timeout = 2000")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS contexts (
                namespace TEXT NOT NULL,
                context_id TEXT NOT NULL,
                revision INTEGER NOT NULL,
                payload TEXT NOT NULL,
                sha256 TEXT NOT NULL,
                PRIMARY KEY(namespace, context_id, revision)
            );
            CREATE TABLE IF NOT EXISTS contents (
                sha256 TEXT PRIMARY KEY,
                content BLOB NOT NULL
            );
            CREATE TABLE IF NOT EXISTS artifacts (
                namespace TEXT NOT NULL,
                artifact_id TEXT NOT NULL,
                revision INTEGER NOT NULL,
                owner TEXT NOT NULL,
                metadata TEXT NOT NULL,
                sha256 TEXT NOT NULL,
                PRIMARY KEY(namespace, artifact_id, revision)
            );
            CREATE TABLE IF NOT EXISTS audit (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                namespace TEXT NOT NULL,
                object_id TEXT NOT NULL,
                operation TEXT NOT NULL,
                revision INTEGER NOT NULL
            );
        """)
        self.db.commit()

    def close(self):
        self.db.close()

    @staticmethod
    def scope(namespace: str):
        if not namespace or any(x in namespace for x in ("\n", "\r")):
            raise ValueError("invalid namespace")

    def put_context(self, namespace: str, envelope: dict) -> str:
        self.scope(namespace)
        required = ("context_id", "run_id", "task_id", "revision",
                    "project_revision", "objective", "authoritative_inputs",
                    "artifact_refs", "permissions")
        if any(key not in envelope for key in required):
            raise ValueError("missing context fields")
        payload = canonical(envelope)
        hashval = digest(payload.encode("utf8"))
        with self.db:
            self.db.execute("INSERT INTO contexts VALUES (?,?,?,?,?)",
                            (namespace, envelope["context_id"], envelope["revision"], payload, hashval))
            self.db.execute("INSERT INTO audit(namespace,object_id,operation,revision) VALUES (?,?,?,?)",
                            (namespace, envelope["context_id"], "put-context", envelope["revision"]))
        return hashval

    def get_context(self, namespace: str, context_id: str, revision: int) -> dict:
        self.scope(namespace)
        row = self.db.execute(
            "SELECT payload FROM contexts WHERE namespace=? AND context_id=? AND revision=?",
            (namespace, context_id, revision)).fetchone()
        if row is None:
            raise KeyError("context not visible or absent")
        return json.loads(row[0])

    def put_artifact(self, namespace: str, record: dict, data: bytes, expected_revision: int) -> int:
        self.scope(namespace)
        required = ("artifact_id", "owner", "kind", "storage_ref", "sha256",
                    "status", "visibility", "producer_task_id")
        if any(k not in record for k in required):
            raise ValueError("missing artifact fields")
        if record["sha256"] != digest(data):
            raise ValueError("artifact digest mismatch")
        if record["status"] == "approved" and not record.get("approval_refs"):
            raise ValueError("approved artifact requires approval reference")
        with self.db:
            row = self.db.execute(
                "SELECT revision,owner FROM artifacts WHERE namespace=? AND artifact_id=? ORDER BY revision DESC LIMIT 1",
                (namespace, record["artifact_id"])).fetchone()
            actual = row[0] if row else 0
            if actual != expected_revision:
                raise ConflictError("stale artifact revision")
            if row and row[1] != record["owner"]:
                raise ConflictError("artifact ownership cannot silently change")
            revision = actual + 1
            metadata = dict(record, revision=revision)
            self.db.execute("INSERT OR IGNORE INTO contents VALUES (?,?)", (record["sha256"], data))
            self.db.execute("INSERT INTO artifacts VALUES (?,?,?,?,?,?)",
                            (namespace, record["artifact_id"], revision, record["owner"],
                             canonical(metadata), record["sha256"]))
            self.db.execute("INSERT INTO audit(namespace,object_id,operation,revision) VALUES (?,?,?,?)",
                            (namespace, record["artifact_id"], "put-artifact", revision))
        return revision

    def get_artifact(self, namespace: str, artifact_id: str, revision: int | None = None) -> tuple[dict, bytes]:
        self.scope(namespace)
        q = ("SELECT metadata,sha256 FROM artifacts WHERE namespace=? AND artifact_id=? "
             + ("ORDER BY revision DESC LIMIT 1" if revision is None else "AND revision=?"))
        params = (namespace, artifact_id) if revision is None else (namespace, artifact_id, revision)
        row = self.db.execute(q, params).fetchone()
        if row is None:
            raise KeyError("artifact not visible or absent")
        content = self.db.execute("SELECT content FROM contents WHERE sha256=?", (row[1],)).fetchone()
        if content is None or digest(content[0]) != row[1]:
            raise ValueError("artifact content integrity violation")
        return json.loads(row[0]), content[0]

    def audit_events(self, namespace: str) -> list[tuple]:
        self.scope(namespace)
        return self.db.execute(
            "SELECT object_id,operation,revision FROM audit WHERE namespace=? ORDER BY id",
            (namespace,)).fetchall()
