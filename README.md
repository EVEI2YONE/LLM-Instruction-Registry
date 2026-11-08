# LLM Instruction Registry

A versioned catalog of reusable LLM instruction systems grouped by **primary role** and indexed through searchable **capabilities** and **domains**. [Meta-LLM Orchestrator v18](instruction-sets/progenitors/meta-llm-orchestrator/README.md) is the foundational progenitor.

## Browse by role

- [Progenitors](instruction-sets/progenitors/README.md) — Foundational instruction architectures for producing and orchestrating instruction systems.
- [Curators](instruction-sets/curators/README.md) — Maintain authoritative, source-backed, current and searchable knowledge catalogs.
- [Experts](instruction-sets/experts/README.md) — Specialized expertise, evidence-based advice, teaching and technical judgment.
- [Strategists](instruction-sets/strategists/README.md) — Product and business direction, prioritization and long-term roadmaps.
- [Orchestrators](instruction-sets/orchestrators/README.md) — Coordinate specialists, dependencies, workflows, decisions and handoffs.
- [Generalists](instruction-sets/generalists/README.md) — Broad conversational and everyday problem-solving assistance.

## Lookup catalog

| Instruction set | Role | Version | Purpose | Archive |
|---|---|---|---|---|
| [Meta-LLM Orchestrator](instruction-sets/progenitors/meta-llm-orchestrator/README.md) | progenitor | v18 | Foundational progenitor for composing and coordinating specialized LLM instruction sets. | [ZIP](instruction-sets/progenitors/meta-llm-orchestrator/meta-llm-orchestrator_v18.zip) |
| [AI Knowledge Atlas](instruction-sets/curators/ai-knowledge-atlas/README.md) | curator | v2.1 | Living evidence-backed AI research catalog; source freshness, relevance, knowledge-gap curation, agent-friendly search and technical architecture reference. | [ZIP](instruction-sets/curators/ai-knowledge-atlas/ai-knowledge-atlas_v2.1.zip) |
| [UI/UX Design System Architect](instruction-sets/curators/ui-ux-design-system-architect/README.md) | curator | v1.1 | Catalog-first UI/UX knowledge and component audits and prioritized migration guidance. | [ZIP](instruction-sets/curators/ui-ux-design-system-architect/ui-ux-design-system-architect_v1.1.zip) |
| [Coding Partner / Mentor / Teacher](instruction-sets/experts/coding-partner-mentor-teacher/README.md) | expert | v1 | Engineering assistance, debugging, code review, and practical mentorship. | [ZIP](instruction-sets/experts/coding-partner-mentor-teacher/coding-partner-mentor-teacher_v1.zip) |
| [Psychology Advice & Research](instruction-sets/experts/psychology-advice-research/README.md) | expert | v1 | Psychology education, non-clinical advice, and evidence-aware research synthesis. | [ZIP](instruction-sets/experts/psychology-advice-research/psychology-advice-research_v1.zip) |
| [SOLID Visual Architecture](instruction-sets/experts/solid-visual-architecture/README.md) | expert | v1 | Architecture visualization and SOLID-oriented design instruction system. | [ZIP](instruction-sets/experts/solid-visual-architecture/solid-visual-architecture_v1.zip) |
| [Technical Research Project Instructions](instruction-sets/experts/technical-research-project-instructions/README.md) | expert | v2 | Evidence-backed technical research, architecture consulting, and teaching. | [ZIP](instruction-sets/experts/technical-research-project-instructions/technical-research-project-instructions_v2.zip) |
| [App Planning](instruction-sets/strategists/app-planning/README.md) | strategist | v1 | Business, product, architecture, stack, research, and engineering handoff planning. | [ZIP](instruction-sets/strategists/app-planning/app-planning_v1.zip) |
| [Business App Idea](instruction-sets/strategists/business-app-idea/README.md) | strategist | v1 | Instruction set for shaping business application concepts into actionable plans. | [ZIP](instruction-sets/strategists/business-app-idea/business-app-idea_v1.zip) |
| [Feature Extension Planning Council](instruction-sets/orchestrators/feature-extension-planning-council/README.md) | orchestrator | v1 | Council-based feature planning, scope, architecture, risk, and implementation handoffs. | [ZIP](instruction-sets/orchestrators/feature-extension-planning-council/feature-extension-planning-council_v1.zip) |
| [General-Purpose ChatGPT Conversations](instruction-sets/generalists/general-purpose-chatgpt-conversations/README.md) | generalist | v2 | Efficient, friendly general-purpose ChatGPT conversations with mode-sensitive pacing, credible research, source filtering, and self-heal guidance. | [ZIP](instruction-sets/generalists/general-purpose-chatgpt-conversations/general-purpose-chatgpt-conversations_v2.zip) |

**Pending, not registered as available:** [Executive Product Repository Review](instruction-sets/strategists/executive-product-repo-review/README.md), which currently has sources but no validated package ZIP.

Use [registry.json](registry.json) for programmatic lookup by stable `id`, `role`, `capabilities`, `domains` or `tags`. See [role taxonomy and relocation map](docs/ROLE_TAXONOMY.md).

## Agentic search and discovery

Use the [agent discovery protocol](docs/AGENTIC_SEARCH.md) and zero-dependency [registry lookup CLI](scripts/search_registry.py) to find instruction sets by natural-language goal, primary `role`, exact `capability`, or `domain`. The CLI returns compact ranked JSON with canonical source paths and match-explanation fields, without loading every package into context.

```sh
python3 scripts/search_registry.py search --query "coding mentor"
python3 scripts/search_registry.py search --role curator --capability catalog-maintenance
python3 scripts/search_registry.py facets
python3 scripts/search_registry.py validate
```

The [GitHub Actions discovery tests](.github/workflows/registry-search-checks.yml) verify metadata and canonical paths. Ranking is deterministic lexical relevance, not semantic inference, quality scoring or proof of tool capabilities.
## Folder structure

```text
instruction-sets/
  progenitors/ | curators/ | experts/ | strategists/ | orchestrators/ | generalists/
    <package-id>/
      README.md
      <package-id>_vN[.M].zip
      sources/
        README.md
        <instruction sources>
```

Every ZIP's internal root remains `<package-id>/`, regardless of role directory. Existing binary archives and source contents were relocated unchanged for this reorganization.

## Agent publishing instructions

Read [CONTRIBUTING.md](CONTRIBUTING.md), [docs/PUBLISHING.md](docs/PUBLISHING.md) and [docs/ROLE_TAXONOMY.md](docs/ROLE_TAXONOMY.md) before adding or moving instruction sets. Preserve actual sources and binary ZIP files, maintain canonical metadata and verify paths in a PR. Do **not** rerun the legacy `scripts/rebuild_registry.py` script, which only supported an older `packages/` migration.

## Workflow-aware collaboration

[Meta-LLM Orchestrator v19](instruction-sets/progenitors/meta-llm-orchestrator/README.md) can generate standalone or workflow-aware specialists. [SDLC workflow-specific usage](workflows/software-delivery-lifecycle/README.md) explains coordinating them with existing project artifacts. [Workflow architecture](docs/WORKFLOW_ARCHITECTURE.md) supports future workflow profiles.

## Top-down organizational workflow
[Organization-to-MVP](workflows/organization-idea-to-mvp/README.md) coordinates strategy through MVP. Dedicated [frontend](instruction-sets/experts/frontend-engineering-specialist/README.md), [backend](instruction-sets/experts/backend-engineering-specialist/README.md) and [AI/ML](instruction-sets/experts/ai-ml-engineering-specialist/README.md) specialists support implementation.
