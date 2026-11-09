# Curated domain reference routing (proposal)

This document maps existing registry specialists to the user's curated reference repositories. It is a **routing and review reference**, not a published specialist instruction upgrade or evidence of runtime access. The registry remains the authority for package selection, and `governance/approval.json` and applicable ownership rules govern consequential actions.

## Domain catalogs

| Work requiring curated guidance | Repository | Primary specialist (registry ID) | Other relevant consumers |
| --- | --- | --- | --- |
| UI/UX refactoring, component/design-system audits, migration guidance | https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog.git | `ui-ux-design-system-architect` | `ui-ux-product-designer`, `frontend-engineering-specialist`, `accessibility-usability-reviewer` (as applicable) |
| Software engineering architecture, backend modularity, extensibility, scalability and refactoring | https://github.com/EVEI2YONE/Software-Architecture-Atlas.git | `backend-architecture-consultant` | `architecture-delivery-specialist`, `api-integration-design-specialist`, `data-architecture-specialist` (as applicable) |
| AI architecture guidance, RAG/agent evaluation, evidence freshness and AI research gaps | https://github.com/EVEI2YONE/AI-Knowledge-Atlas.git | `ai-knowledge-atlas` | `ai-ml-engineering-specialist` |

The primary specialists above correspond to existing registry entries; do not create duplicate packages merely to add catalog links. These catalogs are distinct from the instruction package registry.

## Workflow entry points and responsibilities

- `product-lifecycle-orchestrator` selects the applicable workflow/specialist based on task intent. It does not replace a domain expert.
- `catalog-grounded-consultant` coordinates cross-domain catalog consultation, gap triage, batched authorized catalog-only PRs, source refresh, and grounded refactor playbooks.
- `idea-to-mvp-orchestrator` and `feature-extension-planning-council` request domain specialist evidence when the proposed work implicates UI/UX, software architecture, or AI architecture.
- `knowledge-context-steward` records repository URI, commit/release revision, evidence timestamps, knowledge gaps, and provenance for handoffs.
- `meta-llm-orchestrator` is the instruction authoring/upgrading route if published specialist behavior needs to change. This document **does not** modify those packages.

## Consumption contract

1. Match the requested domain and select the primary specialist from the **live** `registry.json`; verify its actual package kind, version, sources, approval and relevant manifest sections.
2. Fetch the applicable domain catalog using an authorized GitHub connection. Verify the repository and pin an immutable commit SHA (or an actually approved release revision) before relying on its contents. A URL alone does not prove access, completeness, freshness, or approval.
3. Cite the specific catalog files/sections and commit used for domain recommendations. Label missing/inaccessible evidence as `UNVERIFIED` or `BLOCKED`, not as nonexistent; do not fabricate catalog findings.
4. Use `catalog-grounded-consultant` to coordinate generalizable gaps. Check for duplicate open issues/PRs, and prepare narrowly scoped catalog changes only with authorization.
5. Keep **domain catalog updates** separate from **instruction-registry package upgrades**. Both require the relevant source ownership checks. Published specialist instruction or manifest changes require the normal generator, version, source/ZIP consistency, tests and reviewed publication process in `docs/PUBLISHING.md`.
6. Human review and approval are required for PR merges; no assistant/agent may self-approve or silently merge. After a merge, verify the target branch, merged SHA, and fresh catalog content before resuming dependent work.
7. Do not assume an executable subagent: delegation requires an actually verified adapter. Sequential consultation is an acceptable transparent fallback.

## Scope and verification

This proposal documents routing to three provided repositories and existing specialist IDs only. It does not modify `registry.json`, any package manifest, `sources/SKILL.md`, released ZIP, workflow runtime, or approvals. Follow-up **versioned** package changes should be separately reviewed if the intent is to make these links mandatory in specialist instructions.

Validation checklist for this docs-only change:
- [x] Every named specialist ID checked against the current `registry.json`.
- [x] Repository names checked via GitHub repository search.
- [x] No source package, archive, or registry schema changes.
- [ ] Independent reviewer approves wording and scope.
- [ ] Human-authorized merge.
