# Meta-LLM Orchestrator v21 — lookup-first canonical source

The entrypoint is `SKILL.md`. Its action-triggered lookup table and modes derive from `manifest.json`. Read only task-required sections under `sections/`; load exactly one workspace adapter after probing the target.

**Architecture:** the generator is not the Product Lifecycle Orchestrator and does not spawn agents by itself. To generate dynamically composable agents, use the verified `runtime/ADAPTER_CONTRACT.md`, `runtime/CONTEXT_AND_ARTIFACT_CONTRACT.md` and versioned context/artifact schemas. Central common rules are currently draft v0 and cannot be assumed injected.

**Generation:** use `sections/procedures/registry-reuse.md`, then classify source instructions, generate the manifest and entrypoint, adapt to a verified workspace, validate, package and publish. This package has 13 addressable sections, six adapters, the YAML agent metadata and the deterministic `tools/build_lookup_package.py`.

**Verification:** from repo root run `python3 orchestrators/meta/meta-llm-orchestrator/sources/tools/build_lookup_package.py --check --archive orchestrators/meta/meta-llm-orchestrator/meta-llm-orchestrator_v21.zip`. For future source edits, use `--render` to refresh generated lookup tables and hashes, and `--zip` to build the deterministic versioned archive.

**History:** original v18, v19 and v20 ZIP files are preserved beside the new v21 ZIP. The v20 compiled source is historical, not part of the v21 canonical source tree. Other registered packages are not migrated by this release.
