# 03 Core Quality Standards

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `01_core/03_quality_contract.md`

# Core — Quality and scientific integrity contract

Atlas documents must distinguish **what was measured**, **what primary sources claim**, **what engineering reasoning suggests**, and **what is unknown**. The claim is the verification unit; a bibliography alone cannot validate a paragraph.

## Claim status
- `primary_supported`: accurately described by checked primary evidence within the original setting.
- `official_documented`: verified against a named provider specification, version and date.
- `engineering_inference`: architecture recommendation, not independently established.
- `original_measured`: experiment run exists with methodology, data, logs, hardware and metrics.
- `comparative_measured`: comparable baselines with data and controls; report uncertainty.
- `conflicted`: relevant source findings disagree; report conditions and test needed.
- `hypothesis`: plausible claim without sufficient validation.
- `unknown`: insufficient trustworthy evidence.
- `deprecated_or_changed`: formerly accurate behavior no longer current in stated version.

No file name, API schema acceptance, model self-confidence, embedding similarity or polished summary is proof of technical correctness. Use `not_run`, not `pass`, for unavailable tests. Explicitly label unverified examples. Never claim current SOTA without a dated, relevant comparison and acknowledged limitations.

## Evidence trace
For major claims, preserve `claim_id`, text, source title/URL, publication or docs version, access/review date, quoted supporting location (section/table/API field), applicability conditions, contradictions, evidence class, and intended Atlas path. Review actual source content where available; if unavailable, mark `not_verified` rather than inferring from its title.

## Editing standards
A good entry identifies scope, prerequisites, mechanism, I/O/typed structures where applicable, alternatives, counterexamples, failure modes, evaluation, and authoritative references. Technical depth must be proportional. Do not append 14 empty headings to a small glossary entry. Cross-link to canonical pages instead of copying their content.
