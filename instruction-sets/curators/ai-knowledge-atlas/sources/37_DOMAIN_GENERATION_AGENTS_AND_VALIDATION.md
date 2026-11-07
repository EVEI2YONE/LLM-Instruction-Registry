# 37 Domain Generation Agents And Validation

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `09_domain_playbooks/d_reference-conditioned-generation-and-transformation.md`

# Domain D — Reference-Conditioned Generation and Transformation

**Use when:** a coding-agent request implicates this domain. Do not assume all entries are missing. This is a research *checklist*, not an inventory of verified Atlas gaps.

## Candidate subjects from the example research request (18)
1. Multi-reference image conditioning
2. Reference-specific feature isolation
3. Identity-preserving image transformation
4. Style-preserving image transformation
5. Pose-guided generation
6. Image-reference adapters
7. Cross-attention conditioning
8. Spatial conditioning networks
9. Keypoint-conditioned generation
10. Dense pose and depth conditioning
11. Masked and localized image editing
12. Attribute-preservation constraints
13. Reference contamination and identity leakage
14. Conditioning conflicts
15. Multi-stage generation and refinement
16. Geometry versus appearance disentanglement
17. Generation consistency across iterative corrections
18. Model-specific conditioning interfaces

## Initial Atlas entry candidates (recheck current target revision)
- `architectures/systems/generation/reference-conditioned-generation.md`
- `architectures/systems/generation/identity-consistent-generation.md`
- `architectures/systems/generation/pose-guided-generation.md`
- `models/vision/image-editing-models.md`

## Specialized investigation probes
- Does a candidate model actually support independent multi-reference roles?
- Which appearance properties can be preserved under extreme geometric pose change?
- Which adapter/control path operates in image versus latent feature space?
- What baseline reveals identity/style leakage from the pose image?

## Techniques and distinctions to research
- Appearance and pose pathways separated
- Spatial control based on validated geometry
- Localized editing and original-pixel compositing where feasible
- Independent output validation and bounded repair

## Regression failures to test
- Pose drawing becomes the authoritative identity
- Global repaint destroys unmasked background
- Repeated editing progressively drifts facial features

## Expected domain-specific deliverables
- Conditioning mechanism matrix with documented provider constraints
- Reference precedence and preservation tradeoff contract
- Pose fidelity/identity/background-locality evaluation plan

## Evidence and editing gate
For each candidate, inspect relevant existing entries in full and label as `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, or `conflict_or_deprecation`. Do not convert this prompt's concept list directly into filenames. A research plan is not an experiment result. Source comparative technical claims to primary papers, official documentation, actual code, or reproducible studies. Document limits and independent baselines.

## Agent-to-agent handoff
Return canonical paths inspected, uncertainties, gap decisions, cross-domain dependencies, priority rationale, source review status and specific experiments required. When no trusted write authorization exists, keep proposed changes separate from verified changes.

---

## Original source: `09_domain_playbooks/e_agent-reasoning-tool-affordances-and-execution.md`

# Domain E — Agent Reasoning, Tool Affordances, and Execution

**Use when:** a coding-agent request implicates this domain. Do not assume all entries are missing. This is a research *checklist*, not an inventory of verified Atlas gaps.

## Candidate subjects from the example research request (16)
1. Tool affordance discovery
2. Runtime inspection of provider interfaces
3. Structural versus semantic capability verification
4. Capability-aware model registries
5. Constraint-preserving strategy synthesis
6. Typed execution-plan validation
7. Deterministic planning safeguards
8. Agent-generated execution hypotheses
9. Bounded reasoning and proposal repair
10. Provider adapter contract testing
11. Multi-input tool schema validation
12. Provider-response compatibility testing
13. Failure classification and remediation
14. Context-aware model selection
15. Policy-equivalent model fallback
16. Multi-agent versus deterministic orchestration

## Initial Atlas entry candidates (recheck current target revision)
- `architectures/systems/routing/capability-registries.md`
- `architectures/systems/routing/model-selection-and-fallback.md`
- `architectures/systems/routing/policy-aware-tool-execution.md`
- `agents/tool-use.md`

## Specialized investigation probes
- What provider operations and payload types are independently verified?
- Does a tool adapter preserve reference order and role metadata?
- Which operations are deterministic guards versus language-model suggestions?
- Does fallback preserve policy, constraints, modality and provenance?

## Techniques and distinctions to research
- Hard filtering before provider scoring
- Explicit tool I/O schemas and observed payload checks
- Bounded retry with idempotency and state reconciliation
- Deterministic policy enforcement at executor boundary

## Regression failures to test
- Schema-valid input was semantically ignored
- Fallback changes edit into unrelated generation
- Agent's proposed plan lacks an executable tool path

## Expected domain-specific deliverables
- Three-layer capability table: declared/operational/semantic
- Typed plan validity and executor authorization contract
- Provider adapter test suite and failure classifier

## Evidence and editing gate
For each candidate, inspect relevant existing entries in full and label as `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, or `conflict_or_deprecation`. Do not convert this prompt's concept list directly into filenames. A research plan is not an experiment result. Source comparative technical claims to primary papers, official documentation, actual code, or reproducible studies. Document limits and independent baselines.

## Agent-to-agent handoff
Return canonical paths inspected, uncertainties, gap decisions, cross-domain dependencies, priority rationale, source review status and specific experiments required. When no trusted write authorization exists, keep proposed changes separate from verified changes.

---

## Original source: `09_domain_playbooks/f_validation-evaluation-and-recovery.md`

# Domain F — Validation, Evaluation, and Recovery

**Use when:** a coding-agent request implicates this domain. Do not assume all entries are missing. This is a research *checklist*, not an inventory of verified Atlas gaps.

## Candidate subjects from the example research request (18)
1. Independent visual result evaluation
2. Reference-conditioned generation benchmarks
3. Pose-alignment evaluation
4. Keypoint distance metrics
5. Identity consistency evaluation
6. Attribute-preservation metrics
7. Rendering-style consistency
8. Background and composition preservation
9. Anatomical plausibility evaluation
10. Edit-locality metrics
11. Multidimensional task-success scoring
12. Model-as-judge reliability
13. Evaluator independence and calibration
14. Visual error taxonomies
15. Targeted correction strategies
16. Bounded validation/retry loops
17. Human-in-the-loop visual evaluation
18. Cost, latency, and quality tradeoffs

## Initial Atlas entry candidates (recheck current target revision)
- `evaluation/multimodal-upload-grounding.md`
- `architectures/systems/reliability/multimodal-validation-loops.md`
- `architectures/systems/reliability/evidence-grounded-execution.md`
- `evaluation/robustness.md`

## Specialized investigation probes
- What objective measures separately evaluate pose, identity, style and edit locality?
- Which automatic evaluators correlate with human judgment and under what data?
- What qualifies a local repair versus full regeneration?
- Which violations are hard failures even when a weighted average score is high?

## Techniques and distinctions to research
- Task-specific reference comparisons
- Hard preservation constraints before optional ranking metrics
- Blind human checks on failure-prone cases
- Model/tool trace plus reproducible result artifacts

## Regression failures to test
- One aggregate score hides broken identity
- Judge and generator share the same systematic bias
- Retry loop repeats the same faulty strategy without updating diagnosis

## Expected domain-specific deliverables
- Multidimensional evaluation matrix and severity gates
- Independent evaluator and human-review protocol
- Error taxonomy with targeted remediation and retry budget

## Evidence and editing gate
For each candidate, inspect relevant existing entries in full and label as `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, or `conflict_or_deprecation`. Do not convert this prompt's concept list directly into filenames. A research plan is not an experiment result. Source comparative technical claims to primary papers, official documentation, actual code, or reproducible studies. Document limits and independent baselines.

## Agent-to-agent handoff
Return canonical paths inspected, uncertainties, gap decisions, cross-domain dependencies, priority rationale, source review status and specific experiments required. When no trusted write authorization exists, keep proposed changes separate from verified changes.
