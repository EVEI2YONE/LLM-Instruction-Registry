# Generated outputs, context and handoff contract

Read when specifying the output of an agent package, generating subagent handoffs, or defining cross-environment resumption.

For each generated package define one stable ID and kind, entrypoint, source-contract version, target workspace, purpose/not-for, capabilities, use cases, authority, necessary tools and source read triggers. Handoffs remain compatible with `governance/handoff.schema.json`: `workflow_id`, `stage_id`, `producer_version`, `project_revision`, `authoritative_inputs`, `outputs`, `evidence`, `status` and `next_owner`.

When the runtime supports extra fields, include `run_id`, `task_id`, `context_ref`, resolved `package@version:section-id` references, artifact IDs/digests/revisions, privilege/visibility scope, approvals and risk classifications. Preserve the legacy handoff's required fields until a separately reviewed schema update. Never assume a child inherited prompt history or saw draft sibling artifacts.

Expose `blocked`, `provisional`, `failed` or `needs-approval` appropriately. Only mark `complete` after verified outputs and evidence. Version and compare-and-swap artifact records as the target project's actual store supports; absent a durable store, provide explicit downloadable/exported handoff instead of claiming cross-session continuity.

Treat reference schemas in `schemas/` and contracts under `runtime/` as external pinned dependencies, not an invitation to copy and fork their full text into the generated package.
