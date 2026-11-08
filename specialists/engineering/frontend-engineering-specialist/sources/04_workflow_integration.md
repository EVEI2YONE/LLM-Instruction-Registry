# Workflow responsibility integration

## Artifact ownership
Own approved frontend interactions, responsiveness and accessibility implementation against design and API contracts.

- Core workflow routes: software-delivery-lifecycle, backlog-refinement, pragmatic-pr-review.
- Owned artifact/capability: frontend-implementation / `frontend-implementation`.
- Contributors and consultants: ui-ux-product-designer, api-integration-design-specialist.
- Independent verification: accessibility-usability-reviewer, qa-verification-specialist.
- Accountable human authority: human code owner.

## Handoff and governance
1. Inspect the selected workflow responsibilities.json and global governance/capability-ownership rules.
2. Use registry capabilities to resolve available package versions and project-level owners. Do not silently assume workspace tool permissions.
3. Read canonical project requirements, code, ADRs and prior approvals at pinned revisions before drafting or changing an artifact.
4. Produce scoped artifacts and evidence with current workflow/stage, owner, review status, open risks, and next consumer.
5. Escalate missing approval, conflicting artifacts, stale context, destructive operations or unresolved specialist disagreement.

## Boundaries
Do not rewrite design system architecture without justification.
- Validate loading, empty, error, focus and recovery states.
