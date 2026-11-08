# Registry-first discovery and identity resolution

Use before naming a new specialist, workflow coordinator, primary router, meta instruction generator, or reusable contract.

1. Resolve the logical registry source through `references/source-locations.json` and `source-bootstrap` first, then pin the actual repository branch and commit. Review only the root registry metadata, role taxonomy, publishing rules, relevant workflow ownership metadata and up to three likely matches. Start with `python3 scripts/search_registry.py search --query "requested capability"`, then narrow by role/domain; never read all package sources by default.
2. Compare each candidate's `id`, `kind`, `role`, capabilities, aliases, use cases, source revision, boundaries, actual source availability, and expected output owner. Reuse a matching package. Extend/version a partial match. Create a new package only after documenting the capability gap.
3. Keep role and execution independent: `meta-orchestrator` generates instruction packages, `primary-orchestrator` routes user intent, `workflow-orchestrator` coordinates named stages, and `specialist` owns bounded domain outputs. Workflow participation does not remove a specialist's standalone use.
4. Resolve the target project's approved owners, interface conventions, CODEOWNERS, ADRs, workflow responsibilities and artifact location. Repository instructions do not authorize write or human approval. Do not copy a sibling's entire instructions into a new package; reference capability and version.
5. Capture a decision record: selected or proposed package ID and `kind`, current version/commit, reuse-vs-upgrade-vs-create rationale, overlapping candidates, target compatibility, owners, source integrity and unresolved dependencies.

**Escalate** when existing package boundaries conflict, ownership cannot be resolved, or current registry evidence is inaccessible. Treat inaccessible as `not_verified`, not `absent`. Never invent a package or change approved organizational ownership based on the generated instructions alone.
