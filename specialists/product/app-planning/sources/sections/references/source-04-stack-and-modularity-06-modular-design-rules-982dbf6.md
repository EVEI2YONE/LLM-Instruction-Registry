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