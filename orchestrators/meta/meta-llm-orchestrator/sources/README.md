# Meta-LLM Orchestrator v22 — lookup-first canonical source

The entrypoint is `SKILL.md`. Its action-triggered lookup table and modes derive from `manifest.json`. Read only task-required sections under `sections/`; load exactly one workspace adapter after probing the target.

**Architecture:** the generator is not the Product Lifecycle Orchestrator and does not spawn agents by itself. To generate dynamically composable agents, use the verified `runtime/ADAPTER_CONTRACT.md`, `runtime/CONTEXT_AND_ARTIFACT_CONTRACT.md` and versioned context/artifact schemas. Central common rules are currently draft v0 and cannot be assumed injected.

**Generation:** use `sections/procedures/registry-reuse.md`, then classify source instructions, generate the manifest and entrypoint, adapt to a verified workspace, validate, package and publish. This package has 15 addressable sections, six adapters, the YAML agent metadata and the deterministic `tools/build_lookup_package.py`.

**Verification:** from repo root run `python3 orchestrators/meta/meta-llm-orchestrator/sources/tools/build_lookup_package.py --check` then `python3 orchestrators/meta/meta-llm-orchestrator/sources/tools/build_distributions.py --check --output orchestrators/meta/meta-llm-orchestrator/`. Build with `--write` instead of `--check`. There are exactly two new user-facing ZIPs: `meta-llm-orchestrator_v22_hosted.zip` and `meta-llm-orchestrator_v22_local.zip`; no unqualified v22 ZIP. The canonical source directory remains authoritative.

**History:** original v18, v19, v20 and v21 ZIP files are preserved beside the two v22 distributions. The v20 compiled source is historical, not part of the v22 canonical source tree. Other registered packages are not migrated by this release.

## Portable bootstrap (v22)

Read `references/source-locations.json` to resolve the logical registry ID, then `sections/procedures/source-bootstrap.md` to choose verified connected, local, web, or supplied snapshot retrieval. Scripts are run only when actually available and authorized. `sections/procedures/conversation-handoff.md` describes versioned file or inline continuation in sequential hosted chats; it does not assume persistent storage or automatic injection.
