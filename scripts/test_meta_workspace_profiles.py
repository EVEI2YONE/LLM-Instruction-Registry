"""Meta v22: canonical sources, reproducible hosted/local distributions and historical archives."""
import json
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "orchestrators/meta/meta-llm-orchestrator"
SOURCE = META / "sources"

class MetaWorkspaceTests(unittest.TestCase):
    def test_v22_contract(self):
        m = json.loads((SOURCE / "manifest.json").read_text(encoding="utf8"))
        self.assertEqual("v22", m["version"])
        self.assertEqual("lookup-first-v1", m["source_contract"])
        self.assertEqual("unapproved-not-runtime-injected", m["common_rules_status"])
        self.assertEqual(15, len(m["sections"]))
        self.assertEqual({"hosted", "local"}, set(m["distribution_profiles"]))
        reg = json.loads((ROOT / "registry.json").read_text())
        agent = next(x for x in reg["instruction_sets"] if x["id"] == "meta-llm-orchestrator")
        self.assertEqual("v22", agent["version"])
        self.assertEqual({"hosted", "local"}, set(agent["distribution_archives"]))

    def test_canonical_manifest_and_distributions(self):
        for command in [
            [sys.executable, str(SOURCE / "tools/build_lookup_package.py"), "--check"],
            [sys.executable, str(SOURCE / "tools/build_distributions.py"), "--check", "--output", str(META)]
        ]:
            done = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(0, done.returncode, done.stdout + done.stderr)
        from importlib.util import spec_from_file_location, module_from_spec
        spec = spec_from_file_location("build_distributions", SOURCE / "tools/build_distributions.py")
        builder = module_from_spec(spec)
        spec.loader.exec_module(builder)
        payloads = builder.build_payloads(SOURCE)
        for name in ("hosted", "local"):
            with self.subTest(name=name):
                archive = META / f"meta-llm-orchestrator_v22_{name}.zip"
                self.assertTrue(archive.is_file())
                with zipfile.ZipFile(archive) as z:
                    self.assertIsNone(z.testzip())
                    self.assertEqual(set(z.namelist()), {"meta-llm-orchestrator/" + p for p in payloads[name]})
                    for path, data in payloads[name].items():
                        self.assertEqual(data, z.read("meta-llm-orchestrator/" + path))
        self.assertIn(b"## Source section:", payloads["hosted"]["HOSTED_INSTRUCTIONS.md"])
        self.assertNotIn("tools/build_lookup_package.py", payloads["hosted"])
        self.assertIn("tools/build_lookup_package.py", payloads["local"])
        self.assertFalse((META / "meta-llm-orchestrator_v22.zip").exists())

    def test_section_dependency_closure(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        from lookup_sections import validate, lookup
        sections = validate(SOURCE, json.loads((SOURCE / "manifest.json").read_text()))
        results = lookup(sections, "package and publish a versioned instruction release", 1)
        ids = [x["id"] for x in results]
        self.assertIn("package-and-publish", ids)
        self.assertIn("workspace-adaptation", ids)
        self.assertIn("source-provenance", ids)

    def test_historical_archives_preserved(self):
        for version in ("v18", "v19", "v20", "v21"):
            archive = META / f"meta-llm-orchestrator_{version}.zip"
            self.assertTrue(archive.is_file())
            with zipfile.ZipFile(archive) as z:
                self.assertIsNone(z.testzip())

if __name__ == "__main__":
    unittest.main()
