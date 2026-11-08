# Provider-neutral subagent adapter contract

An adapter resolves and invokes a selected published instruction package; it does not change ownership rules. Runtime capability reporting MUST precede spawn.

## Required logical interface

- `probe() -> runtime-capabilities`: demonstrate available tools, child execution, persistence, network, concurrent tasks, and approvals. Unknown is not available.
- `spawn(task, context_ref, resolved_sections) -> execution_handle`: verify authorization, package version, task idempotency and allowed permissions first; return handle with task ID and adapter ID.
- `poll(handle) -> {status, outputs, evidence, cost}`: report pending/running/completed/failed/blocked/cancelled.
- `cancel(handle) -> cancellation_result`: best-effort and truthful. Late results remain provisional until reconciled.
- `resume(handle, new_context_ref) -> execution_handle`: permitted only when the runtime supports persistent tasks; otherwise schedule a new task linked by provenance.

Each adapter declares whether it supports native child sessions, process SDK execution, gateway delegation, or only single-agent fallback. Conformance tests must verify claims. The orchestrator cannot turn ordinary text instructions into new platform-native capabilities.

## Selection

Filter candidate adapters by verified capabilities, user permissions, security constraints, recursion, parallelism and workspace support. Prefer a local/native execution surface for local workflows and a secure configured gateway for hosted environments without native delegation. Do not silently forward personal context to a different provider.

## Gateway minimum

HTTPS with authenticated principal, scoped API tokens, idempotent task submit/status/cancel endpoints, tenant/project/run boundaries, queue and audit storage, signed or content-hashed artifact references, approval checkpoints, tool isolation, rate limiting and operational monitoring. Secrets must never be embedded in task context. Service deployment is outside this repository setup.

## Fallback

When no execution adapter exists, return `unsupported_or_unverified` with required configuration. A single-agent answer may continue only where safe and transparent; it is not evidence that subagents were spawned.
