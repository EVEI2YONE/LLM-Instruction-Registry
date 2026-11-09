# Capability intake

The orchestrator's **own** source files may be platform-neutral. The **new agent instructions it generates must be tailored to the user's intended execution environment**. Before generating or choosing a target package, infer destination only from explicit current request or established conversation context. If unknown, ask exactly one concise natural-language question about where the user intends to use the generated agent. Do not substitute the current ChatGPT/container environment, and do not generate a generic agent as a workaround.

Suggested question: 'Where will you use the generated agent instructions: a ChatGPT Project or Skill, another hosted assistant, a local coding agent, or an API application?'

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

If the generated-agent destination is unknown, ask the single destination question and defer target-specific instruction generation. If known, do not ask again; resolve source-loading mode (injected, verified lookup, hybrid) and registry intent separately, asking one further question only if materially necessary. A request to edit the portable orchestrator's own repository files does not itself request a generated agent and therefore requires no destination question.
## Executable decision contract

For available authorized Python execution, use `tools/intake_gate.py` with a machine-readable JSON intake record. A generated-agent request without a known destination must produce `ASK_DESTINATION` before any target-specific package. A known destination and unknown loading method produce `ASK_LOADING_MODE` only when the loading distinction materially changes the output. Missing registry resolution produces `ASK_REGISTRY_DECISION` rather than speculative new authoring. `REUSE_UNCHANGED` with a changed target is an `ADAPT_EXISTING` output, not a canonical version bump. An `authoring_source_only` request skips generated-agent target clarification.
