# Codex native subagent adaptation — review candidate

**Status: documentation / integration candidate; not a deployed adapter or verified execution result.**

Use this when the execution surface is an *actual Codex app, interactive CLI, or IDE session* that exposes native subagent tools. A ChatGPT conversation using GitHub connectors is **not** automatically a Codex runtime. The existence of a provider-neutral interface in `runtime/ADAPTER_CONTRACT.md` does not create a callable tool.

## Evidence-backed provider capability

OpenAI's Codex subagent documentation describes project-scoped custom agents (`.codex/agents/*.toml`), built-in `explorer`, `worker`, and `default` agents, and explicit user or applicable project/Skill-instruction delegation requests. Current local Codex releases support native subagent workflows, but this package does **not** assume they are exposed in every hosted conversation or client.

- Official documentation: https://learn.chatgpt.com/docs/agent-configuration/subagents
- Config reference: https://learn.chatgpt.com/docs/config-file/config-reference

## Preflight gate — execute inside the real destination session

1. Confirm the host/runtime identity (client, version, project checkout, sandbox, agent controls and authenticated user). A user saying "I'm in Codex" is not enough if the active tool surface remains unchanged.
2. Check native subagent availability by **actual exposed tool or provider agent UI**, not text or configuration alone. Record `schemas/runtime-capabilities.schema.json` with truthful `features`, `spawn_mode`, evidence and constraints.
3. Verify registry checkout/connector, source-read permissions, and a **single immutable registry commit**. Resolve registry candidate, selected `SKILL.md`, manifest `read_when`/dependencies, governance and project revision from the same pinned inputs.
4. Verify the current session explicitly authorizes child delegation. Select a built-in agent (usually read-only discovery via `explorer`) or a reviewed project-specific custom agent; custom role files are configuration, **not** a bypass of parent sandbox or approval controls.
5. If a callable native child mechanism exists, request **exactly one** bounded child task, with source text/paths actually readable by the child. Ask the child to echo verifiable provenance metadata (package ID/version, registry commit, consumed section IDs/hashes) **and** produce grounded task evidence. Do not assume the child inherits retrieved parent instructions, complete chat history, GitHub tokens, or access to a different provider.
6. Capture the actual provider-generated child thread/handle and result. Reconcile assertions against the pinned source and task scope; an instruction echoed by a child is evidence of reception, not necessarily correct behavior.
7. Run `runtime/tests/MULTI_AGENT_PROPAGATION_001.md` and record each gate as PASS / FAIL / BLOCKED / NOT_RUN. Do not infer successful propagation from static configs, citations, CLI version output, mock adapters, or parallel GitHub API calls.

## Practical Codex setup

- Install/use an eligible current Codex app, CLI, or IDE extension with the target project open and the registry available at an authorized pinned ref.
- If using custom agents, create reviewed project-scoped TOML files in `.codex/agents/` with required fields `name`, `description`, `developer_instructions`. Do not invent role filenames or assert that adding them spawns agents. Prefer built-in `explorer` for a first read-only acceptance test.
- Use the project's applicable `AGENTS.md` or Skill to describe **when to delegate** and **how to resolve the registry**. Do not insert secrets or paste every specialist package into a global prompt.
- In the active Codex session explicitly request: "Use one subagent to assess this bounded read-only scope. Resolve the specified package and mandatory sections at pinned registry commit [SHA], record those section refs in the child result, and return source-grounded evidence. Do not submit PRs or modify files."
- Inspect the child thread/handle and the returned result. If no native child session appears, mark `spawn_mode: unavailable` for that session and use the documented sequential fallback.

## Adapter mapping and limits

| Logical contract | Native Codex mapping | Evidence required |
| --- | --- | --- |
| `probe` | Inspect actual Codex session's available subagent mechanism | Host, tool availability, permissions, measured capabilities |
| `spawn` | Invoke native delegation only if exposed/authorized | Provider child thread/handle, task ID, scoped instructions |
| `poll` | Inspect native thread progress if supported | Provider status/result; do not invent programmatic API |
| `cancel` | Stop/steer via actual supported session controls | Observed confirmation; otherwise NOT_AVAILABLE |
| `resume` | Continue supported native thread, or link a new task | Observed continuation; no guaranteed durable child |

The table is a **conceptual mapping**, not an implemented SDK/API adapter. Host-provided subagent tools must be called via their actual documented surface; a plain hosted ChatGPT session must not fabricate them.

For a hosted conversational control plane that lacks native delegation, a separately deployed authenticated gateway can implement `runtime/gateway.openapi.json`. A repository instruction cannot substitute for service deployment, identity isolation, lifecycle persistence, or permissions.

## Governance and cross-agent evidence

Follow `governance/approval.json`, `governance/capability-ownership/ownership-policies.json`, `schemas/subagent-task.schema.json`, and `runtime/CONTEXT_AND_ARTIFACT_CONTRACT.md`. Limit child context to task objective, package/version and verified section bytes/refs, project commit, approved permissions, relevant artifact refs and explicit acceptance criteria. Preserve source text integrity when transmitting instructions. Do not claim an independent reviewer unless the actual provider child was invoked and its trace is available.

The parent still owns scope, orchestration and fan-in. Children cannot approve their own outputs, merges or production releases. Missing access or ambiguity blocks dependent work; an honest sequential fallback is not a passing multi-agent test.
