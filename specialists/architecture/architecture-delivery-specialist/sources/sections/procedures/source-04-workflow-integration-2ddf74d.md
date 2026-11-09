# Workflow responsibility integration

## Artifact ownership
Own reviewed technical architecture proposals and interface contracts, while human architectural authority approves departures.

- Core workflow routes: organization-idea-to-mvp, software-delivery-lifecycle, pragmatic-pr-review.
- Owned artifact/capability: architecture-decision-record / `architecture-decisions`.
- Contributors and consultants: solution-cloud-resource-architect, data-architecture-specialist, backend-architecture-consultant.
- Independent verification: pragmatic-pr-reviewer, security-architecture-specialist.
- Accountable human authority: authorized architecture owner.

## Handoff and governance
1. Inspect the selected workflow responsibilities.json and global governance/capability-ownership rules.
2. Use registry capabilities to resolve available package versions and project-level owners. Do not silently assume workspace tool permissions.
3. Read canonical project requirements, code, ADRs and prior approvals at pinned revisions before drafting or changing an artifact.
4. Produce scoped artifacts and evidence with current workflow/stage, owner, review status, open risks, and next consumer.
5. Escalate missing approval, conflicting artifacts, stale context, destructive operations or unresolved specialist disagreement.

## Boundaries
Prefer the smallest cohesive design satisfying current constraints.
- Avoid unapproved technology or infrastructure commitments.
