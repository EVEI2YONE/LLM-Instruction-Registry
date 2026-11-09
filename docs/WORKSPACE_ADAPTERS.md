# Workspace-adaptive instruction generation

The [Meta-LLM Orchestrator v21](../orchestrators/meta/meta-llm-orchestrator/README.md) generates lookup-first instruction packages using **verified target capabilities**, not assumptions based on provider name.

## Supported target profiles

- [Online hosted chatbot](../orchestrators/meta/meta-llm-orchestrator/sources/adapters/hosted-chat.md)
- [Local Codex-style agent](../orchestrators/meta/meta-llm-orchestrator/sources/adapters/local-codex.md)
- [Local Claude Code-style agent](../orchestrators/meta/meta-llm-orchestrator/sources/adapters/local-claude-code.md)
- [Grok bot](../orchestrators/meta/meta-llm-orchestrator/sources/adapters/grok-bot.md)
- [ChatGPT Project](../orchestrators/meta/meta-llm-orchestrator/sources/adapters/chatgpt-project.md)
- [Generic portable](../orchestrators/meta/meta-llm-orchestrator/sources/adapters/generic-portable.md)

The generator's own source host and the **generated specialist's execution environment** are separate. When the latter is unknown, ask one concise user question before generating the tailored instructions. When known, reuse that answer; verify injection vs selective lookup independently. See [generation architecture](AGENT_INSTRUCTION_GENERATION.md).

Probe real instruction interfaces, repository/source lookup, native child agents, tool permissions, persistence, artifact storage, context/file limits, and human approval boundaries. Classify each capability as verified-available, verified-unavailable, or unknown. Generate native wrappers or upload bundles only for verified targets.

The Meta-LLM generator produces instructions and adapters; the [local/hosted runtime](LOCAL_AND_HOSTED_AGENT_RUNTIME.md) and a verified provider integration must execute any spawned agents. A repository link cannot create a hosted child-agent capability.
