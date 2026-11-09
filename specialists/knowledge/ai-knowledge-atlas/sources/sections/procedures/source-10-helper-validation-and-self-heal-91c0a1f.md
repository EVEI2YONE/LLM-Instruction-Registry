# 10 Helper Validation And Self Heal

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `02_helpers/06_validation_and_self_heal.md`

# Helper — Independent validation and self-heal

## QA gates
- Scope: only authorized repository/files were modified.
- Discovery: candidate gaps checked against current existing content.
- Accuracy: sources support specific claims; unsupported claims labeled hypotheses.
- Semantic: aliases, dependencies, contradictions and alternatives handled.
- Implementation: code labels match actual execution; no phantom tests.
- Navigation: README catalog and internal relative links correct; no orphan documents.
- Research: meaningful metrics/test plans for strong claims; no fabricated performance.
- Agent response: dispositions, exact paths, status and uncertainty returned.

Report checks as `pass`, `fail`, `not_run`, or `not_applicable`, not all as success by default. Blocking failures prevent claiming completion. Missing external web/tool access should be visible in the report.

## Self-heal
When the user or a coding agent identifies a genuine assistant-originated error, record: original behavior, expectation, concrete root cause, failed instruction source, generalized prevention rule, proposed instruction change, and regression test. Correcting a specific document is separate from improving the curator instruction system. Never automatically weaken evidence or permission gates to satisfy feedback.
