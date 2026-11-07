# 28 Workflow Research And Batching

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `06_workflows/02_batched_execution.md`

# Workflow — Phased, reviewable work

| Phase | Key activity | Exit artifact |
| --- | --- | --- |
| 0. Intake | Parse questions, trusted authorization, target revision and constraints | Normalized request |
| 1. Audit | Inspect tree/READMEs/entries and deduplicate gaps | Verified coverage matrix |
| 2. Research | Gather primary evidence, conflicts and open questions | Source ledger and decisions |
| 3. Architecture | Resolve taxonomy, dependencies and canonical paths | File-level plan and graph |
| 4. Authoring | Modify authorized Markdown and optional reference code | Changed files with provenance |
| 5. Verification | Check links, accuracy, source support and test evidence | QA table with not-run statuses |
| 6. Handoff | Report exact changes, limitations, PR if any, agent response | Human report + typed result |

Broad requests (like the supplied multimodal/agentic research prompt) should be partitioned by dependencies and reviewer capacity, not executed as one monolithic generative pass. Prefer `0→1` as the first safe delivery when the scope is too large or permission unclear. Keep each batch coherent and independently reviewable. In later batches, recheck the target branch and previous changes; avoid overwriting concurrent edits.

---

## Original source: `06_workflows/04_broad_research_decomposition.md`

# Workflow — Broad multi-domain agent research request

**Objective:** Long research briefs should be normalized into atomic research questions and routed by actual dependencies, not copied verbatim into Atlas files.

**Why:** Long research briefs should be normalized into atomic research questions and routed by actual dependencies, not copied verbatim into Atlas files.

## Steps
1. Extract the request objective, motivating failure examples and generalizable subject list; flag any assumptions as unverified.
2. Inspect target Atlas main SHA, root, nested indexes and relevant content.
3. Map each candidate subject to existing entries, aliases and evidence status; use the domain playbooks only for relevant subjects.
4. Create a gap inventory and distinguish documentation gaps, algorithm gaps, research unknowns, reference-code gaps and evaluated claims.
5. Group non-conflicting work into bounded batches ordered by prerequisites and reviewer capacity.
6. If authorized, complete a batch with source checks, edits, indexes and validation. Otherwise return a reviewable proposal.
7. Return immediate existing guidance to the coding agent, then verified status and next safe action.

## Exit artifact
Gap inventory, typed dependency map, source ledger, batch plan and agent reply.

## Failure guard
Do not commit to a single giant PR, invent a complete research program, or claim all proposed concepts were absent.

---

## Original source: `06_workflows/06_primary_research_and_reconciliation.md`

# Workflow — Evidence-first research

**Objective:** Turn unclear technical claims into verifiable, qualified Atlas knowledge.

**Why:** Turn unclear technical claims into verifiable, qualified Atlas knowledge.

## Steps
1. State falsifiable or checkable questions.
2. Find and inspect primary research, original code, official APIs and pertinent evaluations.
3. Capture claim-to-source ledger with exact supporting locations, versions and dates.
4. Compare conflicting studies using comparable conditions; avoid mixing unequal metrics.
5. Classify evidence and explicitly isolate hypotheses or unknowns.
6. Write minimal canonical summary with sources and limits.
7. Get independent factual review before promoting strong claims.

## Exit artifact
Claim ledger, qualified findings and uncertainties.

## Failure guard
No invented comparative results, provider capabilities or source quotes.
