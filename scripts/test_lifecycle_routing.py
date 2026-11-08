"""Static routing integrity: do not dispatch to nonexistent workflow IDs."""
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

class LifecycleRoutingTests(unittest.TestCase):
    def test_primary_routes_are_grounded(self):
        registry = json.loads((ROOT / "registry.json").read_text())
        packages = {x["id"]: x for x in registry["instruction_sets"]}
        self.assertEqual("primary-orchestrator", packages["product-lifecycle-orchestrator"]["kind"])
        self.assertEqual("v21", packages["meta-llm-orchestrator"]["version"])
        config = json.loads((ROOT / "orchestrators/primary/product-lifecycle-orchestrator/routing.json").read_text())
        self.assertEqual("available", config["status"])
        workflows = {json.loads(p.read_text())["id"] for p in (ROOT / "workflows").rglob("profile.json")}
        for route in config["routes"]:
            with self.subTest(intent=route["intent"]):
                self.assertIn(route["workflow"], workflows)
        self.assertIn("direct-specialist", config["decisions"])
        self.assertIn("human-escalation", config["decisions"])
if __name__ == "__main__":
    unittest.main()
