# Portable handoff contract

Each meaningful stage emits a compact human-readable summary and a structured record with:
`workflow_id`, `stage_id`, `producer_version`, `project_revision`, `authoritative_inputs`, `outputs`, `evidence`, `status`, `next_owner`.

When supported, add `run_id`, `task_id`, `revision`, `context_ref`, source `package@version:section-id`, content hashes, artifact owner, visibility, permissions, approval references, and idempotency keys. Do not assume the next model can read a created file or has inherited session history.

Child tasks require a bounded objective, explicit dependencies, authorized tools and budget; pass only least-privilege context and artifact references. Never pass credentials, hidden reasoning, full chats, or unrelated attachments.

Without verified persistence, include a bounded inline state; mark persistence NOT_VERIFIED. Statuses include provisional, blocked, needs-approval, failed, and complete. Use complete only after output integrity and required evidence are checked. Human approval must reference the exact revision.