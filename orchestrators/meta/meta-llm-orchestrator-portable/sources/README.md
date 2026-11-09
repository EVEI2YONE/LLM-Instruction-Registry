# Portable Meta-LLM Orchestrator

Review candidate derived from the project's v26 instruction design, independently adapted for platform-neutral operation. This is a separate package proposal: it does not replace the existing `meta-llm-orchestrator` v21 and does not assert formal approval.

The canonical portable source is `SKILL.md` plus `manifest.json` and the indexed `sections/`. The filename SKILL.md is a neutral source-entrypoint convention here, **not** an assertion that any host has installed a native Skill.

## What platform-neutral means
Only the **orchestrator's own source/packaging** is host-neutral. When asked to generate a specialist, the orchestrator **must ask the user which target environment will run the generated agent if the answer is not already known**, and then tailor the generated instruction package to that environment. The source host and target host may differ. Do not generate one generic destination-agnostic specialist package by default.

## Use
1. Read `SKILL.md` and identify the operation.
2. Ask for the intended generated agent environment when not already established; then check its runtime capabilities using `sections/procedures/capability-intake.md`.
3. Use actual repository access to resolve a pinned registry snapshot; compare existing registered packages first.
4. Select triggered sections from the manifest and load their `requires` dependency closure.
5. Generate a canonical package or a target-specific rendered output only when needed.
6. Validate and record both observed and unavailable checks. Installing, deploying, runtime evaluation, and owner approval are separate actions.

## Portability boundary
Supported: manual section lookup, source-driven generation, registry-first reuse when accessible, explicit fallback decisions, output contracts, and evidence-led validation. Optional: native skill activation, hosted prompt injection, shell/Python lookup, child-agent API, network tools, persistent artifacts, and CI. No optional capability is required to understand or apply the core instructions; inaccessible authoritative inputs can still block specific actions.

## Publishing
This PR is intentionally unregistered while review and release gates are outstanding. The submitted ZIP is a real source archive, not an installed extension. Before registering as available, verify canonical JSON Schema, release ownership, archive bytes, registry validation, behavioral evidence, and approval. Keep the existing v21 archive immutable.

## Source basis
User-supplied Meta-LLM v26 review candidate and accompanying correction/provenance materials. These uploaded files are not claimed to be an already-approved registry release.
## Generation intake enforcement

The optional provider-neutral `tools/intake_gate.py` implements a deterministic pre-generation gate and emits an explicit ASK_DESTINATION/ASK_LOADING_MODE/ASK_REGISTRY_DECISION/READY/REVIEW_ONLY resolution. It never discovers repository sources, installs an agent, or grants permission. Without local execution, follow the same decision rules in `SKILL.md` and `sections/procedures/capability-intake.md`. An inferred current host is not a valid substitute for the user's intended generated-agent destination.
