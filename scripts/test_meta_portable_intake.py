"""Deterministic portable Meta-LLM intake contract: no model/tool claims."""
import importlib.util
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PKG = ROOT / "orchestrators/meta/meta-llm-orchestrator-portable"
SOURCE = PKG / "sources"
spec = importlib.util.spec_from_file_location("meta_portable_intake", SOURCE / "tools/intake_gate.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

class PortableIntakeTests(unittest.TestCase):
    def test_destination_missing_asks_once(self):
        got = gate.decide({"purpose": "generate_agent", "registry_resolution": "REUSE_UNCHANGED"})
        self.assertEqual("ASK_DESTINATION", got["status"])
        self.assertIn("Where will you use", got["question"])

    def test_known_destination_not_reasked(self):
        got = gate.decide({"purpose": "generate_agent", "execution_destination": "local-agent",
                           "registry_resolution": "CREATE_NEW", "source_loading_mode": "verified_lookup"})
        self.assertEqual("READY", got["status"])
        self.assertIsNone(got["question"])
        self.assertEqual("local-agent", got["destination"])

    def test_target_not_inferred_from_generator(self):
        got = gate.decide({"purpose": "generate_agent", "generator_host": "chatgpt-project"})
        self.assertEqual("ASK_DESTINATION", got["status"])

    def test_registry_first(self):
        got = gate.decide({"purpose": "generate_agent", "execution_destination": "api-application",
                           "source_loading_mode": "injected"})
        self.assertEqual("ASK_REGISTRY_DECISION", got["status"])

    def test_explicit_reuse_with_adaptation(self):
        got = gate.decide({"purpose": "adapt_agent", "execution_destination": "hosted-assistant",
                           "registry_resolution": "REUSE_UNCHANGED", "source_loading_mode": "injected",
                           "registry_write_authority": "unauthorized"})
        self.assertEqual("READY", got["status"])
        self.assertEqual("ADAPT_EXISTING", got["adaptation_action"])
        self.assertEqual("unauthorized", got["registry_write_authority"])

    def test_loading_is_independent(self):
        got = gate.decide({"purpose": "generate_agent", "execution_destination": "chatgpt-project",
                           "registry_resolution": "REUSE_UNCHANGED"})
        self.assertEqual("ASK_LOADING_MODE", got["status"])

    def test_blocked_resolution(self):
        got = gate.decide({"purpose": "generate_agent", "execution_destination": "local-agent",
                           "registry_resolution": "BLOCKED", "source_loading_mode": "verified_lookup"})
        self.assertEqual("BLOCKED", got["status"])

    def test_source_only_skips_destination(self):
        got = gate.decide({"purpose": "authoring_source_only"})
        self.assertEqual("REVIEW_ONLY", got["status"])

    def test_archive_source_equivalence(self):
        manifest = json.loads((SOURCE / "manifest.json").read_text(encoding="utf-8"))
        archive = PKG / "meta-llm-orchestrator-portable_v1.0.0-candidate.zip"
        with zipfile.ZipFile(archive) as z:
            expected = {"meta-llm-orchestrator-portable/" + p for p in manifest["sources"]}
            self.assertEqual(expected, set(z.namelist()))
            self.assertIsNone(z.testzip())
            for path in manifest["sources"]:
                self.assertEqual((SOURCE / path).read_bytes(),
                                 z.read("meta-llm-orchestrator-portable/" + path))
if __name__ == "__main__":
    unittest.main()
