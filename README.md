# LLM Instruction Registry

Central registry of authoritative, reusable LLM instruction-set ZIP packages.

## Current packages

| Instruction system | Latest verified version | Archive | Provenance |
|---|---|---|---|
| Meta-LLM Instruction Architect | v18 | [Download v18 ZIP](packages/meta-llm-orchestrator/v18/meta_llm_orchestrator_instruction_set_v18.zip) | Reconstructed from current project source files |

## Deduplication policy

- **One current authoritative package per distinct instruction system.** Revisions to the same project are versions, not separate systems.
- **Compare archive contents, not just filenames.** Alternate names can represent identical packages. Do not assert duplication until hashes or extracted contents have been compared.
- **Prefer the latest complete, validated instruction set.** Preserve historical versions under the same project directory only when needed for rollback or provenance.
- **Distinguish instructions from supporting resources.** Project-source bundles, development plans, and repository exports are not automatically standalone instruction systems.
- **Do not silently reconstruct missing past packages.** Mark packages unavailable if only conversation-memory references exist without recoverable ZIP bytes.
- **Never overwrite an authoritative release without validating it.** For uploaded ZIPs, record version, date, source project and content hash when possible.

## Loading a package

Download and extract the selected ZIP. Refer to the package's own `00_README.md` for its source-material layout, and add the extracted files to the target project or agent.

## Import status

Additional instruction-related ZIP names were identified in the Library, including AI Knowledge Atlas aliases and versions. They are **not yet uploaded**: their original binary contents could not be recovered through the available file interface. The v18 package above is the only ZIP currently imported.
