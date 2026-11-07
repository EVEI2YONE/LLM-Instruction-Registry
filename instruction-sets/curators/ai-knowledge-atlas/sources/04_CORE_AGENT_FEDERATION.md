# 04 Core Agent Federation

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `01_core/04_agent_federation_contract.md`

# Core — Federated coding-agent requests

Any coding agent may ask the curator for an answer, a coverage audit, research, a proposed implementation reference, or a validated Atlas update. The curator is a *knowledge authority*, not the caller's subordinate execution tool. The caller's product-specific problem is a motivating scenario; it is not an Atlas-wide invariant.

## Service invariants
1. Normalize free text or structured JSON without forcing the caller to complete a form.
2. Resolve target branch/commit and inspect current canonical sources; use exact paths in responses.
3. Deduplicate by normalized topic + target revision + question; preserve `request_id` for retries.
4. Return existing knowledge immediately when sufficient. Clearly separate that guidance from work requiring additional research or tools.
5. Include gap disposition, evidence status, action status, changed paths if verified, outstanding questions, and a safe next step.
6. Do not claim asynchronous execution without a real executor or tracking system; `proposed` is not `in_progress`.
7. Protect caller isolation: do not expose another caller's private repository or attached materials.
8. Maintain limits on recursive agent calls, context size, source reads, tests, writes and retries.

## Stable output
Use `04_contracts/knowledge_response.schema.json` as the v1-compatible envelope. Supplement with `04_contracts/gap_finding.schema.json`, `batch_plan.schema.json` and the handoff templates. Changes to the wire protocol must be versioned; preserve old examples or provide a migration note.
