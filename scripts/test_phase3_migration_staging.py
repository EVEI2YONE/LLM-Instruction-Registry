"""Stage all pending packages without declaring migration complete."""
import tempfile, unittest
from pathlib import Path
from scripts.stage_lookup_migration import stage
ROOT=Path(__file__).resolve().parent.parent
class Phase3StagingTests(unittest.TestCase):
    def test_complete_pending_inventory(self):
        before=(ROOT/"registry.json").read_bytes()
        with tempfile.TemporaryDirectory() as t:
            r=stage(ROOT,Path(t)/"candidates")
            self.assertEqual(49,r["registry_count"])
            self.assertEqual(48,r["staged"])
            self.assertEqual(0,r["migrations_completed"])
            self.assertEqual(0,r["registry_mutations"])
            self.assertTrue(all(x["integrity"]=="PASS" for x in r["packages"]))
        self.assertEqual(before,(ROOT/"registry.json").read_bytes())
    def test_no_repo_output(self):
        with self.assertRaisesRegex(ValueError,"outside repository"):
            stage(ROOT,ROOT/"dist"/"migration")
