"""Guard the reusable conversation-orchestrator source against incident overfitting.

Project-specific regression fixtures may exist outside the canonical source tree.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "orchestrators/conversation/product-conversation-orchestrator/sources"
BANNED = (
    r"little[ _-]?wins",
    r"staging acceptance",
    r"onboarding workflow",
    r"management workflow",
    r"review detail",
    r"product/architecture decisions resolved",
)


class GenericInstructionBoundaryTests(unittest.TestCase):
    def test_no_project_incident_material_in_reusable_instructions(self):
        manifest = json.loads((SOURCE / "manifest.json").read_text("utf-8"))
        self.assertEqual("v1.4", manifest["version"])
        paths = [manifest["entrypoint"]["path"]] + [s["path"] for s in manifest["sections"]]
        self.assertIn("sections/procedures/deliverable-acceptance.md", paths)
        self.assertNotIn("sections/procedures/readiness-deliverable-acceptance.md", paths)
        for rel in paths:
            text = (SOURCE / rel).read_text("utf-8").lower()
            for word in BANNED:
                with self.subTest(file=rel, pattern=word):
                    self.assertIsNone(re.search(word, text), "project-specific instruction leaked")
        self.assertFalse((SOURCE / "sections/procedures/readiness-deliverable-acceptance.md").exists())

    def test_no_universal_release_or_decision_requirement(self):
        procedure = (SOURCE / "sections/procedures/deliverable-acceptance.md").read_text("utf-8")
        self.assertIn("user-requested output", procedure)
        self.assertIn("authorized owner", procedure)
        self.assertIn("Never import features, release checks", procedure)


if __name__ == "__main__":
    unittest.main()
