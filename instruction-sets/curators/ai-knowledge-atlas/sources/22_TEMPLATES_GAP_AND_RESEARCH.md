# 22 Templates Gap And Research

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `05_templates/01_gap_assessment.md`

# Knowledge Gap Assessment — {{request_id}}

- Target repo/revision: {{repository}} @ {{revision_or_unverified}}
- Requester/use case: {{requester}}
- Authorized operations: {{verified_permissions}}
- Evidence search scope and limitations: {{scope}}

| Need | Verified status | Priority | Existing Atlas paths | Specific missing detail | Dependencies | Recommended action / path | Sources to check | Confidence + reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ... | already sufficient / clarify / extend / create / research / implementation / conflict | ... | ... | ... | ... | ... | ... | ... |

## Reused knowledge
Return exact relevant paths and what they support.

## False-positive gap assertions
Document topics thought to be missing that were already covered.

## Recommended bounded batches
Group related edits with small independent validation boundaries.

## Deferred/open questions
Describe insufficiency, not invented conclusions.

---

## Original source: `05_templates/06_comprehensive_gap_inventory.md`

# Complete gap inventory — {{request_id}}

- Target branch and SHA: {{ref}}
- Search scope (paths, aliases, source date): {{search_scope}}
- Caller / application context (redacted): {{context}}
- Verified permissions: {{trusted_authorization}}

| ID | Atomic topic | Alias checks / existing paths | Disposition | Missing specific detail | Impact priority + rationale | Dependencies | Proposed canonical home | Source review | Confidence + reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{id}} | {{topic}} | {{paths}} | {{status}} | {{gap}} | {{priority}} | {{prerequisites}} | {{path}} | {{status}} | {{confidence}} |

## Coverage already sufficient
{{paths + exact supporting sections; no unnecessary edit}}

## Missing implementation versus missing documentation
{{distinguish illustrative code, runnable reference, reproduced benchmark and full system}}

## Bounded batches
{{group by actual prerequisites; include validation, reviewer effort and authorization}}

## Deferred and disputed findings
{{conflicts, uncertainty, potentially incorrect initial claims}}

---

## Original source: `05_templates/20_research_backlog_item.md`

# Research question — {{id}}

- Canonical topic and Atlas paths: {{topic}}
- Evidence state: {{supported / conflicting / unknown}}
- Hypothesis: {{testable statement}}
- Existing evidence and exact sources: {{claim ledger}}
- Alternatives and simplest baseline: {{competitors}}
- Dataset / synthetic cases / privacy requirements: {{data}}
- Metrics and hard acceptance: {{criteria}}
- Budget/resources and permissions: {{approved or proposed}}
- Decision outcome: {{promote / reject / unresolved if not run}}
- Owner/dependencies/status: {{tracking}}
