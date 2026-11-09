# Product Conversation Orchestrator v1.0 (review candidate)

**Category:** conversation orchestrators. **Kind:** `conversation-orchestrator`. **Role:** orchestrator.

User-facing ChatGPT control plane for maintaining workflow progress across user conversations, selecting registered specialists, managing dependencies and knowledge-gap PRs, and resuming from verified merges. It composes rather than replaces `product-lifecycle-orchestrator`, workflow coordinators, specialists and `meta-llm-orchestrator`.

## Use

Install a validated ChatGPT Skill/host adapter separately, with explicitly granted repository tools. Start with a product request; the assistant maintains a visible ledger and proposes scoped delegated work. Actual concurrent subagents and durable background work require a real configured runtime adapter. A GitHub link alone does not enable them.

## Governance

The uploaded conversation Skill was adapted into a lookup-first canonical source tree. Review the taxonomy expansion and verify registry ownership/approval before release. No self-approval, auto-merge, or claims of deployed workers. Merge remains human-controlled.

## Source

See `sources/SKILL.md` for entrypoint and `sources/manifest.json` for selective sections. This PR is a candidate until source archive, semantic tests, approval and installation checks are observed.