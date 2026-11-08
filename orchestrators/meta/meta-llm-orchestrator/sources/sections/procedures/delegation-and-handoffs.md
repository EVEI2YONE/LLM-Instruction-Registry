# Generate dynamically composable agent contracts

Read when about to create an agent that will select collaborators, spawn children, coordinate workflows, or share context and artifacts.

An instruction package declares **capabilities and boundaries**; only an actual runner/SDK or authenticated hosted gateway executes children. Keep the primary user-facing router, workflow coordinators, meta-generator and independent specialists distinct. Do not embed one model's process control commands into all packages.

Define each new agent's required input and output artifacts, ownership role, supported tasks, source lookups, prohibited actions, review and approval gates, tool requirements, and a graceful single-agent fallback. Point to existing `registry.json` capabilities instead of duplicating a specialist. The orchestrator should filter candidates on exact package version and verified runtime capabilities before dispatching.

When delegating, construct `schemas/subagent-task.schema.json` records with a task/run ID, parent task, package/version, objective, context reference, idempotency key, capabilities, permissions, dependencies and bounded recursion, retries, concurrency and time budgets. Context is a least-privilege `schemas/context-envelope.schema.json` snapshot containing pinned authoritative source refs, allowed artifact refs, task objective and approved tool scopes. Never forward entire chat history, credentials, hidden scratchpad or unrelated project attachments.

Produced artifacts use `schemas/artifact-record.schema.json`: content digest, one owner, producer task, visibility, status, revision and provenance. Children propose drafts; owners reconcile concurrent updates with compare-and-swap; independent reviewers check guarded changes; human approvals reference exact revisions. Fan-in occurs only after dependency outcomes and artifact integrity are verified. Failed/blocked children must not be reported as complete.

Verify actual `runtime/ADAPTER_CONTRACT.md`, `runtime/CONTEXT_AND_ARTIFACT_CONTRACT.md` and target-specific installation. A repository link alone cannot spawn agents on hosted websites.
