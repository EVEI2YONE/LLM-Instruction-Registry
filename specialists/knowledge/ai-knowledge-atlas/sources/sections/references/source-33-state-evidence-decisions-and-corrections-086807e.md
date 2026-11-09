# 33 State Evidence Decisions And Corrections

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `07_state/03_evidence_review_queue.md`

# Source verification and contradiction queue

| Claim ID | Affected Atlas path | Source location | Evidence type | Review date/version | Review status | Concern | Next verification |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Review rule
Prioritize changed provider APIs and high-impact security/quality claims. Add adverse and contradictory evidence. Only `verified` claims support strong assertion; cite version and conditions. Backlog `not_verified` work instead of silently treating it as validated.

---

## Original source: `07_state/05_invariant_and_regression_registry.md`

# Validated architecture invariants and regressions

| Invariant ID | Domain | Exact requirement | Counterexample/failure | Enforcing document/tool | Regression case | Last result | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EX-REF-01 | Multimodal | Image ordinals resolve within request upload set | Most recent uploaded image substituted | Domain A/B playbooks | Distinct images 1–4 | not_run | Proposed test |
| EX-CAP-01 | Tools | Declared input support not equivalent to actual media delivery | Image field accepted, pixel payload omitted | Domain E playbook | Adapter payload trace | not_run | Proposed test |

A regression is `pass` only with a recorded run. New feedback should amend relevant instruction and acceptance test rather than only writing an apology or patching one example.

---

## Original source: `07_state/06_open_research_registry.md`

# Open research questions with decision criteria

| Question ID | Hypothesis | Existing evidence | Baselines | Dataset/cases | Metrics | Budget | Dependencies | Status | Decision criteria |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`proposed` means a plan; `not_run` means no test results exist. A lack of proof is not proof of failure. Keep competing methods and negative findings, and close only after documented decision or explicit deferral.

---

## Original source: `07_state/07_source_inventory_and_review_dates.md`

# Source inventory and review recency

| Canonical Atlas path | Principal external sources | Source review date | Entry status | Critical limitations | Last verified commit |
| --- | --- | --- | --- | --- | --- |

This table records what has actually been checked by the Atlas agent; do not populate with guesses from repository filenames. For time-sensitive provider data, verify versions before claiming a current capability; older basic papers may not need constant rechecking.

---

## Original source: `07_state/08_decision_and_reversal_ledger.md`

# Documented decision and reversal ledger

| Decision ID | Topic and scope | Chosen approach | Alternatives | Reasons and evidence | Date/SHA | Reversal trigger | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use to distinguish an architectural choice made under known constraints from a general knowledge fact. If later evidence changes, add a superseding entry and update affected documents instead of silently deleting history.

---

## Original source: `07_state/correction_log.md`

# Correction Log (template)

| Date | Failure | Root cause | General rule | Test | Fixed in |
| --- | --- | --- | --- | --- | --- |
| … | … | … | … | … | … |

## v2 correction — component depth mismatch
- Observation: user reported fewer substantive components than were originally described despite a 40-file ZIP.
- Cause: count/existence validation passed while detailed domain workflows and implementation/evaluation specialization were not fully written.
- Change: add A–H playbooks, operational workflows, source and dependency protocols, schemas, end-to-end examples, read-only validators, and an explicit feature-to-file map.
- Prevention: audit *substantive coverage* alongside file existence, with sample walkthroughs and minimum-depth checks. See `08_validation/06_self_heal_instructions.md`.
- Status: applied to this instruction-package revision; Atlas repository itself not modified.

---

## Original source: `07_state/decision_log.md`

# Decision Log (template)

| Date | Target revision | Decision | Reason | Paths | Alternatives considered |
| --- | --- | --- | --- | --- | --- |
| … | … | … | … | … | … |

---

## Original source: `07_state/source_ledger.md`

# Source Ledger (template)

| Claim | Source | Source date/version | Evidence class | Limits | Reviewed on |
| --- | --- | --- | --- | --- | --- |
| … | … | … | … | … | … |
