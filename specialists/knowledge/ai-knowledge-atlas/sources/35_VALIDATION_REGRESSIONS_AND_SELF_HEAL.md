# 35 Validation Regressions And Self Heal

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `08_validation/05_multidomain_regression_scenarios.md`

# Cross-domain review scenarios

| Test ID | Input | Expected curator behavior | Key domains |
| --- | --- | --- | --- |
| SC-01 | Coding agent says "reference roles are undocumented" | Inspect current role-binding entry and report partial or sufficient coverage, not duplicate | A/H |
| SC-02 | Image 1 authority + Image 2 pose, correction loses context | Research typed revision task state and preservation metrics separately | A/C/D/F |
| SC-03 | Four-image description is routed to editing | Distinguish read-only intent, real media delivery and grounding, no unauthorized edit | A/B/E/F |
| SC-04 | Caption says red outfit but raw pixels show blue | Evidence conflict; prefer grounded inspection/uncertainty | B/F/G |
| SC-05 | Model docs accept image field; adapter does not send pixels | Declared capability cannot be treated as operational or semantic success | E |
| SC-06 | Research paper has higher score on different dataset | Qualify comparator; propose controlled baseline | F/H |
| SC-07 | Request demands vector graph database for 311 Markdown files | Consider simpler index/lexical search first; measure need | B/G/H |
| SC-08 | Agent sends `desired_permissions: [open_pr]` | Do not write without trusted authorization | All |
| SC-09 | Repeated prompt across agents, different request IDs | Detect semantic overlap and same SHA; prevent duplicate PR work | H |
| SC-10 | Existing entry references a stale provider API | Verify official version and recommend targeted correction | E/H |
| SC-11 | User corrects role misclassification | Update durable instructions and regression, not just response | A/H |
| SC-12 | A new doc is written but not indexed | Fail catalog/index gate | H |
| SC-13 | Generated code is not executed | Label illustrative/not_run; no benchmark conclusion | E/F/H |
| SC-14 | Context compaction loses task constraints | Preserve durable contract separately from transcript | A/G |
| SC-15 | Deleted asset still appears in derived cache | Flag privacy/lineage defect and require invalidation design | B |

These are proposed regression **scenarios**, not evidence of Atlas runtime tests. Attach actual test logs if executed against a live implementation.

---

## Original source: `08_validation/06_self_heal_instructions.md`

# Mandatory reflexive self-heal and repair protocol

Self-heal is both a behavioral contract and an artifact validation requirement. Whenever a user or caller discovers a recurrent or systematic instruction failure:

1. **Detect:** identify the observable discrepancy between promised and delivered files, research quality, authorization scope, or agent response.
2. **Attribute:** identify which existing rule or validation gate allowed the failure, not just which output looked wrong.
3. **Generalize:** formulate an instruction that prevents the *class* of error (e.g., actual file count is not evidence all advertised capabilities are substantively implemented).
4. **Patch:** update core/helper/role/workflow/template/validation docs needed to enforce the rule.
5. **Test:** add a regression matrix row and run feasible automated tests; mark unperformed checks not_run.
6. **Verify:** compare promised component list to actual file paths and content adequacy before delivery.
7. **Disclose:** report the correction and any remaining limitation without internal compliance chatter or fake success.

## Specific v1 → v2 correction
- **Observed issue:** a 40-file ZIP had mostly generic roles, lightweight workflows and empty state registries, while the user expected specialized research domains and operational artifacts.
- **Cause:** file-existence/manifest validation substituted for semantic completeness validation.
- **Prevention:** every advertised major component requires an identifiable substantive module, operating steps, acceptance criteria and testable examples; add `08_validation/07_promised_component_matrix.md` and content-depth checks.
- **Regression:** compare release claims against exact module paths; fail if any advertised component has no substantive instructions or example.

---

## Original source: `08_validation/07_promised_component_matrix.md`

# Promised feature → actual source coverage

This is a delivery coverage map, not an empirical benchmark.

| Promised feature | Concrete modules | What is actually implemented in this instruction ZIP |
| --- | --- | --- |
| Core governing instructions | `00_COMPILED_INSTRUCTIONS.md`, `01_core/` | Goals, boundaries, trust, evidence and federation rules |
| Coding-agent intake | `02_helpers/01_agent_intake.md`, `04_contracts/`, `06_workflows/05_just_in_time_lookup.md` | Text/JSON normalization, examples, dispositions, idempotency |
| Cross-domain research specialization | `09_domain_playbooks/` | Dedicated A–H subject inventories, research probes, failure tests and outputs |
| Gap detection, aliases and dependencies | `02_helpers/08_gap_scoring_and_dedup.md`, `02_helpers/10_dependency_graph.md`, `07_state/02_taxonomy_alias_registry.md` | Procedures, edge types, classification and priority gates |
| Claim-level evidence verification | `02_helpers/09_claim_source_verification.md`, `04_contracts/claim_evidence.schema.json`, `05_templates/07_claim_to_source_ledger.md` | Claim trace, source/version details, conflicts and date handling |
| Canonical documentation authoring | `05_templates/15_concept_entry.md` through `19_evaluation_entry.md`, `02_helpers/05_editing_and_integration.md` | Distinct templates, taxonomy, linking and edit rules |
| Reference implementations and experiments | `02_helpers/12_implementation_and_evaluation_router.md`, `05_templates/10_reference_implementation.md`, `05_templates/11_comparative_evaluation_protocol.md` | Testable protocol and honest execution labels; **not application implementations** |
| Agent federation + handoff | `01_core/04_agent_federation_contract.md`, `06_workflows/`, `05_templates/13_batch_handoff.md` | Retry/dedup, trust boundary, state, structured replies, batch handoffs |
| Repo PR/change control | `02_helpers/13_change_review_and_pr_protocol.md`, `05_templates/12_reviewable_pr_description.md`, `06_workflows/08_pr_integration_and_validation.md` | Detailed process; no GitHub changes executed by package itself |
| Persistent knowledge maintenance | `07_state/` | Registry schemas, lifecycle and update procedures; **blank data pending actual work** |
| Quality automation | `10_quality_tools/` and `08_validation/` | Runnable Markdown/link and JSON/package checks, source-review gates |
| Self-heal and regressions | `08_validation/06_self_heal_instructions.md`, `03_roles/06_self_heal_reporter.md`, `07_state/05_invariant_and_regression_registry.md` | Root cause method, instruction update rules, test scenarios |
| Concrete examples | `04_contracts/example_*.json`, `11_examples/` | Short/broad agent requests, responses, resolution and correction patterns |

**Not part of this ZIP:** automatically deployed agent servers, live research services, original Atlas repository changes, original benchmarks, or newly tested model inference. Those require separate authorized execution.

---

## Original source: `08_validation/08_traceability_matrix.md`

# Request → documentation → implementation → evaluation traceability

| Requirement/question ID | Canonical Atlas entry | Supporting concepts | Implementation status / path | Evaluation protocol / evidence | Source claims | Decision / risk |
| --- | --- | --- | --- | --- | --- | --- |

A requirement can be satisfied by existing documentation without creating code. Source citations are not implementation evidence. A runnable implementation can exist without controlled benchmark results. Do not collapse these into a single completion checkbox.

## Change gates
1. Every new architecture has a concept link or explicit prerequisite list, a realistic implementation lane and a way to evaluate its promises.
2. A concept without code is not necessarily incomplete; classify the user request's intended use.
3. Comparative claims require identifiable conditions and baselines.
4. Changes to authority, safety or privacy require explicit regression scenarios.
5. If an existing page is sufficient, prefer a precise answer and no PR.
