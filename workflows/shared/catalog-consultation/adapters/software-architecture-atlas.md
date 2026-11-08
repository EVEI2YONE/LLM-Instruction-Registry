# Software Architecture Atlas backend adapter

**Catalog:** https://github.com/EVEI2YONE/Software-Architecture-Atlas
**Consultant:** [Backend Architecture Consultant](../../../instruction-sets/experts/backend-architecture-consultant/README.md)
**Coordinator:** catalog-grounded-consultant; **implementation:** backend-engineering-specialist.

## Retrieval
Read actual repository SHA, then README.md, AGENTS.md, catalog/index.json, catalog/taxonomy.json and docs/retrieval.md. Search IDs, tags, aliases and related concepts using `python scripts/search_catalog.py "<question>" --json` when available. Retrieve only relevant full pages and sources. Status: stub means unknown, draft provisional, reviewed sourced (not target-proven), deprecated superseded. Coverage inventory is a timestamped snapshot. Atlas categories include principles, domain-design, code-organization, dependencies, runtime, distributed-systems, data, performance, quality, operations and governance.

## Architecture criteria
Examine actual backend modules/ownership, dependency direction, public contracts and API versioning, reuse vs over-abstraction, data transactions, concurrency, security, testability, deployment boundaries, observable workloads and scaling constraints. Compare no-change, feature modules in one deployable, modular monolith, library/project split or services based on concrete tradeoffs.

## Knowledge-gap / PR and reassessment
Use docs/curation-workflow.md, templates/gap-request.md, research/open-gaps.md and CONTRIBUTING.md. Historical docs/knowledge-gap-batches.md is not proof of open missing knowledge. Classify one gap per verified reusable concept issue, deduplicate aliases and batch by dependencies. When authorized create/reuse scoped Atlas-only PR with per-batch commits; validate with `python scripts/validate_catalog.py` and tests for index/search changes. Keep unmerged guidance provisional. Refresh Atlas baseline/PR head and target SHA before final ranked playbook. Backend code changes use a separate explicitly authorized PR.
