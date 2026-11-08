"""Reference single-host worker for runnable local process delegation."""
from __future__ import annotations

import json
import threading
import time
from pathlib import Path

from runtime.package_resolver import PackageResolver
from runtime.policy import check_permissions
from runtime.process_adapter import ProcessAgentAdapter
from runtime.state_store import StateStore, digest
from runtime.task_queue import TaskQueue


class Worker:
    def __init__(self, root: str | Path, db_path: str | Path, adapter: ProcessAgentAdapter):
        self.root = Path(root)
        self.db_path = str(db_path)
        self.adapter = adapter
        self.queue = TaskQueue(db_path)
        self.resolver = PackageResolver(root)

    def run_one(self, project: str) -> bool:
        task = self.queue.claim_ready(project)
        if task is None:
            return False
        try:
            check_permissions(self.root, task["permissions"])
            if any(self.adapter.probe()["features"].get(cap) != "verified-available"
                   for cap in task["required_capabilities"]):
                raise PermissionError("required adapter capabilities not verified")
            store = StateStore(self.db_path)
            try:
                ctx = store.get_context(project, task["context_ref"], 1)
                if ctx["task_id"] != task["task_id"] or ctx["run_id"] != task["run_id"]:
                    raise PermissionError("wrong task or run context")
                package = self.resolver.resolve(task["package_id"], task["package_version"], task["objective"])
                # Forward only authorized versioned artifacts that this child has
                # been explicitly granted. Never mutate the immutable envelope.
                materialized = []
                for artifact_ref in ctx.get("artifact_refs", []):
                    artifact_id, sep, rev_str = artifact_ref.partition("@")
                    revision = int(rev_str) if sep else None
                    meta, raw = store.get_artifact(project, artifact_id, revision)
                    if (meta["visibility"] == "private-task" and
                            meta["producer_task_id"] != task["task_id"]):
                        raise PermissionError("private artifact not available to child")
                    if len(raw) > 512 * 1024:
                        raise ValueError("artifact exceeds shared-context limit")
                    import base64
                    materialized.append({
                        "artifact_id": artifact_id, "revision": meta["revision"],
                        "sha256": meta["sha256"], "status": meta["status"],
                        "content_base64": base64.b64encode(raw).decode("ascii")
                    })
                runtime_context = dict(ctx, resolved_artifacts=materialized)
                result = self.adapter.execute(task, runtime_context, package)
                if self.queue.read(project, task["task_id"])["status"] == "cancelled":
                    return True
                if result["status"] == "complete":
                    artifact_refs = []
                    for item in result.get("artifacts", []):
                        if self.queue.read(project, task["task_id"])["status"] == "cancelled":
                            return True
                        if not isinstance(item, dict) or not isinstance(item.get("content"), str):
                            raise ValueError("invalid child artifact")
                        raw = item["content"].encode("utf8")
                        hashval = digest(raw)
                        aid = item["artifact_id"]
                        rec = {
                            "artifact_id": aid, "owner": package["package_id"],
                            "kind": item.get("kind", "text"), "storage_ref": "sha256:" + hashval,
                            "sha256": hashval, "status": "draft",
                            "visibility": "run", "producer_task_id": task["task_id"],
                            "input_refs": [task["context_ref"]], "approval_refs": [],
                        }
                        revision = store.put_artifact(project, rec, raw, 0)
                        artifact_refs.append({"artifact_id": aid, "revision": revision, "sha256": hashval})
                    result["artifact_refs"] = artifact_refs
                # Only publish outputs if still running; a cancelled task cannot complete.
                self.queue.finish(project, task["task_id"], result)
            finally:
                store.close()
        except (ValueError, RuntimeError, PermissionError, KeyError, OSError) as exc:
            # Keep errors generic; never leak private prompt/context content.
            status = "blocked" if isinstance(exc, (PermissionError, KeyError)) else "failed"
            self.queue.finish(project, task["task_id"], {
                "protocol": "local-agent-result-v1",
                "task_id": task["task_id"], "status": status,
                "reason": type(exc).__name__,
            })
        return True


class WorkerPool:
    """Bounded single-process dispatcher. Running tasks are blocked at restart."""

    def __init__(self, worker: Worker, projects: list[str], max_workers: int = 2):
        if max_workers < 1 or max_workers > 8:
            raise ValueError("max_workers out of range")
        self.worker = worker
        self.projects = tuple(sorted(set(projects)))
        self.stop_flag = threading.Event()
        self.capacity = threading.Semaphore(max_workers)
        self.thread = None
        self.children = set()
        self.lock = threading.Lock()

    def start(self):
        for project in self.projects:
            self.worker.queue.recover_running(project)
        self.thread = threading.Thread(target=self.loop, name="agent-dispatcher", daemon=True)
        self.thread.start()

    def loop(self):
        while not self.stop_flag.is_set():
            if not self.capacity.acquire(timeout=0.1):
                continue
            found = False
            for project in self.projects:
                if self.worker.queue.readiness(project):
                    found = True
                    break
            if not found:
                self.capacity.release()
                self.stop_flag.wait(0.1)
                continue
            thread = threading.Thread(target=self.run_and_release, args=(project,), daemon=True)
            with self.lock:
                self.children.add(thread)
            thread.start()

    def run_and_release(self, project):
        try:
            self.worker.run_one(project)
        finally:
            self.capacity.release()
            with self.lock:
                self.children.discard(threading.current_thread())

    def stop(self):
        self.stop_flag.set()
        if self.thread is not None:
            self.thread.join(timeout=3)
