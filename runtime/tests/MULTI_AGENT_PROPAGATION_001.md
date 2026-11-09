# MULTI_AGENT_PROPAGATION_001 — single Codex specialist execution

**Objective:** prove one actual Codex subagent receives correct pinned registry instructions and returns independently traceable read-only evidence. **Status in this repository PR: NOT_RUN**; execution requires a separately configured Codex session, not GitHub read tools alone.

## Preconditions

- A recorded active client/session and its exposed tool surface; an installed Codex IDE integration and ChatGPT website may share ChatGPT functionality but need separate observations of tool visibility and instruction policy.
- **Explicit user authorization for exactly one read-only child delegation**, or an applicable authorized Skill rule that permits that exact action. A general readiness assessment does not automatically authorize spawning.
- A user-approved read-only assessment scope in `EVEI2YONE/Little_Wins` or a non-sensitive fixture repository; record exact project commit.
- A pinned *full* `EVEI2YONE/LLM-Instruction-Registry` commit, selected registered specialist and actual entrypoint plus mandatory section dependency closure. Do not use `status: available` as formal approval evidence.
- Controlled child permissions, explicit owner, one task ID, one idempotency key, finite budget and a permitted scoped context envelope. No production, merge or investment actions.

## Procedure

1. Record **delegation authorization** first (user request or applicable instruction) and active host tool/policy evidence. If absent, stop with `POLICY_GATED_NOT_ATTEMPTED`; this is **not** evidence of tool unavailability.
2. Probe runtime; record `runtime_id`, `execution_surface`, `spawn_mode`, feature availability, permissions and measured-at timestamp.
3. Select an applicable specialist by recorded capability; read its exact version and required sections from one registry snapshot. Record source section hashes or verified IDs.
4. Construct `schemas/subagent-task.schema.json` input and a scoped context envelope: project SHA, registry SHA, precise question, expected artifact, sections transmitted and acceptance criteria.
5. Trigger **one real native child** through the exposed Codex session/tool; capture the provider-issued child thread/handle. Do not substitute a parallel API call, mock handle, generic ChatGPT response or sequential answer.
6. Ask child to report its package/version, consumed section identifiers, source revisions, allowed tools, file/line evidence and outcome. Compare these claims against delivered instructions and observed tool trace.
7. Poll/wait using supported provider controls and record completion/failure status and visible execution evidence. If poll or cancellation is not exposed, record unavailable rather than faking them.
8. Independently inspect result/provenance, source drift, actual artifact and scope conformance. Parent reconciles the output without treating unreviewed child assertions as approved decisions.
9. Persist a continuation artifact only through a verified store; otherwise provide a bounded inline record. Any new instruction/approval source version requires a fresh verification before resume.

## PASS criteria (all required)

- [ ] Actual provider child ID/thread observed.
- [ ] Child task and least-privilege scopes match the authorized envelope.
- [ ] Correct specialist version and pinned registry/project revisions verified in accessible trace.
- [ ] Required instruction section content or verified identical refs delivered to the child's accessible context.
- [ ] Child produced independent source-grounded output and owned artifact/provenance.
- [ ] Parent reconciled output, with explicit incomplete/failed/blocked handling and no fabricated approvals.

**FAIL** if an unauthorized/wrong-version child ran, context exceeds scope, instructions were not transmitted, or output attribution cannot be established. **POLICY_GATED_NOT_ATTEMPTED** when the run had no delegation authorization; do not treat this as provider failure. **TOOL_UNAVAILABLE** only when an authorized preflight finds no callable native spawn tool. **SPAWN_FAILED** only after an actual attempted invocation. **BLOCKED** for other access or dependency failures. **NOT_RUN** when no authorized propagation test was initiated. Only a real child with verified propagated instructions can PASS.

## Source feedback fixture

Two user-supplied observations concerning Little Wins project revision `838630151b3c033939e03241ee9c61986bcd9703` and registry revision `10ff0fcffa021eb4ece668b6aae8e1308a289032`:

- **ChatGPT website run:** live registry specialist reads succeeded, but no callable native spawn interface was exposed in that conversation. Zero subagents; propagation NOT_RUN.
- **Codex IDE access to ChatGPT functionality:** installed Product Conversation Orchestrator Skill entrypoint and lookup/handoff guidance loaded, but **no live registry specialist selection**. Installed/host instructions required explicit delegation authorization, which was not supplied in that readiness request; the assistant did **not attempt a spawn**. Its 359 local tests and passing GitHub CI concern the sequential product assessment, not multi-agent execution. Zero subagents; propagation NOT_RUN. Record `POLICY_GATED_NOT_ATTEMPTED` for this invocation, not `TOOL_UNAVAILABLE`.

These are **user-supplied historical reports**, not independently reproduced runtime traces. Neither observation establishes whether instruction propagation would succeed after an expressly authorized child spawn.

Do not promote a release-readiness or production conclusion on this fixture alone. Repeat the bounded independent review after real runtime activation and preserve human approval gates.
