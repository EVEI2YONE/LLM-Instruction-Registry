# 38 Domain Context And Knowledge Organization

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `09_domain_playbooks/g_context-engineering-and-adaptive-computation.md`

# Domain G — Context Engineering and Adaptive Computation

**Use when:** a coding-agent request implicates this domain. Do not assume all entries are missing. This is a research *checklist*, not an inventory of verified Atlas gaps.

## Candidate subjects from the example research request (12)
1. Context-window budgeting for multimodal agents
2. Exact retrieval versus embedding retrieval
3. Evidence-aware context assembly
4. Persistent task memory versus conversational history
5. Observation compression and information loss
6. Adaptive analysis depth
7. Selective multimodal inference
8. Cost-aware capability selection
9. Reuse of validated analysis outputs
10. Cache-assisted versus direct multimodal inference
11. Progressive evidence escalation
12. Quality-aware inference budgets

## Initial Atlas entry candidates (recheck current target revision)
- `architectures/systems/multimodal/context-engineering.md`
- `architectures/systems/retrieval/hierarchical-multimodal-retrieval.md`
- `architectures/systems/operations/adaptive-inference-budgets.md`
- `algorithms/retrieval/hybrid-search.md`

## Specialized investigation probes
- When can a validated compact observation stand in for raw media?
- Which evidence gaps require escalating from metadata to crops to full pixels?
- What is the measured cost and quality of direct multimodal inference versus retrieval?
- How can long-term task contracts survive aggressive history compression?

## Techniques and distinctions to research
- Exact-first targeted retrieval
- Tiered evidence assembly and uncertainty disclosure
- Validated cache reuse with compatibility checks
- Distinct durable task contract versus disposable chat transcript

## Regression failures to test
- Summarization loses reference precedence
- A cached caption hides a fine image detail
- Large prompt crowds out decisive source evidence

## Expected domain-specific deliverables
- Context budget and selective-retrieval policy
- Direct-model versus cache-assisted baseline experiment
- Evidence sufficiency and escalation triggers

## Evidence and editing gate
For each candidate, inspect relevant existing entries in full and label as `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, or `conflict_or_deprecation`. Do not convert this prompt's concept list directly into filenames. A research plan is not an experiment result. Source comparative technical claims to primary papers, official documentation, actual code, or reproducible studies. Document limits and independent baselines.

## Agent-to-agent handoff
Return canonical paths inspected, uncertainties, gap decisions, cross-domain dependencies, priority rationale, source review status and specific experiments required. When no trusted write authorization exists, keep proposed changes separate from verified changes.

---

## Original source: `09_domain_playbooks/h_research-quality-and-knowledge-organization.md`

# Domain H — Research Quality and Knowledge Organization

**Use when:** a coding-agent request implicates this domain. Do not assume all entries are missing. This is a research *checklist*, not an inventory of verified Atlas gaps.

## Candidate subjects from the example research request (10)
1. Technical concept-entry standards
2. Architecture-to-algorithm traceability
3. Architecture-to-implementation traceability
4. Evidence-quality classification
5. Research-source freshness and validity
6. Reproducible experiment specifications
7. Open-question tracking
8. Contradictory evidence management
9. Cross-category dependency mapping
10. Agent-oriented knowledge retrieval and indexing

## Initial Atlas entry candidates (recheck current target revision)
- `research/paper-review.md`
- `research/reproduction-study.md`
- `evaluation/reproducibility.md`
- `architectures/README.md`

## Specialized investigation probes
- Does an entry name its canonical place and directly supporting sources?
- Which claims are unsupported, outdated, contradictory or original Atlas measurements?
- Can a coding agent locate and trust the relevant entry without loading the entire repository?
- Do architecture, implementation and evaluation files link to each other coherently?

## Techniques and distinctions to research
- Root-to-leaf navigation and meaningful catalog summaries
- Source-linked evidence labels
- Canonical entry and alias policy
- Independent review and explicit not-run tests

## Regression failures to test
- Duplicate pages contradict each other
- Unreviewed citations are treated as experimental confirmation
- New topic is orphaned from nested README

## Expected domain-specific deliverables
- Canonical taxonomy and typed dependency graph
- Claim-to-source ledger with review dates and contradictions
- Automated link/index checks, reproducibility and PR review matrix

## Evidence and editing gate
For each candidate, inspect relevant existing entries in full and label as `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, or `conflict_or_deprecation`. Do not convert this prompt's concept list directly into filenames. A research plan is not an experiment result. Source comparative technical claims to primary papers, official documentation, actual code, or reproducible studies. Document limits and independent baselines.

## Agent-to-agent handoff
Return canonical paths inspected, uncertainties, gap decisions, cross-domain dependencies, priority rationale, source review status and specific experiments required. When no trusted write authorization exists, keep proposed changes separate from verified changes.

## Living Atlas stewardship extensions (v2.1)
- Maintain a review queue with priority from knowledge volatility, agent query frequency when telemetry is authorized, architectural dependencies, source contradictions and stale review timestamps.
- Track canonical topic ownership and aliases; update root and nested README summaries with precise retrieval hints, not uninformative autogenerated labels.
- When introducing a new paper or method, identify which existing claims it revises, which use cases it actually supports, and whether reproduction evidence exists.
- Distinguish reviewed research from new developments that have merely been discovered; preserve uncertainty and revision history.
- Produce an agent-search smoke-test for each significant batch: representative queries, expected canonical retrieval targets, evidence-grounded answers, and false positive/duplicate checks.
