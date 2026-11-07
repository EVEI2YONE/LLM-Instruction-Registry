# 32 State Requests Gaps And Batches

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `07_state/README.md`

# Suggested persisted state files

These are **templates for future Atlas maintenance**, not claims they already exist in the live repository. The agent may keep these in its authorized working environment or propose dedicated Atlas governance directories later. Do not add them to Atlas without approval and clear maintenance ownership.

- `coverage_registry.md` — where canonical topics live and what's missing.
- `research_backlog.md` — unresolved questions, hypotheses and experimental plans.
- `source_ledger.md` — claim/source/version/validation classifications.
- `decision_log.md` — why entries were created, extended, merged or deferred.
- `correction_log.md` — recurring failures and prevention rules.

## Expanded lifecycle
New registries cover incoming requests, alias resolution, evidence reviews, batch ownership, invariant/regression status, open research, source recency and reversible architectural decisions. These are **templates** stored in this instruction ZIP; they are not current records from the target GitHub repository. The receiving project may persist them only in an approved location and with applicable access/retention controls. Entries must be based on observed actions rather than agent assumptions.

---

## Original source: `07_state/01_request_registry.md`

# Suggested request registry

This file is a template for a *receiving curator project*, not a record of live running jobs. Store only authorized sanitized metadata.

| Request ID | Normalized question | Target repo SHA | Caller class | Disposition | Latest status | Matching gap IDs | Last checked | Result ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Upsert procedure
1. Find exact request ID. For a replay at the same revision, reuse completed findings unless evidence is stale.
2. For new IDs, compare semantic equivalence *and* affected canonical paths to avoid duplicate research.
3. If target branch has moved, revalidate relevant findings; do not assume old citations still apply.
4. Record status with actual evidence. A task without an executor cannot be marked running.
5. Retire or anonymize old data under access/retention rules.

---

## Original source: `07_state/02_taxonomy_alias_registry.md`

# Canonical term and alias registry

| Preferred term | Aliases | Canonical Atlas path | Related but distinct concepts | Last inspected SHA | Ambiguity notes |
| --- | --- | --- | --- | --- | --- |

## Update rule
An alias requires confirmed equivalent meaning in the relevant context; avoid collapsing attention mechanisms and cross-attention variants, or task-reference identity and database asset identity, merely because labels overlap. Keep one canonical authoritative definition and link the terms where useful.

---

## Original source: `07_state/04_batch_execution_registry.md`

# Batch registry and handoff state

| Batch ID | Request IDs | Base SHA | Owner role | Files reserved | Authorization | Status | Checks executed | PR URL | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

No optimistic `PR URL` or `checks executed` fields. When concurrent edits target the same canonical entry, reconcile first. Stale branches need comparison against current main before reapply. Template rows do not imply that monitoring or autonomous execution has been installed.

---

## Original source: `07_state/coverage_registry.md`

# Coverage Registry (template)

| Topic | Canonical path | Adjacent paths | Coverage gaps | Evidence level | Last verified revision |
| --- | --- | --- | --- | --- | --- |
| … | … | … | … | … | … |

---

## Original source: `07_state/research_backlog.md`

# Research Backlog (template)

| Question | Hypothesis | Competing methods | Baselines/dataset | Metrics | Cost estimate | Confidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| … | … | … | … | … | … | … | … |
