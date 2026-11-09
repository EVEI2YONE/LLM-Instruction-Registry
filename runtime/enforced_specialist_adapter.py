"""Fail-closed local execution boundary for registry specialists.

This is an operator-wired reference component, NOT a deployed ChatGPT tool.
The same trusted process must own prepare, execute and accept. It deliberately
does not expose a generic direct-execute method.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
import json
from pathlib import Path
import re
import secrets
import time
from typing import Callable

from runtime.instruction_execution_gate import GateError

_SHA = re.compile(r"[0-9a-f]{40}\Z")


def _hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


@dataclass(frozen=True)
class Prepared:
    token: str
    mode: str
    package_id: str
    package_version: str
    registry_commit: str
    instruction_sha256: str
    section_ids: tuple[str, ...]


class EnforcedSpecialistAdapter:
    """Trusted in-process bridge; caller cannot generate its own receipts.

    `runner` must be operator-supplied and actually deliver the supplied
    instruction bytes to the executor (or return a verifiable delivery record).
    `verifier` must be independent of the model being assessed and inspect the
    real artifact/trace against requirements.
    """

    def __init__(self, registry_root: str | Path, registry_sha: str,
                 runner: Callable, verifier: Callable, *, ttl_seconds: int = 300):
        self.root = Path(registry_root).resolve()
        if not _SHA.fullmatch(registry_sha):
            raise GateError("invalid pinned registry SHA")
        if not callable(runner) or not callable(verifier):
            raise GateError("trusted runner and verifier are required")
        if ttl_seconds < 1:
            raise GateError("positive token TTL required")
        self.registry_sha = registry_sha
        self.runner = runner
        self.verifier = verifier
        self.ttl = ttl_seconds
        self._secret = secrets.token_bytes(32)
        self._prepared = {}
        self._executed = {}

    def _signed(self, payload: dict) -> str:
        raw = _canonical(payload)
        return _hash(raw) + "." + hmac.new(self._secret, raw, "sha256").hexdigest()

    def _package(self, package_id: str) -> tuple[dict, dict[str, bytes]]:
        registry = json.loads((self.root / "registry.json").read_text("utf-8"))
        record = next((r for r in registry["instruction_sets"] if r["id"] == package_id), None)
        if not record:
            raise GateError("BLOCKED_INSTRUCTIONS: specialist not registered")
        source_dir = (self.root / record["sources"]).resolve()
        if not source_dir.is_relative_to(self.root):
            raise GateError("BLOCKED_INSTRUCTIONS: source path outside registry")
        manifest = json.loads((source_dir / "manifest.json").read_text("utf-8"))
        if manifest["id"] != package_id or manifest["version"] != record["version"]:
            raise GateError("BLOCKED_INSTRUCTIONS: package/version mismatch")
        section_map = {s["id"]: s for s in manifest["sections"]}
        data = {}
        entry = manifest["entrypoint"]
        entry_data = (source_dir / entry["path"]).read_bytes()
        if _hash(entry_data) != entry["sha256"]:
            raise GateError("BLOCKED_INSTRUCTIONS: entrypoint hash mismatch")
        data["SKILL.md"] = entry_data
        return manifest, data

    def prepare_specialist(self, task: dict, *, native_available: bool,
                           delegation_authorized: bool) -> Prepared:
        """Resolve source and dependency closure BEFORE permitting execution."""
        for k in ("task_id", "project_revision", "package_id", "required_sections",
                  "required_rule_ids", "objective"):
            if k not in task:
                raise GateError("BLOCKED_INSTRUCTIONS: missing task field " + k)
        if not task["task_id"] or not task["objective"] or not _SHA.fullmatch(task["project_revision"]):
            raise GateError("invalid task identity or immutable project revision")
        if not task["required_rule_ids"]:
            raise GateError("acceptance rules required")
        mode = "NATIVE_CHILD" if native_available and delegation_authorized else "SEQUENTIAL_SPECIALIST"
        manifest, data = self._package(task["package_id"])
        section_map = {s["id"]: s for s in manifest["sections"]}
        required = set()
        def load(sid: str, visiting: set):
            if sid in visiting:
                raise GateError("BLOCKED_INSTRUCTIONS: cyclic section dependency")
            if sid in required:
                return
            s = section_map.get(sid)
            if not s:
                raise GateError("BLOCKED_INSTRUCTIONS: required dependency missing " + sid)
            visiting.add(sid)
            for dep in s.get("requires", []):
                load(dep, visiting)
            visiting.remove(sid)
            p = (self.root / next(r["sources"] for r in json.loads(
                (self.root / "registry.json").read_text("utf-8"))["instruction_sets"]
                if r["id"] == task["package_id"]) / s["path"]).resolve()
            if not p.is_relative_to(self.root):
                raise GateError("BLOCKED_INSTRUCTIONS: section escapes registry")
            content = p.read_bytes()
            if _hash(content) != s["sha256"]:
                raise GateError("BLOCKED_INSTRUCTIONS: section hash mismatch " + sid)
            data[sid] = content
            required.add(sid)
        for sid in task["required_sections"]:
            load(sid, set())
        if not required:
            raise GateError("BLOCKED_INSTRUCTIONS: empty specialist section selection")
        ordered = tuple(sorted(required))
        digest = _hash(_canonical({k: _hash(v) for k, v in sorted(data.items())}))
        identity = {k: task[k] for k in ("task_id", "project_revision", "package_id",
                                      "required_rule_ids", "objective")}
        payload = {"task": identity, "registry_sha": self.registry_sha,
                   "version": manifest["version"], "mode": mode,
                   "instruction_digest": digest, "sections": ordered,
                   "issued": int(time.time()), "nonce": secrets.token_hex(16)}
        token = self._signed(payload)
        self._prepared[token] = (payload, data, dict(task))
        return Prepared(token, mode, task["package_id"], manifest["version"],
                        self.registry_sha, digest, ordered)

    def execute_specialist(self, task: dict, token: str) -> dict:
        """Only verified prepared tasks can reach the operator-controlled runner."""
        if token not in self._prepared or token in self._executed:
            raise GateError("BLOCKED_INSTRUCTIONS: missing, forged or already-used preflight")
        payload, content, original = self._prepared[token]
        if not hmac.compare_digest(self._signed(payload), token):
            raise GateError("invalid preflight signature")
        if time.time() > payload["issued"] + self.ttl:
            raise GateError("expired preflight")
        if _canonical(task) != _canonical(original):
            raise GateError("task changed since preflight")
        # Reserve the token *before* invoking the runner: no replays on failure.
        self._executed[token] = {"status": "running"}
        result = self.runner(task=dict(original), mode=payload["mode"],
                             instructions=dict(content), registry_sha=self.registry_sha)
        if not isinstance(result, dict) or not result.get("execution_id") or not result.get("delivery_ref"):
            self._executed[token] = {"status": "blocked"}
            raise GateError("PROPAGATION_NOT_VERIFIED: runner supplied no delivery trace")
        if payload["mode"] == "NATIVE_CHILD" and not result.get("child_handle"):
            self._executed[token] = {"status": "blocked"}
            raise GateError("PROPAGATION_NOT_VERIFIED: real child handle required")
        if payload["mode"] == "SEQUENTIAL_SPECIALIST" and result.get("child_handle"):
            self._executed[token] = {"status": "blocked"}
            raise GateError("sequential result cannot report a child handle")
        self._executed[token] = {"status": "executed", "result": result}
        return result

    def accept_specialist_result(self, task: dict, token: str) -> dict:
        """Only an independent trusted verifier can approve application."""
        if token not in self._prepared or token not in self._executed:
            raise GateError("no matching executed preflight")
        payload, _, original = self._prepared[token]
        state = self._executed[token]
        if _canonical(task) != _canonical(original) or state["status"] != "executed":
            raise GateError("execution not eligible for acceptance")
        result = state["result"]
        decision = self.verifier(task=dict(original), result=dict(result),
                                 required_rule_ids=tuple(original["required_rule_ids"]),
                                 instruction_sha256=payload["instruction_digest"])
        if not isinstance(decision, dict) or decision.get("verified") is not True:
            raise GateError("APPLICATION_NOT_VERIFIED: independent acceptance denied")
        if set(original["required_rule_ids"]) - set(decision.get("verified_rule_ids", [])):
            raise GateError("APPLICATION_NOT_VERIFIED: mandatory rule not checked")
        if not result.get("artifact_ref") or not decision.get("evidence_refs"):
            raise GateError("APPLICATION_NOT_VERIFIED: artifact or evidence missing")
        state["status"] = "accepted"
        return {"status": "accepted", "task_id": task["task_id"], "mode": payload["mode"],
                "artifact_ref": result["artifact_ref"], "evidence_refs": decision["evidence_refs"]}
