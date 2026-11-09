value or impact.

### Scope
#### In Scope
- Items included in this effort.

#### Out of Scope
- Items intentionally excluded.

### Constraints
- Business constraints.
- Operational constraints.

### Risks
- Business risks.
- Adoption risks.
- Rollout concerns.

## 4. Architectural Plan
### System Impact
- Affected systems, modules, services, or components.
- Integration points.
- Data flow or control flow implications.

### Key Architectural Decisions
For each decision include:
- Decision.
- Rationale.
- Tradeoff.

### Technical Constraints
- Platform, tooling, team, repo, infrastructure, or integration constraints.

## 5. Development Flow Plan
### Phases
For each phase include:
- Phase name.
- Goal.
- Major activities.
- Dependencies.
- Exit criteria.

### Validation Strategy
- Tests, review gates, artifact checks, or approval gates.

## 6. Supporting Schemas
Include only when useful:
- Domain schema.
- API schema.
- Task schema.
- Data model schema.
- Workflow schema.
- Artifact schema.
- Event/message schema.
- Permission or role schema.

## 7. Revision Review
### Inconsistencies Found
### Feasibility Concerns
### Missing Implementations
### Open Unknowns

## 8. Refined Draft
- Revised business, architectural, development, platform, and modular direction in approval-candidate form.

## 9. Tech Stack Alignment Review
### Target Platforms
### Stack Categories
### Recommended Primary Stack
### Alternative Stack Options
### Consistency Assessment
### Stack Decision

## 10. Modular Design Review
### Recommended Structure
### Example Structure
### Dependency Direction Rules
### Ownership Rules
### Modularity Decision

## 11. Research Handoff
### Research Goals
### Required Research Topics
### Research Questions
### Expected Research Artifacts
### Research Boundaries

## 12. Handoff Guidance for Antigravity IDE

## 13. Handoff Guidance for Claude

## 14. Final Validation Checklist


---

# Default Platform Strategy

Use this stack direction unless the project context clearly justifies a different choice.

## Primary default

- Browser: React + TypeScript.
- Mobile: React Native + TypeScript.
- Desktop: Tauri + Rust + React + TypeScript.
- API/backend: Python + FastAPI by default.
- Background workers/jobs: Python by default.
- Database: PostgreSQL by default.
- SQLite: Use only when scale, concurrency model, offline needs, and operational profile justify it.
- Cache/queue support: Redis by default when needed.
- Blob/file storage: S3-compatible storage when needed.
- TypeScript validation/contracts: Zod.
- Python validation/contracts: Pydantic.

## Stack principles

- Prefer TypeScript-first client development unless there is a clear reason not to.
- Minimize unnecessary stack fragmentation across delivery surfaces.
- Use Rust only when native desktop integration, performance, security, concurrency, or systems-level behavior materially justifies it.
- Compare at least one primary and one alternative stack when running stack review.
- Optimize for consistency, maintainability, delivery speed, platform fit, testability, and operational clarity.
- Do not treat defaults as immutable; explicitly revise when project constraints disprove them.

## Stack review categories

Evaluate and explicitly decide:

- Frontend/UI framework.
- Mobile framework.
- Desktop runtime.
- Backend runtime/framework.
- Database/persistence.
- Cache/queue.
- Blob/file storage.
- Schema/contract model.
- Auth/security.
- Testing.
- Deployment/infrastructure.
- Observability.
- Repository/module organization.


---

# Modular Design Rules

## Recommended structure

Use or adapt this structure for TypeScript-first app projects:

```text
src/
  app/
    pages/
    routes/
    layouts/
    providers/
  features/
    <feature-name>/
      components/
      hooks/
      services/
      models/
  models/
    domain/
    api/
    view/
  shared/
    constants/
    enums/
    types/
    utils/
    config/
```

For backend services, mirror the same ownership logic:

```text
backend/
  app/
    main.py
    routing/
    dependencies/
  features/
    <feature-name>/
      routes.py
      service.py
      repository.py
      models.py
  models/
    domain/
    api/
    persistence/
  shared/
    config/
    constants/
    errors/
    utils/
```

## Dependency direction rules

- `app/` may import from `features/`, `models/`, and `shared/`.
- `features/` may import from `models/` and `shared/`.
- `models/` may import from `shared/`.
- `shared/` must not import project-specific higher layers.
- Feature modules should not import across feature boundaries unless the dependency is deliberately promoted to `models/` or `shared/`.
- Shared code must remain genuinely cross-cutting; do not turn it into a junk drawer.

## Ownership rules

- `app/`: routes, pages, layouts, providers, application composition, bootstrapping, and top-level orchestration.
- `features/`: user-facing capability modules, feature-scoped components, feature services, feature hooks, and feature-local models.
- `models/`: domain types, API DTOs/contracts, view models, schema definitions, and cross-feature model vocabulary.
- `shared/`: constants, enums, environment/config utilities, low-level helpers, common types, and infrastructure-neutral references.

## Schema and constant placement

- Put API contracts and DTOs in `models/api/` when shared across features.
- Put domain concepts in `models/domain/`.
- Put feature-local schemas in `features/<feature>/models/` until they are reused.
- Put enums and constants in `shared/enums/` or `shared/constants/` only when cross-feature.
- Avoid string literal duplication by centralizing stable vocabulary in named constants or enums.

## Modularity review must identify

- Junk-drawer folders.
- Accidental cross-feature coupling.
- Schema ownership ambiguity.
- Repeated literals or duplicated DTOs.
- Backend/frontend contract drift.
- Areas where folder structure hides domain boundaries instead of clarifying them.


---

# Research Agent Handoff Guidance

The Research Agent receives the refined plan, stack direction, modular direction, open unknowns, and research questions.

## Research Agent responsibilities

- Research external dependencies, official documentation, security patterns, package options, API/platform constraints, storage approaches, performance considerations, integration feasibility, pricing/limits, and deployment constraints.
- Gather evidence that validates or challenges proposed scope and stack.
- Produce concrete findings, tradeoffs, and references.
- Highlight anything that should revise the plan before scaffolding or task generation.

## Required research outputs

- Referenced findings summary.
- Shortlist of candidate libraries, services, APIs, SDKs, or platform options.
- Official documentation links or authoritative source references.
- Feasibility notes.
- Risks and limitations.
- Recommended changes to the plan if needed.

## Research boundaries

- The Research Agent gathers evidence and recommendations.
- The Research Agent must not silently rewrite the approved architecture.
- Any proposed changes must be flagged explicitly with rationale and impact.


---

# Antigravity IDE Handoff Guidance

Antigravity IDE receives the validated plan and research artifacts.

## Antigravity responsibilities

- Reconcile the plan and research findings against the real project architecture and code context.
- Scaffold the project or propose a scaffold.
- Normalize the modular design for consistency.
- Generate implementation planning artifacts and structured execution tasks.
- Verify artifact accuracy and consistency.

## Must validate against actual code context

- Existing repository structure.
- Existing package manager and build tooling.
- Current module boundaries.
- Current data models and API contracts.
- Existing auth, storage, deployment, observability, and testing patterns.
- Any mismatch between the approved plan and real project constraints.

## Stable unless code context disproves it

- Approved stack direction.
- Approved modular boundaries.
- Schema ownership rules.
- Enum and constant placement rules.
- Dependency direction rules.
- Research-backed dependency choices.

## Required artifact generation

- Architecture reconciliation notes.
- Scaffold plan or scaffold diff summary.
- Implementation artifact set.
- Execution task list.
- Validation checklist.
- Any required plan revisions caused by real code context.


---

# Claude Handoff Guidance

Claude receives the validated architecture, implementation artifacts, task artifacts, and research findings after Antigravity IDE has reconciled them with the actual project context.

## Claude responsibilities

- Break implementation work into smaller actionable tasks.
- Partition work into subagent/worktree-friendly execution packets.
- Preserve approved stack and modular boundaries unless explicitly told to revise them.
- Use research artifacts to avoid redundant discovery work.
- Ground integration 