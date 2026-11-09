# Context-first mini registry snapshot (2026-11-09)

Distribution artifact for upload-limited ChatGPT Projects; **not** a separately registered instruction set, approved release, or substitute for live specialist source retrieval.

- Archive: [LLM-Instruction-Registry-context-first-mini-40-files.zip](LLM-Instruction-Registry-context-first-mini-40-files.zip)
- Source registry commit: `efb51d7e0ca9dcd4ece064ed7e94e4324c437206`
- Package metadata indexed: **50**
- Flat archive entries: **40** (12 Conversation Orchestrator source files plus 28 context-first indexing and workflow aids)
- Format: standard ZIP, stored entries (no compression); binary source is held as a Git blob
- Priorities: context recovery, workflow identification, scope preservation, capability indexing, verified instruction loading, fail-closed task start

## Important limitations

The archive contains complete registry **metadata**, but not all 50 specialist instruction sets. A matching index entry never authorizes a specialist task by itself: fetch the exact pinned package entrypoint, manifest, `read_when` sections and transitive `requires` dependencies, then verify actual loading before execution.

This is a regenerated distribution snapshot based on the pinned registry and canonical Conversation Orchestrator files. It is not claimed to be byte-identical to any previously shared local ZIP. Runtime behavior, provider child spawning, and hosted instruction propagation are **NOT_RUN**.

## Review guidance

Review the source SHA, ZIP inventory, metadata parity and gate requirements. Do not merge without normal human approvals. This PR makes no changes to `registry.json`, canonical instruction sources, approvals or runtime adapters.
