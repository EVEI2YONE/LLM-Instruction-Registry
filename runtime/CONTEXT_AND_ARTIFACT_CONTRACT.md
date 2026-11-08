# Shared context, artifact and handoff contract

## Context propagation

- A parent task persists an immutable context envelope with `run_id`, project revision, selected source refs, objective, task permissions, visible artifact refs, and a version/hash.
- Children receive an authorized *subset* of the parent snapshot plus local working state. They do not see the parent's hidden scratchpad, credentials or unrelated attachments.
- Parent/child/sibling contexts use explicit references, never magic shared memory. Long-lived knowledge belongs in the appropriate project/catalog, not in agent conversation memory.
- Decisions and policy changes require an accountable owner and versioned audit trail. Children can propose a change, not silently approve it.

## Artifact writes

- Distinguish content bytes from artifact metadata. Content is immutable/content-hashed; metadata changes use expected revision (compare-and-swap).
- One owner is assigned for each authoritative artifact. A concurrent writer must propose changes or perform an authorized merge, not overwrite another child.
- Review and approval outcomes are separate from a producer's completion status. Approved artifacts record the exact reviewed revision.
- Visibility can be `private-task`, `run`, `project`, or `public`; access is enforced by the actual storage backend, not merely asserted in metadata.
- The store should support local filesystem initially and interchangeable SQLite/object storage/cloud backend for cross-machine/hosted use.

## Fan-in / resumption

A coordinator waits for required child results, verifies provenance and expected artifact revisions, reconciles conflicts, and publishes a new parent snapshot. Restarting a process must use persisted run/task IDs; resubmitting an idempotency key must not duplicate work. Retained state needs retention, backup and deletion policy owned by the runtime operator.

## Handoff compatibility

The existing `governance/handoff.schema.json` remains authoritative for workflow handoffs until a reviewed next version. New execution envelopes may add optional `run_id`, `task_id`, `context_ref`, `artifact_ids` and `common_rules_version` in a future schema revision; do not silently break existing consumers.
