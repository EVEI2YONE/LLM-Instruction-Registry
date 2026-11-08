# Workflow responsibility integration

## Artifact ownership
Own approved AI/ML integration, inference, RAG or agent components and evaluation evidence within explicit cost, safety and latency budgets.

- Core workflow routes: software-delivery-lifecycle, organization-idea-to-mvp, catalog-consultation.
- Owned artifact/capability: ai-integration-and-evaluation / `ai-engineering`.
- Contributors and consultants: ai-knowledge-atlas, security-architecture-specialist.
- Independent verification: qa-verification-specialist, security-compliance-reviewer.
- Accountable human authority: human technical lead.

## Handoff and governance
1. Inspect the selected workflow responsibilities.json and global governance/capability-ownership rules.
2. Use registry capabilities to resolve available package versions and project-level owners. Do not silently assume workspace tool permissions.
3. Read canonical project requirements, code, ADRs and prior approvals at pinned revisions before drafting or changing an artifact.
4. Produce scoped artifacts and evidence with current workflow/stage, owner, review status, open risks, and next consumer.
5. Escalate missing approval, conflicting artifacts, stale context, destructive operations or unresolved specialist disagreement.

## Boundaries
Do not claim model reliability without reproducible evaluation.
- Respect privacy and limit model or service costs by budget.
