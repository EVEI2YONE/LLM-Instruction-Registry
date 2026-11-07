# LLM Instruction Registry

A discoverable, version-aware collection of reusable LLM instruction systems. Each top-level folder represents **one distinct instruction set**, with a canonical ZIP, supporting sources, and a human-readable overview.

## Catalog

| Instruction set | Purpose | Current version | Availability |
| --- | --- | --- | --- |
| [Meta-LLM Orchestrator](meta-llm-orchestrator/README.md) | **Progenitor** instruction system for designing and organizing additional instruction sets | v18 | [ZIP available](meta-llm-orchestrator/meta-llm-orchestrator.zip) |
| AI Knowledge Atlas | Research-backed knowledge/instruction package; exact owner-designated archive: `AI-Knowledge-Atlas-40-Project-Sources.zip` | Undetermined | **Not uploaded**; no package folder is published yet |

For programmatic lookup, read [registry.json](registry.json). The registry lists only **available** instruction sets; planned or missing archives are not advertised as loadable.

## Repository layout

```text
/
├── README.md
├── registry.json
├── CONTRIBUTING.md
├── meta-llm-orchestrator/
│   ├── README.md
│   ├── meta-llm-orchestrator.zip
│   └── sources/
│       └── README.md
└── <new-instruction-set>/
    ├── README.md
    ├── <new-instruction-set>.zip
    └── sources/
        └── README.md
```

The `<new-instruction-set>` folder is illustrative, not a checked-in package. Use lowercase kebab-case slugs for folder names and package archive names.

## Finding and using an instruction set

1. Browse the catalog above, or search `registry.json` by `id`, `name`, `tags`, or `description`.
2. Read the package's `README.md` to understand its purpose, scope, usage, and relationship to other instruction sets.
3. Download the corresponding ZIP. Read instructions **inside the archive** before applying them.
4. Consult `sources/` for provenance and optional external context; do not assume those files are required at runtime.

## Canonical release policy

- Each instruction-set ID has **one active canonical archive** at `<slug>/<slug>.zip`. Its version is tracked in `registry.json` and the package README.
- Keep the original **Meta-LLM Orchestrator v18** archive as the foundational progenitor. A newer system does not automatically supersede it.
- Do not invent an archive when its original bytes are unavailable. Specifically, the Atlas ZIP is known by name but is **not present** in this repository.
- A canonical update should record the new version, explain what changed, and update the catalog and registry together.
- Never silently replace historical content with a speculative reconstruction. See [CONTRIBUTING.md](CONTRIBUTING.md) for additions and versioning.

## Migration note

The original `packages/meta-llm-orchestrator/v18/meta_llm_orchestrator_instruction_set_v18.zip` has been relocated to `meta-llm-orchestrator/meta-llm-orchestrator.zip` without changing its Git blob. Update consumers of the old path.
