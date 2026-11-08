# 26 Templates Reporting And Handoff

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `05_templates/04_agent_reply.md`

# Response to coding-agent knowledge request {{request_id}}

**Disposition:** {{classification}} · **Status:** {{complete / partial / proposed / blocked}}

## Already present
- {{exact Atlas path}} — {{supported guidance}}

## Verified knowledge gaps
- {{gap}} → {{extend/create/research/implement/evaluate}}, evidence quality, confidence.

## Safe guidance available now
{{answer only what sources establish; limitations}}

## Changes / PR
{{actual modified file list and verified PR link OR “No repository changes made”}}

## Validation and remaining unknowns
{{pass/fail/not run, unresolved questions, research plan}}

## Next recommended action
{{smallest useful next step for caller}}

Attach matching structured `knowledge_response.schema.json` result when serving an automated workflow.

---

## Original source: `05_templates/05_self_heal_record.md`

# Curator self-heal record — {{date}}

- Trigger and reproduced failure: {{observed_behavior}}
- Expected behavior: {{expected}}
- Root cause / wrong assumption: {{root_cause}}
- Failed instruction files or gates: {{sources}}
- Generalized prevention rule: {{rule}}
- Proposed instruction edits: {{changes}}
- Regression scenario and pass/fail condition: {{test}}
- Status: proposed / applied / verified

Do not state "applied" unless the indicated source files were actually changed.

---

## Original source: `05_templates/12_reviewable_pr_description.md`

# Atlas contribution — {{batch}}

## Why this is needed
{{verified gap and user/agent scenario; no unsupported absence claims}}

## Existing material reviewed
{{main branch SHA and precise canonical paths}}

## Changes
{{file-by-file documentation vs example code vs index alterations}}

## Evidence classification
{{direct published claims / engineering guidance / original measurements / unverified questions}}

## Validation
| Check | Result | Evidence |
| --- | --- | --- |
| Relative Markdown links | pass / fail / not_run | {{command/log}} |
| Catalog inclusion | pass / fail / not_run | {{file list}} |
| Source attribution | pass / fail / not_run | {{review log}} |
| Tests and experiments | pass / fail / not_run | {{actual runs}} |
| Permission/scope | pass / fail | {{trusted grant / changed paths}} |

## Risks, open questions, and reviewer requests
{{unresolved checks, contradictory evidence, conceptual placements needing human review}}

**Merge:** not requested / requested / completed (only with verified tool result).

---

## Original source: `05_templates/13_batch_handoff.md`

# Knowledge work batch handoff — {{batch_id}}

- Incoming requests: {{ids}}
- Atlas base SHA: {{sha}}
- Worker/role and trusted permissions: {{agent + verified scope}}
- Initial candidate gaps: {{finding IDs}}
- Inspected canonical paths: {{files}}
- Primary sources reviewed: {{links, checked status}}
- Decision changes since last batch: {{changes}}
- Actual changed paths: {{verified diff or None}}
- Validation: {{pass / fail / not_run with evidence}}
- Remaining contradictions or blocked prerequisites: {{issues}}
- Proposed next batch: {{bounded tasks and acceptance}}
- Handoff state: {{proposed / partial / complete / blocked}}

Never phrase a proposed future batch as running in the background unless a job actually exists.

---

## Original source: `05_templates/14_agent_return_packet.md`

# Coding-agent answer and curator feedback — {{request_id}}

## Answer supported now
{{exact checked paths, relevant technical guidance and explicit limitations}}

## Disposition per uncertainty
{{atomic gap IDs, status, rationale, source quality and canonical paths}}

## Changes made (if any)
{{verified branch, file paths, test output and actual PR URL; otherwise No changes}}

## Known unknowns and risks
{{source and implementation uncertainties, privacy, provider revisions}}

## Recommended caller action
{{what can safely be used immediately; what requires additional verification}}

## Machine-readable envelope
Provide compatible `04_contracts/knowledge_response.schema.json` JSON alongside this summary when requested by an automated caller. Distinguish `complete`, `partial`, `proposed`, `blocked` and `rejected` accurately.
