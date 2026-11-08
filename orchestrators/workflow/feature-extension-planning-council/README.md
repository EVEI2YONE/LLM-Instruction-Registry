# Feature Extension Planning Council

**Version:** `v1` · **Role:** Specialized feature planning · **Canonical archive:** [feature-extension-planning-council_v1.zip](feature-extension-planning-council_v1.zip)

## Overview

An agent-facing council framework for planning extensions to an existing application. It brings together scope, architecture, research, risk, and validation perspectives so a Technical Project Manager and development team can receive an actionable handoff.

## When to use it

Use it when proposing a new feature in an existing product, evaluating how it fits the current design, choosing an implementation sequence, or preparing an extension for team delivery.

## Main capabilities

- Specialist council sub-roles and reusable research, schema, and architecture helpers.
- Feature-scope and dependency evaluation, including SOLID design considerations.
- Planning templates for development phases, pseudocode, schemas, and handoffs.
- Decision/risk/question registries, correction logs, expected-artifact and validation tables.

## Typical inputs and outputs

**Provide:** The current app context, proposed change, existing architecture, stakeholders, constraints, and success criteria.

**Expect:** A structured feature-extension plan with architecture, acceptance criteria, sequencing, risks, supporting schemas/pseudocode, and a TPM/development-team handoff.

## Getting started

1. Download and extract [feature-extension-planning-council_v1.zip](feature-extension-planning-council_v1.zip). Its internal root folder is `feature-extension-planning-council/`.
2. Use [the compiled instruction set](sources/00_compiled_instruction_set.md) as the top-level contract; follow [source priorities](sources/00_README.md).
3. Keep supporting files together when loading them into a ChatGPT Project or other compatible agent environment. Read the source hierarchy and manifest before omitting files.

## Sources and structure

The modular tree includes `01_core/`, `02_general_helpers/`, `03_sub_roles/`, `04_templates/`, `05_handoffs/`, `06_sources_to_update/`, `07_tables/`, and `08_examples/`, plus a manifest.

Browse [sources/](sources/README.md) for separately published reference material and provenance.

## Boundaries and notes

Plans should distinguish verified existing behavior from assumptions. This package produces planning and handoff artifacts, not automatic production implementation.

## Provenance

Migrated from the original v1 sources. No original archive was supplied for that package; the canonical ZIP was assembled from its source tree. See [the original package README](sources/ORIGINAL_PACKAGE_README.md).

This instruction system is independent in the [registry](../../../registry.json). [Meta-LLM Orchestrator v18](../../progenitors/meta-llm-orchestrator/README.md) is retained as the foundational progenitor; that designation does not imply all specialized packages have identical internal behavior.
