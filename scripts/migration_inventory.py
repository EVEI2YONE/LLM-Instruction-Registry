#!/usr/bin/env python3
"""Build or verify complete migration inventory without modifying packages."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def inventory(root: Path) -> dict:
    registry = json.loads((root / "registry.json").read_text(encoding="utf8"))
    packages = sorted(registry["instruction_sets"], key=lambda p: p["id"])
    seen = set()
    records = []
    for package in packages:
        pid = package["id"]
        if pid in seen:
            raise ValueError("duplicate registered package: " + pid)
        seen.add(pid)
        sources = root / package["sources"]
        if not sources.is_dir() or not (root / package["archive"]).is_file():
            raise ValueError("missing source/archive for " + pid)
        records.append({
            "id": pid,
            "kind": package["kind"],
            "role": package["role"],
            "baseline_version": package["version"],
            "baseline_archive": package["archive"],
            "baseline_sources": package["sources"],
            "migration_status": "pending",
            "target_source_contract": "lookup-first-v1",
            "new_version": None,
            "validation": "NOT_RUN"
        })
    return {
        "schema_version": 1,
        "baseline_ref": "6cc9c6891e274caf5ae48bdd1d8147110a488b37",
        "policy": "all registered packages; no pilot subset",
        "count": len(records),
        "packages": records,
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=ROOT)
    p.add_argument("--output", type=Path)
    p.add_argument("--verify", type=Path)
    args = p.parse_args(argv)
    try:
        obj = inventory(args.root)
        if args.verify:
            saved = json.loads(args.verify.read_text(encoding="utf8"))
            if saved != obj:
                print("migration inventory out of sync", file=sys.stderr)
                return 1
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf8")
        elif not args.verify:
            print(json.dumps(obj, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print("inventory failed: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
