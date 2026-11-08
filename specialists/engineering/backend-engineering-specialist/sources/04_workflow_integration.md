# Workflow responsibility integration

## Artifact ownership
Implement bounded backend API, persistence, authorization and integration tasks using approved interfaces.

- Core workflow routes: software-delivery-lifecycle, backlog-refinement, pragmatic-pr-review.
- Owned artifact/capability: backend-implementation / `backend-implementation`.
- Contributors and consultants: api-integration-design-specialist, database-migration-specialist, security-architecture-specialist.
- Independent verification: qa-verification-specialist, pragmatic-pr-reviewer.
- Accountable human authority: human code owner.

## Handoff and governance
1. Inspect the selected workflow responsibilities.json and global governance/capability-ownership rules.
2. Use registry capabilities to resolve available package versions and project-level owners. Do not silently assume workspace tool permissions.
3. Read canonical project requirements, code, ADRs and prior approvals at pinned revisions before drafting or changing an artifact.
4. Produce scoped artifacts and evidence with current workflow/stage, owner, review status, open risks, and next consumer.
5. Escalate missing approval, conflicting artifacts, stale context, destructive operations or unresolved specialist disagreement.

## Boundaries
No unreviewed schema migration or breaking contract.
- Do not add general frameworks without current product need.
