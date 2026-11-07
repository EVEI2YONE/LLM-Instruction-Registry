# Psychology Advice & Research

**Version:** `v1` · **Role:** Specialized educational and research assistant · **Canonical archive:** [psychology-advice-research_v1.zip](psychology-advice-research_v1.zip)

## Overview

A source-aware psychology instruction set intended to explain concepts, synthesize research, and offer practical non-clinical reflection or coping guidance while making uncertainty and safety boundaries explicit.

## When to use it

Use it to learn about psychological concepts, compare research findings, or discuss general approaches to everyday behavior and well-being—not for diagnosis or treatment decisions.

## Main capabilities

- Research synthesis with attention to source quality, uncertainty, and citation practices.
- General psychological education and practical reflection-oriented advice.
- Separate helper and sub-role guidance for research, advice, and response structure.
- Response templates, phased handoffs, correction/source inventories, and package validation.

## Typical inputs and outputs

**Provide:** A psychology question, situation, research topic, context that can be shared safely, and any requested depth.

**Expect:** A concept explanation or evidence-aware synthesis with practical non-clinical options and appropriate uncertainty.

## Getting started

1. Download and extract [psychology-advice-research_v1.zip](psychology-advice-research_v1.zip). Its internal root folder is `psychology-advice-research/`.
2. Start with [the compiled instruction set](sources/00_compiled_instruction_set.md) and review [source loading guidance](sources/00_README.md).
3. Keep supporting files together when loading them into a ChatGPT Project or other compatible agent environment. Read the source hierarchy and manifest before omitting files.

## Sources and structure

The folder contains `01_core/`, `02_helpers/`, `03_sub_roles/`, `04_templates/`, `05_handoffs/`, `06_sources_to_update/`, `07_tables/`, and `99_manifest.json`.

Browse [sources/](sources/README.md) for separately published reference material and provenance.

## Boundaries and notes

This is not a clinical diagnosis, therapy, or emergency-support system. Avoid presenting unsettled findings as certainty and consult qualified professionals for individual clinical decisions.

## Provenance

Based on the original psychology research v1 source package, with its [original README](sources/ORIGINAL_PACKAGE_README.md) retained.

This instruction system is independent in the [registry](../../../registry.json). [Meta-LLM Orchestrator v18](../../progenitors/meta-llm-orchestrator/README.md) is retained as the foundational progenitor; that designation does not imply all specialized packages have identical internal behavior.
