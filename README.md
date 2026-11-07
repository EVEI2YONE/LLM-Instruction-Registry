# LLM Instruction Registry

A versioned catalog of standalone LLM instruction sets. **Meta-LLM Orchestrator v18** is the foundational progenitor. Each package has its own top-level folder, ZIP, sources, and explanatory README.

## Lookup catalog

| Instruction set | Version | Purpose | Archive |
|---|---|---|---|
| [Meta-LLM Orchestrator](meta-llm-orchestrator/README.md) | v18 | Foundational progenitor for composing and coordinating specialized LLM instruction sets. | [meta-llm-orchestrator_v18.zip](meta-llm-orchestrator/meta-llm-orchestrator_v18.zip) |
| [App Planning](app-planning/README.md) | v1 | Business, product, architecture, stack, research, and engineering handoff planning. | [app-planning_v1.zip](app-planning/app-planning_v1.zip) |
| [Business App Idea](business-app-idea/README.md) | v1 | Instruction set for shaping business application concepts into actionable plans. | [business-app-idea_v1.zip](business-app-idea/business-app-idea_v1.zip) |
| [Coding Partner / Mentor / Teacher](coding-partner-mentor-teacher/README.md) | v1 | Engineering assistance, debugging, code review, and practical mentorship. | [coding-partner-mentor-teacher_v1.zip](coding-partner-mentor-teacher/coding-partner-mentor-teacher_v1.zip) |
| [Feature Extension Planning Council](feature-extension-planning-council/README.md) | v1 | Council-based feature planning, scope, architecture, risk, and implementation handoffs. | [feature-extension-planning-council_v1.zip](feature-extension-planning-council/feature-extension-planning-council_v1.zip) |
| [Psychology Advice & Research](psychology-advice-research/README.md) | v1 | Psychology education, non-clinical advice, and evidence-aware research synthesis. | [psychology-advice-research_v1.zip](psychology-advice-research/psychology-advice-research_v1.zip) |
| [SOLID Visual Architecture](solid-visual-architecture/README.md) | v1 | Architecture visualization and SOLID-oriented design instruction system. | [solid-visual-architecture_v1.zip](solid-visual-architecture/solid-visual-architecture_v1.zip) |
| [Technical Research Project Instructions](technical-research-project-instructions/README.md) | v2 | Evidence-backed technical research, architecture consulting, and teaching. | [technical-research-project-instructions_v2.zip](technical-research-project-instructions/technical-research-project-instructions_v2.zip) |

For programmatic lookup, use [registry.json](registry.json). Every listed archive is checked in and has a matching internal top-level directory.

## Folder convention

\`\`\`text
<instruction-set>/
  README.md
  <instruction-set>_vN.zip
  sources/
    README.md
\`\`\`

Read the package README before loading an archive; individual instruction systems may have different entrypoints or prerequisites.

## Canonical and pending packages

- **Meta-LLM Orchestrator v18** remains the progenitor independently of later derivatives.
- **AI Knowledge Atlas**: owner-designated archive \`AI-Knowledge-Atlas-40-Project-Sources.zip\` is **not uploaded**; no reconstructed or placeholder archive is published.
- Archive versions remain explicit in their filenames and metadata. See [CONTRIBUTING.md](CONTRIBUTING.md) to add an instruction set.
