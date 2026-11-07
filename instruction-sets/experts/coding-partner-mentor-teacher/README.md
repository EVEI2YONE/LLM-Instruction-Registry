# Coding Partner / Mentor / Teacher

**Version:** `v1` · **Role:** Specialized engineering assistant · **Canonical archive:** [coding-partner-mentor-teacher_v1.zip](coding-partner-mentor-teacher_v1.zip)

## Overview

A practical software-engineering assistant focused on direct recommendations, debugging, small examples, design judgment, and mentorship. It favors maintainability and clarity over unnecessary abstraction.

## When to use it

Use it during everyday coding, troubleshooting, code review, concept learning, or evaluating an implementation tradeoff when you want a concise senior-engineer perspective.

## Main capabilities

- Answer-first recommendations with brief reasoning and small relevant examples.
- Debugging flow centered on likely cause, minimal fix, why it failed, and verification.
- Design reviews that identify coupling, fragility, unnecessary complexity, and pragmatic upgrade paths.
- Teaching mode that builds from a simple mental model to production considerations.
- Reusable response helpers, examples, guardrails, self-heal notes, and validation material.

## Typical inputs and outputs

**Provide:** Code or logs, a technical question, relevant language/framework, desired behavior, and any constraints.

**Expect:** A recommended approach, explanation, compact example or fix, caution about likely pitfalls, and a next verification step.

## Getting started

1. Download and extract [coding-partner-mentor-teacher_v1.zip](coding-partner-mentor-teacher_v1.zip). Its internal root folder is `coding-partner-mentor-teacher/`.
2. Load [the compiled instruction prompt](sources/00_compiled_instruction_prompt.md) first, then consult the helper and example files.
3. Keep supporting files together when loading them into a ChatGPT Project or other compatible agent environment. Read the source hierarchy and manifest before omitting files.

## Sources and structure

Files include `01_core_role_instruction_set.md`, `02_response_helpers.md`, `03_quick_reference_examples.md`, `04_boundaries_and_preferences.md`, `05_self_heal_instruction_set.md`, `06_manifest.json`, and `07_validation_table.md`.

Browse [sources/](sources/README.md) for separately published reference material and provenance.

## Boundaries and notes

It is designed to guide engineering work; it does not replace running tests or checking implementation-specific documentation. The source prompt records a package version of 1.0.0; the registry archive uses the release label `v1`.

## Provenance

Repackaged from the original coding partner v1 archive and accompanying source files. See [the original package README](sources/ORIGINAL_PACKAGE_README.md).

This instruction system is independent in the [registry](../../../registry.json). [Meta-LLM Orchestrator v18](../../progenitors/meta-llm-orchestrator/README.md) is retained as the foundational progenitor; that designation does not imply all specialized packages have identical internal behavior.
