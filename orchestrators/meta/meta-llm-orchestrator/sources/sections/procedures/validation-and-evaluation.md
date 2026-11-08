# Validate generated instruction systems

Read when about to approve, publish, test, migrate or assess a new instruction package or workspace adapter.

## Static gates
- Valid skill frontmatter and stable ID/version/kind; entrypoint within advisory word budget unless justified for always-rules.
- Manifest section IDs/paths real, unique, under the package root, hashes and measured word counts current, no missing dependencies, cycles or unreachable mandatory sections.
- Mode and action lookup tables match the manifest's canonical `modes` and `read_when`, with no hand-edited drift; no duplicate authoritative compiled instructions.
- Referential links and pinned catalog knowledge valid or explicitly inaccessible; executable tools are real separate files, not falsely advertised Markdown snippets.
- Shared governance and human approval controls cannot be omitted by deferred loading; no unsupported native workspace filename, tool call, or inferred background action.
- ZIP CRC, safe paths, source byte equivalence and preserved prior releases; registry metadata and ownership consistency; no unrelated package changes.

## Behavioral tests
For each published package, design representative direct-task and workflow-mode requests with expected mode, mandatory section closure, allowed tools, output artifacts and human-approval result. Include negative cases: no matching package, inaccessible catalog, stale source, unknown runtime, unsafe delegated permissions, missing predecessor, simultaneous edits and unsupported hosted native subagents. Measure task completion, missed mandatory instructions, words/tokens read, lookup count and latency against the prior package baseline.

A real language-model evaluation requires running an actual configured model; deterministic CI can check references, archive integrity and synthetic routing only. Never label model behavior, external tool integration, real provider child agents or hosted deployment PASS if they were not executed. Save a per-package validation ledger and treat a failure as a versioned correction with a regression case.
