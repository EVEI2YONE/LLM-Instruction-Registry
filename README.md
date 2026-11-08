# LLM Instruction Registry
Versioned specialist packages, workflow coordinators and a user-facing orchestration entry point.

## Architecture
- [User-facing Product Lifecycle Orchestrator (scaffold)](orchestrators/primary/product-lifecycle-orchestrator/README.md)
- [Workflow coordinators](orchestrators/workflow/README.md)
- [Meta-LLM progenitor](orchestrators/meta/meta-llm-orchestrator/README.md)
- [Declarative workflows](workflows/README.md)
- [Independent specialists](specialists/README.md)
- [Shared governance and schemas](governance/README.md)
- [Canonical available package index](registry.json)

```text
orchestrators/primary/ | workflow/ | meta/
workflows/strategic/ | planning/ | engineering/ | operations/ | shared/
specialists/business/ | product/ | design/ | architecture/ | engineering/ | quality/ | security/ | operations/ | knowledge/ | research/ | general/
governance/  schemas/  templates/  knowledge/  docs/  scripts/
```

The primary orchestrator chooses a direct specialist for bounded tasks or a workflow (possibly composed with other workflows) for multi-stage work. Workflow profiles define sequential, parallel, council, conditional, feedback and approval stages, resolving specialist packages by capability. Published package IDs, versions and ZIP blobs are preserved by this relocation.

**Scaffold status:** The new primary entry point and composable example profiles are not published agent releases. [Migration notes](docs/MIGRATION_MAP.md).
