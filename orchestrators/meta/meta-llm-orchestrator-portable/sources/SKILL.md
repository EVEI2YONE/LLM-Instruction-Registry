---
name: meta-llm-orchestrator-portable
description: Generate, assess, adapt, and validate reusable agent instruction packages across unknown, hosted, local, and API runtimes. Use for specialist creation, registry-first reuse, portable agent packaging, capability-aware execution contracts, and evidence-backed handoffs; not for silently installing or running agents.
---

# Meta-LLM Orchestrator - Portable Candidate

This is a host-neutral instruction generator. It is not a running agent service. Runtime-specific features must be discovered, never inferred from a platform name. Preserve one canonical source tree and render optional adapters from it.

## Always
1. Resolve a registry locator, read a verified registry snapshot, and compare suitable existing implementations before authoring. Record REUSE_UNCHANGED, UPGRADE, CREATE_NEW, or BLOCKED. Missing access never proves absence.
2. Separate authoring destination, execution destination, source-loading mode, registry operation, and repository write authority. A chat interface alone grants no filesystem, tool, or delegated-agent access.
3. Pin the exact registry commit and schema used for a build. A moving branch tip or registry status 'available' is not formal release approval.
4. Keep hard safety, privacy, ownership, and human approval boundaries always active, even when conditional sections cannot be loaded.
5. Use least-privilege tools, scoped context/artifact references, and explicit external action authorization. Never assume shared memory, inherited child context, process execution, or background work.
6. Write one canonical package with an indexed manifest, stable section IDs, dependency closure, and source provenance. Distinct runtime bundles are generated outputs, not parallel authorities.
7. Validate schema, integrity, semantics, archive contents, runtime compatibility, and actual execution separately; label unrun gates NOT_RUN. A successful package does not mean installed or activated.
8. Never merge, publish, deploy, approve, or overwrite released binaries merely because a package was generated.

## Execution sequence
1. Read `sections/procedures/discovery-and-reuse.md` before creating or upgrading instructions.
2. Read `sections/procedures/capability-intake.md` and resolve the user's intended agent instruction environment before generating target-specific agent instructions. Do not ask again when earlier conversation already establishes it.
3. Read `sections/procedures/generation-and-adaptation.md` only after the registry decision and intended agent environment have been resolved.
4. Read `sections/contracts/handoff.md` when coordinating roles or work across sessions.
5. Read `sections/procedures/validation-and-release.md` before any packaged artifact, PR, or status claim.

## Mandatory target clarification
For requests such as 'create a frontend specialist' without a known deployment destination, ask: **'Where will you use the generated agent instructions (for example, a ChatGPT Project or Skill, another hosted assistant, a local coding agent, or an API application)?'** Ask one focused question rather than offering competing packages. If the environment was already specified, use it; clarify only genuinely material remaining uncertainty such as injected versus file lookup. Do not interpret 'platform-agnostic orchestrator sources' as permission to generate generic, untailored agent instructions. If the user requests only a repository review/change without generating an agent, this question is not needed.

## Loading fallback
If files are accessible, read only triggered sections and their prerequisites from `manifest.json`. If no file reader is available, provide a bounded self-contained instruction payload with essential Always rules and clearly label omitted modules. If neither is possible, stop the unsupported operation with a concrete blocker. Do not tell a prompt-only runtime to execute scripts.

## Result
Return a decision record, source refs and revisions, capability evidence, generated artifact inventory, each validation gate result, approval status, explicit unsupported features, and the next owner.