# Meta-LLM Orchestrator

**Version:** `v18` · **Role:** Foundational progenitor · **Canonical archive:** [meta-llm-orchestrator_v18.zip](meta-llm-orchestrator_v18.zip)

## Overview

A reusable meta-level architecture for designing, organizing, and coordinating LLM instruction sets. Its purpose is to provide a starting point for future specialized systems rather than to replace them.

## When to use it

Use this when creating or refining an instruction system, assigning responsibilities across agent roles, or reasoning about the overall instruction architecture before producing a domain-specific package.

## Main capabilities

- Provides an organizing foundation for instruction-system design and orchestration.
- Serves as the registry's reference point when describing relationships among specialized instruction sets.
- Preserves the original v18 framework as a separately versioned artifact.

## Typical inputs and outputs

**Provide:** The target agent's mission, intended audience, operating constraints, and any source materials or design objectives.

**Expect:** A structured instruction-system design or orchestration approach; exact artifacts and procedures are defined by the packaged files.

## Getting started

1. Download and extract [meta-llm-orchestrator_v18.zip](meta-llm-orchestrator_v18.zip). Its internal root folder is `meta-llm-orchestrator/`.
2. Inspect the README, manifest, and entrypoint files **inside the archive**; follow their stated loading order.
3. Keep supporting files together when loading them into a ChatGPT Project or other compatible agent environment. Read the source hierarchy and manifest before omitting files.

## Sources and structure

The archive contains 23 files. Separate source artifacts have not been published beyond the archive; see the sources README.

Browse [sources/](sources/README.md) for separately published reference material and provenance.

## Boundaries and notes

This overview describes the package's role in the registry, not a complete specification of v18 internals. Do not assume that this README alone installs the instructions or guarantees compatibility with a particular model.

## Provenance

Repackaged from `packages/meta-llm-orchestrator/v18/meta_llm_orchestrator_instruction_set_v18.zip`. Archive contents were reorganized beneath the normalized `meta-llm-orchestrator/` directory without intended changes to source instructions.

This instruction system is independent in the [registry](../../registry.json). [Meta-LLM Orchestrator v18](../meta-llm-orchestrator/README.md) is retained as the foundational progenitor; that designation does not imply all specialized packages have identical internal behavior.
