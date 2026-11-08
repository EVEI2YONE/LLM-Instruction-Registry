# Composable workflows

The [primary lifecycle orchestrator](../orchestrators/primary/product-lifecycle-orchestrator/README.md) selects a bounded specialist or one/more workflow profiles. Workflows specify task routing and execution patterns rather than duplicating specialist instructions.

## Existing high-level workflows
- [Organization-to-MVP](strategic/organization-idea-to-mvp/README.md)
- [Software Delivery Lifecycle](engineering/software-delivery-lifecycle/README.md)
- [Catalog Consultation](shared/catalog-consultation/README.md)

## Focused workflow scaffolds
- [product-discovery](strategic/product-discovery/README.md)
- [business-feasibility](strategic/business-feasibility/README.md)
- [technical-feasibility](planning/technical-feasibility/README.md)
- [solution-architecture](planning/solution-architecture/README.md)
- [roadmap-release-planning](planning/roadmap-release-planning/README.md)
- [change-impact-analysis](shared/change-impact-analysis/README.md)
- [architecture-governance](engineering/architecture-governance/README.md)
- [release-governance](operations/release-governance/README.md)
- [incident-response](operations/incident-response/README.md)
- [product-outcomes](operations/product-outcomes/README.md)
- [backlog-refinement](planning/backlog-refinement/profile.json)
- [pragmatic-pr-review](engineering/pragmatic-pr-review/profile.json)
- [specialist-consultation](shared/specialist-consultation/profile.json)
- [approval-governance](shared/approval-governance/profile.json)

Execution patterns: sequential, parallel, council, conditional, feedback and approval. Workflow-local `responsibilities.json` defines artifact ownership and reviewer/approver contracts; [global policy](../governance/capability-ownership/README.md) sets cross-workflow rules. These are **declarative profiles**, not proof a workflow engine is deployed.
