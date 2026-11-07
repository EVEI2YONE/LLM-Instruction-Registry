# Instruction-set primary-role taxonomy

A package has **one primary role** (the central responsibility it owns), plus zero or more nonexclusive `capabilities` and `domains`. Do not duplicate an instruction set under multiple roles merely because it offers overlapping abilities.

| Primary role | Directory | Definition |
|---|---|---|
| `progenitor` | `instruction-sets/progenitors/` | Foundational instruction architectures for producing and orchestrating instruction systems. |
| `curator` | `instruction-sets/curators/` | Maintain authoritative, source-backed, current and searchable knowledge catalogs. |
| `expert` | `instruction-sets/experts/` | Specialized expertise, evidence-based advice, teaching and technical judgment. |
| `strategist` | `instruction-sets/strategists/` | Product and business direction, prioritization and long-term roadmaps. |
| `orchestrator` | `instruction-sets/orchestrators/` | Coordinate specialists, dependencies, workflows, decisions and handoffs. |
| `generalist` | `instruction-sets/generalists/` | Broad conversational and everyday problem-solving assistance. |

## Classification

1. Inspect the real instructions and README, not just the package name. A curator maintains a persistent catalog; an expert researches or advises without necessarily owning catalog stewardship.
2. Choose the role by primary ownership and outputs. Record multiple capabilities and domains for other discovery routes.
3. Keep stable package IDs independent of role; if reclassified, relocate its folder, retain its archive's internal `<package-id>/` root, and update canonical paths and links.
4. Do not label incomplete packages available. When information is insufficient, mark status explicitly instead of inventing a ZIP or version.

## Migration map

| Former path | New path |
|---|---|
| `instruction-sets/meta-llm-orchestrator/` | `instruction-sets/progenitors/meta-llm-orchestrator/` |
| `instruction-sets/ai-knowledge-atlas/` | `instruction-sets/curators/ai-knowledge-atlas/` |
| `instruction-sets/ui-ux-design-system-architect/` | `instruction-sets/curators/ui-ux-design-system-architect/` |
| `instruction-sets/technical-research-project-instructions/` | `instruction-sets/experts/technical-research-project-instructions/` |
| `instruction-sets/coding-partner-mentor-teacher/` | `instruction-sets/experts/coding-partner-mentor-teacher/` |
| `instruction-sets/psychology-advice-research/` | `instruction-sets/experts/psychology-advice-research/` |
| `instruction-sets/solid-visual-architecture/` | `instruction-sets/experts/solid-visual-architecture/` |
| `instruction-sets/app-planning/` | `instruction-sets/strategists/app-planning/` |
| `instruction-sets/business-app-idea/` | `instruction-sets/strategists/business-app-idea/` |
| `instruction-sets/executive-product-repo-review/` | `instruction-sets/strategists/executive-product-repo-review/` |
| `instruction-sets/feature-extension-planning-council/` | `instruction-sets/orchestrators/feature-extension-planning-council/` |
| `instruction-sets/general-purpose-chatgpt-conversations/` | `instruction-sets/generalists/general-purpose-chatgpt-conversations/` |

The previous GitHub paths might not redirect. Use the stable `id` and `registry.json` for programmatic lookup. No duplicate old-path ZIPs are retained.
