# Generate lookup-first source packages

Use when about to author or regenerate a package, section index, entrypoint or a specialized agent instruction set.

## Source layout

Publish one canonical package source directory, rooted under the existing registry package's `sources/` path: `SKILL.md`, `manifest.json`, human `README.md`, `agents/openai.yaml` where supported, and only relevant directories under `sections/{procedures,templates,contracts,roles,playbooks,examples,references}/`, `adapters/`, and `tools/`. Some narrow specialists legitimately fit entirely in a single `SKILL.md` with an empty `sections` array.

## Entry point

Write YAML frontmatter with lower-case stable `name`; describe use cases and exclusions (`Not for ...`). Include role identity, up to ten always-rules specific to the package, optional mode selection, action-triggered lookup table and handoff guidance. The tables are rendered/verified from the manifest, not edited separately. Do not require reading the entire compiled file up front; do not duplicate cross-package policy. For the meta generator itself, the entrypoint contains enough authority boundaries to operate if optional shared rules are unavailable.

## Section index

Use `schemas/lookup-package.schema.json` and `source_contract: lookup-first-v1`. For each section, record stable `id`, `kind`, real relative `path`, action-based `read_when`, short `summary`, `requires`, measured `words`, and `sha256`. Mark non-triggered calibration examples `reference_only: true`. Include native target adapters separately and pin any external knowledge catalog references to the inspected commit, recording access and provisional status.

Use `scripts/lookup_sections.py check <id>` to verify paths, content integrity and dependencies, `lookup <id> "task"` for prioritized matched sections and prerequisite closure, and `show <id> <section-id>` for selective retrieval *after registration*. During initial generation validate the candidate directory directly with the included package-build checks.

## Deliverables

Export the complete canonical source, manifest, generated entrypoint, tests, a real byte-equivalent versioned ZIP, and target-specific generated distribution bundles only when required by actual platform limitations. A prompt-only target receives an explicitly bounded inline artifact and an unavailable-sections list. The generator does not install an agent, deploy a website or grant subagent APIs merely by writing files.
