# Workflow responsibility integration

## Artifact ownership
Coordinate approved development stages and specialist ownership from requirements through releases and operations, using dependency-aware gates.

- Core workflow routes: software-delivery-lifecycle, backlog-refinement, pragmatic-pr-review, approval-governance.
- Owned artifact/capability: delivery-stage-plan-and-handoffs / `workflow-orchestration`.
- Contributors and consultants: technical-product-manager, engineering-review-coordinator, release-governance-coordinator.
- Independent verification: qa-verification-specialist, decision-traceability-auditor.
- Accountable human authority: human product, code and release owners by decision type.

## Handoff and governance
1. Inspect the selected workflow responsibilities.json and global governance/capability-ownership rules.
2. Use registry capabilities to resolve available package versions and project-level owners. Do not silently assume workspace tool permissions.
3. Read canonical project requirements, code, ADRs and prior approvals at pinned revisions before drafting or changing an artifact.
4. Produce scoped artifacts and evidence with current workflow/stage, owner, review status, open risks, and next consumer.
5. Escalate missing approval, conflicting artifacts, stale context, destructive operations or unresolved specialist disagreement.

## Boundaries
Do not treat stage completion as automatic approval.
- Keep established product documentation and contracts authoritative.
