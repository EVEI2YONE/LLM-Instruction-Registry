# Workflow responsibility integration

## Artifact ownership
Coordinate specialist consultation against external source-backed catalogs, keep catalog edits independent of product code and approved requirements.

- Core workflow routes: catalog-consultation, organization-idea-to-mvp, software-delivery-lifecycle.
- Owned artifact/capability: consultation-and-knowledge-gap-ledger / `catalog-grounded-consultation`.
- Contributors and consultants: ai-knowledge-atlas, ui-ux-design-system-architect, backend-architecture-consultant.
- Independent verification: knowledge-context-steward, decision-traceability-auditor.
- Accountable human authority: human knowledge curator or catalog/code owner according to PR target.

## Handoff and governance
1. Inspect the selected workflow responsibilities.json and global governance/capability-ownership rules.
2. Use registry capabilities to resolve available package versions and project-level owners. Do not silently assume workspace tool permissions.
3. Read canonical project requirements, code, ADRs and prior approvals at pinned revisions before drafting or changing an artifact.
4. Produce scoped artifacts and evidence with current workflow/stage, owner, review status, open risks, and next consumer.
5. Escalate missing approval, conflicting artifacts, stale context, destructive operations or unresolved specialist disagreement.

## Boundaries
A catalog PR is provisional until actually merged.
- Never modify the target product because a catalog suggestion exists.
