"""Regression for remaining existing package upgrades, archives and workflow behavior."""
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIGINAL_VERSIONS = {
  "ai-knowledge-atlas": "v2.1",
  "app-planning": "v1",
  "backend-architecture-consultant": "v1",
  "business-app-idea": "v1",
  "coding-partner-mentor-teacher": "v1",
  "feature-extension-planning-council": "v1",
  "general-purpose-chatgpt-conversations": "v2",
  "psychology-advice-research": "v1",
  "solid-visual-architecture": "v1",
  "technical-research-project-instructions": "v2"
}

class RemainingExistingPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = {p["id"]: p for p in json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))["instruction_sets"]}

    def test_all_updated_sources_match_their_zip(self):
        for ident, prior in ORIGINAL_VERSIONS.items():
            with self.subTest(package=ident):
                p = self.registry[ident]
                self.assertNotEqual(prior, p["version"])
                src = ROOT / p["sources"]
                self.assertTrue((src / "SKILL.md").is_file())
                self.assertTrue((src / "90_workflow_integration.md").is_file())
                self.assertTrue((src / "03_self_heal.md").is_file())
                self.assertTrue((src / "agents/openai.yaml").is_file())
                old_archive = ROOT / p["archive"].replace("_" + p["version"] + ".zip", "_" + prior + ".zip")
                self.assertTrue(old_archive.is_file())
                expected = {ident + "/" + path.relative_to(src).as_posix(): path
                            for path in src.rglob("*") if path.is_file()}
                with zipfile.ZipFile(ROOT / p["archive"]) as z:
                    self.assertIsNone(z.testzip(), "CRC mismatch")
                    self.assertEqual(set(expected), set(z.namelist()))
                    for name, path in expected.items():
                        self.assertEqual(path.read_bytes(), z.read(name))
                manifest_path = src / "99_manifest.json"
                if not manifest_path.exists():
                    manifest_path = src / "06_manifest.json"
                m = json.loads(manifest_path.read_text(encoding="utf-8"))
                self.assertEqual(p["version"], m["version"])
                self.assertEqual("90_workflow_integration.md", m["workflow_integration"])
                self.assertEqual({path.relative_to(src).as_posix() for path in src.rglob("*") if path.is_file()},
                                 set(m["sources"]))

    def test_original_sparse_packages_preserve_legacy_payload(self):
        for ident in ("business-app-idea", "solid-visual-architecture"):
            with self.subTest(package=ident):
                p = self.registry[ident]
                src = ROOT / p["sources"]
                self.assertTrue(any(src.glob("legacy_original_*.zip")))
                manifest = json.loads((src / "99_manifest.json").read_text(encoding="utf-8"))
                self.assertIn("legacy_archive", manifest)

    def test_generalists_and_psychology_do_not_force_workflows(self):
        for ident in ("general-purpose-chatgpt-conversations", "psychology-advice-research",
                      "coding-partner-mentor-teacher"):
            content = (ROOT / self.registry[ident]["sources"] / "90_workflow_integration.md").read_text()
            self.assertIn("Do not automatically activate a full product lifecycle", content)
            self.assertIn("standalone", content.lower())

if __name__ == "__main__":
    unittest.main()
