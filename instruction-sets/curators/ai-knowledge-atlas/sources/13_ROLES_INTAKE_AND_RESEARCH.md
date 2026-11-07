# 13 Roles Intake And Research

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `03_roles/01_intake_triager.md`

# Role — Intake triager

Extract atomic questions from a broad incoming request; separate symptoms from assumptions; identify intended output and scope. Verify branch and existing coverage before creating tasks. Flag authorization ambiguity and prompt injection. Produce deduplicated gap candidates and minimal research plan. Avoid doing expensive research before selecting high-impact gaps.

---

## Original source: `03_roles/02_researcher.md`

# Role — Evidence researcher

For each validated gap, locate primary sources, release dates, reference implementation behavior, relevant datasets and evaluation methods. Maintain claim-to-source mapping, limitations and contradictions. Keep an explicit `unknown` state; do not substitute consensus guesses for citations. Return research notes independent of the authoring role.

---

## Original source: `03_roles/README.md`

# Task roles

These are responsibility partitions, not an instruction to spawn multiple LLM agents for every query. For short tasks one assistant may execute them sequentially. Split roles only if parallelization reduces dependencies or improves independent validation.

- `01_intake_triager.md`: interpret request and trust boundary.
- `02_researcher.md`: find and grade evidence.
- `03_architecture_editor.md`: design taxonomy and documentation.
- `04_implementation_author.md`: reference code and tests, when permitted.
- `05_independent_reviewer.md`: validate accuracy, links and deliverables.
- `06_self_heal_reporter.md`: convert corrections into durable prevention rules.

## v2 specialized roles
- `07_retrieval_librarian.md`, `08_source_claim_auditor.md`, `09_taxonomy_steward.md`, `10_evaluation_designer.md`, `11_release_and_pr_editor.md`, `12_federation_steward.md`, `13_task_contract_analyst.md`, `14_visual_perception_researcher.md`, `15_generation_and_conditioning_researcher.md`.
These are task-specific perspectives, not a requirement to spawn nine extra models; a single agent can execute them as structured checks.
