# Deliverable acceptance: project- and task-agnostic

Apply this procedure whenever specialist outputs, sequential phases, or tool results are synthesized into a substantive user deliverable. It prevents **loss of material evidence**, not a prescribed domain-specific report format. Neither successful delegation nor a valid instruction receipt completes the user's requested deliverable.

## Determine acceptance from the actual task

1. Identify the **user-requested output**, its format, scope, level of detail, and acceptance criteria. Add only requirements explicitly supported by applicable registered specialist instructions, authoritative project sources, or higher-priority governance. Never import features, release checks, product/architecture decisions, terminology, or constraints from a previous project or regression fixture.
2. Collect the complete relevant outputs. Build a source-linked **material findings ledger**: each distinct material finding, conclusion, limitation, dependency, recommendation, unresolved question, or decision *as actually supplied*. Include stable IDs, source references, significance, and task relevance; preserve conflicting findings instead of silently choosing one.
3. Synthesize in the presentation best suited to the user's request. Preserve all material findings and source limitations without requiring a particular template, verdict, requirement matrix, validation taxonomy, release checklist, or backlog when those were not requested or supported. Lead with the requested answer; keep orchestration provenance concise and secondary.
4. Compare the deliverable against the ledger and task-specific criteria **before claiming completion**. Each material finding must be faithfully represented or explicitly excluded with a grounded reason; every claimed resolved decision needs authoritative resolution evidence and an authorized owner. If acceptance fails, revise the deliverable or report `DELIVERABLE_INCOMPLETE` with the precise omissions. A short status summary does not replace a substantive requested artifact.
5. Do not promote a project-specific example, test fixture, or incident observation to canonical instruction or a universal condition. Task-specific acceptance tests may require specialized fields, but only when the actual task and source authority justify them.

## Trust boundary

`runtime/deliverable_acceptance_gate.py` can verify that a structured deliverable retains source finding IDs and required task criteria, with traceable references. It cannot determine whether the original specialist findings are true, authenticate references, or prove substantive faithfulness from self-reported summaries. The reviewer must inspect actual source artifacts. A downstream execution adapter should fail closed on an incomplete report when such an independent check is configured.
