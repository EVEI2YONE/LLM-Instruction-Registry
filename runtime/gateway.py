"""Authenticated localhost reference gateway with durable task execution.

Start: python -m runtime.gateway
This service is for controlled local development. External exposure requires
TLS-terminating proxy, production identity and hardened tenant isolation.
"""
from __future__ import annotations

import base64
import hmac
import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from runtime.package_resolver import PackageResolver
from runtime.policy import check_permissions
from runtime.process_adapter import ProcessAgentAdapter
from runtime.state_store import StateStore, ConflictError, digest
from runtime.task_queue import TaskQueue, TaskConflict
from runtime.worker import Worker, WorkerPool
from runtime.refs import parse_ref

MAX_REQUEST = 1024 * 1024


class Gateway:
    """Token bindings map opaque credentials to project and API capabilities."""

    def __init__(self, root: str | Path, db_path: str | Path,
                 tokens: dict[str, dict], worker_argv: list[str] | None = None,
                 project_scope: str | None = None):
        self.root = Path(root).resolve()
        self.db_path = str(db_path)
        self.tokens = tokens
        if not tokens or any(not token or not isinstance(spec.get("projects"), list)
                             or not isinstance(spec.get("scopes"), list)
                             for token, spec in tokens.items()):
            raise ValueError("token bindings require projects and scopes")
        self.projects = sorted({p for bind in tokens.values() for p in bind["projects"]})
        self.queue = TaskQueue(self.db_path)
        self.resolver = PackageResolver(self.root)
        self.pool = None
        if worker_argv:
            adapter = ProcessAgentAdapter(worker_argv, self.root, timeout=120)
            if adapter.probe()["spawn_mode"] == "unavailable":
                raise ValueError("worker executable not available")
            self.pool = WorkerPool(Worker(self.root, db_path, adapter), self.projects, max_workers=2)

    def start(self):
        if self.pool:
            self.pool.start()

    def stop(self):
        if self.pool:
            self.pool.stop()

    def authenticate(self, bearer: str, project: str | None, scope: str) -> tuple[dict, str]:
        match = None
        for key, binding in self.tokens.items():
            if hmac.compare_digest(key, bearer):
                match = binding
        if match is None:
            raise PermissionError("invalid credentials")
        if scope not in match["scopes"]:
            raise PermissionError("missing API scope")
        if project is None:
            if len(match["projects"]) != 1:
                raise PermissionError("project must be specified")
            project = match["projects"][0]
        if project not in match["projects"]:
            raise PermissionError("project inaccessible")
        return match, project

    def handler(self):
        gateway = self

        class Handler(BaseHTTPRequestHandler):
            server_version = "InstructionGateway/0.1"

            def log_message(self, format, *args):
                # No Authorization or request payload logging.
                return

            def send_json(self, status, obj):
                data = json.dumps(obj, sort_keys=True).encode("utf8")
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Cache-Control", "no-store")
                self.send_header("X-Content-Type-Options", "nosniff")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def request_body(self):
                length = self.headers.get("Content-Length")
                if length is None or not length.isdecimal() or int(length) > MAX_REQUEST:
                    raise ValueError("missing or excessive Content-Length")
                body = self.rfile.read(int(length))
                if len(body) != int(length):
                    raise ValueError("incomplete body")
                parsed = json.loads(body)
                if not isinstance(parsed, dict):
                    raise ValueError("JSON body must be object")
                return parsed

            def authorize(self, scope, project=None):
                header = self.headers.get("Authorization", "")
                if not header.startswith("Bearer "):
                    raise PermissionError("bearer token required")
                binding, selected = gateway.authenticate(header[7:], project, scope)
                self.binding = binding
                return selected

            def require_run(self, run_id):
                allowed = self.binding.get("run_ids", [])
                if run_id not in allowed and "*" not in allowed:
                    raise PermissionError("run scope denied")

            def do_GET(self):
                try:
                    url = urlparse(self.path)
                    path = url.path
                    args = parse_qs(url.query)
                    project = args.get("project_id", [None])[0]
                    if path == "/healthz":
                        self.send_json(200, {"ok": True, "service": "local-reference"})
                        return
                    project = self.authorize("read", project)
                    if path == "/v1/capabilities":
                        self.send_json(200, {
                            "runtime_id": "local-reference-gateway", "project_id": project,
                            "spawn_mode": "process-or-sdk" if gateway.pool else "unavailable",
                            "features": {"child-process": "verified-available" if gateway.pool else "verified-unavailable"},
                            "hosted_provider_native": "unknown",
                        })
                    elif path == "/v1/packages/resolve":
                        q = args.get("query", [""])[0]
                        if not q.strip():
                            raise ValueError("query is required")
                        self.send_json(200, {"results": gateway.resolver.search(q, 5)})
                    elif path.startswith("/v1/tasks/") and path.count("/") == 3:
                        task_id = path.split("/")[-1]
                        task_record = gateway.queue.read(project, task_id)
                        self.require_run(task_record["task"]["run_id"])
                        self.send_json(200, task_record)
                    elif path.startswith("/v1/contexts/") and path.count("/") == 3:
                        context_id = path.split("/")[-1]
                        revision = int(args.get("revision", ["1"])[0])
                        store = StateStore(gateway.db_path)
                        try:
                            context = store.get_context(project, context_id, revision)
                            self.require_run(context["run_id"])
                            self.send_json(200, context)
                        finally:
                            store.close()
                    elif path.startswith("/v1/artifacts/") and path.count("/") == 3:
                        aid = path.split("/")[-1]
                        rev = args.get("revision", [None])[0]
                        store = StateStore(gateway.db_path)
                        try:
                            meta, raw = store.get_artifact(project, aid, int(rev) if rev else None)
                            if meta["visibility"] in ("run", "private-task"):
                                task_record = gateway.queue.read(project, meta["producer_task_id"])
                                self.require_run(task_record["task"]["run_id"])
                            if meta["visibility"] == "private-task" and (
                                    meta["producer_task_id"] not in self.binding.get("task_ids", [])):
                                raise PermissionError("private task artifact")
                        finally:
                            store.close()
                        self.send_json(200, {"record": meta, "content_base64": base64.b64encode(raw).decode("ascii")})
                    else:
                        self.send_json(404, {"error": "not_found"})
                except PermissionError:
                    self.send_json(403, {"error": "forbidden"})
                except KeyError:
                    self.send_json(404, {"error": "not_found"})
                except (ValueError, json.JSONDecodeError):
                    self.send_json(400, {"error": "bad_request"})

            def do_POST(self):
                try:
                    path = urlparse(self.path).path
                    body = self.request_body()
                    project = body.get("project_id")
                    if path == "/v1/contexts":
                        project = self.authorize("write", project)
                        envelope = body.get("envelope")
                        if not isinstance(envelope, dict):
                            raise ValueError("envelope required")
                        store = StateStore(gateway.db_path)
                        try:
                            self.require_run(envelope["run_id"])
                            hashval = store.put_context(project, envelope)
                        finally:
                            store.close()
                        self.send_json(201, {"context_ref": envelope["context_id"] + "@" + str(envelope["revision"]), "sha256": hashval})
                    elif path == "/v1/tasks":
                        project = self.authorize("delegate", project)
                        if gateway.pool is None:
                            self.send_json(503, {"error": "worker_not_configured"})
                            return
                        task = body.get("task")
                        if not isinstance(task, dict):
                            raise ValueError("task required")
                        if self.headers.get("Idempotency-Key") != task.get("idempotency_key"):
                            raise ValueError("idempotency header mismatch")
                        self.require_run(task["run_id"])
                        check_permissions(gateway.root, task.get("permissions", []))
                        gateway.resolver.pin(task["package_id"], task["package_version"])
                        store = StateStore(gateway.db_path)
                        try:
                            ctx_id, ctx_rev = parse_ref(task["context_ref"], 1)
                            ctx = store.get_context(project, ctx_id, ctx_rev)
                        finally:
                            store.close()
                        if (ctx.get("task_id"), ctx.get("run_id")) != (task.get("task_id"), task.get("run_id")):
                            raise PermissionError("task context identity mismatch")
                        if set(task["permissions"]) - set(ctx.get("permissions", [])):
                            raise PermissionError("permissions exceed context")
                        res = gateway.queue.submit(project, task)
                        self.send_json(202, res)
                    elif path.startswith("/v1/tasks/") and path.endswith("/cancel"):
                        project = self.authorize("delegate", project)
                        task_id = path.split("/")[-2]
                        self.require_run(gateway.queue.read(project, task_id)["task"]["run_id"])
                        changed = gateway.queue.cancel(project, task_id)
                        if not changed and not gateway.queue.read(project, task_id):
                            raise KeyError()
                        self.send_json(202, {"task_id": task_id, "cancelled": changed})
                    else:
                        self.send_json(404, {"error": "not_found"})
                except PermissionError:
                    self.send_json(403, {"error": "forbidden"})
                except (TaskConflict, ConflictError):
                    self.send_json(409, {"error": "conflict"})
                except KeyError:
                    self.send_json(404, {"error": "not_found"})
                except (ValueError, TypeError, json.JSONDecodeError):
                    self.send_json(400, {"error": "bad_request"})

        return Handler


def serve(root: str | Path, db_path: str | Path, tokens: dict, argv: list[str] | None,
          host: str = "127.0.0.1", port: int = 8765) -> None:
    if host not in ("127.0.0.1", "::1", "localhost") and os.getenv("GATEWAY_ALLOW_PROXY_BIND") != "yes":
        raise ValueError("non-loopback gateway requires explicit proxy deployment confirmation")
    gateway = Gateway(root, db_path, tokens, worker_argv=argv)
    httpd = ThreadingHTTPServer((host, port), gateway.handler())
    gateway.start()
    try:
        httpd.serve_forever()
    finally:
        httpd.shutdown()
        gateway.stop()
        httpd.server_close()


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    token_bindings = os.getenv("AGENT_GATEWAY_TOKENS_JSON")
    if not token_bindings:
        sys.exit("AGENT_GATEWAY_TOKENS_JSON is required (never commit tokens)")
    bindings = json.loads(token_bindings)
    argv_str = os.getenv("AGENT_WORKER_ARGV_JSON")
    argv = json.loads(argv_str) if argv_str else None
    serve(root=root, db_path=os.getenv("AGENT_STATE_DB", "runtime-state.sqlite3"),
          tokens=bindings, argv=argv, host=os.getenv("AGENT_GATEWAY_HOST", "127.0.0.1"),
          port=int(os.getenv("AGENT_GATEWAY_PORT", "8765")))
