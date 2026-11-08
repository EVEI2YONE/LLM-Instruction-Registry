# Publishing instruction packages and workflows

Read [CONTRIBUTING](../CONTRIBUTING.md), [taxonomy](ROLE_TAXONOMY.md), [workspace adapters](WORKSPACE_ADAPTERS.md) and the current [registry](../registry.json). Inspect current main, active PRs and source ownership before writing.

1. Select kind: `primary-orchestrator`, `workflow-orchestrator`, `meta-orchestrator` or `specialist`; select one professional role, stable ID, version, capabilities, domains, aliases and intended use cases.
2. Resolve existing equivalents by registry search; prefer reuse or a new version over duplicating a capability. If the target workspace differs from the authoring environment, classify actual available tools/permissions and choose a runtime adapter.
3. Publish one canonical package in `orchestrators/primary/<id>/`, `orchestrators/workflow/<id>/`, `orchestrators/meta/<id>/` or `specialists/<domain>/<id>/`. Include `SKILL.md`, compiled instructions, domain/context modules, self-heal, manifest and source README.
4. Create a real binary `<id>_vN.zip` with exactly one `<id>/` root and byte-identical browsable source files. Validate ZIP CRC and inventory. A README link is not an archive; do not register pending source-only entries as available.
5. Preserve previous versioned ZIPs and Git blobs. Pure directory moves should reuse blob SHA; instruction changes create a new version. Disclose reconstruction provenance if original content is unavailable.
6. Update `registry.json` (schema v3), category/root READMEs, workflow references, ownership matrices and search tests in the same PR. Changes to existing source manifests must include new modules in their listed source inventory.
7. Run registry validation and the archive/workflow/ownership regression tests. For workspace-specific outputs, run relevant capability and installation checks only if the actual tools are available.
8. Open/update one reviewable PR with source count, ZIP paths and verification evidence. Never claim deployment, merge or human approval without actual tool confirmation.

Published instruction sets define behavior, not proof of a running workflow engine or external API access. Never run the legacy one-time `scripts/rebuild_registry.py` against the current layout.
