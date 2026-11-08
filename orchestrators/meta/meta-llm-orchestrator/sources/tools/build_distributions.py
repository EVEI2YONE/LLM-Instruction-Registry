#!/usr/bin/env python3
"""Build exactly two reproducible Meta-LLM v22 ZIPs from one canonical source.

No network access or runtime shell is needed to use the hosted distribution.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

SOURCE = Path(__file__).resolve().parent.parent
ROOT_NAME = "meta-llm-orchestrator"
ZIP_DATE = (1980, 1, 1, 0, 0, 0)
VERSION = "v22"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canon_json(value) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf8")


def safe_read(root: Path, rel: str) -> bytes:
    path = Path(rel)
    if path.is_absolute() or ".." in path.parts or "\\" in rel:
        raise ValueError("unsafe path " + rel)
    full = (root / path).resolve()
    if not full.is_relative_to(root.resolve()) or not full.is_file() or full.is_symlink():
        raise ValueError("unavailable or escaped file " + rel)
    return full.read_bytes()


def source_files(root: Path) -> dict[str, bytes]:
    m = json.loads(safe_read(root, "manifest.json"))
    if m["id"] != ROOT_NAME or m["version"] != VERSION:
        raise ValueError("expected canonical Meta-LLM v22")
    declared = set(m["sources"])
    actual = set()
    for f in root.rglob("*"):
        if f.is_symlink():
            raise ValueError("source symlink forbidden")
        if f.is_file():
            actual.add(f.relative_to(root).as_posix())
    if actual != declared:
        raise ValueError("canonical source inventory drift")
    return {path: safe_read(root, path) for path in sorted(declared)}


def build_payloads(root: Path) -> dict[str, dict[str, bytes]]:
    sources = source_files(root)
    meta = json.loads(sources["manifest.json"])
    sections = sorted((s["path"] for s in meta["sections"]))
    if len(sections) != 15 or not all(s in sources for s in sections):
        raise ValueError("unexpected section inventory")
    common = ["SKILL.md", "agents/openai.yaml", "references/source-locations.json"]
    local = dict(sources)  # Complete offline indexed sources; load procedures selectively.
    local["README-DISTRIBUTION.md"] = b"# Meta-LLM Orchestrator v22 Local\n\nStart at `SKILL.md`. Use `manifest.json` and `sections/` for lookup-first loading. The scripts are provided as source but execute only if locally authorized. Resolve repositories using `references/source-locations.json` and record pin/permission evidence; never broaden least-privilege access.\n"
    hosted_sections = ["# Meta-LLM Orchestrator v22 - Hosted: complete instruction payload", "", "This is an assembled, bounded instruction document, not a running tool. Install it in the host-supported instruction surface. The quoted source material is subject to the host instruction hierarchy; approved governance is not invented.", "", "## Canonical entrypoint", sources["SKILL.md"].decode("utf8")]
    for path in sections:
        hosted_sections += ["", "---", "", "## Source section: " + path, "", sources[path].decode("utf8")]
    for path in ["adapters/chatgpt-project.md", "adapters/hosted-chat.md", "adapters/grok-bot.md", "adapters/generic-portable.md"]:
        hosted_sections += ["", "---", "", "## Runtime adapter: " + path, "", sources[path].decode("utf8")]
    hosted_sections += ["", "---", "", "## Source location catalog", "", "```json", sources["references/source-locations.json"].decode("utf8").rstrip(), "```", "", "## Availability limits", "The full instruction *package* is present. The external registry and knowledge repositories are not embedded unless separately verified. Do not claim access to their latest contents without a connected source. Use an inline state handoff if persistent file creation or later retrieval is not verified."]
    hosted = {path: sources[path] for path in common if path != "SKILL.md"}
    hosted["SKILL.md"] = sources["SKILL.md"]
    hosted["HOSTED_INSTRUCTIONS.md"] = ("\n".join(hosted_sections).rstrip() + "\n").encode("utf8")
    hosted["README-DISTRIBUTION.md"] = b"# Meta-LLM Orchestrator v22 Hosted\n\nInject `HOSTED_INSTRUCTIONS.md` (the complete assembled agent instruction payload) through a supported hosting instruction mechanism. Do not assume scripts or lockfiles exist in the chat runtime. The external knowledge and agent registry are source references, not bundled complete knowledge repositories. If the host truncates instructions, do not claim successful installation.\n"
    def add_distribution_manifest(variant, payload):
        index = {path: digest(data) for path, data in sorted(payload.items())}
        manifest = {"schema_version": 1, "package": ROOT_NAME, "version": VERSION, "variant": variant, "source_contract": "lookup-first-v1", "canonical_entrypoint_sha256": digest(sources["SKILL.md"]), "files_sha256": index, "build_method": "deterministic-stored-zip-1980", "included_full_instruction_payload": variant == "hosted", "script_execution_required": False, "external_registry_embedded": False}
        payload["distribution-manifest.json"] = canon_json(manifest)
    add_distribution_manifest("hosted", hosted)
    add_distribution_manifest("local", local)
    return {"hosted": hosted, "local": local}


def zip_bytes(files: dict[str, bytes]) -> bytes:
    # Pure in-memory ZIP without timestamps that depend on the build host.
    from io import BytesIO
    stream = BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as z:
        for path, data in sorted(files.items()):
            zi = zipfile.ZipInfo(ROOT_NAME + "/" + path, date_time=ZIP_DATE)
            zi.compress_type = zipfile.ZIP_STORED
            zi.create_system = 3
            zi.external_attr = 0o100644 << 16
            zi.flag_bits = 0
            z.writestr(zi, data)
    return stream.getvalue()


def run(root: Path, output: Path, write: bool) -> dict:
    # Validate source hashes/manifest before rendering derived packages.
    import build_lookup_package as lookup
    lookup.check(root, json.loads(safe_read(root, "manifest.json")))
    result = {}
    for variant, contents in build_payloads(root).items():
        artifact = output / f"{ROOT_NAME}_{VERSION}_{variant}.zip"
        expected = zip_bytes(contents)
        if write:
            artifact.parent.mkdir(parents=True, exist_ok=True)
            artifact.write_bytes(expected)
        if not artifact.is_file() or artifact.read_bytes() != expected:
            raise ValueError("distribution ZIP missing or not reproducible: " + str(artifact))
        with zipfile.ZipFile(artifact) as z:
            assert z.testzip() is None
            assert len(z.namelist()) == len(contents)
            for path, data in contents.items():
                assert z.read(ROOT_NAME + "/" + path) == data
        result[variant] = {"path": str(artifact), "files": len(contents), "bytes": len(expected), "sha256": digest(expected)}
    return result


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path, default=SOURCE.parent)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        print(json.dumps({"ok": True, "variants": run(args.source.resolve(), args.output.resolve(), args.write)}, indent=2))
        return 0
    except (ValueError, KeyError, OSError, AssertionError, zipfile.BadZipFile) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
