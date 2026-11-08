# Product lifecycle orchestration architecture

There are three separate orchestration responsibilities:
1. **Primary user-facing orchestrator** (`orchestrators/primary/`): classify the request and route directly to one specialist, to a workflow, or to composed workflows.
2. **Workflow coordinators** (`orchestrators/workflow/`): choose collaborators, dependencies, sequential/parallel/council/conditional/feedback execution patterns, evidence gates and approval handoffs.
3. **Meta-LLM instruction generator** (`orchestrators/meta/`): create and version reusable instruction packages for the actual target workspace, not operate the product delivery pipeline.

Independent specialists live in `specialists/<domain>/`; declarative workflows live in `workflows/<group>/`. [Global ownership](../governance/capability-ownership/README.md) and workflow-local `responsibilities.json` bind exactly one artifact owner, contributors, consultants, independent reviewers and accountable human approvers.

The user-facing router may directly invoke a specialist for a bounded task. A multi-stage product idea uses Organization-to-MVP before authorized SDLC handoff. Refactors, incidents and PR review can enter at relevant specialist/workflow stages without repeating full business ideation. Project sources own actual PRDs, ADRs, code and release truth; the registry stores reusable behavior.

The [Meta-LLM workspace adapters](WORKSPACE_ADAPTERS.md) distinguish ChatGPT Projects, local Codex/Claude Code-style agents, Grok bots, hosted chatbots and other runtimes. Platform capabilities and permissions are discovered, not inferred. Workflow profiles are instructions and contracts, not proof of a deployed orchestrator service.
