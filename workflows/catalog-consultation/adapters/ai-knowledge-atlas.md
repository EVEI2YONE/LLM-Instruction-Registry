# AI Knowledge Atlas consultation adapter

## Existing specialist and catalog scope
Use `instruction-sets/curators/ai-knowledge-atlas/` (v2.1 as currently registered) as the **curator** and its real catalog repository as evidence. Do not conflate the LLM Instruction Registry with the AI Knowledge Atlas repository.
Use its consolidated instructions:
- `sources/00_ORIENTATION_AND_COMPILED_RULES.md`: canonical authority, evidence, retrieval and permission.
- `sources/06_HELPER_COVERAGE_AND_GAP_SCORING.md`: presence/depth/correctness/sources/implementation/coverage and disposition taxonomy.
- `sources/28_WORKFLOW_RESEARCH_AND_BATCHING.md`: dependency-aware atomic batches.
- `sources/29_WORKFLOW_IMPLEMENTATION_AND_PR.md`: authorized catalog PR and test evidence.

## Intake and routing
Appropriate for AI product questions, LLMs/agents, model/provider comparisons, RAG, evaluation, multimodal input, model-serving, cost and security. Inspect actual app code/architecture/media and corresponding catalog entries. Return existing guidance before suggesting catalog edits. Keep project-specific implementation failures in target repo issues. Primary research/official APIs or reproducible benchmarks may be required to validate generalizable AI claims.

## Curation and reassessment
Create atomic gaps and classify per Atlas dispositions. On authorized catalog branch batch canonical documentation and cross-links, record source freshness and executed/not_run tests, and open/reuse a catalog PR. Refresh catalog approved baseline and proposed PR ref, then re-read affected target paths. Report provisional vs approved recommendations and handoff scoped changes to AI/ML Engineering, Backend or Architecture Specialist as appropriate.
