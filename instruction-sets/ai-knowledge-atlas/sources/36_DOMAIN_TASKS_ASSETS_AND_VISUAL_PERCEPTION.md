# 36 Domain Tasks Assets And Visual Perception

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `09_domain_playbooks/README.md`

# Domain playbooks for broad coding-agent research requests

These eight playbooks cover **all subject lists A–H** in the user-supplied multimodal/agentic research brief. They are optional research overlays; the curator first classifies what the incoming request genuinely needs. None of these subjects should automatically become a new Atlas entry.

| Playbook | Research focus |
| --- | --- |
| A | Multimodal task contracts, reference semantics, corrections and authority |
| B | Asset identity, metadata, provenance, caches and retrieval |
| C | Pose, stylized geometry, spatial representations and uncertainty |
| D | Reference-conditioned editing, pose control and appearance preservation |
| E | Tool and model capability verification, planning and execution |
| F | Independent evaluation, error taxonomies and bounded recovery |
| G | Context efficiency, retrieval and adaptive inference budgets |
| H | Research quality, taxonomy, traceability and discoverability |

For every task, choose a relevant subset and return evidence, not just coverage checklists.

---

## Original source: `09_domain_playbooks/a_task-contracts-intent-and-reference-semantics.md`

# Domain A — Task Contracts, Intent, and Reference Semantics

**Use when:** a coding-agent request implicates this domain. Do not assume all entries are missing. This is a research *checklist*, not an inventory of verified Atlas gaps.

## Candidate subjects from the example research request (12)
1. Unified multimodal task contracts
2. Request-scoped reference-role binding
3. Reference authority and precedence
4. Conflict resolution among reference inputs
5. Conversational reference resolution across turns
6. Upload-set identity and ordinal semantics
7. Task continuation, correction, revision, and retry
8. Immutable constraints and mutable task parameters
9. Constraint propagation across execution graphs
10. Requested output modality versus model capability
11. Read-only versus write-capable task authorization
12. Preservation of original intent across tool failures

## Initial Atlas entry candidates (recheck current target revision)
- `architectures/systems/multimodal/reference-role-resolution.md`
- `architectures/systems/routing/intent-and-capability-routing.md`
- `architectures/systems/orchestration/agent-execution-state-machines.md`
- `agents/memory-and-state.md`

## Specialized investigation probes
- Is the request a new task, correction, continuation or retry, and what evidence proves it?
- Which task state fields are immutable across a correction, and which are explicitly mutable?
- Which source assets control identity, pose, composition and style, and what is their precedence?
- Does read-only analysis ever get routed to a writing tool, even under fallback?

## Techniques and distinctions to research
- Versioned declarative contract
- Immutable original-request intent with explicit amendment events
- State-machine transition guards
- Constraint propagation into execution and validation nodes

## Regression failures to test
- Correction silently drops original image authority
- Image ordinal is resolved against the wrong upload set
- Generated response changes requested output modality without approval

## Expected domain-specific deliverables
- Typed task contract with role binding, constraint set and revision history
- State-transition table for correction vs retry vs fresh intent
- Authorization boundary table and conflict-resolution tests

## Evidence and editing gate
For each candidate, inspect relevant existing entries in full and label as `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, or `conflict_or_deprecation`. Do not convert this prompt's concept list directly into filenames. A research plan is not an experiment result. Source comparative technical claims to primary papers, official documentation, actual code, or reproducible studies. Document limits and independent baselines.

## Agent-to-agent handoff
Return canonical paths inspected, uncertainties, gap decisions, cross-domain dependencies, priority rationale, source review status and specific experiments required. When no trusted write authorization exists, keep proposed changes separate from verified changes.

---

## Original source: `09_domain_playbooks/b_asset-intelligence-metadata-and-retrieval.md`

# Domain B — Asset Intelligence, Metadata, and Retrieval

**Use when:** a coding-agent request implicates this domain. Do not assume all entries are missing. This is a research *checklist*, not an inventory of verified Atlas gaps.

## Candidate subjects from the example research request (16)
1. Immutable asset identities
2. Ordered upload and message attachment references
3. Source and derivative asset separation
4. Versioned analysis records
5. Typed multimodal observations
6. Observation provenance and source attribution
7. Request-specific semantic roles
8. Content-addressed analysis caches
9. Cache compatibility and invalidation
10. Artifact dependency and derivation graphs
11. Exact-first retrieval
12. Hierarchical multimodal evidence retrieval
13. Evidence sufficiency and escalation
14. Semantic similarity versus exact identity
15. Scoped access and cross-thread authorization
16. Multimodal metadata lifecycle management

## Initial Atlas entry candidates (recheck current target revision)
- `architectures/systems/multimodal/asset-intelligence.md`
- `architectures/systems/asset-data/analysis-metadata-schemas.md`
- `architectures/systems/asset-data/content-addressed-analysis-cache.md`
- `architectures/systems/retrieval/hierarchical-multimodal-retrieval.md`

## Specialized investigation probes
- Which metadata is safe and inexpensive to store on upload?
- Which task-triggered analysis requires original media rather than cached captions?
- What combinations of source digest, analyzer version, preprocessing and access policy define cache compatibility?
- How are revoked or deleted assets invalidated across thumbnails, graphs, embeddings and derivative analyses?

## Techniques and distinctions to research
- Exact asset resolution before semantic retrieval
- Source-linked typed observations
- Per-analyzer status and uncertainty
- Cross-scope access filters and deletion propagation

## Regression failures to test
- Misleading filename becomes visual fact
- Similarity retrieval substitutes the wrong image for an exact asset ID
- Deleted asset observations leak from caches or retrieval indexes

## Expected domain-specific deliverables
- Asset/observation/provenance/derivative entity schema
- Lazy-versus-eager decision table with privacy and latency costs
- Versioned cache keys and invalidation test scenarios

## Evidence and editing gate
For each candidate, inspect relevant existing entries in full and label as `already_sufficient`, `clarify_existing`, `extend_existing`, `create_distinct_entry`, `research_needed`, `implementation_missing`, or `conflict_or_deprecation`. Do not convert this prompt's concept list directly into filenames. A research plan is not an experiment result. Source comparative technical claims to primary papers, official documentation, actual code, or reproducible studies. Document limits and independent baselines.

## Agent-to-agent handoff
Return canonical paths inspected, uncertainties, gap decisions, cross-domain dependencies, priority rationale, source review status and specific experiments required. When no trusted write authorization exists, keep proposed changes separate from verified changes.

---

## Original source: `09_domain_playbooks/c_visual-perception-and-spatial-understanding.md`

# Domain C — Visual Perception and Spatial Understanding

**Use when:** a coding-agent request implicates this domain. Do not assume all entries are missing. This is a research *checklist*, not an inventory of verified Atlas gaps.

## Candidate subjects from the example research request (16)
1. Human pose estimation architectures
2. 2D versus 3D pose estimation
3. Whole-body and fine-grained landmark estimation
4. Pose representation and skeleton topology
5. Keypoint schema interoperability
6. Sketch-to-pose interpretation
7. Pose estimation from stylized or anatomical drawings
8. Occlusion-aware spatial reasoning
9. Limb ambiguity and foreshortening
10. Geometric correspondence and image registration
11. Dense pose and spatial surface representations
12. Segmentation, depth, and edge-based representations
13. Subject and attribute decomposition
14. Region-level visual grounding
15. Spatial preprocessing and coordinate transformation
16. Uncertainty representation in inferred geometry

## Initial Atlas entry candidates (recheck current target revision)
- `models/vision/object-detection-models.md`
- `models/vision/segmentation-models.md`
- `architectures/systems/generation/pose-guided-generation.md`
- `evaluation/multimodal-benchmarks.md`

## Specialized investigation probes
- Do published pose models support stylized drawings or only photographs?
- What coordinate space, landmark topology and uncertainty encode body pose?
- Can a 2D skeleton represent occlusion, depth, hands and crossed limbs adequately?
- How does target camera projection change the apparent transfer of a reference pose?

## Techniques and distinctions to research
- Keypoints with confidence and topology
- Occlusion-aware landmark inference
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
