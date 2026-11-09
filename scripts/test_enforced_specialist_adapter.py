"""Contract tests: no specialist run without preflight and traceable acceptance.

These use a trusted fixture runner, not hosted ChatGPT or a real LLM.
"""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from runtime.enforced_specialist_adapter import EnforcedSpecialistAdapter
from runtime.instruction_execution_gate import GateError

SHA = "7d68443e5d8e3a02c9f91439fd82687d38ca8af1"
PROJECT_SHA = "838630151b3c033939e03241ee9c61986bcd9703"


class EnforcedExecutionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "specialists" / "product-readiness" / "sources"
        (self.source / "sections").mkdir(parents=True)
        self.entry = self.source / "SKILL.md"
        self.entry.write_text("# Specialist\nRequire explicit staging acceptance.\n")
        self.core = self.source / "sections" / "core.md"
        self.core.write_text("Require project evidence.\n")
        self.release = self.source / "sections" / "release.md"
        self.release.write_text("Require verified staging acceptance.\n")
        self.manifest = self.source / "manifest.json"
        self._save_manifest()
        (self.root / "registry.json").write_text(json.dumps({
            "instruction_sets": [{
                "id": "product-readiness", "version": "v1",
                "sources": "specialists/product-readiness/sources/"
            }]
        }))
        self.calls = []
        def runner(**kwargs):
            self.calls.append(kwargs)
            return {
                "execution_id": "parent:task-1" if kwargs["mode"] == "SEQUENTIAL_SPECIALIST" else "child:1",
                "child_handle": "child:1" if kwargs["mode"] == "NATIVE_CHILD" else None,
                "delivery_ref": "trace:delivered-exact-bytes",
                "artifact_ref": "artifact:staging-readiness",
            }
        self.runner = runner
        self.verifier = lambda **kw: {
            "verified": True,
            "verified_rule_ids": kw["required_rule_ids"],
            "evidence_refs": ["artifact:staging-readiness#staging"]
        }
        self.adapter = self.make_adapter()
        self.task = {
            "task_id": "task-1", "project_revision": PROJECT_SHA,
            "package_id": "product-readiness",
            "objective": "Assess feature readiness for EVEI2YONE/Little_Wins",
            "required_sections": ["release"],
            "required_rule_ids": ["staging-evidence"]
        }

    def _save_manifest(self):
        h = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
        self.manifest.write_text(json.dumps({
            "id": "product-readiness", "version": "v1",
            "entrypoint": {"path": "SKILL.md", "sha256": h(self.entry)},
            "sections": [
                {"id": "core", "path": "sections/core.md", "sha256": h(self.core), "requires": []},
                {"id": "release", "path": "sections/release.md",
                 "sha256": h(self.release), "requires": ["core"]}
            ]
        }))

    def make_adapter(self, *, verifier=None, runner=None):
        return EnforcedSpecialistAdapter(
            self.root, SHA, runner or self.runner,
            self.verifier if verifier is None else verifier)

    def test_little_wins_assessment_before_preflight_blocked(self):
        with self.assertRaisesRegex(GateError, "preflight"):
            self.adapter.execute_specialist(self.task, "missing")
        self.assertEqual([], self.calls)

    def test_sequential_fallback_delivers_full_closure(self):
        prepared = self.adapter.prepare_specialist(
            self.task, native_available=False, delegation_authorized=True)
        self.assertEqual("SEQUENTIAL_SPECIALIST", prepared.mode)
        self.assertEqual(("core", "release"), prepared.section_ids)
        result = self.adapter.execute_specialist(self.task, prepared.token)
        self.assertEqual({"SKILL.md", "core", "release"},
                         set(self.calls[0]["instructions"]))
        self.assertEqual("trace:delivered-exact-bytes", result["delivery_ref"])
        accepted = self.adapter.accept_specialist_result(self.task, prepared.token)
        self.assertEqual("accepted", accepted["status"])

    def test_no_explicit_spawn_request_still_uses_native_if_available(self):
        p = self.adapter.prepare_specialist(self.task, native_available=True,
                                            delegation_authorized=True)
        self.assertEqual("NATIVE_CHILD", p.mode)
        self.adapter.execute_specialist(self.task, p.token)
        self.assertEqual("accepted",
                         self.adapter.accept_specialist_result(self.task, p.token)["status"])

    def test_missing_entrypoint_is_blocked(self):
        self.entry.unlink()
        with self.assertRaises((FileNotFoundError, GateError)):
            self.adapter.prepare_specialist(self.task, native_available=False,
                                            delegation_authorized=True)
        self.assertFalse(self.calls)

    def test_missing_required_dependency_blocked(self):
        data = json.loads(self.manifest.read_text())
        data["sections"][1]["requires"] = ["nonexistent"]
        self.manifest.write_text(json.dumps(data))
        with self.assertRaisesRegex(GateError, "dependency missing"):
            self.adapter.prepare_specialist(self.task, native_available=False,
                                            delegation_authorized=True)

    def test_instruction_hash_mismatch_blocks(self):
        self.core.write_text("tampered")
        with self.assertRaisesRegex(GateError, "hash mismatch"):
            self.adapter.prepare_specialist(self.task, native_available=False,
                                            delegation_authorized=True)

    def test_task_change_invalidates_token(self):
        p = self.adapter.prepare_specialist(self.task, native_available=False,
                                            delegation_authorized=True)
        changed = dict(self.task, objective="Different task")
        with self.assertRaisesRegex(GateError, "task changed"):
            self.adapter.execute_specialist(changed, p.token)

    def test_no_replay_after_execute(self):
        p = self.adapter.prepare_specialist(self.task, native_available=False,
                                            delegation_authorized=True)
        self.adapter.execute_specialist(self.task, p.token)
        with self.assertRaisesRegex(GateError, "already-used"):
            self.adapter.execute_specialist(self.task, p.token)

    def test_incomplete_child_delivery_blocks(self):
        def runner(**kw):
            return {"execution_id": "child:1", "delivery_ref": "", "artifact_ref": "artifact:a"}
        self.adapter = self.make_adapter(runner=runner)
        p = self.adapter.prepare_specialist(self.task, native_available=True,
                                            delegation_authorized=True)
        with self.assertRaisesRegex(GateError, "delivery trace"):
            self.adapter.execute_specialist(self.task, p.token)

    def test_specialist_ignoring_required_behavior_blocks_acceptance(self):
        def verify(**kw):
            return {"verified": True, "verified_rule_ids": [],
                    "evidence_refs": ["artifact:fake"]}
        self.adapter = self.make_adapter(verifier=verify)
        p = self.adapter.prepare_specialist(self.task, native_available=False,
                                            delegation_authorized=True)
        self.adapter.execute_specialist(self.task, p.token)
        with self.assertRaisesRegex(GateError, "mandatory rule"):
            self.adapter.accept_specialist_result(self.task, p.token)

    def test_independent_verifier_rejection_blocks_acceptance(self):
        self.adapter = self.make_adapter(verifier=lambda **kw: {"verified": False})
        p = self.adapter.prepare_specialist(self.task, native_available=False,
                                            delegation_authorized=True)
        self.adapter.execute_specialist(self.task, p.token)
        with self.assertRaisesRegex(GateError, "acceptance denied"):
            self.adapter.accept_specialist_result(self.task, p.token)

    def test_sequential_runner_cannot_claim_child(self):
        self.adapter = self.make_adapter(runner=lambda **kw: {
            "execution_id": "parent:task-1", "delivery_ref": "trace:x",
            "artifact_ref": "artifact:x", "child_handle": "fake"})
        p = self.adapter.prepare_specialist(self.task, native_available=False,
                                            delegation_authorized=True)
        with self.assertRaisesRegex(GateError, "sequential result"):
            self.adapter.execute_specialist(self.task, p.token)


if __name__ == "__main__":
    unittest.main()
