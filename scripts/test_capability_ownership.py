"""Validate workflow-local responsibility declarations without external dependencies."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIRS = [
    "workflows/planning/backlog-refinement",
    "workflows/engineering/pragmatic-pr-review",
    "workflows/shared/specialist-consultation",
    "workflows/shared/approval-governance",
    "workflows/strategic/organization-idea-to-mvp",
    "workflows/engineering/software-delivery-lifecycle",
    "workflows/shared/catalog-consultation",
]

class OwnershipTests(unittest.TestCase):
    def test_models(self):
        policies = json.loads((ROOT / "governance/capability-ownership/ownership-policies.json").read_text())
        self.assertTrue(policies["single_owner_per_artifact"])
        self.assertIn("merge", policies["human_only_approvals"])

    def test_local_matrices(self):
        registry = json.loads((ROOT / "registry.json").read_text())
        caps = {c for agent in registry["instruction_sets"] for c in agent["capabilities"]}
        for d in DIRS:
            with self.subTest(workflow=d):
                matrix = json.loads((ROOT / d / "responsibilities.json").read_text())
                self.assertEqual(d.rsplit("/", 1)[1], matrix["workflow_id"])
                seen = set()
                for item in matrix["assignments"]:
                    self.assertNotIn(item["artifact"], seen)
                    seen.add(item["artifact"])
                    self.assertIsInstance(item["owner"], str)
                    self.assertTrue(item["owner"])
                    # Existing capabilities are preferred; proposals can be unresolved until
                    # the specialist package is published, but do not silently grant authority.
                    self.assertTrue(item["approver"]["authority"])
                    self.assertTrue(item["approver"]["required_when"])
                    self.assertIsInstance(item["reviewers"], list)
                    self.assertGreater(len(caps), 0)

if __name__ == "__main__":
    unittest.main()
