"""Contract smoke checks for proposed source-resolution metadata; no external dependencies."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

class SourceResolutionProposalTests(unittest.TestCase):
    def test_catalog_is_host_neutral_and_does_not_infer_access(self):
        cat = json.loads((ROOT / "references" / "external-sources.json").read_text())
        self.assertEqual(cat["schema_version"], 1)
        ids = [source["id"] for source in cat["sources"]]
        self.assertEqual(len(ids), len(set(ids)))
        registry = next(s for s in cat["sources"] if s["id"] == "llm-instruction-registry")
        self.assertEqual(registry["revision_policy"]["strategy"], "resolve-and-pin-commit")
        self.assertEqual(registry["fallback"], "unavailable-not-verified")
        self.assertEqual(registry["entrypoints"]["search_script"], "scripts/search_registry.py")
    def test_schemas_parse_and_define_required_gates(self):
        names = ["source-catalog", "generation-context-lock", "distribution-manifest"]
        for name in names:
            with self.subTest(name=name):
                spec = json.loads((ROOT / "schemas" / (name + ".schema.json")).read_text())
                self.assertEqual(spec["$schema"], "https://json-schema.org/draft/2020-12/schema")
                self.assertTrue(spec["required"])
        lock = json.loads((ROOT / "schemas/generation-context-lock.schema.json").read_text())
        self.assertIn("governance", lock["required"])
        self.assertIn("resolution", lock["required"])
        dist = json.loads((ROOT / "schemas/distribution-manifest.schema.json").read_text())
        self.assertEqual(set(dist["properties"]["variant"]["enum"]), {"portable", "connected", "prompt"})

if __name__ == "__main__":
    unittest.main()
