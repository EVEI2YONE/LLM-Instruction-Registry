#!/usr/bin/env python3
"""Deterministic lookup-first entrypoint, manifest and ZIP validation/build."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKERS = [
    ("<!-- GENERATED MODES START -->", "<!-- GENERATED MODES END -->"),
    ("<!-- GENERATED TRIGGERS START -->", "<!-- GENERATED TRIGGERS END -->"),
]
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def words(txt):
    return len(txt.split())


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe(root, name):
    p = Path(name)
    if p.is_absolute() or ".." in p.parts or "\\" in name:
        raise ValueError("unsafe path: " + name)
    resolved = (root / p).resolve()
    if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        raise ValueError("missing/escaped file: " + name)
    return resolved


def files(root):
    out = []
    for f in root.rglob("*"):
        if f.is_symlink():
            raise ValueError("symlink forbidden")
        if f.is_file():
            out.append(f.relative_to(root).as_posix())
    return sorted(out)


def replace_region(txt, start, end, body):
    if txt.count(start) != 1 or txt.count(end) != 1:
        raise ValueError("missing or duplicate generated region")
    a, b = txt.index(start) + len(start), txt.index(end)
    if a >= b:
        raise ValueError("misordered generated region")
    return txt[:a] + "\n" + body.strip() + "\n" + txt[b:]


def render(txt, manifest):
    tick = chr(96)
    modes = ["| Mode | Use when | First section |", "|---|---|---|"]
    for mode in manifest.get("modes", []):
        modes.append("| %s | %s | %s |" % (mode["id"], mode["when"], tick + mode["start_with"] + tick))
    triggers = ["| About to... | Read |", "|---|---|"]
    for section in manifest["sections"]:
        if section.get("reference_only"):
            continue
        for phrase in section["read_when"]:
            triggers.append("| %s | %s |" % (phrase, tick + section["path"] + tick))
    txt = replace_region(txt, MARKERS[0][0], MARKERS[0][1], "\n".join(modes))
    return replace_region(txt, MARKERS[1][0], MARKERS[1][1], "\n".join(triggers))


def refresh(root, manifest):
    for sec in manifest["sections"]:
        content = safe(root, sec["path"]).read_bytes()
        sec["sha256"], sec["words"] = sha(content), words(content.decode("utf8"))
    entry_path = root / "SKILL.md"
    entry = render(entry_path.read_text(encoding="utf8"), manifest)
    entry_path.write_text(entry, encoding="utf8")
    manifest["entrypoint"] = {"path": "SKILL.md", "words": words(entry), "sha256": sha(entry.encode("utf8"))}
    manifest["sources"] = files(root)
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf8")


def check(root, manifest):
    if manifest["source_contract"] != "lookup-first-v1" or not ID_PATTERN.fullmatch(manifest["id"]):
        raise ValueError("invalid package identity")
    if manifest["entrypoint"]["path"] != "SKILL.md":
        raise ValueError("invalid entrypoint")
    ids, graph = set(), {}
    for sec in manifest["sections"]:
        sid = sec["id"]
        if not ID_PATTERN.fullmatch(sid) or sid in ids or not sec["path"].startswith("sections/"):
            raise ValueError("bad/duplicate section")
        if not sec.get("read_when") and not sec.get("reference_only"):
            raise ValueError("orphan section: " + sid)
        ids.add(sid)
        graph[sid] = sec.get("requires", [])
        content = safe(root, sec["path"]).read_bytes()
        if sha(content) != sec["sha256"] or words(content.decode("utf8")) != sec["words"]:
            raise ValueError("section integrity drift: " + sid)
        if sec["words"] > 1500:
            raise ValueError("oversized section: " + sid)
    done, stack = set(), set()
    def visit(sid):
        if sid in done:
            return
        if sid in stack:
            raise ValueError("dependency cycle")
        stack.add(sid)
        for dep in graph[sid]:
            if dep not in ids:
                raise ValueError("unknown dependency " + dep)
            visit(dep)
        stack.remove(sid)
        done.add(sid)
    for sid in ids:
        visit(sid)
    for mode in manifest.get("modes", []):
        safe(root, mode["start_with"])
    entry = safe(root, "SKILL.md").read_bytes()
    if sha(entry) != manifest["entrypoint"]["sha256"] or words(entry.decode("utf8")) != manifest["entrypoint"]["words"]:
        raise ValueError("entrypoint digest/word count drift")
    if render(entry.decode("utf8"), manifest) != entry.decode("utf8"):
        raise ValueError("entrypoint lookup table drift")
    if manifest["entrypoint"]["words"] > 1500:
        raise ValueError("entrypoint word budget exceeded")
    if sorted(manifest["sources"]) != files(root):
        raise ValueError("source inventory drift")
    if manifest["id"] == "meta-llm-orchestrator" and manifest["version"] != "v21":
        raise ValueError("meta version mismatch")


def check_zip(root, archive, ident):
    expected = {ident + "/" + name: (root / name).read_bytes() for name in files(root)}
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None or set(z.namelist()) != set(expected) or len(z.namelist()) != len(expected):
            raise ValueError("archive CRC/inventory mismatch")
        for name, data in expected.items():
            if z.read(name) != data:
                raise ValueError("archive content mismatch: " + name)


def write_zip(root, archive, ident):
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name in files(root):
            info = zipfile.ZipInfo(ident + "/" + name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, (root / name).read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    check_zip(root, archive, ident)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--zip", type=Path)
    parser.add_argument("--archive", type=Path)
    args = parser.parse_args(argv)
    try:
        root = args.source.resolve()
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf8"))
        if args.render:
            refresh(root, manifest)
        check(root, manifest)
        if args.zip:
            write_zip(root, args.zip, manifest["id"])
        if args.archive:
            check_zip(root, args.archive, manifest["id"])
        print(json.dumps({"ok": True, "version": manifest["version"], "sections": len(manifest["sections"]), "files": len(files(root)), "entrypoint_words": manifest["entrypoint"]["words"]}))
        return 0
    except (ValueError, KeyError, OSError, UnicodeError, zipfile.BadZipFile) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
