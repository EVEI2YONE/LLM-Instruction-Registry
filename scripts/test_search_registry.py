"""Deterministic metadata discovery smoke tests; run with unittest discover."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from search_registry import facets, load, search, validate

ROOT = Path(__file__).resolve().parent.parent
DATA = load(ROOT / "registry.json")


class RegistryDiscoveryTests(unittest.TestCase):
    def test_registry_valid(self):
        self.assertEqual([], validate(DATA, ROOT))

    def test_unique_canonical_ids(self):
        ids = [x["id"] for x in DATA["instruction_sets"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_exact_lookup(self):
        self.assertEqual("ai-knowledge-atlas", search(DATA, "ai-knowledge-atlas")[0]["id"])

    def test_alias_lookup(self):
        self.assertEqual("coding-partner-mentor-teacher", search(DATA, "coding mentor")[0]["id"])

    def test_filtered_curator(self):
        matches = search(DATA, role="curator", capability="catalog-maintenance")
        self.assertEqual(["ai-knowledge-atlas"], [x["id"] for x in matches])

    def test_domain_filter(self):
        matches = search(DATA, domain="psychology")
        self.assertEqual(["psychology-advice-research"], [x["id"] for x in matches])

    def test_facets(self):
        self.assertEqual(1, facets(DATA)["role"]["progenitor"])

    def test_unmatched_query(self):
        self.assertEqual([], search(DATA, "frobnicate-quantum-banana"))

    def test_deterministic_results(self):
        self.assertEqual(search(DATA, "research"), search(DATA, "research"))

    def test_limit(self):
        self.assertEqual(2, len(search(DATA, limit=2)))

    def test_bad_path_detected(self):
        altered = copy.deepcopy(DATA)
        altered["instruction_sets"][0]["archive"] = "bad/path.zip"
        self.assertTrue(any("invalid canonical archive" in x for x in validate(altered, ROOT)))


if __name__ == "__main__":
    unittest.main()
