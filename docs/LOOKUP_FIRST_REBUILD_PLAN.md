# Repository-wide lookup-first rebuild plan

Status: **foundation preparation**. Baseline: main at `6cc9c6891e274caf5ae48bdd1d8147110a488b37`, 49 published packages. Scope is **every published package**, not a sample or pilot. This foundation PR MUST NOT modify published instruction package sources, manifests, archives, or version numbers.

## Goal

Turn the registry into a versioned, lookup-first source of instructions usable from personal computers, local coding agents, cloud agent runners, and hosted chat agents. A target runtime may directly read selected source sections, invoke native subagents, call a user-controlled external orchestration gateway, or degrade truthfully to one agent. Repository contents alone cannot create a hosted provider capability.

## Architectural invariants

1. Search registry metadata before opening packages; never load all packages to route one request.
2. One canonical modular source tree per package; compiled files and upload-constrained bundles are generated outputs.
3. Only always-needed package rules are loaded initially. Task-triggered sections, schemas, examples, and knowledge are fetched selectively, with dependency closure.
4. Shared rules are centrally owned and pinned, but each runtime MUST verify injection of applicable rules. Do not assume session/subagent inheritance.
5. Project documents and external knowledge catalogs remain authoritative in their respective repositories; knowledge references pin reviewed revisions.
6. Each delegated subtask gets isolated working context plus explicit shared-context and artifact references, never an unrestricted copy of every conversation or secret.
7. Every artifact has an owner, durable ID, content hash, visibility scope, revision and provenance. Concurrent writers use optimistic concurrency or explicit locks; reviewers cannot silently overwrite owner outputs.
8. Agent instantiation must be supported by a verified adapter. No native subagent API means explicitly configured gateway or single-agent fallback.
9. Human approvals are enforced at runtime. Conflicting approval policies block consequential actions pending a reviewed reconciliation.
10. Preserve every existing archive/version. A migrated package is a new version with identical or consciously revised behavior and proven source-to-archive equality.

## Execution phases

### F0 — Foundations (THIS PR; no instruction sets changed)
- Add canonical schemas: package sections, runtime capabilities, delegation task, context envelope and artifact record.
- Add shared-rules *baseline* referencing existing authority files, not replacing them.
- Add deterministic package-section lookup, dependency ordering, integrity/path checks, and full-registry migration inventory.
- Add runtime-neutral adapter and shared-context/artifact contracts plus runnable in-process reference coordination tests.
- Add CI checks for these new files; all legacy packages remain valid and unchanged.
- Document outstanding policy conflicts and target-specific capability checks.

### F1 — Generator and distribution contracts
- Publish a new Meta-LLM Orchestrator version with canonical source classification and manifest-rendered entrypoints.
- Add deterministic build outputs for local sources, skill archives, ChatGPT Project bundles, and prompt-only hosted targets; never hand-maintain generated bundles.
- Add common-rules version pinning, source hashing, manifest-to-index round-trip checks, provider adapters, and section sizing diagnostics.

### F2 — Whole-catalog conversion
- Regenerate and verify **all 49 baseline packages**. No pilot subset. Implementation may be batched for reviewability and parallelized across package groups, but completion is one repo-wide migration target.
- Preserve all older published ZIPs; publish each new archive and sources with its corresponding manifest.
- Update registry references, docs, adapters, capability ownership, dependencies, and tests for the complete catalog.
- Resolve stale cross-package references, duplicated rules, inlined scripts/schemas, and source-era README/version drift.
- Maintain a machine-readable ledger with per-package state, evidence, old/new versions and decisions.

### F3 — Runtime integration
- Local: checkout or read-only clone, verified runtime capabilities, configurable provider process/SDK adapter, scoped workspaces and local durable context/artifact store.
- Hosted: use native subagent features only where actually exposed; otherwise provide an authorized external HTTPS orchestration gateway with authenticated, audited run/task/artifact APIs. In chat-only environments provide a clear single-agent fallback.
- Support dynamic specialist selection, fan-out/fan-in, cancellation, dependency-aware scheduling, bounded recursion, tool permissions, retries/idempotency and explicit human gates.
- Add conformance tests for each runtime adapter. Never claim an adapter can spawn agents until it has successfully executed a test.

### F4 — Repo-wide verification and cutover
- Run static checks on all 49 packages plus behavior evaluations over representative user intents from **every package**.
- Compare baseline and migrated context tokens, retrieval calls, latency, missing instructions, acceptance success, citation/source provenance, and artifact conflict behavior.
- Require zero unresolved links, zero missing mandatory sections, zero unsafe permission escalation, and recorded human acceptance of approval-policy changes.
- Switch registry default versions in a reviewed PR after the full catalog passes; keep rollback to prior versions.

## Acceptance gates

- Inventory enumerates **all** current registered packages and detects additions/removals.
- Zero package source or historical archive changes in F0.
- Entrypoints and section manifests match deterministically; sections and dependency graph resolve without path traversal or cycles.
- Common-rules references are versioned and delivered per runtime, with explicit unsupported/unknown states.
- Local and hosted adapters implement a common protocol; capability matrices are measured rather than inferred from provider branding.
- Context snapshots and artifact references carry version, provenance, access scope and conflict semantics.
- Delegation can run concurrently only with declared capabilities and bounded permissions.
- A missing tool, source, authority, or approval gives blocked/fallback status, never fabricated completion.
- Dynamic runtime validation is reported as NOT_RUN until an actual configured provider or gateway executes it.

## Source of truth and review

This document is the F0 plan. The migration ledger is `migration/inventory.json`, generated by `scripts/migration_inventory.py`. Runtime contracts are in `runtime/`; schemas in `schemas/`. The authoritative package registry remains `registry.json`. Original instruction content stays in existing package trees until F2. No automatic merges or deployments.
