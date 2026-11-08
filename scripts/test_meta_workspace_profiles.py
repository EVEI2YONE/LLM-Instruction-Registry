"""Meta v22 lookup-first package, adapters and historical archive verification."""
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
        self.assertTrue(m["self_heal_required"])
        self.assertEqual(13, len(m["sections"]))
        for x in ("local-codex.md", "local-claude-code.md", "hosted-chat.md",
                  "chatgpt-project.md", "grok-bot.md", "generic-portable.md"):
            self.assertTrue((SOURCE / "adapters" / x).is_file())
        self.assertFalse((SOURCE / "00_compiled_instruction_set.md").exists())
        reg = json.loads((ROOT / "registry.json").read_text())
        self.assertEqual("v22", next(x["version"] for x in reg["instruction_sets"]
                                     if x["id"] == "meta-llm-orchestrator"))

    def test_entrypoint_manifest_and_zip(self):
        script = SOURCE / "tools/build_lookup_package.py"
        archive = META / "meta-llm-orchestrator_v22.zip"
        done = subprocess.run([sys.executable, str(script), "--check", "--archive",
                               str(archive)], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, done.returncode, done.stdout + done.stderr)
        with zipfile.ZipFile(archive) as z:
            expected = {"meta-llm-orchestrator/" + f.relative_to(SOURCE).as_posix(): f
                        for f in SOURCE.rglob("*") if f.is_file()}
            self.assertIsNone(z.testzip())
            self.assertEqual(set(expected), set(z.namelist()))
            for name, path in expected.items():
                self.assertEqual(path.read_bytes(), z.read(name))

    def test_section_dependency_closure(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        from lookup_sections import validate, lookup
        secs = validate(SOURCE, json.loads((SOURCE / "manifest.json").read_text()))
        found = lookup(secs, "package and publish a versioned instruction release", 1)
        ids = [x["id"] for x in found]
        self.assertIn("package-and-publish", ids)
        self.assertIn("workspace-adaptation", ids)
        self.assertIn("source-provenance", ids)

    def test_historical_archives_preserved(self):
        for version in ("v18", "v19", "v20", "v21"):
            path = META / ("meta-llm-orchestrator_" + version + ".zip")
            self.assertTrue(path.is_file())
            with zipfile.ZipFile(path) as z:
                self.assertIsNone(z.testzip())

if __name__ == "__main__":
    unittest.main()
