"""Ensure existing workflow-enabled package revisions have complete, byte-identical releases."""
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPDATED_IDS = [
  "organizational-strategy-specialist",
  "product-delivery-specialist",
  "architecture-delivery-specialist",
  "engineering-execution-specialist",
  "backend-engineering-specialist",
  "frontend-engineering-specialist",
  "ai-ml-engineering-specialist",
  "qa-verification-specialist",
  "devsecops-release-specialist",
  "operations-reliability-specialist",
  "software-delivery-lifecycle",
  "idea-to-mvp-orchestrator",
  "catalog-grounded-consultant"
]

class UpdatedPackageIntegrityTests(unittest.TestCase):
    def test_source_manifest_and_archives(self):
        data = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
        packages = {x["id"]: x for x in data["instruction_sets"]}
        for ident in UPDATED_IDS:
            with self.subTest(id=ident):
                item = packages[ident]
                src = ROOT / item["sources"]
                manifest = json.loads((src / "99_manifest.json").read_text(encoding="utf-8"))
                self.assertEqual(item["version"], manifest["version"])
                self.assertEqual("04_workflow_integration.md", manifest["workflow_integration"])
                source_files = manifest.get("sources", manifest.get("source_files", []))
                self.assertIn("04_workflow_integration.md", source_files)
                expected = {ident + "/" + x.relative_to(src).as_posix(): x
                            for x in src.rglob("*") if x.is_file()}
                with zipfile.ZipFile(ROOT / item["archive"]) as z:
                    self.assertIsNone(z.testzip(), "bad ZIP CRC")
                    self.assertEqual(set(expected), set(z.namelist()))
                    for name, path in expected.items():
                        self.assertEqual(path.read_bytes(), z.read(name))
                # Retain an accessible prior-release archive rather than overwrite history.
                old = item["version"].rsplit(".", 1)[0]
                older = ROOT / item["archive"].replace("_" + item["version"] + ".zip",
                                                       "_" + old + ".zip")
                self.assertTrue(older.is_file(), "prior version archive missing")
if __name__ == "__main__":
    unittest.main()
