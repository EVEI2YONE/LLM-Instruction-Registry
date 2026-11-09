inference
- Depth and dense-pose augmentation when needed
- Original-pixel review for disputed geometry

## Regression failures to test
- Crossed limbs interpreted backward
- Crop-space keypoints applied as full-image coordinates
- Missing body parts guessed with unjustified certainty

## Expected domain-specific deliverables
- Sparse/whole-body/dense/depth representation comparison
- Interoperable keypoint and coordinate mapping schema
- Spatial perception benchmark protocol for photo and sketch inputs

## Evidence and editing gate
For each candidate, inspect relevant existing entries in full and label as `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, or `conflict_or_deprecation`. Do not convert this prompt's concept list directly into filenames. A research plan is not an experiment result. Source comparative technical claims to primary papers, official documentation, actual code, or reproducible studies. Document limits and independent baselines.

## Agent-to-agent handoff
Return canonical paths inspected, uncertainties, gap decisions, cross-domain dependencies, priority rationale, source review status and specific experiments required. When no trusted write authorization exists, keep proposed changes separate from verified changes.
