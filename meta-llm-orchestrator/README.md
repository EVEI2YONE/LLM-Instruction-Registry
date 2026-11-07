# Meta-LLM Orchestrator

**Role:** Foundational progenitor instruction set  
**Canonical version:** v18  
**Archive:** [meta-llm-orchestrator.zip](meta-llm-orchestrator.zip)

## Purpose

The Meta-LLM Orchestrator is the foundational instruction architecture in this registry. Its role is to guide the creation, organization, and refinement of other LLM instruction systems, not to serve as an interchangeable replacement for every specialized package.

## What it does

- Provides a reference instruction framework for designing new instruction sets.
- Serves as the stable progenitor against which specialized instruction sets can describe their derivation and differences.
- Supports reuse of the original v18 release as a separate artifact even when newer specialized systems are published.

Specific internal steps, requirements, and constraints remain authoritative **inside the ZIP**; this README does not claim to reproduce or validate the archive's internal instructions.

## Using it

1. Download [the canonical archive](meta-llm-orchestrator.zip).
2. Extract it locally and read its included entrypoint instructions/README.
3. Adapt the instruction framework to a new domain, documenting any deviations in that domain's own README and sources.
4. Register the resulting instruction set as an independent top-level folder, rather than modifying the progenitor archive.

## Provenance and status

The canonical ZIP here is the **unchanged Git blob** from the previous repository path:

`packages/meta-llm-orchestrator/v18/meta_llm_orchestrator_instruction_set_v18.zip`

Original recorded release: `v18`. No claims are made about verification of internal archive files here. Supporting provenance belongs in [sources/](sources/README.md).

## Limitations

- The canonical ZIP is a packaged instruction system, not a guaranteed executable tool.
- The README describes repository-level intent; consult the archive to understand its actual requirements.
- Later instruction sets must document their own features and boundaries instead of assuming that all progenitor capabilities apply.
