# Product Lifecycle Orchestrator — scaffolding

**Pending**: user-facing orchestration design, not yet a validated ZIP instruction release.

The entry point classifies intent, checks authoritative project context and revision, then delegates:
1. Direct bounded work to an independent specialist selected by capabilities in `registry.json`.
2. Multi-stage/cross-domain work to one declarative workflow profile.
3. Complex outcomes to a composition of workflows with pinned, auditable handoffs.
4. Ambiguous authority, investment, production, merges and irreversible actions to human approval.

Specialists return scoped artifacts, evidence, risks, disagreements and next owner. The orchestrator enforces stage dependencies, bounded rework, and approval; it must not invent action completion, duplicate canonical PRDs/ADRs, or self-authorize releases.

[Routing contract](routing.json) · [Workflow catalog](../../../workflows/README.md)
