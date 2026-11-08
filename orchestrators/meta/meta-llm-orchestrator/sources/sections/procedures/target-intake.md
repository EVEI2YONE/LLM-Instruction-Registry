# Target runtime and generation intake

Use when about to create or upgrade an instruction package and the intended runtime, deployment surface, or permissions matter.

## Determine the assignment
Capture the user's desired agent outcome and representative user requests; expected inputs, outputs, boundaries, and success criteria; whether a new package, new version, correction, workflow profile, or deployment adapter is being requested. Distinguish **authoring environment** (where you are generating instructions) from **execution environment** (where the agent will run). Do not equate a provider name or subscription with tool access.

Record runtime capabilities individually as `verified-available`, `verified-unavailable`, or `unknown`, with evidence/ref/date: instructions channel, checkout/repository access, shell, file read/write, tool calls, child-agent API or SDK/process execution, gateway connection, network, persistence, artifact storage, concurrent execution, user permissions, human approvals, source quotas, available context and package/import limits. Use `schemas/runtime-capabilities.schema.json` and the target workspace's verified native configuration.

## Choose an execution mode
- **Local machine:** Can the target access a pinned checkout and a trusted provider SDK/process? Verify an installed runner and permission sandbox separately.
- **Hosted chat website:** Does it actually expose callable native subagents, or a registered tool to an authenticated gateway? Otherwise target a single-agent assistant and disclose limited functionality.
- **Hosted API application:** Which service owns identity, task queue, worker execution, state, secrets, and human callback?
- **Offline/prompt-only:** Supply deterministic generated bundles or prompt text only; mark inaccessible sections/capabilities and require manual ingestion.

## Decision output
Produce a compact target-capabilities report, selected adapter, missing capabilities and fallbacks, intended package kind, expected artifact format, autonomy/approval boundary, and version-pinned repo/project evidence. If an essential capability is unknown, do not silently turn that into a claim of installation, execution, durable memory, or spawn ability. Prefer a portable output with a verified later integration step.
