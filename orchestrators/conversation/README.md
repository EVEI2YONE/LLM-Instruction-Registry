# Conversation orchestrators

- [Product Conversation Orchestrator v1.0 review candidate](product-conversation-orchestrator/README.md) — User-facing ChatGPT control plane for intent, tracked tasks, specialist routing, knowledge-gap PR dependencies and conversation continuation.

This category owns **conversational coordination and progress state**. It delegates lifecycle route selection to the existing primary orchestrator and stage ownership to registered workflow coordinators. No direct access to other chats, persistent subagent runtime, tool permission or merge approval follows merely from this category.
