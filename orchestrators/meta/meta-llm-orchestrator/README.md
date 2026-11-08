# Meta-LLM Orchestrator v22 — hosted and local

This is the lookup-first instruction **generator**, not a deployed product workflow or child-agent runtime. A single canonical source tree at [sources/](sources/) produces exactly two user-facing v22 ZIP distributions:

- **[Hosted v22](meta-llm-orchestrator_v22_hosted.zip)**: full assembled Meta-LLM instructions in `HOSTED_INSTRUCTIONS.md`; no script execution required by the receiving model. External registry and curated knowledge repos remain references, not bundled comprehensive copies.
- **[Local v22](meta-llm-orchestrator_v22_local.zip)**: canonical indexed source tree, procedures, manifests and tools for least-privileged source resolution and authorized lookup.

Run `python3 sources/tools/build_distributions.py --check --output .` to verify both release ZIPs against canonical sources. Rebuild only with `--write` under review. Full source manifest and entrypoint: [sources/manifest.json](sources/manifest.json), [sources/SKILL.md](sources/SKILL.md).

Previously released archives remain unchanged: [v21](meta-llm-orchestrator_v21.zip), [v20](meta-llm-orchestrator_v20.zip), [v19](meta-llm-orchestrator_v19.zip), [v18](meta-llm-orchestrator_v18.zip). Hosted instruction injection and file persistence require actual provider support; a ZIP cannot grant tools or approval powers.
