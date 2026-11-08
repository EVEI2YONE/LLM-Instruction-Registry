"""Integrity checks for newly authored lifecycle instruction packages."""
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEW_IDS = [
  "product-lifecycle-orchestrator",
  "specialist-consultation-coordinator",
  "engineering-review-coordinator",
  "release-governance-coordinator",
  "technical-product-manager",
  "backlog-story-refinement-specialist",
  "business-feasibility-analyst",
  "market-competitive-research-specialist",
  "ux-research-journey-specialist",
  "ui-ux-product-designer",
  "accessibility-usability-reviewer",
  "solution-cloud-resource-architect",
  "data-architecture-specialist",
  "security-architecture-specialist",
  "api-integration-design-specialist",
  "database-migration-specialist",
  "integration-engineering-specialist",
  "pragmatic-pr-reviewer",
  "test-automation-specialist",
  "security-compliance-reviewer",
  "product-analytics-specialist",
  "incident-root-cause-analyst",
  "knowledge-context-steward",
  "decision-traceability-auditor"
]

class NewPackageIntegrityTests(unittest.TestCase):
    def test_new_packages_in_registry(self):
        reg = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
        found = {p["id"]: p for p in reg["instruction_sets"]}
        self.assertEqual(len(NEW_IDS), len(set(NEW_IDS)))
        for ident in NEW_IDS:
            with self.subTest(package=ident):
                p = found[ident]
                src = ROOT / p["sources"]
                self.assertTrue((src / "SKILL.md").is_file())
                self.assertTrue((src / "03_self_heal.md").is_file())
                self.assertTrue((src / "99_manifest.json").is_file())
                with zipfile.ZipFile(ROOT / p["archive"]) as z:
                    self.assertIsNone(z.testzip(), "bad CRC")
                    expected = {ident + "/" + str(x.relative_to(src)).replace("\\", "/"): x
                                for x in src.rglob("*") if x.is_file()}
                    self.assertEqual(set(expected), set(z.namelist()))
                    for name, path in expected.items():
                        self.assertEqual(path.read_bytes(), z.read(name))
if __name__ == "__main__":
    unittest.main()
