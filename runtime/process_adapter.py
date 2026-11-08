"""Allowlisted local process bridge for executing actual child agents.

The user/operator supplies a trusted executable implementing the JSON protocol.
No shell, client-controlled command, arbitrary cwd, inherited secrets, or network
permissions are granted by this module. OS sandboxing remains operator-owned.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

from runtime.refs import parse_ref

MAX_RESULT_BYTES = 1024 * 1024


class ProcessAgentAdapter:
    def __init__(self, argv: list[str], cwd: str | Path, timeout: int = 120,
                 env_allowlist: tuple[str, ...] = ("PATH", "LANG", "LC_ALL", "SYSTEMROOT")):
        if not argv or not all(isinstance(x, str) and x for x in argv):
            raise ValueError("trusted fixed argv required")
        self.argv = list(argv)
        self.cwd = Path(cwd).resolve()
        if not self.cwd.is_dir():
            raise ValueError("working directory does not exist")
        if timeout < 1 or timeout > 3600:
            raise ValueError("invalid timeout")
        self.timeout = timeout
        self.env_allowlist = tuple(env_allowlist)

    def probe(self) -> dict:
        executable = self.argv[0]
        if os.path.isabs(executable):
            available = Path(executable).is_file()
        else:
            import shutil
            available = bool(shutil.which(executable))
        return {
            "runtime_id": "local-process",
            "spawn_mode": "process-or-sdk" if available else "unavailable",
            "features": {"child-process": "verified-available" if available else "verified-unavailable"},
        }

    def execute(self, task: dict, context: dict, package: dict) -> dict:
        if self.probe()["spawn_mode"] == "unavailable":
            raise RuntimeError("configured local worker executable unavailable")
        if parse_ref(task.get("context_ref"), 1)[0] != context.get("context_id"):
            raise ValueError("task context_ref mismatch")
        if task.get("run_id") != context.get("run_id"):
            raise ValueError("task/context run mismatch")
        if task.get("task_id") != context.get("task_id"):
            raise ValueError("task/context child mismatch")
        if set(task.get("permissions", [])) - set(context.get("permissions", [])):
            raise PermissionError("worker requested permissions beyond its context")
        if (task.get("package_id"), task.get("package_version")) != (
                package.get("package_id"), package.get("package_version")):
            raise ValueError("wrong resolved package")
        payload = json.dumps({
            "protocol": "local-agent-v1",
            "task": task,
            "context": context,
            "package": package,
        }, separators=(",", ":")).encode("utf8")
        if len(payload) > MAX_RESULT_BYTES:
            raise ValueError("agent request too large")
        env = {k: os.environ[k] for k in self.env_allowlist if k in os.environ}
        if not os.path.isabs(self.argv[0]) and "PATH" not in env:
            raise ValueError("PATH required for relative executable")
        try:
            done = subprocess.run(self.argv, input=payload, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, cwd=self.cwd, env=env,
                                  timeout=self.timeout, check=False)
        except subprocess.TimeoutExpired as exc:
            raise TimeoutError("local child exceeded time budget") from exc
        if len(done.stdout) > MAX_RESULT_BYTES or len(done.stderr) > MAX_RESULT_BYTES:
            raise ValueError("worker output exceeds bounded size")
        if done.returncode != 0:
            # Never return stderr: it might contain provider secrets.
            raise RuntimeError("child worker failed (exit code %s)" % done.returncode)
        try:
            result = json.loads(done.stdout)
        except (ValueError, UnicodeDecodeError) as exc:
            raise ValueError("worker did not return valid JSON") from exc
        if not isinstance(result, dict) or result.get("protocol") != "local-agent-result-v1":
            raise ValueError("invalid child result contract")
        if result.get("task_id") != task["task_id"] or result.get("status") not in ("complete", "blocked", "failed"):
            raise ValueError("child result task/status invalid")
        for key in ("artifacts", "evidence"):
            if not isinstance(result.get(key, []), list):
                raise ValueError("child result must have arrays")
        return result
