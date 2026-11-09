# Registry lookup and bounded delegation

Verify current registry metadata and exact candidate instructions before assignment. Prefer `product-lifecycle-orchestrator` for lifecycle routing, the relevant `workflow-orchestrator` for stage-specific coordination, `catalog-grounded-consultant` for knowledge-gap consultation, and domain specialists such as `ai-ml-engineering-specialist` or `ai-knowledge-atlas` for bounded outputs. The conversation orchestrator owns the ledger, not every specialist artifact.

Probe actual runtime adapter capabilities using `runtime/ADAPTER_CONTRACT.md`: `probe`, `spawn`, `poll`, `cancel`, and `resume`. Only claim a spawned child when the tool returns a valid execution handle. Where unavailable, perform tasks sequentially with explicit ownership and no fake child status.

For an actual child prepare records compatible with `schemas/subagent-task.schema.json`: `run_id`, `task_id`, `package_id`, `package_version`, `objective`, `context_ref`, `idempotency_key`, `required_capabilities`, `permissions`, `limits`; include prerequisite IDs, allowed artifact refs, output owners and review gate. Limit context to least privilege: no entire transcript or credentials.

Child output is a proposal until checked for correct version, provenance, artifact hash/revision, acceptance tests and ownership. Reconcile multiple contributors by explicit artifact owner and revision lock; never let the last writer silently overwrite. Retry only bounded idempotent tasks; otherwise report blocked.