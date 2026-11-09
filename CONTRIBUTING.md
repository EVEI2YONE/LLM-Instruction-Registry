# Contributing

Canonical packages now live under `orchestrators/meta/`, `orchestrators/workflow/`, and `specialists/<domain>/`; workflows live under `workflows/<category>/`. Published packages must contain real ZIP archives plus browsable source files. Preserve package IDs and binary blobs across moves. Update registry paths and tests in one PR; do not register source-only scaffolds as available. Never merge without authorization.

## Specialist instruction authoring

Use the [Meta-LLM Orchestrator](orchestrators/meta/meta-llm-orchestrator/README.md) and [generation architecture](docs/AGENT_INSTRUCTION_GENERATION.md) to create, upgrade, repair or retarget specialist instructions. Search registered canonical sources first; do not clone a similar release ZIP as a template. Distinguish the generator's own host from the generated agent's intended execution environment; ask the user for the latter if not already established. Existing specialists can still be directly used without generation. Preserve old archive blobs and require separate migration reviews.
