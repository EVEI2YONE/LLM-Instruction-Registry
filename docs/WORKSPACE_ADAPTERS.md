# Workspace-adaptive instruction generation
The [Meta-LLM Orchestrator v20](../orchestrators/meta/meta-llm-orchestrator/README.md) generates instruction architectures for **target runtime capabilities**, not based on provider name alone.

## Supported target profiles
- [Online hosted chatbot](../orchestrators/meta/meta-llm-orchestrator/sources/workspaces/online-hosted-chatbot.md)
- [Local Codex-style agent](../orchestrators/meta/meta-llm-orchestrator/sources/workspaces/codex-local.md)
- [Local Claude Code-style agent](../orchestrators/meta/meta-llm-orchestrator/sources/workspaces/claude-code-local.md)
- [Grok bot](../orchestrators/meta/meta-llm-orchestrator/sources/workspaces/grok-bot.md)
- [ChatGPT Project](../orchestrators/meta/meta-llm-orchestrator/sources/workspaces/chatgpt-project.md)
- [Generic portable](../orchestrators/meta/meta-llm-orchestrator/sources/workspaces/generic-portable.md)

Inspect tool access, permissions, supported instruction entrypoints, persistence, file limits and approval boundaries. Classify capabilities available/unavailable/unknown and create a thin runtime adapter around a portable core. The Meta-LLM generator is separate from the product-facing router.
