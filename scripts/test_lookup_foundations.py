"""Contract tests for lookup-first foundations. Run with unittest discovery."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))
import lookup_sections as ls
from runtime.state_store import StateStore, ConflictError, digest
from runtime.reference_adapter import Adapter, UnsupportedSpawn
from migration_inventory import inventory, verify_snapshot


class LookupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "pkg"
        (self.source / "sections").mkdir(parents=True)
        (self.source / "SKILL.md").write_text("# Test", encoding="utf8")
        for name in ("intake", "execute"):
            (self.source / "sections" / (name + ".md")).write_text(name, encoding="utf8")
        self.sections = [
            dict(id="intake", kind="procedure", path="sections/intake.md",
                 read_when=["collect initial requirements"], summary="intake", words=1),
            dict(id="execute", kind="procedure", path="sections/execute.md",
                 read_when=["execute change"], summary="do change", requires=["intake"], words=1)
        ]

    def tearDown(self):
        self.tmp.cleanup()

    def test_lookup_dependencies(self):
        sectionmap = ls.validate(self.source, {"sections": self.sections})
        hits = ls.lookup(sectionmap, "execute change", 1)
        self.assertEqual([x["id"] for x in hits], ["intake", "execute"])

    def test_cycle_rejected(self):
        self.sections[0]["requires"] = ["execute"]
        with self.assertRaisesRegex(ValueError, "circular"):
            ls.validate(self.source, {"sections": self.sections})

    def test_path_escape_rejected(self):
        self.sections[0]["path"] = "../escape.md"
        with self.assertRaises(ValueError):
            ls.validate(self.source, {"sections": self.sections})

    def test_missing_orphan_trigger_rejected(self):
        self.sections[0]["read_when"] = []
        with self.assertRaisesRegex(ValueError, "unreachable"):
            ls.validate(self.source, {"sections": self.sections})

    def test_sha_rejected(self):
        self.sections[0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "sha256"):
            ls.validate(self.source, {"sections": self.sections})


class DurableStoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "state.db"
        self.store = StateStore(self.path)

    def tearDown(self):
        self.store.close()
        self.tmp.cleanup()

    def test_context_is_immutable_and_namespace_scoped(self):
        env = dict(run_id="run", task_id="child", context_id="ctx", revision=1,
                   project_revision="sha", objective="review", authoritative_inputs=["pkg@v1"],
                   artifact_refs=[], permissions=["read"])
        self.store.put_context("project-a", env)
        self.assertEqual(self.store.get_context("project-a", "ctx", 1), env)
        with self.assertRaises(KeyError):
            self.store.get_context("project-b", "ctx", 1)
        with self.assertRaises(Exception):
            self.store.put_context("project-a", env)
        self.store.close()
        self.store = StateStore(self.path)
        self.assertEqual(self.store.get_context("project-a", "ctx", 1), env)

    def test_artifact_cas_immutability_and_approval(self):
        data = b"draft"
        record = dict(artifact_id="a", owner="doc-owner", kind="document",
                      storage_ref="sha256:" + digest(data), sha256=digest(data),
                      status="draft", visibility="run", producer_task_id="child")
        self.assertEqual(self.store.put_artifact("project-a", record, data, 0), 1)
        with self.assertRaises(ConflictError):
            self.store.put_artifact("project-a", record, data, 0)
        with self.assertRaises(KeyError):
            self.store.get_artifact("project-b", "a")
        self.assertEqual(self.store.get_artifact("project-a", "a")[1], data)
        revised = dict(record, owner="other")
        with self.assertRaises(ConflictError):
            self.store.put_artifact("project-a", revised, data, 1)
        approved = dict(record, status="approved")
        with self.assertRaises(ValueError):
            self.store.put_artifact("project-a", approved, data, 1)
        approved["approval_refs"] = ["human-approval@sha"]
        self.assertEqual(self.store.put_artifact("project-a", approved, data, 1), 2)
        self.assertEqual(self.store.get_artifact("project-a", "a", 1)[0]["status"], "draft")

    def test_digest_mismatch(self):
        data = b"bytes"
        record = dict(artifact_id="a", owner="owner", kind="document",
                      storage_ref="sha256:0", sha256="0"*64,
                      status="draft", visibility="run", producer_task_id="child")
        with self.assertRaises(ValueError):
            self.store.put_artifact("project-a", record, data, 0)


class MockDelegationTests(unittest.TestCase):
    def test_unsupported_runtime_fails_without_fabrication(self):
        adapter = Adapter("hosted-chat", {"spawn": "unknown"})
        with self.assertRaises(UnsupportedSpawn):
            adapter.spawn({"task_id": "a", "idempotency_key": "a", "context_ref": "ctx"}, "ctx", [])

    def test_mock_idempotency_and_capability_gate(self):
        adapter = Adapter("fake", {"research": "verified-available"}, spawn_mode="mock")
        task = dict(task_id="a", idempotency_key="key", context_ref="ctx",
                    required_capabilities=["research"])
        handle = adapter.spawn(task, "ctx", ["intake"])
        self.assertEqual(handle, adapter.spawn(task, "ctx", ["intake"]))
        self.assertTrue(handle["mock_only"])
        adapter.cancel(handle)
        self.assertEqual(adapter.poll(handle)["status"], "cancelled")
        task["required_capabilities"] = ["merge"]
        task["idempotency_key"] = "other-key"
        with self.assertRaises(UnsupportedSpawn):
            adapter.spawn(task, "ctx", [])


class InventoryTests(unittest.TestCase):
    def test_whole_registry_baseline(self):
        data = inventory(ROOT)
        self.assertEqual(data["count"], 49)
        self.assertEqual(len({p["id"] for p in data["packages"]}), 49)
        self.assertTrue(all(p["migration_status"] == "pending" for p in data["packages"]))
        self.assertEqual(sum(p["kind"] == "specialist" for p in data["packages"]), 40)

    def test_snapshot_matches(self):
        live = inventory(ROOT)
        expected = json.loads((ROOT / "migration" / "inventory.json").read_text(encoding="utf8"))
        self.assertEqual([], verify_snapshot(ROOT, expected))
        meta = next(x for x in expected["packages"] if x["id"] == "meta-llm-orchestrator")
        self.assertEqual(("v20", "v22", "completed"),
                         (meta["baseline_version"], meta["new_version"], meta["migration_status"]))


if __name__ == "__main__":
    unittest.main()
