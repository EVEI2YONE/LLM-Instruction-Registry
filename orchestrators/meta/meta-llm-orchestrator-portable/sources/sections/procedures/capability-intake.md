# Capability intake

Record these independent fields before building runtime output:
- `execution_destination`: actual host, API application, local runner, or unknown
- `source_loading_mode`: injected, verified_lookup, hybrid, or unknown
- `registry_operation`: reuse, upgrade, create, or unknown
- `registry_write_authority`: authorized, unauthorized, or unknown
- `approval_source`, `instruction_size_limit`, and evidence/status for each

Probe, do not infer: instruction channel, file reads and writes, network/repository access, shell/interpreter, tool APIs, native child-agent execution, persistent state, artifact store, actor identity, scope, quotas, and human approval callbacks. Mark each verified-available, verified-unavailable, or unknown.

Select a progressive execution tier:
A. Prompt-only: self-contained bounded instructions and manual handoff; no implied runtime files, registry script, or child agents.
B. File-readable: selective section retrieval via manifest with prerequisite closure; manual retrieval works without Python.
C. Tool-enabled: use only verified, permissioned tools and scoped artifact refs.
D. Multi-agent: only an authenticated verified runner/gateway can start children and enforce task budgets.

If essential destination details remain unknown, ask one specific question; when the user explicitly requested a review-only source PR, the destination is portable review source and no target installation is implied.