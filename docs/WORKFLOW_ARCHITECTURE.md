# Workflow architecture

Reusable instruction sets reside under instruction-sets/; workflow profiles live under workflows/. Specialization, workflow awareness, context-space awareness and execution permissions are independent. The Meta-LLM v19 generator chooses standalone vs workflow-aware vs orchestrator, discovers existing project sources and produces scoped instructions. The SDLC profile is the first example, not a mandatory default. Scope durable artifacts to project owners; do not duplicate project source of truth in this registry. [SDLC guide](../workflows/software-delivery-lifecycle/README.md).

## Organization-to-MVP and implementation specialization
Organization-to-MVP covers strategy, portfolio and MVP decision gates, while SDLC covers technical delivery and operations; both use the same canonical artifact references. Dedicated frontend/backend/AI packages have distinct ownership. AI Knowledge Atlas remains a research curator.
