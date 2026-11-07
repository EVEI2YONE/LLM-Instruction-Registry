# 11 Helper Retrieval And Capabilities

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `02_helpers/11_retrieval_budget_and_indexing.md`

# Helper — Context-efficient Atlas retrieval and cataloging

Use exact branch/path lookup for known references, then lexical/alias search, then subcategory README traversal, then optional semantic retrieval for broad questions. An embedding match is a *candidate*, not a verified answer; fetch the exact authoritative page and inspect relevant claims. Prefer BM25 or repository search before introducing vector infrastructure for a small Markdown corpus.

## Working set
- Start with root README, category README and small sets of candidate pages.
- Read only needed sections unless accuracy requires the complete file.
- Track which paths and commit SHA were actually inspected; do not claim whole-repo review after a narrow search.
- Cache path, section anchor, SHA and source-review metadata, not private caller artifacts.
- Reopen original references if summaries omit geometry, exceptions, footnotes or tests.

## Index maintenance
For new entries update local nested README, parent category README, root discovery links when topic warrants, and 2–5 canonical related links. Replace generic "Topic reference" summaries with meaningful descriptions as files are touched. Do not create misleading circular *dependency* edges, although ordinary reciprocal links are fine.

## Retrieval response
Return exact Markdown paths, short reason each is relevant, retrieved revision and uncertainty. Cite unmerged branch paths explicitly as pending rather than current mainline knowledge.

---

## Original source: `02_helpers/15_model_and_tool_capability_research.md`

# Helper — Capability and executable-contract verification

Model API accepts a type ≠ model interprets it; an interface mentioning image editing ≠ ability to preserve identity or pose. Verify at three levels:
1. **Declared:** official API/schema/README supports exact required operation, number and types of inputs, model version, output modality and constraints.
2. **Operational:** an actual authorized invocation successfully transmits and processes those inputs; tool adapter log/test supports this.
3. **Semantic:** task-specific evaluation confirms the model used the relevant inputs as intended and meets the quality/policy constraints.

Document negative cases (missing image payload, unsupported multi-reference roles, fallback losing original image, tool returning success without semantic compliance). Record provider revision and test context. Do not substitute LLM speculation for provider documentation or a real capability test. Keep planning invariants deterministic where possible and narrow agent discretion to strategy proposals.

## Search-friendly catalog contract (v2.1)
Each canonical entry should have an unambiguous scope, title, one-paragraph agent-facing abstract, searchable terminology/aliases, tags or facets where useful, upstream prerequisites, downstream implementation/evaluation links, last source check, and unambiguous evidence classification. Index entries should communicate intent and relevance—not merely say 'Topic reference'. For retrieval responses, return a compact citation-bearing packet: question, resolved canonical paths/SHAs, findings, evidence scope, limitations, and next verification action. Exact lookup/lexical search precede semantic or graph expansion; validate every retrieved claim against source text. Monitor search misses and synonym collisions as catalog gaps.
