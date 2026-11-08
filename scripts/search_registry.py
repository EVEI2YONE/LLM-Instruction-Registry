#!/usr/bin/env python3
"""Offline, deterministic instruction-set discovery from registry metadata."""
from __future__ import annotations
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry.json"
ROLES = ("progenitor", "curator", "expert", "strategist", "orchestrator", "generalist")
DIRS = {"progenitor": "progenitors", "curator": "curators", "expert": "experts",
        "strategist": "strategists", "orchestrator": "orchestrators", "generalist": "generalists"}
FIELDS = ("id", "name", "description", "version", "role", "status", "readme",
          "archive", "sources", "tags", "capabilities", "domains", "aliases", "use_cases")
WEIGHTS = {"id": 12, "name": 10, "aliases": 9, "capabilities": 8,
           "use_cases": 6, "domains": 5, "tags": 4, "description": 2}


def token_set(s):
    return set(re.findall(r"[a-z0-9]+", s.casefold()))


def load(path=REGISTRY):
    with Path(path).open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict) or not isinstance(data.get("instruction_sets"), list):
        raise ValueError("Invalid registry: instruction_sets must be an array")
    return data


def validate(data, root=ROOT):
    errors = []
    if data.get("schema_version") != 3:
        errors.append("schema_version must be 3")
    seen = set()
    for i, item in enumerate(data["instruction_sets"]):
        at = f"instruction_sets[{i}]"
        if not isinstance(item, dict):
            errors.append(at + ": not an object")
            continue
        missing = [k for k in FIELDS if k not in item]
        if missing:
            errors.append(at + ": missing " + ", ".join(missing))
            continue
        ident, role = item["id"], item["role"]
        if not isinstance(ident, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ident):
            errors.append(at + ": bad ID")
            continue
        if ident in seen:
            errors.append(at + ": duplicate ID " + ident)
        seen.add(ident)
        if role not in DIRS:
            errors.append(at + ": invalid role")
            continue
        if item["status"] != "available":
            errors.append(at + ": only available entries belong in canonical registry")
        for key in ("tags", "capabilities", "domains", "aliases", "use_cases"):
            values = item[key]
            if (not isinstance(values, list) or not values
                    or any(not isinstance(v, str) or not v.strip() for v in values)):
                errors.append(at + ": invalid " + key)
            elif len(set(x.casefold() for x in values)) != len(values):
                errors.append(at + ": duplicate " + key)
        prefix = item["readme"].removesuffix("README.md")
        expected_kind = "meta-orchestrator" if role == "progenitor" else "workflow-orchestrator" if role == "orchestrator" else "specialist"
        if item.get("kind") != expected_kind:
            errors.append(at + ": invalid kind")
        if not prefix.startswith(("orchestrators/" if role in ("progenitor", "orchestrator") else "specialists/")) or not prefix.endswith(f"/{ident}/"):
            errors.append(at + ": invalid canonical location")
        for key in ("readme", "archive", "sources"):
            p = item[key]
            if not isinstance(p, str) or not p.startswith(prefix) or ".." in Path(p).parts:
                errors.append(at + ": invalid canonical " + key)
                continue
            candidate = Path(root) / p
            if key == "sources":
                if not candidate.is_dir() or not (candidate / "README.md").is_file():
                    errors.append(at + ": missing sources README")
            elif not candidate.is_file():
                errors.append(at + ": missing " + key + ": " + p)
        if item["archive"] != prefix + ident + "_" + item["version"] + ".zip":
            errors.append(at + ": archive/version mismatch")
    return errors


def score(item, query):
    query = query.casefold().strip()
    if not query:
        return 1, ["filter-only"]
    words = token_set(query)
    candidates = []
    for field, weight in WEIGHTS.items():
        values = item[field] if isinstance(item[field], list) else [item[field]]
        for value in values:
            value = value.casefold()
            if value == query or value == query.replace(" ", "-"):
                rank = weight * 5
            elif len(query) >= 3 and query in value:
                rank = weight * 3
            elif words and words <= token_set(value):
                rank = weight * 2
            else:
                shared = len(words & token_set(value))
                rank = weight * shared // len(words) if shared else 0
            if rank:
                candidates.append((rank, field))
    if not candidates:
        return 0, []
    candidates.sort(key=lambda x: (-x[0], x[1]))
    fields = list(dict.fromkeys(x[1] for x in candidates))
    return candidates[0][0] + min(len(fields) - 1, 8), fields


def search(data, query="", role=None, capability=None, domain=None, limit=20):
    output = []
    for item in data["instruction_sets"]:
        if item["status"] != "available":
            continue
        if role and item["role"].casefold() != role.casefold():
            continue
        if capability and capability.casefold() not in [x.casefold() for x in item["capabilities"]]:
            continue
        if domain and domain.casefold() not in [x.casefold() for x in item["domains"]]:
            continue
        rank, fields = score(item, query)
        if not rank:
            continue
        output.append({key: item[key] for key in
                       ("id", "name", "description", "role", "version", "readme",
                        "archive", "sources", "capabilities", "domains")}
                      | {"score": rank, "matched_fields": fields})
    output.sort(key=lambda x: (-x["score"], x["id"]))
    return output[:limit]


def facets(data):
    result = {}
    for key in ("role", "capabilities", "domains", "tags"):
        counts = Counter(v for item in data["instruction_sets"] if item["status"] == "available"
                         for v in (item[key] if isinstance(item[key], list) else [item[key]]))
        result[key] = dict(sorted(counts.items()))
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--registry", type=Path, default=REGISTRY)
    sub = ap.add_subparsers(dest="command", required=True)
    finder = sub.add_parser("search", help="Search canonical instruction sets by metadata")
    finder.add_argument("--query", default="")
    finder.add_argument("--role", choices=ROLES)
    finder.add_argument("--capability")
    finder.add_argument("--domain")
    finder.add_argument("--limit", type=int, default=20)
    finder.add_argument("--format", choices=["json", "text"], default="json")
    sub.add_parser("validate", help="Check registry metadata and existing canonical paths")
    sub.add_parser("facets", help="Enumerate roles, capabilities, domains and tags")
    args = ap.parse_args(argv)
    try:
        data = load(args.registry)
        errors = validate(data, args.registry.parent)
        if errors:
            print(json.dumps({"ok": False, "errors": errors}, indent=2), file=sys.stderr)
            return 2
        if args.command == "validate":
            print(json.dumps({"ok": True, "packages": len(data["instruction_sets"])}))
            return 0
        if args.command == "facets":
            print(json.dumps({"schema_version": 1, "facets": facets(data)}, indent=2))
            return 0
        if args.limit < 1:
            ap.error("--limit must be >= 1")
        results = search(data, query=args.query, role=args.role,
                         capability=args.capability, domain=args.domain, limit=args.limit)
        if args.format == "text":
            for r in results:
                print(f'{r["score"]:3}  {r["name"]}: {r["readme"]}  [{", ".join(r["matched_fields"])}]')
        else:
            print(json.dumps({"schema_version": 1, "query": args.query,
                              "filters": {"role": args.role, "capability": args.capability,
                                          "domain": args.domain},
                              "count": len(results), "results": results}, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
