# MULTI_AGENT_PROPAGATION_001 — single Codex specialist execution

**Objective:** prove one actual Codex subagent receives correct pinned registry instructions and returns independently traceable read-only evidence. **Status in this repository PR: NOT_RUN**; execution requires a separately configured Codex session, not GitHub read tools alone.

## Preconditions

- A known Codex client/session with observed native subagent execution interface.
- A user-approved read-only assessment scope in `EVEI2YONE/Little_Wins` or a non-sensitive fixture repository; record exact project commit.
- A pinned *full* `EVEI2YONE/LLM-Instruction-Registry` commit, selected registered specialist and actual entrypoint plus mandatory section dependency closure. Do not use `status: available` as formal approval evidence.
- Controlled child permissions, explicit owner, one task ID, one idempotency key, finite budget and a permitted scoped context envelope. No production, merge or investment actions.

## Procedure

1. Probe runtime; record `runtime_id`, `execution_surface`, `spawn_mode`, feature availability, permissions and measured-at timestamp.
2. Select an applicable specialist by recorded capability; read its exact version and required sections from one registry snapshot. Record source section hashes or verified IDs.
3. Construct `schemas/subagent-task.schema.json` input and a scoped context envelope: project SHA, registry SHA, precise question, expected artifact, sections transmitted and acceptance criteria.
4. Trigger **one real native child** through the exposed Codex session/tool; capture the provider-issued child thread/handle. Do not substitute a parallel API call, mock handle, generic ChatGPT response or sequential answer.
5. Ask child to report its package/version, consumed section identifiers, source revisions, allowed tools, file/line evidence and outcome. Compare these claims against delivered instructions and observed tool trace.
6. Poll/wait using supported provider controls and record completion/failure status and visible execution evidence. If poll or cancellation is not exposed, record unavailable rather than faking them.
7. Independently inspect result/provenance, source drift, actual artifact and scope conformance. Parent reconciles the output without treating unreviewed child assertions as approved decisions.
8. Persist a continuation artifact only through a verified store; otherwise provide a bounded inline record. Any new instruction/approval source version requires a fresh verification before resume.

## PASS criteria (all required)

- [ ] Actual provider child ID/thread observed.
- [ ] Child task and least-privilege scopes match the authorized envelope.
- [ ] Correct specialist version and pinned registry/project revisions verified in accessible trace.
- [ ] Required instruction section content or verified identical refs delivered to the child's accessible context.
- [ ] Child produced independent source-grounded output and owned artifact/provenance.
- [ ] Parent reconciled output, with explicit incomplete/failed/blocked handling and no fabricated approvals.

**FAIL** if an unauthorized/wrong-version child ran, context exceeds scope, instructions were not transmitted, or output attribution cannot be established. **BLOCKED** when native spawning or required access is absent. **NOT_RUN** when the test was not actually executed.

## Source feedback fixture

Reported field observation: Little Wins project revision `838630151b3c033939e03241ee9c61986bcd9703`; registry revision `10ff0fcffa021eb4ece668b6aae8e1308a289032`; parent-only retrieval succeeded; native spawn and instruction propagation were not exposed in the tested conversation; `0` subagents spawned. Treat these as **report-supplied historical observations**, not a repeatable success or independently verified fresh project assessment.

Do not promote a release-readiness or production conclusion on this fixture alone. Repeat the bounded independent review after real runtime activation and preserve human approval gates.
