# 12 Helper Implementation And Progress

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `02_helpers/12_implementation_and_evaluation_router.md`

# Helper — Implementation and experimental lanes

Do not let a request for "implementation" imply that all knowledge entries require code. Pick the lightest useful lane:

| Lane | Output | Acceptance |
| --- | --- | --- |
| conceptual example | Explanatory pseudocode / illustrative interface | Explicit `not_executed` label |
| reference implementation | Small versioned program and setup | Reproducible run command and tests; state whether executed |
| integration recipe | Framework-specific configuration, I/O and failure path | Version constraints, external dependency warnings |
| evaluation design | Dataset, baselines, hypotheses, metrics, cost, failure cases | Rerunnable protocol, no invented numbers |
| verified comparative experiment | Actual artifacts, logs and results | Runs happened, baselines controlled, raw outputs retained |

Check licenses, security and resource costs before code execution. Do not run untrusted downloaded scripts without inspection. Prefer a deterministic baseline before proposing a multi-agent architecture or expensive training.

Minimum tested-code evidence: commit/file SHA, environment, dependencies, seed where meaningful, exact commands, test output, and known unresolved failures. A successful code generation model response is not evidence of a correct implementation.

---

## Original source: `02_helpers/14_status_progress_and_handoff.md`

# Helper — Honest state and partial handoff

Status vocabulary: `proposed` (plan only), `partial` (some verified outputs), `complete` (all declared deliverables checked), `blocked` (authorization/dependency missing), `rejected` (out-of-scope or prohibited). `in_progress` may be used only if an actual running executor/job exists; do not fake background work.

Break broad research into independently reviewable batches; every batch must produce a handoff packet containing target branch SHA, findings, source claims, files inspected, files modified, QA results, unresolved risks, recommended next batch, and requests deduplicated.

An agent should remain useful without being granted write access: deliver existing relevant content, a gap inventory, sources to verify and a safe proposed diff plan. If research tools are unavailable, do not imply sources were freshly checked. Human-facing summaries must not contradict the structured response envelope.
