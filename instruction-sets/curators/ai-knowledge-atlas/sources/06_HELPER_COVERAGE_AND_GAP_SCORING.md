# 06 Helper Coverage And Gap Scoring

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `02_helpers/02_coverage_auditor.md`

# Helper — Repository coverage auditor

1. Record actual branch/revision and collection time.
2. Inspect root README and current folder tree, then the most relevant category and nested README files.
3. Search for canonical term, alternate names, neighboring concepts and techniques. Read candidate entries, not merely their titles.
4. Score each knowledge need for **presence**, **depth**, **correctness**, **source support**, **operational utility**, **evaluation coverage**, and **cross-link discoverability**. Do not collapse into a single uncalibrated score.
5. Assign one disposition: `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, or `conflict_or_deprecation`.
6. For partial coverage, identify exact missing subsections. For complete coverage, return relevant paths and usage cautions. For an apparently missing term, check whether a differently named entry already covers the mechanism.
7. Prefer extending one authoritative home entry and adding cross-links over creating competing definitions.

Report one decision row per knowledge need with: name, status, priority, existing paths, missing specifics, dependency concepts, proposed path/edit, key sources to examine, and confidence with reasoning.

---

## Original source: `02_helpers/08_gap_scoring_and_dedup.md`

# Helper — Coverage, gap priority and duplicate control

## Deterministic triage sequence
1. Create an atomic knowledge need from each unanswered question; keep scenario facts separate from general requirements.
2. Resolve aliases (e.g., "reference role binding" versus "reference-role resolution") and record search terms.
3. Inspect root and nested README, path names, candidate full documents, and incoming branch. A filename match is insufficient.
4. Record each dimension independently: presence, factual correctness, depth, reproducibility, link discoverability, implementation utility, evidence strength and freshness.
5. Choose **one** canonical disposition: `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, `conflict_or_deprecation`.
6. Explain why a new entry is conceptually distinct if `create_distinct_entry` is selected. Prefer extension if mechanism, audience and prerequisite set match an existing canonical page.
7. Identify missing dependencies and mark their readiness. Do not author an advanced page built on absent definitions without a plan.

## Priority, not fabricated numerical confidence
- **Critical:** missing safety/authorization invariants, known incorrect claims influencing design, or an essential dependency blocking an active workflow.
- **High:** recurring agent demand, foundational concept omission, unsupported implementation guidance with concrete engineering impact.
- **Medium:** clearer examples, links, supplemental comparisons, outdated-but-not-harmful detail.
- **Exploratory:** speculative or nascent technique without established utility.

Prioritization is judgment plus evidence. Avoid arbitrary weighted precision unless validated against an agreed rubric. Report confidence with an explanation and search limits. `Not found` means not found in the inspected snapshot, not that the technique does not exist.

## Duplicate decisions
| Same underlying mechanism | Different scope or interface | Action |
| --- | --- | --- |
| Yes | No | Extend canonical entry / add alias |
| Yes | Yes | Consider distinct implementation/architecture page, cross-linked |
| No | Yes or no | New canonical entry may be warranted |
| Unclear | Any | Research and record ambiguity first |
