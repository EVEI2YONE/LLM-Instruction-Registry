# General Helper Instruction Sets

## Helper: Extension Intake Classifier

Purpose: Determine what kind of extension is being planned and what details are needed.

Classify by:

- Extension surface: browser extension, IDE extension, app plugin, SaaS integration, API add-on, workflow automation, UI module, backend service extension, SDK/library extension, or platform-specific module.
- User value: productivity, automation, reporting, AI assistance, collaboration, compliance, developer tooling, data sync, or UX enhancement.
- Integration model: local-only, client-server, external API, webhook/event-driven, embedded UI, background worker, scheduled job, or hybrid.
- Risk class: low, medium, high, regulated, security-sensitive, privacy-sensitive, or monetization-critical.
- Delivery maturity: concept, prototype, MVP, production, migration, refactor, or scale-up.

If details are missing, proceed with reasonable assumptions and clearly mark them.

## Helper: Research Protocol

When researching, prefer:

1. Official platform documentation.
2. Official SDK/API references.
3. Standards documents and security guidance.
4. Maintained source repositories and release notes.
5. Reputable implementation guides only after primary sources.

Research output must include:

- What is confirmed.
- What is inferred.
- What changed recently or may change.
- Constraints that affect architecture.
- Risks requiring validation spikes.

## Helper: SOLID Architecture Mapper

Use SOLID principles as follows:

- Single Responsibility Principle: each module, service, adapter, handler, schema, and workflow has one reason to change.
- Open/Closed Principle: extension points use interfaces, strategies, configuration, or plugin registries rather than direct modification.
- Liskov Substitution Principle: implementations of shared contracts must be interchangeable without breaking callers.
- Interface Segregation Principle: split broad interfaces into role-specific ports such as `CommandHandler`, `QueryProvider`, `PolicyEvaluator`, `StoragePort`, and `NotificationPort`.
- Dependency Inversion Principle: domain/application logic depends on abstractions; platform SDKs, HTTP clients, databases, AI providers, and UI frameworks live behind adapters.

For each major design choice, explain which principle it supports and what coupling it avoids.

## Helper: Pseudocode and Schema Standards

Use pseudocode when it clarifies:

- Control flow.
- State transitions.
- API orchestration.
- Error handling.
- Permission checks.
- Extension lifecycle hooks.
- Event processing.

Use schemas when it clarifies:

- Inputs and outputs.
- Configuration files.
- Storage records.
- API requests/responses.
- Events.
- Commands and queries.
- Decision records.

Prefer JSON Schema-like structures for data contracts and TypeScript-like interfaces for module boundaries unless a platform stack is specified.

## Helper: Plan Synthesis Protocol

Every development plan must include:

- Scope boundary.
- Architecture boundary.
- Dependency boundary.
- Phased implementation path.
- Parallelizable workstreams.
- Acceptance criteria.
- Testing strategy.
- Rollout and rollback plan.
- Observability requirements.
- Risk register.
- Open questions.
- Owner-ready task groupings.

## Helper: Handoff Readiness Validator

Before finalizing, verify the plan is usable by a TPM and engineering team:

- Can a TPM convert phases into epics and milestones?
- Can engineering identify modules, contracts, dependencies, and sequencing?
- Are risks actionable rather than vague?
- Are open questions separated from implementation tasks?
- Are test scenarios and acceptance criteria measurable?
- Are non-functional requirements explicit?
- Are integration points and external constraints named?