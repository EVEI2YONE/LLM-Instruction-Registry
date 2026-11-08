"""Pinned, path-safe package resolver. Read only the requested package."""
from __future__ import annotations

import json
import re
from pathlib import Path

PACKAGE_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class PackageResolver:
    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()
        self.registry = json.loads((self.root / "registry.json").read_text(encoding="utf8"))
        self.by_id = {p["id"]: p for p in self.registry["instruction_sets"]}

    def search(self, objective: str, limit: int = 5) -> list[dict]:
        # Registry-first lexical routing, not model inference or proof of suitability.
        # Reuse the canonical ranking implementation to avoid alternate score semantics.
        from scripts.search_registry import search
        return search(self.registry, query=objective, limit=limit)

    def pin(self, package_id: str, version: str) -> tuple[dict, Path]:
        if not PACKAGE_ID.fullmatch(package_id):
            raise ValueError("invalid package id")
        item = self.by_id.get(package_id)
        if not item or item.get("status") != "available":
            raise ValueError("unavailable package")
        if item["version"] != version:
            raise ValueError("package version is not the selected published version")
        rel = Path(item["sources"])
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError("unsafe package path")
        folder = (self.root / rel).resolve()
        if not folder.is_relative_to(self.root) or not folder.is_dir():
            raise ValueError("invalid package folder")
        return item, folder

    def resolve(self, package_id: str, version: str, action: str) -> dict:
        item, folder = self.pin(package_id, version)
        entry = folder / "SKILL.md"
        if not entry.is_file():
            raise ValueError("missing package entrypoint")
        sections = []
        manifest = folder / "manifest.json"
        if manifest.is_file():
            from scripts.lookup_sections import load_manifest, validate, lookup, safe_file
            m = load_manifest(folder)
            if m["id"] != package_id or m["version"] != version:
                raise ValueError("manifest identity mismatch")
            section_map = validate(folder, m)
            for section in lookup(section_map, action, 6):
                source = safe_file(folder, section["path"])
                sections.append({"id": section["id"], "content": source.read_text(encoding="utf8")})
        else:
            # Legacy packages remain usable during the all-49 migration.
            # The canonical compiled file is a fallback for fidelity, NOT an
            # invitation to load all other packages.
            compiled = folder / "00_compiled_instruction_set.md"
            if not compiled.is_file():
                choices = sorted(folder.glob("00_*COMPILED*.md"))
                if not choices:
                    choices = sorted(folder.glob("00_*compiled*.md"))
                compiled = choices[0] if choices else None
            if compiled is not None and compiled.is_file():
                sections = [{"id": "legacy-compiled", "content": compiled.read_text(encoding="utf8")}]
            else:
                raise ValueError("legacy package lacks required canonical compiled instructions")
        return {
            "package_id": package_id, "package_version": version,
            "entrypoint": entry.read_text(encoding="utf8"),
            "sections": sections, "registry_source": item["sources"],
            "legacy": not manifest.is_file(),
        }
