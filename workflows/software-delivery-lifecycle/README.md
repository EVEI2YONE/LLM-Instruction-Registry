# How to use instruction sets for the Software Delivery Lifecycle (v1)

This is a **workflow README**, not a package README. Future workflows receive their own sibling directory and guide. This workflow can reuse both newly generated and existing specialist packages.

## Launch
1. Provide product repository URL, change objective, constraints and current branch if known.
2. Invoke software-delivery-lifecycle for multi-stage work, or an individual specialist for isolated phase work.
3. Discover registry candidates using `registry.json` and `docs/AGENTIC_SEARCH.md`; load only selected entrypoints and pin their versions.
4. Inspect existing product docs, CODEOWNERS, ADRs, contracts, implementation and tests BEFORE drafting new durable artifacts. Confirm artifact authority and revision.
5. Delegate using stage, scope, owned paths, canonical input IDs and commit revisions, deliverable/evidence gates, permissions and next consumers.
6. Each specialist reconciles stale inputs on resume, writes only owned authoritative artifacts through review, and emits a durable handoff on completion.
7. The coordinator checks approval and evidence at each gate, routes affected siblings, and requests authorization for production or irreversible operations.
8. Carry incidents and measured outcomes into product backlog/owners rather than duplicating project history.

## Routes
- Greenfield: business-app-idea / product-delivery-specialist -> app-planning -> research -> architecture + UI/UX -> engineering -> QA -> release -> operations.
- Feature extension: feature-extension-planning-council -> targeted product/architecture/UX -> implementation -> QA -> release.
- Refactor: repo intake -> architecture + baseline tests -> engineering -> QA -> release.
- Incident: operations -> targeted engineering/architecture -> regression QA -> controlled release.

## Precedence and anti-drift
Project documents remain in product repo; reusable instructions remain here. Approved product requirements govern intent, approved ADRs/contracts govern design, code at pinned SHA governs implemented behavior, CI evidence governs tests, and actual deployment record governs release. New drafts do not override approved authority. No redundant new PRDs/ADRs when existing canonical owner can accept an update. Cross-thread handoffs use links + revisions, never assumed memory.

## Future workflows
Create `workflows/<workflow-id>/README.md` and `profile.json`, with stage/authority/handoff tests. Keep specialists domain-focused and add profile-specific adapters rather than hardcoding SDLC into all domains.

## Behavioral tests
- Existing PRD -> patch proposal, not new competing PRD.
- Changed upstream revision -> stale handoff is reconciled.
- Concurrent sibling edits -> owner review and source SHA check.
- No CI or deployment access -> mark unverified, no false claim.
- Workflow-independent specialist -> no forced SDLC stage.

## Specialized engineering
Select [frontend](../../instruction-sets/experts/frontend-engineering-specialist/README.md), [backend](../../instruction-sets/experts/backend-engineering-specialist/README.md), and optional [AI/ML](../../instruction-sets/experts/ai-ml-engineering-specialist/README.md) by approved scope. Require interface version alignment. For organizational idea-to-MVP investment gates start with [Organization-to-MVP](../organization-idea-to-mvp/README.md).
