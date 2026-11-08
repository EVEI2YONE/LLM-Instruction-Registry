#!/usr/bin/env python3
"""Deterministic section lookup for lookup-first package manifests.

Legacy packages remain discoverable via search_registry.py but deliberately
do not pretend to have a section index until migrated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
WORDS = re.compile(r"[a-z0-9]+")


def tokens(s: str) -> set[str]:
    return set(WORDS.findall(s.lower()))


def safe_file(base: Path, relative: str) -> Path:
    """Allow only existing regular files below the canonical package root."""
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError("unsafe section path: " + relative)
    base_real = base.resolve()
    resolved = (base_real / path).resolve()
    if not resolved.is_relative_to(base_real) or not resolved.is_file():
        raise ValueError("missing or escaping section path: " + relative)
    return resolved


def find_package(root: Path, package_id: str) -> Path:
    if not ID.fullmatch(package_id):
        raise ValueError("invalid package id")
    registry = json.loads((root / "registry.json").read_text(encoding="utf8"))
    matches = [p for p in registry["instruction_sets"] if p["id"] == package_id]
    if len(matches) != 1:
        raise ValueError("package not registered: " + package_id)
    folder = safe_directory(root, matches[0]["sources"])
    return folder


def safe_directory(root: Path, relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("unsafe package directory")
    base = root.resolve()
    resolved = (base / path).resolve()
    if not resolved.is_relative_to(base) or not resolved.is_dir():
        raise ValueError("missing or escaping package directory")
    return resolved


def load_manifest(folder: Path) -> dict:
    path = folder / "manifest.json"
    if not path.is_file():
        raise ValueError("legacy package lacks lookup-first manifest: " + str(folder))
    data = json.loads(path.read_text(encoding="utf8"))
    if data.get("source_contract") != "lookup-first-v1":
        raise ValueError("unsupported source_contract")
    if not ID.fullmatch(str(data.get("id", ""))):
        raise ValueError("invalid manifest id")
    if not isinstance(data.get("sections"), list):
        raise ValueError("sections must be array")
    return data


def validate(folder: Path, manifest: dict) -> dict:
    if not safe_file(folder, "SKILL.md"):
        raise ValueError("missing SKILL.md")
    sections = {}
    for section in manifest["sections"]:
        sid = section.get("id")
        if not isinstance(sid, str) or not ID.fullmatch(sid) or sid in sections:
            raise ValueError("invalid or duplicate section id: " + str(sid))
        path = section.get("path", "")
        if not isinstance(path, str) or not path.startswith("sections/"):
            raise ValueError("section not inside sections/: " + str(path))
        source = safe_file(folder, path)
        content = source.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if section.get("sha256") and digest != section["sha256"]:
            raise ValueError("sha256 mismatch for " + sid)
        if "words" in section and len(content.decode("utf8").split()) != section["words"]:
            raise ValueError("word-count mismatch for " + sid)
        if not section.get("read_when") and not section.get("reference_only"):
            raise ValueError("unreachable non-reference section " + sid)
        sections[sid] = section
    for sid, section in sections.items():
        for req in section.get("requires", []):
            if req not in sections:
                raise ValueError("missing dependency " + req + " for " + sid)
    for sid in sections:
        dependency_order([sid], sections)
    return sections


def dependency_order(ids: list[str], sections: dict) -> list[str]:
    ordered, visiting, complete = [], set(), set()

    def visit(sid: str) -> None:
        if sid not in sections:
            raise ValueError("unknown section: " + sid)
        if sid in visiting:
            raise ValueError("circular section dependency: " + sid)
        if sid in complete:
            return
        visiting.add(sid)
        for dependency in sections[sid].get("requires", []):
            visit(dependency)
        visiting.remove(sid)
        complete.add(sid)
        ordered.append(sid)

    for sid in ids:
        visit(sid)
    return ordered


def lookup(sections: dict, query: str, limit: int = 5) -> list[dict]:
    words = tokens(query)
    ranked = []
    for sid, section in sections.items():
        phrases = section.get("read_when", [])
        score = max([len(words & tokens(p)) * 4 for p in phrases] + [0])
        score += len(words & tokens(section.get("summary", "")))
        score += len(words & tokens(sid))
        if words and not score:
            continue
        ranked.append((score, sid))
    ranked.sort(key=lambda x: (-x[0], x[1]))
    matches = [sid for _, sid in ranked[:limit]]
    return [
        {"id": sid, "path": sections[sid]["path"],
         "words": sections[sid].get("words"),
         "requires": sections[sid].get("requires", [])}
        for sid in dependency_order(matches, sections)
    ]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    lk = commands.add_parser("lookup")
    lk.add_argument("package")
    lk.add_argument("query")
    lk.add_argument("--limit", type=int, default=5)
    sh = commands.add_parser("show")
    sh.add_argument("package")
    sh.add_argument("section_id")
    check = commands.add_parser("check")
    check.add_argument("package")
    args = parser.parse_args(argv)
    try:
        folder = find_package(args.root, args.package)
        manifest = load_manifest(folder)
        if manifest["id"] != args.package:
            raise ValueError("manifest does not match requested package")
        sections = validate(folder, manifest)
        if args.command == "lookup":
            if args.limit < 1:
                raise ValueError("limit must be positive")
            print(json.dumps({"package": args.package, "version": manifest["version"],
                              "sections": lookup(sections, args.query, args.limit)}, indent=2))
        elif args.command == "show":
            if args.section_id not in sections:
                raise ValueError("unknown section " + args.section_id)
            print(safe_file(folder, sections[args.section_id]["path"]).read_text(encoding="utf8"))
        else:
            print(json.dumps({"ok": True, "package": args.package, "count": len(sections)}))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
