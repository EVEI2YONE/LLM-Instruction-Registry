# LLM Instruction Registry

A versioned registry of **orchestrators**, **composable workflows**, **independent specialists** and **shared governance contracts**.

## Entry points
- [Product Lifecycle Orchestrator v1](orchestrators/primary/product-lifecycle-orchestrator/README.md) — user-facing intent routing, specialist selection and workflow composition.
- [Meta-LLM Orchestrator v21](orchestrators/meta/meta-llm-orchestrator/README.md) — repository-first generation for verified chatbot, local agent, bot and ChatGPT Project workspaces.
- [Workflow catalog](workflows/README.md) — stages, execution patterns, coordination and capability ownership.
- [Specialist catalog](specialists/README.md) — independently invocable domain packages.
- [Available package registry](registry.json) — 49 registered packages with actual versioned archives and browsable sources.

## Architecture
```text
orchestrators/
  primary/    # user-facing intent router
  workflow/   # organization, feature, SDLC, research and release councils
  meta/       # generator and instruction-system evolution
workflows/
  strategic/ planning/ engineering/ operations/ shared/
specialists/
  business/ product/ design/ architecture/ engineering/
  quality/ security/ operations/ knowledge/ research/ general/
governance/
  capability-ownership/  # global ownership model and workflow matrices
  approval.json  handoff.schema.json
schemas/ templates/ knowledge/ docs/ scripts/
```

The primary orchestrator can call one specialist for a bounded task, a workflow for multi-stage coordination, or compose workflows for cross-lifecycle work. Workflow-local `responsibilities.json` binds artifact Owner, Consultant, Reviewer and human Approver capabilities; the target project provides actual accountable humans and approved document owners. The Meta-LLM progenitor generates and updates instructions, **not** day-to-day product work.

## Workflows and governance
- [Organization-to-MVP](workflows/strategic/organization-idea-to-mvp/README.md)
- [Software Delivery Lifecycle](workflows/engineering/software-delivery-lifecycle/README.md)
- [Catalog Consultation](workflows/shared/catalog-consultation/README.md)
- [Focused workflow profiles](workflows/README.md) for story refinement, architecture, consultation, PR review, release, incidents, impact analysis and outcomes.
- [Capability ownership and authority policy](governance/capability-ownership/README.md)
- [Workspace adapters](docs/WORKSPACE_ADAPTERS.md)
- [New lifecycle instruction package inventory](docs/LIFECYCLE_INSTRUCTION_CATALOG.md)

## Validation
```sh
python3 scripts/search_registry.py validate
python3 scripts/search_registry.py search --query "pragmatic PR reviewer"
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Published packages are ZIP archives plus complete browsable sources, with stable package IDs and version history. Workflow profiles are declarative and do not imply a live deployed scheduler. Actual runtime tool permissions must be verified. **Human approval** is required for merges, investments, production deployments and irreversible actions.

[Contribution guide](CONTRIBUTING.md) · [Publishing](docs/PUBLISHING.md) · [Role taxonomy](docs/ROLE_TAXONOMY.md) · [Migration map](docs/MIGRATION_MAP.md)

## Existing package upgrades
All previously uncovered original specialists and the Feature Extension Planning Council now have new versioned archives with optional workflow integration. Research, psychology, teaching and general conversation remain independently invocable; they are not automatically routed through the product lifecycle. See [the complete upgrade inventory](docs/LIFECYCLE_INSTRUCTION_CATALOG.md).

## Lookup-first rebuild foundations (draft)

The [full-registry migration plan](docs/LOOKUP_FIRST_REBUILD_PLAN.md) covers **all 49 published packages**, without a pilot subset. During the infrastructure phase, existing package sources, versioned ZIPs and `registry.json` remain unchanged.

- [Local and hosted agent runtime architecture](docs/LOCAL_AND_HOSTED_AGENT_RUNTIME.md)
- [Provider adapter and gateway setup](runtime/EXECUTION_SETUP.md) · [Gateway API contract](runtime/gateway.openapi.json)
- [Portable adapter profiles](adapters/README.md) · [Shared context and artifact contracts](runtime/CONTEXT_AND_ARTIFACT_CONTRACT.md)
- [Complete package migration inventory](migration/inventory.json)
- [Pending approval-policy reconciliation](docs/APPROVAL_POLICY_RECONCILIATION.md)

The new section-lookup CLI supports **lookup-first packages once migrated**; current packages continue to use `scripts/search_registry.py`. Local child-agent SDK integrations and hosted gateway deployment are separate runtime integration work, not implied by the presence of this repository.
