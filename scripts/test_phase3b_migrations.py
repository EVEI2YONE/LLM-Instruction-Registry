"""Phase 3B package integrity and source migration traceability (not behavior tests)."""
import hashlib
import json
import unittest
import zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def digest(b):return hashlib.sha256(b).hexdigest()
class Phase3BStaticTests(unittest.TestCase):
    def test_registry_inventory_and_archive_integrity(self):
        registry=json.loads((ROOT/"registry.json").read_text())["instruction_sets"]
        inventory=json.loads((ROOT/"migration/inventory.json").read_text())["packages"]
        rows={x["id"]:x for x in inventory}
        self.assertEqual(49,len(registry))
        self.assertEqual(set(rows),{x["id"] for x in registry})
        migrated=0
        for pkg in registry:
            with self.subTest(package=pkg["id"]):
                src=ROOT/pkg["sources"]
                manifest=json.loads((src/"manifest.json").read_text())
                self.assertEqual(pkg["id"],manifest["id"])
                self.assertEqual(pkg["version"],manifest["version"])
                self.assertEqual("lookup-first-v1",manifest["source_contract"])
                names={p.relative_to(src).as_posix() for p in src.rglob("*") if p.is_file()}
                self.assertEqual(names,set(manifest["sources"]))
                for sec in manifest["sections"]:
                    data=(src/sec["path"]).read_bytes()
                    self.assertEqual(digest(data),sec["sha256"])
                    self.assertEqual(len(data.decode("utf8").split()),sec["words"])
                    self.assertLessEqual(sec["words"],1500)
                with zipfile.ZipFile(ROOT/pkg["archive"]) as z:
                    self.assertIsNone(z.testzip())
                    self.assertEqual({pkg["id"]+"/"+name for name in names},set(z.namelist()))
                    for name in names:
                        self.assertEqual((src/name).read_bytes(),z.read(pkg["id"]+"/"+name))
                record=rows[pkg["id"]]
                if pkg["id"]=="meta-llm-orchestrator":continue
                migrated+=1
                self.assertEqual("completed",record["migration_status"])
                self.assertEqual(pkg["version"],record["new_version"])
                self.assertTrue((ROOT/record["baseline_archive"]).is_file())
                trace=json.loads((src/"MIGRATION_TRACEABILITY.json").read_text())
                self.assertEqual("NOT_RUN",trace["semantic_equivalence"])
                self.assertEqual("NOT_VERIFIED",trace["owner_approval"])
                for m in trace["files"]:
                    data=b"".join((src/x).read_bytes() for x in m["indexed_sections"])
                    self.assertEqual(m["sha256"],digest(data))
                    self.assertEqual(m["reconstructed_sha256"],digest(data))
                    if m["source"]!="SKILL.md":
                        self.assertEqual((src/m["source"]).read_bytes(),data)
        self.assertEqual(48,migrated)
