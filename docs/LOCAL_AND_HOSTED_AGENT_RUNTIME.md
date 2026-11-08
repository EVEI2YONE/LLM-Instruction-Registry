# Local and hosted agent runtime architecture

This repository publishes **instruction systems and contracts**, not a predeployed agent hosting service. It must be usable by personal-machine agents and hosted chat agents without falsely assuming identical tools or memory.

## Responsibilities

- **Registry/resolver:** discovery, selection, version/hash pinning, section lookup and dependency closure.
- **Primary orchestrator:** chooses bounded specialist, workflow, or composed workflow.
- **Runner:** probes capabilities, schedules tasks, binds adapters, checks policy, tracks lineage and status.
- **Subagent adapter:** invokes a real provider-native child, local process/SDK child, or external gateway; must return measured outcomes.
- **Shared context store:** durable, scoped, versioned references to project facts, decisions and run snapshots.
- **Artifact store:** immutable content-addressed objects and versioned artifact metadata with one accountable owner.
- **Approval gateway:** human decisions anchored to exact revisions; may block transitions.

## Portable interaction flow

1. Probe the runtime and persist `runtime-capabilities`: actual source access, native child-agent APIs, network, shell, storage, concurrency, secret handling and approval UI.
2. Fetch registry metadata and select an exact package version; pin package, shared rules and project revision.
3. Resolve required sections for an action using dependency closure. Load each once per run, and record section IDs and SHA256.
4. Open a run with minimal context snapshot, artifact references and allowed capability scope.
5. Form `subagent-task` records; require an eligible adapter. Reconcile requested permissions against verified runtime and user policy before invocation.
6. Spawn only when the adapter implements it. On restricted hosted sites, call an explicitly configured external gateway via an exposed tool/action; absent both, continue only with a documented single-agent mode.
7. Each child receives a **context envelope**, never unrestricted parent chat history, secrets or writable shared state. Child returns findings plus proposed artifact updates.
8. Commit artifacts via content hashes and compare-and-swap metadata revisions. Disjoint writes may proceed in parallel. Conflicts require owner reconciliation and independent review when applicable.
9. Persist handoffs, evidence, approvals, cancellation/retry outcomes and next owner. Aggregate parent state only after validated child results.
10. Report actual completed operations, blocked actions, unsupported capabilities and unresolved decisions.

## Runtime matrix

| Target | Instruction loading | Dynamic child execution | Context and artifacts |
|---|---|---|---|
| Local Python/CLI/IDE | Git checkout and local section lookup | Injected SDK/process adapter after tool/permission check | Filesystem/SQLite or configured store, scoped paths |
| Claude Code / local coding environment | Verified repo and skill integration | Only native/runtime APIs actually supported | Local store plus explicit artifact references |
| Codex/local coding environment | Verified repo instructions and selected sections | Native/runtime support or configured external runner | Repo/project references plus local store |
| ChatGPT Project / hosted chat | Project sources, connector or verified upload bundle | Native tools if present; otherwise authorized gateway; otherwise single-agent | Connected external store or explicit conversation-attached artifacts |
| Other hosted chat website | Available prompt/tools only | Exposed function-call gateway or supported native API; never assume arbitrary subprocess access | External authenticated service or explicit transient output |
| Provider API / Agent SDK application | Programmatic fetch and section retrieval | Application-runner SDK adapter | Application-owned durable stores |

## Shared context principles

Use one immutable parent snapshot per delegation boundary. Distinguish: authoritative project facts, working hypotheses, scratchpad, decisions, credentials (NEVER in shared context), tool capability grants, and long-term memories. Store snapshots by immutable reference, maintain a separate mutable run index with optimistic concurrency, and record provenance. Child context is **minimum necessary**, scoped per task, and can only see authorized artifact IDs. Sibling children don't observe partial writes automatically.

## Artifact principles

Artifact records name content digest, storage URI/reference, schema, owner capability, producer task, parent revisions, visibility, status, and approvals. Store bytes separately from metadata. Drafts are never automatically treated as approved facts. Publication and consequential actions require project policy and authenticated human approval. Merges are explicit fan-in actions with conflict checks.

## Orchestration restrictions

Set maximum spawn depth, parallelism, task budget, retry count, deadline, and permitted actions. Each spawn gets a unique task and idempotency key. Reviewers should be independent of producer tasks. Parent/child cancellation is propagated with audit records; work completed after cancellation is provisional until reconciled. Workers cannot expand their own permissions or edit authoritative instructions.

## Hosted integration boundary

A repo URL is **not** a mechanism for hosted subagent creation. A hosted site must provide either (a) a callable native subagent API, or (b) an authenticated tool to an operator-controlled gateway. The gateway needs deployment, identity, secret storage, job queue, audit log, context/artifact persistence, rate limits, approval callbacks and operational controls. No remote gateway is deployed as part of this setup. Workspace adapters must report `verified-available`, `verified-unavailable` or `unknown` before claiming capability.

## Test plan

Unit tests cover section closure, security, context snapshots, artifact compare-and-swap, ownership, and adapter fallback. Contract tests exercise adapter tool calls, retry behavior, cancellation and fan-in under fake adapters. Integration tests require an explicitly configured local SDK or deployed HTTPS gateway and are NOT_RUN otherwise.
