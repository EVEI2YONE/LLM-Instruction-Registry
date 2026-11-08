"""Single-host SQLite task queue: durable, project-scoped, idempotent and dependency-aware.

This is a local/reference executor queue, not a distributed, hardened hosted service.
"""
from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path

from runtime.state_store import canonical


class TaskConflict(Exception):
    pass


class TaskQueue:
    def __init__(self, db_path: str | Path):
        self.path = str(db_path)
        with self.connect() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS tasks (
                    project TEXT NOT NULL,
                    task_id TEXT NOT NULL,
                    run_id TEXT NOT NULL,
                    idem TEXT NOT NULL,
                    spec TEXT NOT NULL,
                    status TEXT NOT NULL,
                    attempts INTEGER NOT NULL DEFAULT 0,
                    result TEXT,
                    created REAL NOT NULL,
                    updated REAL NOT NULL,
                    PRIMARY KEY(project,task_id),
                    UNIQUE(project,idem)
                );
                CREATE INDEX IF NOT EXISTS task_status ON tasks(project,status);
            """)

    def connect(self):
        conn = sqlite3.connect(self.path, timeout=5)
        conn.execute("PRAGMA busy_timeout=5000")
        return conn

    @staticmethod
    def check_spec(task: dict) -> None:
        fields = ("run_id", "task_id", "package_id", "package_version", "objective",
                  "context_ref", "idempotency_key", "required_capabilities", "permissions", "limits")
        if any(key not in task for key in fields):
            raise ValueError("missing task fields")
        if not isinstance(task["limits"], dict):
            raise ValueError("invalid limits")
        depth = task["limits"].get("max_depth")
        concurrency = task["limits"].get("max_parallel")
        if not isinstance(depth, int) or not (0 <= depth <= 5):
            raise ValueError("max_depth outside safe range")
        if not isinstance(concurrency, int) or not (1 <= concurrency <= 8):
            raise ValueError("max_parallel outside safe range")
        if not isinstance(task.get("dependencies", []), list):
            raise ValueError("invalid dependencies")
        if not all(isinstance(v, list) for v in (task["permissions"], task["required_capabilities"])):
            raise ValueError("invalid permission/capability arrays")

    def submit(self, project: str, task: dict) -> dict:
        if not project:
            raise ValueError("project is required")
        self.check_spec(task)
        if task["task_id"] in task.get("dependencies", []):
            raise ValueError("self dependency")
        now = time.time()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            old = db.execute("SELECT spec,status,result FROM tasks WHERE project=? AND idem=?",
                             (project, task["idempotency_key"])).fetchone()
            if old:
                if old[0] != canonical(task):
                    raise TaskConflict("idempotency key reused with different task")
                return {"task": task, "status": old[1], "result": json.loads(old[2]) if old[2] else None}
            existing = db.execute("SELECT 1 FROM tasks WHERE project=? AND task_id=?",
                                  (project, task["task_id"])).fetchone()
            if existing:
                raise TaskConflict("task ID already exists")
            for dep in task.get("dependencies", []):
                row = db.execute("SELECT run_id FROM tasks WHERE project=? AND task_id=?",
                                 (project, dep)).fetchone()
                if not row or row[0] != task["run_id"]:
                    raise ValueError("dependency missing or from a different run")
            db.execute("INSERT INTO tasks(project,task_id,run_id,idem,spec,status,created,updated) "
                       "VALUES(?,?,?,?,?,?,?,?)",
                       (project, task["task_id"], task["run_id"], task["idempotency_key"],
                        canonical(task), "queued", now, now))
        return {"task": task, "status": "queued", "result": None}

    def read(self, project: str, task_id: str) -> dict:
        with self.connect() as db:
            row = db.execute("SELECT spec,status,result,attempts FROM tasks WHERE project=? AND task_id=?",
                             (project, task_id)).fetchone()
        if row is None:
            raise KeyError("task absent or inaccessible")
        return {"task": json.loads(row[0]), "status": row[1],
                "result": json.loads(row[2]) if row[2] else None, "attempts": row[3]}

    def claim_ready(self, project: str) -> dict | None:
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            rows = db.execute("SELECT task_id,spec FROM tasks WHERE project=? AND status='queued' ORDER BY created,task_id",
                              (project,)).fetchall()
            for task_id, spec in rows:
                task = json.loads(spec)
                deps = task.get("dependencies", [])
                if deps:
                    params = ",".join("?" for _ in deps)
                    entries = db.execute(
                        "SELECT task_id,status FROM tasks WHERE project=? AND task_id IN (" + params + ")",
                        (project, *deps)).fetchall()
                    statuses = {k: v for k, v in entries}
                    if any(statuses.get(dep) in ("failed", "blocked", "cancelled") for dep in deps):
                        db.execute("UPDATE tasks SET status='blocked',result=?,updated=? WHERE project=? AND task_id=?",
                                   (canonical({"reason": "dependency failed or blocked"}), time.time(), project, task_id))
                        continue
                    if any(statuses.get(dep) != "complete" for dep in deps):
                        continue
                running = db.execute("SELECT COUNT(*) FROM tasks WHERE project=? AND run_id=? AND status='running'",
                                     (project, task["run_id"])).fetchone()[0]
                if running >= task["limits"]["max_parallel"]:
                    continue
                updated = db.execute(
                    "UPDATE tasks SET status='running', attempts=attempts+1, updated=? "
                    "WHERE project=? AND task_id=? AND status='queued'",
                    (time.time(), project, task_id)).rowcount
                if updated:
                    return task
        return None

    def finish(self, project: str, task_id: str, result: dict) -> bool:
        if result.get("status") not in ("complete", "blocked", "failed"):
            raise ValueError("invalid task status")
        with self.connect() as db:
            changed = db.execute(
                "UPDATE tasks SET status=?,result=?,updated=? WHERE project=? AND task_id=? AND status='running'",
                (result["status"], canonical(result), time.time(), project, task_id)).rowcount
        return changed == 1

    def cancel(self, project: str, task_id: str) -> bool:
        with self.connect() as db:
            affected = db.execute("UPDATE tasks SET status='cancelled',updated=? "
                                  "WHERE project=? AND task_id=? AND status IN ('queued','running')",
                                  (time.time(), project, task_id)).rowcount
        return affected == 1

    def recover_running(self, project: str) -> int:
        # Reference single-process worker startup recovery: replay safe idempotent
        # tasks only; user agents must ensure external side-effects are idempotent.
        with self.connect() as db:
            changed = db.execute("UPDATE tasks SET status='blocked',result=?,updated=? "
                                 "WHERE project=? AND status='running'",
                                 (canonical({"reason": "runner restarted; manual reconciliation required"}),
                                  time.time(), project)).rowcount
        return changed
