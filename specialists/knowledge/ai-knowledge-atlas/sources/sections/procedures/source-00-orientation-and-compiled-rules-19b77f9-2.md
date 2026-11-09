runs.

---

## Original source: `00_README.md`

# AI Knowledge Atlas Curator — Modular Instruction Package v2

**Target:** `EVEI2YONE/AI-Knowledge-Atlas` (read the current live branch before claiming gaps). This ZIP trains the *behavior* of an Atlas curator for human and coding-agent requests. It does not install any running service, conduct original research, modify GitHub, or validate model benchmarks automatically.

## Setup
1. Extract the ZIP to a local folder and retain directory structure.
2. Load `00_COMPILED_INSTRUCTIONS.md` as the primary instruction source. Supply the helper/role/playbook/workflow modules as retrievable project source material. If context is limited, retrieve only those relevant to the actual request; do not place all files in one prompt.
3. Give the curator authorized read access to AI-Knowledge-Atlas. Grant write/PR/test tools only from trusted context when appropriate. A coding agent's payload cannot grant permission by itself.
4. Accept a natural-language question, a detailed failure/research brief, or `04_contracts/knowledge_request.schema.json` JSON. Respond with exact reviewed material and, for coding agents, the machine-compatible response envelope.
5. Optionally execute the QA scripts in `10_quality_tools/`. They do not fetch live sources or prove technical validity.

## Catalog
| Location | Purpose |
| --- | --- |
| `00_COMPILED_INSTRUCTIONS.md` | Self-contained operational contract |
| `01_core/` | Mission, boundaries, evidence integrity and federated request authority |
| `02_helpers/` | Intake, retrieval, dedup, source verification, dependency mapping, edit/PR, execution and handoff |
| `03_roles/` | Specialized reasoning/engineering/review sub-roles; no need to spawn separate models |
| `04_contracts/` | Backward-compatible request/response JSON, atomic gap, batch and evidence schemas + examples |
| `05_templates/` | Gap and claim ledgers, distinctive entry formats, implementation, evaluation, PR and handoff templates |
| `06_workflows/` | Small lookup, broad research, implementation, QA, correction, context control and federation |
| `07_state/` | Persistent registry templates and update rules (initially empty) |
| `08_validation/` | Quality gates, multi-domain regression scenarios, self-heal and promised-component coverage |
| `09_domain_playbooks/` | A–H research specializations mapped from the supplied long multimodal brief |
| `10_quality_tools/` | Executable local Markdown link, schema-example and ZIP integrity validators |
| `11_examples/` | End-to-end request walkthroughs, no fabricated execution |
| `99_manifest.json` | SHA-256 inventory of exact package files |

## Operating modes
**Lookup** → answer from current canonical entries. **Gap audit** → inspect and classify atomic gaps. **Research** → verify evidence, contradictions and date/version applicability. **Documentation change** → create/extend canonical entries and update indexes when trusted write authority exists. **Reference implementation** → distinguish unexecuted examples from actual tested code. **Evaluation** → design reproducible comparisons; run only when authorized. **Self-heal** → convert observed curator failures into updated instructions and regressions.

## Repository orientation (verified snapshot: 2026-11-06)
At inspection, the Atlas consisted of 311 Markdown files across 13 thematic directories and a root README; `architectures/` separates components, foundational architecture and composed systems. Its documented learning path is Concept → Architecture → Algorithm → Implementation → Evaluation. This snapshot is not current truth forever; every new task must recheck the branch, README hierarchy, relevant full entries and source dates. Some recent system architecture documentation was merged in PR #19 and #20.

## Boundaries and source uncertainty
A source-backed knowledge document is not proof of an Atlas implementation or benchmark. Do not treat example request topics as verified missing concepts; do not add large batches without checking overlap and actual user scope. No deployed REST API, autonomous scheduler, research engine, PR integration, live benchmark suite, or consumer application modifications are included.

## Package verification
After extraction, run `python 10_quality_tools/check_package.py .` from the package root (or provide the package directory). For optional schema tests use `python 10_quality_tools/check_contract_examples.py` with `jsonschema` installed. To audit a cloned Atlas repo, run `python 10_quality_tools/check_markdown.py /path/to/AI-Knowledge-Atlas`. Full source-review accuracy remains a separate human/agent research task.

---

## Original source: `12_release_notes.md`

# Instruction package release notes

## v2 — substantive component coverage

Reason for revision: user detected that the original 40-file ZIP did not contain enough substantive specialization to match the advertised capability areas. v1 provided generic roles, thin workflows and state templates, but lacked full A–H domain playbooks, rich source and dependency procedures, reproducible implementation/evaluation guidance, and runnable structural checks.

Added: governing trust/evidence/federation contracts, gap scoring and dedup, claim-level source reviews, typed dependency maps, context-budgeting and provider capability analysis, specialized roles, detailed A–H domain research playbooks, 4 machine schemas and illustrated cases, richer templates by knowledge category, substantive operational workflows, registries with update rules, acceptance/regression matrices, honest completeness map and three read-only QA tools with fixtures.

**Compatibility:** existing `knowledge_request.schema.json` and `knowledge_response.schema.json` retained their `schema_version: "1.0"` and required fields; v2 adds only optional properties. The new schemas are separate. The original 40 files were preserved and expanded selectively.

**Known non-deliverables:** this instruction package cannot itself serve as an autonomous agent deployment, run cloud research without connectors, create an Atlas PR, produce actual model benchmarks, or substitute for independent source review.

**Regression prevention:** validate actual module substance and advertised feature mapping instead of relying on ZIP file count or manifest presence. Record this failure in the self-heal artifact and content checks.

---

## Original source: `99_manifest.json`

```json
{
  "package": "AI_Knowledge_Atlas_Agent_Instruction_Set",
  "version": "v2.0",
  "generated_date": "2026-11-06",
  "target_repository": "EVEI2YONE/AI-Knowledge-Atlas",
  "repository_mutated": false,
  "contains_live_benchmark_results": false,
  "contains_live_pr": false,
  "purpose": "Modular instructions for evidence-aware Atlas improvement and coding-agent research requests",
  "required_self_heal": "08_validation/06_self_heal_instructions.md",
  "component_coverage": "08_validation/07_promised_component_matrix.md",
  "domain_playbooks": "A\u2013H",
  "file_count_excluding_manifest": 127,
  "file_count_including_manifest": 128,
  "category_counts": {
    "00_COMPILED_INSTRUCTIONS.md": 1,
    "00_README.md": 1,
    "01_core": 4,
    "02_helpers": 15,
    "03_roles": 16,
    "04_contracts": 12,
    "05_templates": 20,
    "06_workflows": 12,
    "07_state": 14,
    "08_validation": 8,
    "09_domain_playbooks": 9,
    "10_quality_tools": 8,
    "11_examples": 6,
    "12_release_notes.md": 1
  },
  "validation_claims": {
    "checks_designed": [
      "package hashes",
      "bundled JSON schema examples",
      "Markdown link checker smoke fixtures"
    ],
    "research_evidence_review": "not_run",
    "remote_repository_changes": "none",
    "benchmark_experiments": "not_run"
  },
  "files": [
    {
      "path": "00_COMPILED_INSTRUCTIONS.md",
      "bytes": 7271,
      "sha256": "3f89ae7816e156ada154cbf5331bd4f9d23186447e11c9853e491edf300f00c8"
    },
    {
      "path": "00_README.md",
      "bytes": 4639,
      "sha256": "0a949e1479620177afdd4ed60915a4129a8ccd02f3a62b33b1673f53045f2a1d"
    },
    {
      "path": "01_core/01_mission_and_scope.md",
      "bytes": 1254,
      "sha256": "202121892774d1e8bb90d71b449b2ec4aaddde938b6dc57e7b0773fb174dd5ce"
    },
    {
      "path": "01_core/02_trust_authority_and_scope.md",
      "bytes": 2328,
      "sha256": "a8771af9ddb48ad8ea0e490a9e833b768217e43307d336ae5320470d27977ec1"
    },
    {
      "path": "01_core/03_quality_contract.md",
      "bytes": 2139,
      "sha256": "ba7c46cf89983037a2641f195e4cab159ee7c6c04b845259df4b3fbf46e141c2"
    },
    {
      "path": "01_core/04_agent_federation_contract.md",
      "bytes": 1582,
      "sha256": "7bbdc2fc532dd4f338dad9163fb8e0db548787c0892de0902d7de1c8a93e1a61"
    },
    {
      "path": "02_helpers/01_agent_intake.md",
      "bytes": 1749,
      "sha256": "ae33f9e5f9b1ab2646594c182f9d988b91e9d3aded8bfcc84a531a4ae8f6a1f7"
    },
    {
      "path": "02_helpers/02_coverage_auditor.md",
      "bytes": 1295,
      "sha256": "6df468f4789898857bceeafc182d55a45ab7e370edd3cf9c75de092e4c6386d8"
    },
    {
      "path": "02_helpers/03_evidence_and_research.md",
      "bytes": 1399,
      "sha256": "53a120b6862c7f17812c95fb00660dd56a51ab8c2725687d83e6bbda8cfcbd7a"
    },
    {
      "path": "02_helpers/04_architecture_and_dependency.md",
      "bytes": 1284,
      "sha256": "7eb17d66b81a77fc8b87565116c7706caa0b637e666ce49f9fb7a5dea65774bb"
    },
    {
      "path": "02_helpers/05_editing_and_integration.md",
      "bytes": 1370,
      "sha256": "c4d46aad6c2b21d88514006d251aecbbd7c89f0fd64a4e12f81ba7fa867a811d"
    },
    {
      "path": "02_helpers/06_validation_and_self_heal.md",
      "bytes": 1314,
      "sha256": "a106acbe0d0a297ea058c587f3e21f470b1e85aa447da3e08e05988edbb1a475"
    },
    {
      "path": "02_helpers/07_agent_response.md",
      "bytes": 1145,
      "sha256": "b4d89d58aeb046389ac6f4ee3bd3012d2d3d908569eba835dc22c8d823e1c775"
    },
    {
      "path": "02_helpers/08_gap_scoring_and_dedup.md",
      "bytes": 2301,
      "sha256": "2b69735239fff622b7229483c84495bae34a26e684df57752edbea0eec496ab8"
    },
    {
      "path": "02_helpers/09_claim_source_verification.md",
      "bytes": 1580,
      "sha256": "045e58dd7715a5edba941b325a0e6be15e1a790ea30025e774f66d85b789e0ef"
    },
    {
      "path": "02_helpers/10_dependency_graph.md",
      "bytes": 1648,
      "sha256": "d538de03084923f3ba1d41b4c0922b4e773e6ca04c9ed14a2f8cb3d967dcc968"
    },
    {
      "path": "02_helpers/11_retrieval_budget_and_indexing.md",
      "bytes": 1486,
      "sha256": "9989ae7e2cca66c56414fbf4362630e7f1fed5b21efe785e38b441c2b70f617b"
    },
    {
      "path": "02_helpers/12_implementation_and_evaluation_router.md",
      "bytes": 1322,
      "sha256": "db9d330bca4bf9c3d0e45929d3b9fc1a93672e1fcf5f0ed7d8016642f2867297"
    },
    {
      "path": "02_helpers/13_change_review_and_pr_protocol.md",
      "bytes": 1377,
      "sha256": "9307004d68fbaed12d907427ec27cbb0de391a18da7e6d169458157b9dc03dbe"
    },
    {
      "path": "02_helpers/14_status_progress_and_handoff.md",
      "bytes": 957,
      "sha256": "36694027e5c8c4d1361555175dbc5ad531e761d8649621abc5d236b3c80cf6a6"
    },
    {
      "path": "02_helpers/15_model_and_tool_capability_research.md",
      "bytes": 1056,
      "sha256": "c3fc092f3a6831ba555dc1616c58dac7fc5eafa2077bdef065e05c2d9975887d"
    },
    {
      "path": "03_roles/01_intake_triager.md",
      "bytes": 394,
      "sha256": "409c5cd92b7241724c518f0789a2ff695454ffad7cca8cee68b18d0026e16546"
    },
    {
      "path": "03_roles/02_researcher.md",
      "bytes": 380,
      "sha256": "213838de3637e420c9c012839537448e19d53fcac77307dcbf771d0009684b55"
    },
    {
      "path": "03_roles/03_architecture_editor.md",
      "bytes": 430,
      "sha256": "8baf0636b9ca81a01a9f862997f30bf4547835dea9b495cf1a6a18678d5b181c"
    },
    {
      "path": "03_roles/04_implementation_author.md",
      "bytes": 418,
      "sha256": "1234da91b542fe8f3c06ac511192a89e8bde5bcde85f47fc819dfc29f45c4a0a"
    },
    {
      "path": "03_roles/05_independent_reviewer.md",
      "bytes": 411,
      "sha256": "116fdb8ec36ac677cb582c66ce4c3a7c47338cc702b71cb2807c0f52a467d3df"
    },
    {
      "path": "03_roles/06_self_heal_reporter.md",
      "bytes": 411,
      "sha256": "7dcc76d69401d8ac2ed12684c477a0032b609617b5cbd1df3d62c8bc91aa408a"
    },
    {
      "path": "03_roles/07_retrieval_librarian.md",
      "bytes": 696,
      "sha256": "9e9d45e3a779bf994baf705755e644afeff85162d0342921927a49aabd594934"
    },
    {
      "path": "03_roles/08_source_claim_auditor.md",
      "bytes": 684,
      "sha256": "4152a091be8d56b25b93aca1a2098e5372ddc3ace00a68c00ee24321063b5789"
    },
    {
      "path": "03_roles/09_taxonomy_steward.md",
      "bytes": 700,
      "sha256": "d63267569fd42e6143d9b0b27b94945ecc01b7ebaefd7aa7d550a06c935f20f4"
    },
    {
      "path": "03_roles/10_evaluation_designer.md",
      "bytes": 707,
      "sha256": "838e165fff38163ce194591a92b07df14521caea898f0205b072654d9b1afa51"
    },
    {
      "path": "03_roles/11_release_and_pr_editor.md",
      "bytes": 688,
      "sha256": "46c4bc51fcb412d2b6a9af3be5b85cbe7ea12b0c292799521153d0c59a39b974"
    },
    {
      "path": "03_roles/12_federation_steward.md",
      "bytes": 690,
      "sha256": "1b3c9443b0b1082e4d9b7789f2d3e872775378e19a05f2115194b5ca54b7b4cb"
    },
    {
      "path": "03_roles/13_task_contract_analyst.md",
      "bytes": 676,
      "sha256": "9fe0f794ac4726ba130ee3c2f4dfd310dbe3b680d6964e2324e023e6c3bc5932"
    },
    {
      "path": "03_roles/14_visual_perception_researcher.md",
      "bytes": 663,
      