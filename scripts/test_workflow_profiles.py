"""Validate proposed workflow profiles and capability ownership contracts."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

class WorkflowContractsTests(unittest.TestCase):
    def test_scaffold_profiles(self):
        paths = list((ROOT / "workflows").rglob("profile.json"))
        self.assertGreaterEqual(len(paths), 17)
        for path in paths:
            with self.subTest(path=str(path)):
                o = json.loads(path.read_text(encoding="utf-8"))
                if o.get("status") != "scaffold":
                    continue  # Legacy published profiles use a different compatible schema.
                stages = o["stages"]
                ids = {x["id"] for x in stages}
                self.assertEqual(len(ids), len(stages))
                for stage in stages:
                    self.assertIn(stage["pattern"], {"sequential","parallel","council","conditional","feedback","approval"})
                    self.assertTrue(set(stage.get("depends_on", [])) <= ids)
                    self.assertNotIn(stage["id"], stage.get("depends_on", []))
                    if stage["pattern"] == "approval":
                        self.assertTrue(stage.get("approval_required"))
                matrix = json.loads((path.parent / "responsibilities.json").read_text(encoding="utf-8"))
                self.assertEqual(path.parent.name, matrix["workflow_id"])
                self.assertTrue(matrix["assignments"])
                for row in matrix["assignments"]:
                    self.assertTrue(row["owner"])
                    self.assertTrue(row["approver"]["required_when"])

if __name__ == "__main__":
    unittest.main()
