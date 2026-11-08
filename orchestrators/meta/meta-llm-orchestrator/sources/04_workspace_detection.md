# Target workspace and capability intake

## Required facts (do not infer from model name)
1. **Execution surface:** ChatGPT Project, hosted online chatbot, local agent/IDE, bot platform, CI agent, generic runner or hybrid.
2. **Target vs authoring:** The agent creating these files may be in a different workspace from the target agent that runs them.
3. **Instructions channel:** system/developer instructions, project configuration, repository agent file, installable skill, provider bot instructions or plain prompt.
4. **Accessible sources:** repository checkout/branch, remote GitHub connector, uploaded documents, knowledge base, API, web, local files, or none.
5. **Tool capabilities:** shell, editor, git, browser, fetch/search, filesystem, subprocesses, tool calling, issue/PR APIs, background/scheduling and sandbox test runner; probe each separately.
6. **Identity and permissions:** authorized actions, readonly/writable paths, network policy, secrets, approval gates and human authority.
7. **Persistence:** state across turns/runs, mutable workspace, connected storage, rehydration strategy, artifact upload limits, runtime/token limits.
8. **Output expectation:** installable skill ZIP, native bot instructions, repository docs, workflow profile, API-ready configuration or review PR.

Classify each capability as `verified-available`, `verified-unavailable` or `unknown`, with evidence. If unknown, choose a portable non-executable fallback and state required verification. A marketing feature description is not evidence that the current session can invoke it.

## Adaptation sequence
Inventory actual sources and permissions -> select [workspace adapter](05_target_adapters.md) -> choose reuse/extension/new package -> write portable core -> generate native wrapper only when supported -> run workspace-tailored tests -> present install/deploy path and actual verification.
