# Agentic instruction-set discovery

**Scope:** This registry indexes reusable agent instruction systems. It does not index every topic inside each package and does not prove that a provider, model, tool or research claim is currently valid.

## Retrieval contract

1. Prefer exact package IDs or canonical paths when known. Otherwise translate the user or coding-agent goal into a text query, optional primary role, capability and domain.
2. Search this registry first; fetch only the top relevant package READMEs and source entrypoints. Do not load every instruction system into context.
3. Compare candidate **purpose, boundaries and actual available source files** before selecting one. Return 1–3 candidates with a concise reason, the canonical paths and the branch/revision inspected.
4. On a miss, retry synonyms or broaden constraints, then respond `no_matching_package` if necessary. Do not invent an instruction set, falsely claim full-repository coverage, or silently edit an unrelated package.
5. Treat `score` only as a deterministic heuristic over indexed text. It is not factual confidence, popularity, model quality or a benchmark.

## Machine-readable search commands

Run these from the repository root with Python 3.10+ (no third-party modules):

```sh
python3 scripts/search_registry.py validate
python3 scripts/search_registry.py facets
python3 scripts/search_registry.py search --query "AI research curator"
python3 scripts/search_registry.py search --query "coding mentor" --format text
python3 scripts/search_registry.py search --role curator --capability catalog-maintenance
python3 scripts/search_registry.py search --domain software-engineering
python3 -m unittest discover -s scripts -p 'test_*.py'
```

`search` emits a JSON object containing `schema_version`, `query`, `filters`, `count`, and `results`. Each result exposes `id`, `name`, `role`, `version`, `description`, `capabilities`, `domains`, and canonical `readme`, `archive`, `sources` paths, alongside `score` and `matched_fields` as an explainable ranking rationale.

## Metadata and maintenance

- `role`: one exclusive primary responsibility; use plural role folders for physical storage.
- `capabilities`: nonexclusive tasks the instruction set guides; `domains`: subject areas; `tags`: broad discovery facets.
- `aliases`: human/agent vocabulary and common synonyms; `use_cases`: concrete user goals expressed in natural language.
- `status`: only validated `available` packages are searchable. The pending Executive Product Repository Review sources do not become an available release just because a folder exists.
- `readme`, `archive`, and `sources`: must resolve to real files/directories matching role, ID and version.

Publishing should update registry metadata, category/root navigation, and alias/use-case search tests in one PR. New synonyms should be assessed for collisions and ambiguity; return multiple relevant results when evidence does not support a confident single choice. Exact and lexical retrieval are sufficient for this small package registry; only consider embeddings after comparing them against this baseline.

### Agent handoff

Provide the selected `id`, exact `readme` and `sources` paths, reason for the match, evidence boundary (metadata only versus source-inspected), and what permissions or tool capabilities still need verification. Tool interfaces and external facts are never guaranteed by an instruction-set description.
