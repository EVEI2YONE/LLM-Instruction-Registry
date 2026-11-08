# Catalog-Grounded Consultation — reusable workflow

This is a reusable **consultation workflow profile**, not a duplicate catalog and not tied to SDLC only. It may be invoked as a checkpoint in organization-to-MVP, engineering SDLC, refactor, research, UX audit or a standalone repository/media review.

## What to provide
A target repo and ref, selected files/code or uploaded media, desired assessment outcome, intended knowledge catalog repo/ref, current workflow stage if any, permission boundaries and existing docs/owner conventions. If catalog repo not specified, choose by capability and discover its canonical repository from selected curator instructions; never infer a URL without verifying it. Check access before claiming coverage.

## Invoke
1. Route to [Catalog-Grounded Consultant](../../instruction-sets/orchestrators/catalog-grounded-consultant/README.md). Select adapter for relevant catalog; consult that curator's currently available instruction set and catalog README.
2. **Assess target and existing catalog** at pinned SHAs. Cite exact inspected paths/media and catalog entries; produce immediate initial assessment and atomic gap ledger.
3. **Triage gaps** into sufficient/clarify/extend/create/research/implementation/conflict. Reject duplicated, target-only, speculative or sensitive findings from shared catalog PR.
4. **Batch research and curation** by dependencies and review size. If authorized open/reuse one active consultation-specific catalog PR and commit each batch; keep research and tests cited, and don't merge automatically.
5. **Re-gather context** after catalog batch/PR update: re-read approved catalog baseline and proposed PR HEAD, target latest revision and changed contracts. Mark approved versus provisional knowledge and resolved/remaining gaps.
6. **Reassess and advise** with revised risks, source-backed recommendations, prioritized refactor playbook, acceptance/tests, rollout/rollback and explicit next owner. Never modify target app merely because catalog was updated.
7. Persist session record by existing project issue/PR/index conventions and references. Do not invent standalone durable document if an authoritative task record exists.

## Initial adapters
- [AI Knowledge Atlas](adapters/ai-knowledge-atlas.md): AI/ML, agent tools, RAG, evaluation, architecture and model constraints.
- [UI/UX Design System Architect](adapters/ui-ux-design-system.md): screenshots/visual media, design system, accessibility, information architecture, frontend migration.

## Collaboration boundaries
The consultant coordinates; curators own catalog knowledge and canonical indexes; Product and Architecture own approved project intent/design; Frontend/Backend/AI Engineering implement target code; QA verifies; Release operates production. Separate catalog PR from target PR, pin both revisions and allow progress with provisional guidance only when risks are explicitly labeled.

## Workflow-independent reuse
Future catalogs add an adapter and profile mapping, not a fork of the full consultant instructions. Consult the registry's role taxonomy and workflow architecture to keep names canonical and discoverable.
