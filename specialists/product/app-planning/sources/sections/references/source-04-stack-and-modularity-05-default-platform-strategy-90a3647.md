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