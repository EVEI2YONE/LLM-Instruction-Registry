# Local workstation adapter profile

Entry: checkout at pinned commit, CLI search/section retrieval, provider-native instruction or skill loader if installed. Verify source path support, subprocess capabilities, git access, network policy, SDK version and permissions.

Execution: native supported subagent/SDK calls or a user-configured local worker with bounded subprocess or tool permissions. Each child gets a distinct run/task ID and a minimum scoped context envelope. No assumption that two CLI providers expose compatible child-agent APIs.

Storage: project-scoped SQLite context/artifact store for a single-machine prototype, immutable artifacts and audit; cross-process identity, concurrent transactional writes, backups and file ACLs must be configured before broader use.

Fallback: if model/SDK unavailable, discovery and planning continue read-only. Mark child execution blocked/unsupported; never return a fake completion. See [setup](../runtime/EXECUTION_SETUP.md).
