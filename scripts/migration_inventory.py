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


def verify_snapshot(root: Path, saved: dict) -> list[str]:
    """Keep frozen baseline archives while accepting explicitly versioned migrations."""
    data = json.loads((root / "registry.json").read_text(encoding="utf8"))
    current = {item["id"]: item for item in data["instruction_sets"]}
    baseline = {item["id"]: item for item in saved["packages"]}
    errors = []
    if len(baseline) != saved["count"] or not set(baseline).issubset(current):
        errors.append("frozen baseline package IDs or count changed")
    # New packages do not retroactively change the frozen migration baseline.
    for ident, old in baseline.items():
        item = current.get(ident)
        if item is None:
            continue
        if item["kind"] != old["kind"] or item["role"] != old["role"]:
            errors.append(ident + ": role/kind drift")
        if not (root / old["baseline_archive"]).is_file():
            errors.append(ident + ": original archive missing")
        if item["sources"] != old["baseline_sources"]:
            errors.append(ident + ": source location drift")
        status = old["migration_status"]
        if status == "pending":
            if item["version"] != old["baseline_version"] or item["archive"] != old["baseline_archive"]:
                errors.append(ident + ": untracked version upgrade")
        elif status == "completed":
            if item["version"] != old.get("new_version") or not (root / item["archive"]).is_file():
                errors.append(ident + ": completed version/archive mismatch")
        else:
            errors.append(ident + ": unsupported migration status")
    return errors


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
            errors = verify_snapshot(args.root, saved)
            if errors:
                print("migration inventory out of sync: " + "; ".join(errors), file=sys.stderr)
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
