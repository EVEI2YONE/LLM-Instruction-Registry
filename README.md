# LLM Instruction Registry

A versioned catalog of standalone LLM instruction sets. **Meta-LLM Orchestrator v18** is the foundational progenitor. Each package has its own folder under `instruction-sets/`, with a ZIP, sources, and explanatory README.

## Lookup catalog

| Instruction set | Version | Purpose | Archive |
|---|---|---|---|
| [Meta-LLM Orchestrator](instruction-sets/meta-llm-orchestrator/README.md) | v18 | Foundational progenitor for composing and coordinating specialized LLM instruction sets. | [meta-llm-orchestrator_v18.zip](instruction-sets/meta-llm-orchestrator/meta-llm-orchestrator_v18.zip) |
| [App Planning](instruction-sets/app-planning/README.md) | v1 | Business, product, architecture, stack, research, and engineering handoff planning. | [app-planning_v1.zip](instruction-sets/app-planning/app-planning_v1.zip) |
| [Business App Idea](instruction-sets/business-app-idea/README.md) | v1 | Instruction set for shaping business application concepts into actionable plans. | [business-app-idea_v1.zip](instruction-sets/business-app-idea/business-app-idea_v1.zip) |
| [Coding Partner / Mentor / Teacher](instruction-sets/coding-partner-mentor-teacher/README.md) | v1 | Engineering assistance, debugging, code review, and practical mentorship. | [coding-partner-mentor-teacher_v1.zip](instruction-sets/coding-partner-mentor-teacher/coding-partner-mentor-teacher_v1.zip) |
| [Feature Extension Planning Council](instruction-sets/feature-extension-planning-council/README.md) | v1 | Council-based feature planning, scope, architecture, risk, and implementation handoffs. | [feature-extension-planning-council_v1.zip](instruction-sets/feature-extension-planning-council/feature-extension-planning-council_v1.zip) |
| [General-Purpose ChatGPT Conversations](instruction-sets/general-purpose-chatgpt-conversations/README.md) | v2 | Everyday ChatGPT conversation, efficient answers, research/source filtering, and self-healing corrections. | [general-purpose-chatgpt-conversations_v2.zip](instruction-sets/general-purpose-chatgpt-conversations/general-purpose-chatgpt-conversations_v2.zip) |
| [Psychology Advice & Research](instruction-sets/psychology-advice-research/README.md) | v1 | Psychology education, non-clinical advice, and evidence-aware research synthesis. | [psychology-advice-research_v1.zip](instruction-sets/psychology-advice-research/psychology-advice-research_v1.zip) |
| [SOLID Visual Architecture](instruction-sets/solid-visual-architecture/README.md) | v1 | Architecture visualization and SOLID-oriented design instruction system. | [solid-visual-architecture_v1.zip](instruction-sets/solid-visual-architecture/solid-visual-architecture_v1.zip) |
| [UI/UX Design System Architect](instruction-sets/ui-ux-design-system-architect/README.md) | v1.1 | Catalog-first design knowledge audits, components, accessibility and UX migration plans. | [ui-ux-design-system-architect_v1.1.zip](instruction-sets/ui-ux-design-system-architect/ui-ux-design-system-architect_v1.1.zip) |
| [Technical Research Project Instructions](instruction-sets/technical-research-project-instructions/README.md) | v2 | Evidence-backed technical research, architecture consulting, and teaching. | [technical-research-project-instructions_v2.zip](instruction-sets/technical-research-project-instructions/technical-research-project-instructions_v2.zip) |

For programmatic lookup, use [registry.json](registry.json). Every listed archive is checked in and has a matching internal top-level directory.

## Folder convention

```text
instruction-sets/
  <instruction-set>/
    README.md
    <instruction-set>_vN.zip
    sources/
      README.md
```

Read the package README before loading an archive; individual instruction systems may have different entrypoints or prerequisites.

## Canonical and pending packages

- **Meta-LLM Orchestrator v18** remains the progenitor independently of later derivatives.
- **AI Knowledge Atlas**: owner-designated archive `AI-Knowledge-Atlas-40-Project-Sources.zip` is **not uploaded**; no reconstructed or placeholder archive is published.
- Archive versions remain explicit in their filenames and metadata. See [CONTRIBUTING.md](CONTRIBUTING.md) to add an instruction set.

## Agent instructions — registering and maintaining instruction sets

These instructions apply to any coding agent or automation that adds, imports, updates, or repackages an instruction set in this repository. **Use this procedure for future packages**, not the one-time legacy migration script.

### 1. Inspect and identify

1. Read this README, [CONTRIBUTING.md](CONTRIBUTING.md), [registry.json](registry.json), and the relevant package README before changing files.
2. Enumerate existing package IDs, versions, ZIPs, and sources. Check for a matching instruction set before creating a new one; avoid duplicate names or competing canonical releases.
3. Choose a stable, lowercase kebab-case folder ID (e.g., `product-strategy-director`). Record the source archive name, version, provenance, and any dependencies. Do not guess missing provenance or silently overwrite releases.
4. Treat **Meta-LLM Orchestrator v18** as the progenitor; retain its separate identity. Derived or specialized instructions should have separate folders under `instruction-sets/`.

### 2. Extract, normalize, and repackage

**Do not simply rename or copy an existing ZIP to a new filename.** The **internal root folder** must match the cleaned package ID.

1. Extract the source ZIP into a temporary working directory, checking that it is readable and contains no unsafe absolute paths, `..` traversal, or symlinks.
2. Inspect the extracted entries. If the archive has a single enclosing folder, use its contents; otherwise use all extracted top-level content. Preserve the relative file hierarchy and file contents.
3. Rehome the content beneath a single folder named `<instruction-set-id>/`. Do not introduce accidental double nesting such as `<id>/<old-folder>/...`.
4. Create a **new ZIP** named `<instruction-set-id>_vN.zip` that includes this enclosing folder, so extraction produces `<instruction-set-id>/...`. Preserve the real version rather than inventing a newer one.
5. Verify the new ZIP opens successfully, passes a CRC/integrity test, includes the expected number of files, and contains **only** members beneath the normalized folder. Compare extracted source content with the new ZIP's content to detect unintended file changes.
6. Never replace an original archive with a fabricated, incomplete, or unverified ZIP. If only a source tree is available, assemble a ZIP from the verified source tree and explicitly document that provenance.

### 3. Create the discoverable package

Every instruction set must have:

```text
instruction-sets/
  <instruction-set-id>/
    ├── README.md
    ├── <instruction-set-id>_vN.zip
    └── sources/
        └── README.md
```

- Package `README.md`: Explain **purpose, audience, capabilities, boundaries, how to load/use it, version, ZIP link, source provenance, and links to key entrypoints**.
- `sources/`: Keep relevant original instruction files, manifests, reference material, and provenance, retaining useful subfolders. Add a `sources/README.md` explaining what is present and what is unavailable. Do not duplicate or manufacture sources.
- Do not put distinct instruction systems in a progenitor or unrelated package folder merely because they were created there historically.

### 4. Register for lookup

1. Add or update **one canonical record**, using paths prefixed with `instruction-sets/`, in [registry.json](registry.json): `id`, `name`, `description`, `version`, `role`, `tags`, `status`, `readme`, `archive`, and `sources`.
2. Update the **Lookup catalog** in this README with the package purpose, version, and valid paths. Keep labels useful for both people and search/lookup agents.
3. Register only files that actually exist. Mark unavailable packages (such as the pending AI Knowledge Atlas archive) as pending in prose, **not** as downloadable or available records.
4. When publishing a new version, update its canonical filename and metadata together. Retain older releases only in clearly labeled history if required; do not expose multiple releases as simultaneously canonical.

### 5. Validate before opening or merging a PR

- Confirm every `registry.json` record resolves to an existing README, ZIP, and sources directory.
- Confirm the filename and internal ZIP root match the package ID and that the registered version matches the filename.
- Test every changed ZIP's integrity and compare extracted file contents with the source files where available.
- Check that no unrelated packages, source files, or history were accidentally deleted.
- Review root and nested README links, manifest references, and source provenance.
- In the PR, state which packages changed, which ZIPs were **actually repackaged**, validation performed, remaining gaps, and any migrations required for old paths.
- If binary ZIPs cannot be accessed or built, **stop short of claiming migration complete**. Document the blocker and leave the PR in draft until verified artifacts are committed.

### One-time migration versus future additions

The `scripts/rebuild_registry.py` script was designed for the original `packages/` hierarchy and is **not a general-purpose import command**. Do not rerun it after the legacy hierarchy has been removed; it intentionally expects legacy inputs and rebuilds the catalog. For future packages, apply the procedure above to only the new or changed instruction set.
