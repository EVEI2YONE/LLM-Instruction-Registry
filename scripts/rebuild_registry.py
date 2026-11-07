#!/usr/bin/env python3
"""Rebuild root-level instruction registry from the legacy packages/ input tree.

Extract each source archive, normalize its top-level directory, and create a
fresh ZIP. Do not use a binary rename as a substitute for repackaging.
"""
from __future__ import annotations
import json
import re
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "packages"
PACKAGES = [
    ("meta-llm-orchestrator", "v18", "Meta-LLM Orchestrator",
     "Foundational progenitor for composing and coordinating specialized LLM instruction sets.",
     "packages/meta-llm-orchestrator/v18/meta_llm_orchestrator_instruction_set_v18.zip", None, "progenitor"),
    ("app-planning", "v1", "App Planning",
     "Business, product, architecture, stack, research, and engineering handoff planning.",
     "packages/app-planning/v1/app_planning_instruction_set_v1.zip", "packages/app-planning/v1", "specialized"),
    ("business-app-idea", "v1", "Business App Idea",
     "Instruction set for shaping business application concepts into actionable plans.",
     "packages/meta-llm-orchestrator/v18/business_app_idea_project_instruction_set_v1.zip", None, "specialized"),
    ("coding-partner-mentor-teacher", "v1", "Coding Partner / Mentor / Teacher",
     "Engineering assistance, debugging, code review, and practical mentorship.",
     "packages/coding-partner-mentor-teacher/v1/coding_partner_mentor_teacher_instruction_set_v1.zip",
     "packages/coding-partner-mentor-teacher/v1", "specialized"),
    ("feature-extension-planning-council", "v1", "Feature Extension Planning Council",
     "Council-based feature planning, scope, architecture, risk, and implementation handoffs.",
     None, "packages/feature-extension-planning-council/v1", "specialized"),
    ("psychology-advice-research", "v1", "Psychology Advice & Research",
     "Psychology education, non-clinical advice, and evidence-aware research synthesis.",
     "packages/psychology-advice-research/v1/psychology_advice_research_project_v1.zip",
     "packages/psychology-advice-research/v1", "specialized"),
    ("solid-visual-architecture", "v1", "SOLID Visual Architecture",
     "Architecture visualization and SOLID-oriented design instruction system.",
     "packages/meta-llm-orchestrator/v18/solid_visual_architecture_instruction_set_v1.zip", None, "specialized"),
    ("technical-research-project-instructions", "v2", "Technical Research Project Instructions",
     "Evidence-backed technical research, architecture consulting, and teaching.",
     "packages/technical-research-project-instructions/v2/technical_research_project_instructions_v2.zip",
     "packages/technical-research-project-instructions/v2", "specialized"),
]

def safe_extract(archive: zipfile.ZipFile, destination: Path) -> None:
    for item in archive.infolist():
        path = Path(item.filename)
        if path.is_absolute() or any(part == ".." for part in path.parts):
            raise ValueError(f"Unsafe archive member: {item.filename}")
        # Explicitly reject symbolic-link entries, which could escape a staging directory.
        if (item.external_attr >> 16) & 0o170000 == 0o120000:
            raise ValueError(f"Symlink archive member: {item.filename}")
    archive.extractall(destination)

def normalized_content(extracted: Path) -> Path:
    items = list(extracted.iterdir())
    if len(items) == 1 and items[0].is_dir():
        return items[0]
    return extracted

def repack(original_zip: Path | None, source_dir: Path | None, archive_path: Path, slug: str) -> int:
    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp)
        extracted = stage / "extracted"
        extracted.mkdir()
        if original_zip:
            with zipfile.ZipFile(original_zip, "r") as source:
                if source.testzip() is not None:
                    raise ValueError(f"Corrupted source ZIP: {original_zip}")
                safe_extract(source, extracted)
        elif source_dir:
            shutil.copytree(source_dir, extracted / slug)
        else:
            raise ValueError(f"No inputs to package for {slug}")
        base = normalized_content(extracted)
        with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as target:
            entries = sorted(p for p in base.rglob("*") if p.is_file())
            if not entries:
                raise ValueError(f"No files extracted for {slug}")
            for path in entries:
                rel = path.relative_to(base)
                target.write(path, arcname=(Path(slug) / rel).as_posix())
        with zipfile.ZipFile(archive_path) as check:
            if check.testzip() is not None:
                raise ValueError(f"Invalid rebuilt ZIP {archive_path}")
            assert all(n.startswith(slug + "/") for n in check.namelist()), archive_path
            assert len([n for n in check.namelist() if not n.endswith("/")]) == len(entries)
        return len(entries)

def main() -> None:
    if not LEGACY.is_dir():
        raise SystemExit("Legacy packages/ directory required; run only on a source branch with originals.")
    with tempfile.TemporaryDirectory() as tmp:
        saved = Path(tmp)
        # Keep inputs outside repository while replacing the package layout.
        shutil.copytree(LEGACY, saved / "packages")
        srcroot = saved / "packages"
        entries = []
        catalog = []
        for slug, version, name, purpose, zip_path, source_path, role in PACKAGES:
            folder = ROOT / slug
            folder.mkdir(exist_ok=True)
            original_zip = (saved / zip_path) if zip_path else None
            source_dir = (saved / source_path) if source_path else None
            if original_zip and not original_zip.is_file():
                raise FileNotFoundError(original_zip)
            if source_dir and not source_dir.is_dir():
                raise FileNotFoundError(source_dir)
            if source_dir:
                old_sources = source_dir / "sources"
                if old_sources.exists():
                    shutil.copytree(old_sources, folder / "sources", dirs_exist_ok=True)
                original_readme = source_dir / "README.md"
                if original_readme.exists():
                    (folder / "sources" / "ORIGINAL_PACKAGE_README.md").write_text(original_readme.read_text(encoding="utf-8"), encoding="utf-8")
            (folder / "sources").mkdir(exist_ok=True)
            if not (folder / "sources" / "README.md").exists():
                (folder / "sources" / "README.md").write_text(
                    f"# {name} — Sources\n\nThis directory holds source materials and provenance for the **{version}** package. "
                    "For packages originating as an archive only, additional sources may not be separately available.\n", encoding="utf-8")
            dest_name = f"{slug}_{version}.zip"
            archive = folder / dest_name
            count = repack(original_zip, source_dir, archive, slug)
            (folder / "README.md").write_text(
                f"# {name}\n\n**Version:** {version}  \n**Role:** {role}  \n"
                f"**Canonical archive:** [{dest_name}]({dest_name})\n\n"
                f"## Purpose\n\n{purpose}\n\n"
                f"## What it contains\n\nThe archive contains **{count} files** under a single "
                f"\`{slug}/\` top-level folder. Its contents were extracted from the original package "
                "and repackaged under the standardized root directory. The files inside the original package "
                "were not conceptually rewritten.\n\n"
                "## Usage\n\nDownload and extract the ZIP, then read the packaged entrypoint, "
                "README, manifest, or compiled instructions as provided. The "
                "[sources/](sources/) folder exposes reference material and provenance when available.\n\n"
                f"## Provenance\n\nOriginal archive: \`{zip_path or 'not supplied; source tree assembled into ZIP'}\`.  \n"
                f"Original source location: \`{source_path or 'archive-only'}\`.\n\n"
                "The [Meta-LLM Orchestrator](../meta-llm-orchestrator/README.md) is the foundational "
                "progenitor; other packages are independently addressable instruction systems.\n",
                encoding="utf-8")
            entries.append({"id": slug, "name": name, "description": purpose, "version": version,
                            "role": role, "tags": [word for word in re.findall(r"[a-z]+", slug) if len(word) > 2],
                            "status": "available", "readme": f"{slug}/README.md",
                            "archive": f"{slug}/{dest_name}", "sources": f"{slug}/sources/"})
            catalog.append(f"| [{name}]({slug}/README.md) | {version} | {purpose} | [{dest_name}]({slug}/{dest_name}) |")
        (ROOT / "registry.json").write_text(json.dumps({"schema_version": 1, "instruction_sets": entries}, indent=2) + "\n", encoding="utf-8")
        (ROOT / "README.md").write_text(
            "# LLM Instruction Registry\n\n"
            "A versioned catalog of standalone LLM instruction sets. **Meta-LLM Orchestrator v18** "
            "is the foundational progenitor. Each package has its own top-level folder, ZIP, "
            "sources, and explanatory README.\n\n## Lookup catalog\n\n"
            "| Instruction set | Version | Purpose | Archive |\n|---|---|---|---|\n" +
            "\n".join(catalog) +
            "\n\nFor programmatic lookup, use [registry.json](registry.json). "
            "Every listed archive is checked in and has a matching internal top-level directory.\n\n"
            "## Folder convention\n\n"
            "\`\`\`text\n<instruction-set>/\n  README.md\n  <instruction-set>_vN.zip\n  sources/\n    README.md\n\`\`\`\n\n"
            "Read the package README before loading an archive; individual instruction systems may "
            "have different entrypoints or prerequisites.\n\n"
            "## Canonical and pending packages\n\n"
            "- **Meta-LLM Orchestrator v18** remains the progenitor independently of later derivatives.\n"
            "- **AI Knowledge Atlas**: owner-designated archive "
            "\`AI-Knowledge-Atlas-40-Project-Sources.zip\` is **not uploaded**; "
            "no reconstructed or placeholder archive is published.\n"
            "- Archive versions remain explicit in their filenames and metadata. "
            "See [CONTRIBUTING.md](CONTRIBUTING.md) to add an instruction set.\n",
            encoding="utf-8")
        shutil.rmtree(LEGACY)
        print("Rebuilt", len(entries), "canonical packages, all ZIPs verified")

if __name__ == "__main__":
    main()
