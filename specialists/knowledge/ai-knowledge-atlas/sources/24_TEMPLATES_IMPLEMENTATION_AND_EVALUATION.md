# 24 Templates Implementation And Evaluation

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `05_templates/03_implementation_and_experiment.md`

# Reference implementation / experimental protocol — {{topic}}

- Classification: pseudocode / untested sample / locally verified / reproduced experiment
- Related Atlas entry: {{path}}
- Hypothesis and intended scope: {{hypothesis}}
- Baseline / alternatives: {{baselines}}
- Inputs, data versions and licenses: {{inputs}}
- Dependencies, model/API versions, commit and hardware: {{environment}}
- Deterministic setup, commands and seeds: {{commands}}
- Expected outputs and acceptance tests: {{tests}}
- Metrics, methods, uncertainty and confounds: {{metrics}}
- Actual run logs and outcomes, **if performed**: {{evidence_or_not_run}}
- Cost/time estimate and constraints: {{resources}}
- Known limitations and follow-ups: {{limitations}}

Never place fabricated numeric results in the "actual outcomes" field. If no execution occurred, explicitly say `Not run`.

---

## Original source: `05_templates/10_reference_implementation.md`

# Reference implementation specification — {{topic}}

- **Execution label:** pseudocode / illustrative untested / locally executed / independently reproduced
- **Repository and exact path:** {{location}}
- **Related Atlas knowledge:** {{path}}
- **Intended behavior:** {{contract}}
- **Scope and non-goals:** {{boundaries}}
- **Inputs / outputs / error contract:** {{types and examples}}
- **Requirements:** {{language, libraries, model version, licenses, hardware}}
- **Security notes:** {{sandbox, secrets, artifact access}}
- **Minimal baseline and alternatives:** {{why chosen}}
- **Setup and commands:** {{not_run if unavailable}}
- **Unit/integration tests:** {{positive, negative, failure, boundary}}
- **Observed test output / logs:** {{actual log or explicitly Not run}}
- **Reproducibility information:** {{commit, dependencies, checksums, seeds, data}}
- **Known limitations:** {{limitations}}

Illustrative code must not be presented as production-ready. No paid service calls without approval.

---

## Original source: `05_templates/11_comparative_evaluation_protocol.md`

# Reproducible comparison protocol — {{question}}

**Hypothesis:** {{falsifiable statement}}
**Competing methods:** {{A, B, simple baseline, no-agent baseline where relevant}}
**Population/dataset and license:** {{data, splits, version, access}}
**Fixed conditions:** {{input contract, preprocessing, prompts, model revisions, hardware}}
**Metrics:** {{per-dimension fidelity/accuracy, calibration, latency, cost, security violations}}
**Hard failure thresholds:** {{non-compensable violations}}
**Randomization/repetitions:** {{seeds, paired cases, confidence/uncertainty}}
**Failure case strata:** {{rare inputs, stylized assets, occlusion, misleading metadata, privacy}}
**Human assessment:** {{rater instructions, blinding, reliability, adjudication}}
**Budget and setup:** {{estimated computational resources; not fabricated spend}}
**Run records:** {{command, commit, logs, artifacts, status Not run or executed}}
**Decision rule:** {{when method A warrants recommendation versus inconclusive}}
**Threats to validity:** {{leakage, benchmark contamination, distribution shift, judge dependence}}

Do not populate result tables with invented values; store experimental plans separate from actual outcomes.

---

## Original source: `05_templates/19_evaluation_entry.md`

# {{Evaluation method}}

> Category: evaluation | Evidence: {{class}} | Review date: {{date}}

## Claim being evaluated
{{specific task and failure type}}
## Dataset, baseline and protocol
{{source, collection, splits, control variables, reproducibility}}
## Measures and acceptance gates
{{per-axis metrics, confidence, non-compensable failures}}
## Human verification and model-judge limitations
{{bias and independence}}
## Results status
{{Not run unless logs/results exist; include uncertainty}}
## Limitations, references and related entries
{{risks, links}}
