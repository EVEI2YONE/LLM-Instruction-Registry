# Classify instructions into canonical layers

Use immediately before converting requirements, existing prompt text or a legacy compiled document into lookup-first modular sources.

Classify each instruction once by **when and why it is required**, not by which source document it came from:

| Instruction property | Canonical home |
|---|---|
| Cross-package common behavior, precedence or authority | Versioned central governance; do not duplicate in packages |
| Package-specific non-negotiable that must hold for every request | `SKILL.md` Always (up to ten concise rules) |
| Conditional action-specific procedure or decision tree | `sections/procedures/<slug>.md` |
| User-facing reusable output shape | `sections/templates/<slug>.md` |
| Machine-validated input/output contract | `sections/contracts/<slug>.schema.json` or referenced schema |
| Internal specialist/subagent responsibility | `sections/roles/<slug>.md` |
| Target/runtime-specific integration | `adapters/<target>.md` |
| Optional domain overlay or one-off scenario | `sections/playbooks/` or `sections/examples/` |
| World/technology/domain fact that changes with time | Pinned external knowledge catalog or actual target source, never copied fact |

Do not move a safety rule behind a trigger if omission could authorize harm, false deployment claims, authority escalation, or irreversible writes. Preserve important invariants even if the entrypoint grows beyond an initial *advisory* word budget; measure actual behavior before setting hard limits.

Store one topic per source file. Give addressable sections stable human-readable IDs; rename IDs only as a breaking versioned change. For `read_when`, use observable action phrases: "about to assess target permissions", "about to package a release", rather than ambiguous topics like "permissions guidance". Record prerequisites as `requires` so dependency closure loads the exact necessary sections once.

For source migrations, preserve normative rules, outputs, examples and provenance. Build a traceability mapping from old files/paragraphs to their new home; flag contradictions for human review rather than silently choosing. Remove mechanically duplicated compiled text from canonical sources; generate bundles as build outputs.
