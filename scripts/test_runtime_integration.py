"""End-to-end local HTTP -> SQLite queue -> child process -> artifact tests.

Fixture is deterministic; these tests do NOT claim a real LLM provider or
public hosted website is configured.
"""
from __future__ import annotations

import base64
import http.client
import json
import sys
import tempfile
import threading
import time
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from runtime.gateway import Gateway
from runtime.package_resolver import PackageResolver
from runtime.process_adapter import ProcessAgentAdapter
from runtime.state_store import StateStore
from runtime.task_queue import TaskQueue


class GatewayIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db = Path(self.temp.name) / "state.sqlite3"
        tokens = {
            "token-alpha": {"projects": ["project-alpha"], "run_ids": ["run-1"], "scopes": ["read", "write", "delegate"]},
            "token-beta": {"projects": ["project-beta"], "run_ids": ["run-1"], "scopes": ["read", "write", "delegate"]},
            "token-read": {"projects": ["project-alpha"], "run_ids": ["run-1"], "scopes": ["read"]},
            "token-other-run": {"projects": ["project-alpha"], "run_ids": ["run-2"], "scopes": ["read", "write", "delegate"]},
        }
        self.gateway = Gateway(
            ROOT, self.db, tokens,
            worker_argv=[sys.executable, str(ROOT / "runtime" / "fixtures" / "echo_agent.py")],
        )
        self.http = ThreadingHTTPServer(("127.0.0.1", 0), self.gateway.handler())
        self.port = self.http.server_address[1]
        self.gateway.start()
        self.server_thread = threading.Thread(target=self.http.serve_forever, daemon=True)
        self.server_thread.start()

    def tearDown(self):
        self.http.shutdown()
        self.http.server_close()
        self.gateway.stop()
        self.server_thread.join(timeout=3)
        self.temp.cleanup()

    def request(self, method: str, path: str, payload=None, token="token-alpha", idem=None):
        conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=10)
        headers = {"Content-Type": "application/json"}
        if token is not None:
            headers["Authorization"] = "Bearer " + token
        if idem is not None:
            headers["Idempotency-Key"] = idem
        data = json.dumps(payload).encode("utf8") if payload is not None else None
        try:
            conn.request(method, path, data, headers)
            response = conn.getresponse()
            body = response.read()
            return response.status, json.loads(body)
        finally:
            conn.close()

    @staticmethod
    def task(tid, context_id, *, permissions=None, dependencies=None, capability="child-process"):
        return {
            "run_id": "run-1", "task_id": tid, "package_id": "pragmatic-pr-reviewer",
            "package_version": "v1", "objective": "review change " + tid,
            "context_ref": context_id, "idempotency_key": tid + "-key",
            "permissions": permissions if permissions is not None else ["read"],
            "required_capabilities": [capability], "dependencies": dependencies or [],
            "limits": {"max_depth": 1, "max_parallel": 2, "timeout_seconds": 30},
        }

    @staticmethod
    def context(tid, context_id, artifact_refs=None, permissions=None):
        return {
            "run_id": "run-1", "task_id": tid, "context_id": context_id, "revision": 1,
            "project_revision": "sha-123", "objective": "review",
            "authoritative_inputs": ["pragmatic-pr-reviewer@v1"],
            "artifact_refs": artifact_refs or [], "permissions": permissions or ["read"],
        }

    def post_context(self, tid, context_id, artifacts=None, token="token-alpha", permissions=None):
        status, data = self.request("POST", "/v1/contexts", {
            "project_id": "project-alpha",
            "envelope": self.context(tid, context_id, artifacts, permissions)
        }, token=token)
        self.assertEqual(status, 201, data)

    def post_task(self, task, project="project-alpha", token="token-alpha"):
        return self.request("POST", "/v1/tasks", {
            "project_id": project, "task": task
        }, token=token, idem=task["idempotency_key"])

    def wait_status(self, task_id, expected="complete"):
        limit = time.time() + 10
        while time.time() < limit:
            status, data = self.request("GET", "/v1/tasks/" + task_id)
            if status == 200 and data["status"] not in ("queued", "running"):
                self.assertEqual(data["status"], expected, data)
                return data
            time.sleep(0.04)
        self.fail("task did not settle")

    def test_health_and_search(self):
        status, data = self.request("GET", "/healthz", token=None)
        self.assertEqual((status, data["ok"]), (200, True))
        status, data = self.request("GET", "/v1/capabilities")
        self.assertEqual(status, 200)
        self.assertEqual(data["spawn_mode"], "process-or-sdk")
        status, data = self.request("GET", "/v1/packages/resolve?query=PR%20review")
        self.assertEqual(status, 200)
        self.assertTrue(data["results"])

    def test_authenticated_fan_out_fan_in_and_artifacts(self):
        self.post_context("child-1", "ctx-1")
        self.post_context("child-2", "ctx-2")
        for tid, ctx in (("child-1", "ctx-1"), ("child-2", "ctx-2")):
            status, data = self.post_task(self.task(tid, ctx))
            self.assertEqual(status, 202, data)
        first = self.wait_status("child-1")
        second = self.wait_status("child-2")
        self.assertEqual(first["result"]["protocol"], "local-agent-result-v1")
        self.assertEqual(second["result"]["protocol"], "local-agent-result-v1")
        for tid in ("child-1", "child-2"):
            status, artifact = self.request("GET", "/v1/artifacts/output-" + tid)
            self.assertEqual(status, 200)
            self.assertEqual(artifact["record"]["owner"], "pragmatic-pr-reviewer")
            self.assertIn(tid.encode(), base64.b64decode(artifact["content_base64"]))
        self.post_context("child-3", "ctx-3", artifacts=["output-child-1@1"])
        status, data = self.post_task(self.task(
            "child-3", "ctx-3", dependencies=["child-1", "child-2"]))
        self.assertEqual(status, 202, data)
        third = self.wait_status("child-3")
        self.assertIn("inherited-artifacts:1", third["result"]["evidence"])
        self.assertEqual(len(third["result"]["artifact_refs"]), 1)

    def test_run_scoping_and_immutable_context_revision(self):
        self.post_context("versioned", "ctx-versioned")
        status, _ = self.request("GET", "/v1/contexts/ctx-versioned", token="token-other-run")
        self.assertEqual(status, 403)
        second = self.context("versioned", "ctx-versioned")
        second["revision"] = 2
        second["objective"] = "revised but immutable version"
        status, resp = self.request("POST", "/v1/contexts",
                                    {"project_id": "project-alpha", "envelope": second})
        self.assertEqual(status, 201, resp)
        self.assertEqual(resp["context_ref"], "ctx-versioned@2")
        status, latest = self.request("GET", "/v1/contexts/ctx-versioned?revision=2")
        self.assertEqual(status, 200)
        self.assertEqual(latest["objective"], second["objective"])
        status, previous = self.request("GET", "/v1/contexts/ctx-versioned?revision=1")
        self.assertEqual(status, 200)
        self.assertNotEqual(previous["objective"], second["objective"])
        status, _ = self.request("POST", "/v1/contexts",
                                 {"project_id": "project-alpha", "envelope": second})
        self.assertEqual(status, 409)

    def test_private_artifact_read_blocked_without_task_grant(self):
        self.post_context("owner-task", "ctx-owner")
        status, _ = self.post_task(self.task("owner-task", "ctx-owner"))
        self.assertEqual(status, 202)
        self.wait_status("owner-task")
        from runtime.state_store import digest
        raw = b"private evidence"
        record = {
            "artifact_id": "private-1", "owner": "pragmatic-pr-reviewer", "kind": "text",
            "storage_ref": "sha256:" + digest(raw), "sha256": digest(raw),
            "status": "draft", "visibility": "private-task",
            "producer_task_id": "owner-task",
        }
        store = StateStore(self.db)
        try:
            store.put_artifact("project-alpha", record, raw, 0)
        finally:
            store.close()
        status, _ = self.request("GET", "/v1/artifacts/private-1")
        self.assertEqual(status, 403)

    def test_auth_and_project_isolation(self):
        self.post_context("isolated", "ctx-isolated")
        status, data = self.request("GET", "/v1/contexts/ctx-isolated?project_id=project-beta", token="token-beta")
        self.assertEqual(status, 404)
        status, data = self.request("GET", "/v1/contexts/ctx-isolated?project_id=project-alpha", token="token-beta")
        self.assertEqual(status, 403)
        status, data = self.request("GET", "/v1/contexts/ctx-isolated", token=None)
        self.assertEqual(status, 403)
        status, data = self.request("POST", "/v1/contexts", {
            "project_id": "project-alpha", "envelope": self.context("x", "ctx-ro")
        }, token="token-read")
        self.assertEqual(status, 403)

    def test_approval_gate_invalid_idempotency_and_unknown_capability(self):
        self.post_context("blocked", "ctx-blocked", permissions=["merge"])
        status, data = self.post_task(self.task("blocked", "ctx-blocked", permissions=["merge"]))
        self.assertEqual(status, 403)
        self.post_context("unverified", "ctx-unverified")
        status, data = self.post_task(self.task("unverified", "ctx-unverified", capability="unverified-skill"))
        self.assertEqual(status, 202, data)
        self.wait_status("unverified", expected="blocked")
        self.post_context("idempotent", "ctx-idempotent")
        t = self.task("idempotent", "ctx-idempotent")
        self.assertEqual(self.post_task(t)[0], 202)
        self.assertEqual(self.post_task(t)[0], 202)
        modified = dict(t, objective="changed objective")
        self.assertEqual(self.post_task(modified)[0], 409)
        self.wait_status("idempotent")

    def test_dep_failure_blocks_child(self):
        self.post_context("fail-first", "ctx-fail-first")
        self.post_context("dependent", "ctx-dependent")
        self.post_task(self.task("fail-first", "ctx-fail-first", capability="missing"))
        self.wait_status("fail-first", expected="blocked")
        self.post_task(self.task("dependent", "ctx-dependent", dependencies=["fail-first"]))
        self.wait_status("dependent", expected="blocked")

    def test_cancel_queued_and_invalid_permissions(self):
        self.post_context("cancel-me", "ctx-cancel")
        task = self.task("cancel-me", "ctx-cancel", capability="missing")
        self.post_task(task)
        # Task may already be blocked; cancellation result describes actual outcome.
        status, data = self.request("POST", "/v1/tasks/cancel-me/cancel",
                                    {"project_id": "project-alpha"})
        self.assertEqual(status, 202)
        task2 = self.task("bad-budget", "ctx-cancel")
        task2["limits"]["max_parallel"] = 100
        status, _ = self.post_task(task2)
        self.assertIn(status, (400, 403))


class ResolverUnitTests(unittest.TestCase):
    def test_legacy_pinned_content_and_wrong_versions(self):
        r = PackageResolver(ROOT)
        x = r.resolve("pragmatic-pr-reviewer", "v1", "review change")
        self.assertTrue(x["legacy"])
        self.assertTrue(x["sections"][0]["content"])
        with self.assertRaises(ValueError):
            r.resolve("pragmatic-pr-reviewer", "v999", "review change")

    def test_local_worker_probe(self):
        local = ProcessAgentAdapter([sys.executable, str(ROOT / "runtime" / "fixtures" / "echo_agent.py")], ROOT)
        self.assertEqual(local.probe()["spawn_mode"], "process-or-sdk")

    def test_queue_recovery(self):
        with tempfile.TemporaryDirectory() as td:
            q = TaskQueue(Path(td) / "queue.db")
            t = GatewayIntegrationTests.task("recover", "ctx")
            q.submit("project", t)
            q.claim_ready("project")
            self.assertEqual(q.recover_running("project"), 1)
            self.assertEqual(q.read("project", "recover")["status"], "blocked")


if __name__ == "__main__":
    unittest.main()
