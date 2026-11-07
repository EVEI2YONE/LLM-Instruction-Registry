# UI/UX Design System Architect — v1.1 (publication staging)

**Status:** Publication incomplete — do not treat this as a released instruction set.

This package defines a **catalog-first, evidence-led UI/UX modernization agent**. It inspects a target application and a separate design knowledge/component catalog; audits missing reference knowledge; proposes a catalog documentation PR first; then maps application-specific gaps into a prioritized migration and remediation plan.

## Core capabilities

- Analyze core product workflows, information architecture, navigation, UI composition, and design debt.
- Classify reference-catalog knowledge as present, missing, weak, outdated, duplicated, or undiscoverable.
- Update the *design knowledge catalog* in a separate reviewable PR before relying on new guidance in application plans.
- Govern reusable primitives, components, patterns, features, pages, dialogs, tokens, themes, spacing, responsive layouts, accessibility, and internationalization.
- Discourage hard-coded visual values, inline styles, monolithic stylesheets, and unnecessary generic components.
- Measure task completion, task time, errors, abandonment, conversion, SUS, CES, and NPS with appropriate study designs.
- Prioritize migration as P0 critical cross-cutting issues; P1 core workflows; P2 IA/navigation; P3 design-system foundations; P4 onboarding/change management; P5 quick wins; P6 secondary features; P7 aesthetics.
- Preserve the distinction between business priority and implementation dependency order.

## Audience and boundaries

For product designers, UX researchers, frontend engineers, technical leads, and AI agents auditing or modernizing GitHub applications. This is an **instruction set**, not the UI/UX knowledge catalog itself or a ready-to-run component library. Catalog PRs and target-app implementation PRs are independent operations. Never claim an unmerged PR is released guidance.

## Package provenance

Source: user-approved UI/UX Design System Architect v1.1 package generated in the conversation on 2026-11-07. Local archive validated as 40 source files with root `ui-ux-design-system-architect/`. The ZIP and full sources were **not transferred to this repository** because the current GitHub connector exposes text/blob operations but not direct transfer from the conversation's container artifact. Do not mark the package available or add a registry entry until the verified archive and matching source files exist on the branch.

## Publication requirements

To finish this staging PR, upload a freshly normalized `ui-ux-design-system-architect_v1.zip` containing `ui-ux-design-system-architect/` at its root, keep the matching 40 source files under `sources/`, create `sources/README.md`, update the root README lookup table and `registry.json` with version `v1.1`, then validate ZIP CRC, source hashes, paths and internal root. Use `v1.1` in metadata; if filename conventions permit, prefer `ui-ux-design-system-architect_v1.1.zip` to avoid version ambiguity.

This staging README intentionally has no archive link because no published archive exists yet.
