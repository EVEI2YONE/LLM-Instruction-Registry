# 23 Templates Documentation

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `05_templates/02_technical_entry.md`

# {{Canonical concept title}}

> **Atlas category:** {{category}}  
> **Evidence classification:** {{published evidence / engineering guidance / original validation / hypothesis}}  
> **Source review:** {{date}}  
> **Validation status:** {{not run / tested + artifacts}}

## Scope and why it matters
{{definition, differentiators, user problem}}

## Preconditions and conceptual dependencies
{{links to prerequisite entries}}

## Mechanism and data contracts
{{specific operation, interfaces, inputs/outputs, math/diagram if useful}}

## Alternatives and tradeoffs
{{comparisons with stated assumptions}}

## Implementation considerations
{{reference approaches without implying execution}}

## Failure modes, risks and limitations
{{specific caveats, policy/security/privacy where relevant}}

## Evaluation and open questions
{{datasets, baselines, metrics, reproducibility and remaining unknowns}}

## Related Atlas entries
{{relative Markdown links}}

## Primary sources
{{source, title, version/date, supported claim}}

<!-- Adapt headings to the topic. Do not fill irrelevant sections to meet a quota. -->

---

## Original source: `05_templates/15_concept_entry.md`

# {{Concept}} — conceptual reference

> Category: concept | Evidence: {{class}} | Source review: {{date}}

## Definition and boundaries
{{distinct from adjacent terms}}
## Mechanism and intuition
{{precise principle, mathematical symbols only if useful}}
## Preconditions and examples
{{one positive and one counterexample}}
## Limitations and misconceptions
{{where concept does not apply}}
## Related methods, architectures and evaluations
{{canonical Atlas links}}
## Primary sources
{{claim-linked references}}

---

## Original source: `05_templates/16_algorithm_entry.md`

# {{Algorithm}} — algorithmic reference

> Category: algorithm | Evidence: {{class}} | Source review: {{date}}

## Task, assumptions and representation
{{inputs, outputs, invariants, objective}}
## Steps and pseudocode
{{non-executed unless explicitly tested}}
## Complexity and behavior
{{time/memory; cite formal results where applicable}}
## Alternatives, edge cases and failure modes
{{fair comparison settings}}
## Implementation and tests
{{reference pattern, test conditions, exact result status}}
## Related Atlas entries and primary sources
{{links and claim-level references}}

---

## Original source: `05_templates/17_system_architecture_entry.md`

# {{System architecture}} — composition and control

> Category: systems architecture | Evidence: {{class}} | Source review: {{date}}

## Problem and boundaries
{{what system solves; non-goals}}
## Components, trust and data flow
{{models, data stores, retrieval, API, policy, human review}}
## Execution state and interfaces
{{state machine, typed contracts, errors, retries, events}}
## Alternatives and resource costs
{{simple baseline first, latency, data/privacy, operational complexity}}
## Failure modes, recovery and security
{{including untrusted input and partial success}}
## Verification plan
{{unit/integration/system evaluations, metrics, hard safety constraints}}
## Cross references and sources
{{concepts -> algorithms -> implementations -> evaluation}}

---

## Original source: `05_templates/18_model_capability_entry.md`

# {{Model / model family}} — documented capabilities

> Category: model family | Source review: {{date}} | Evidence: {{class}}

## Input and output modalities
{{exact documented formats, limits and revisions}}
## Mechanism and training context
{{known vs undocumented}}
## Task-specific capabilities and limitations
{{declared / operational / semantically verified}}
## Evaluation applicability
{{benchmark datasets, model versions, comparisons and missing tests}}
## Deployment and governance
{{licenses, hardware, privacy, maintenance status}}
## Related architecture, implementation and source links
{{canonical references}}
