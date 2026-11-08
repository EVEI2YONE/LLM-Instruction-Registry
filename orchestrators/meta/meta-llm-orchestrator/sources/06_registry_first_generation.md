# Repository-aware instruction authoring and migration

## Current hierarchy
- `orchestrators/primary/<id>/` — user-facing request dispatcher and workflow composer.
- `orchestrators/workflow/<id>/` — workflow coordinators.
- `orchestrators/meta/meta-llm-orchestrator/` — this instruction generator.
- `specialists/<domain>/<id>/` — independent bounded capabilities.
- `workflows/<group>/<workflow-id>/` — declarative stage profiles and `responsibilities.json`.
- `governance/capability-ownership/` — global Owner/Contributor/Consultant/Reviewer/Human Approver contract.
- `registry.json` — available canonical package IDs, role, kind, capabilities and exact source/archive paths.

## Mandatory authoring flow
1. Pin repository branch/revision and review `README.md`, `CONTRIBUTING.md`, `docs/PUBLISHING.md`, current registry and relevant package README.
2. Search exact ID, aliases, capabilities and domain; compare 1–3 candidates before adding a package. If equivalent existing behavior exists, extend it rather than duplicate.
3. Select **kind**, professional role, domain, package ID, version and workspace adapter; choose artifact owner and review/approval boundaries.
4. Build one authoritative source directory with `SKILL.md`, compiled instructions, modular domain/context guidance, self-heal, source README, manifest and target-specific adapters. Keep the number of uploaded sources within the *verified* target limit.
5. Create a real ZIP containing exactly `<id>/` as its only root with byte-matching sources; test CRC, unsafe paths, unexpected symlinks, counts, manifests and version.
6. Commit ZIP *binary* and full source files. For GitHub connector-only paths, use Git Data blob with base64 bytes, tree, commit and update_ref; verify actual ZIP blob and source paths. Do not upload text masquerading as a ZIP.
7. Update `registry.json` and all category/root navigation, workflow references, capability owners and tests only for paths that exist.
8. Create or update a PR; don't merge without separate authorization. Re-read the changed-file list and source SHA references; state what is verified and what is not.

## Versioning
Keep old released ZIP versions and provenance. New source changes require a new versioned archive. Simple file moves should preserve existing binary blob identity; do not repackage merely to rename. If original bytes are unavailable, disclose reconstruction provenance and verify separately.

## Ownership
A generated workflow may reference specialists by capability rather than duplicating their instructions. A specialist must not own business decisions simply because it supplies technical evidence. If a product repo owns a PRD/ADR, propose changes through its owner.
