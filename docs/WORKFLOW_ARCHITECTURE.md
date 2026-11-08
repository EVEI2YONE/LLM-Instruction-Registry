# Workflow architecture

The primary user-facing orchestrator routes requests to a direct specialist, a workflow, or a composition of workflows. Workflow coordinators own local stage order, parallelism, councils, retries, approvals and handoffs; specialists own bounded domain tasks. Meta-LLM remains the progenitor for authoring instruction packages. Governance is cross-cutting. Pin source revisions; only humans approve investment, merges, irreversible action and production.
