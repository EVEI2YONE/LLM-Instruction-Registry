# Technical Research Project Instructions

**Version:** `v2` · **Role:** Specialized research and consulting · **Canonical archive:** [technical-research-project-instructions_v2.zip](technical-research-project-instructions_v2.zip)

## Overview

A structured technical research, architecture consulting, and teaching assistant. It combines evidence evaluation, clear uncertainty handling, decision support, and explainable technical guidance.

## When to use it

Use it for technology research, architecture choices, tradeoff comparisons, technical education, or design critiques where source quality and decision rationale matter.

## Main capabilities

- Source and citation checking, truthfulness and uncertainty rules.
- Request classification for research, consulting, teaching, and review.
- Dedicated synthesizer, architect, teacher, design-review, and self-heal sub-roles.
- Comparison and design-review templates, citation quality checks, tracked corrections, and behavior/delivery validation.

## Typical inputs and outputs

**Provide:** A technical research question or design decision, requirements, constraints, available evidence, and desired format.

**Expect:** An evidence-backed research summary, tradeoff recommendation, design review, or explanation with uncertainty and citations appropriate to the question.

## Getting started

1. Download and extract [technical-research-project-instructions_v2.zip](technical-research-project-instructions_v2.zip). Its internal root folder is `technical-research-project-instructions/`.
2. Begin with [the compiled instruction set](sources/00_compiled_instruction_set.md), then use [the source map](sources/00_README.md) for modular loading.
3. Keep supporting files together when loading them into a ChatGPT Project or other compatible agent environment. Read the source hierarchy and manifest before omitting files.

## Sources and structure

The source tree includes `01_core/`, `02_helpers/`, `03_sub_roles/`, `04_templates/`, `05_sources_to_update/`, `06_validation/`, `07_examples/`, a manifest, and checksums.

Browse [sources/](sources/README.md) for separately published reference material and provenance.

## Boundaries and notes

Research quality depends on access to reliable and current sources. Do not treat unverified claims as established findings, or omit uncertainty when evidence conflicts.

## Provenance

Migrated from the technical research v2 package; the [original README](sources/ORIGINAL_PACKAGE_README.md) and source files remain available.

This instruction system is independent in the [registry](../../registry.json). [Meta-LLM Orchestrator v18](../meta-llm-orchestrator/README.md) is retained as the foundational progenitor; that designation does not imply all specialized packages have identical internal behavior.
