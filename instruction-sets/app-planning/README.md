# App Planning

**Version:** `v1` · **Role:** Specialized planning · **Canonical archive:** [app-planning_v1.zip](app-planning_v1.zip)

## Overview

An end-to-end planning assistant for turning a rough app idea into a structured, modular, research-ready implementation plan. It connects product shaping with technical architecture and downstream developer/agent handoffs.

## When to use it

Use it at the start of a new application or a substantial redesign, when decisions about product scope, platform, dependencies, modularity, research questions, and implementation sequencing are still open.

## Main capabilities

- Guided ideation, idea refinement, critique, and staged planning modes.
- Business and architecture planning with stack alignment and modular boundaries.
- Research questions, follow-on validation, and handoffs to Research Agent, Antigravity IDE, and Claude workflows.
- Templates, source inventories, revision notes, and self-heal checks.

## Typical inputs and outputs

**Provide:** An app concept, target users, problem to solve, desired capabilities, constraints, and known platform preferences.

**Expect:** A refined concept, staged development plan, modular architecture guidance, research backlog, and agent-ready implementation handoffs.

## Getting started

1. Download and extract [app-planning_v1.zip](app-planning_v1.zip). Its internal root folder is `app-planning/`.
2. Start with [the compiled instruction set](sources/00_compiled_instruction_set.md); see [source loading order](sources/00_README.md).
3. Keep supporting files together when loading them into a ChatGPT Project or other compatible agent environment. Read the source hierarchy and manifest before omitting files.

## Sources and structure

The source tree exposes `01_core/`, `02_operating_modes/`, `03_planning_workflow/`, `04_stack_and_modularity/`, `05_handoffs/`, `06_templates/`, `07_validation/`, `08_sources/`, and `09_self_heal/`, plus a manifest and original reference text.

Browse [sources/](sources/README.md) for separately published reference material and provenance.

## Boundaries and notes

This package focuses on planning rather than immediately writing production code. Architecture and tool recommendations remain contingent on project requirements and current external evidence.

## Provenance

Derived from the original App Planning v1 source package and normalized ZIP. The original package README is retained at [sources/ORIGINAL_PACKAGE_README.md](sources/ORIGINAL_PACKAGE_README.md).

This instruction system is independent in the [registry](../../registry.json). [Meta-LLM Orchestrator v18](../meta-llm-orchestrator/README.md) is retained as the foundational progenitor; that designation does not imply all specialized packages have identical internal behavior.
