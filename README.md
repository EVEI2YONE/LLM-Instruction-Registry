# LLM Instruction Registry

Central registry of authoritative, reusable LLM instruction-set ZIP packages.

## Canonical packages

| Instruction system | Authoritative package | Role | Repository status |
|---|---|---|---|
| Meta-LLM Instruction Architect | [`meta_llm_orchestrator_instruction_set_v18.zip`](packages/meta-llm-orchestrator/v18/meta_llm_orchestrator_instruction_set_v18.zip) | **Progenitor** instruction architecture; retain as the foundational system | Uploaded |
| Technical Research Project Instructions v2 | [`technical_research_project_instructions_v2.zip`](packages/technical-research-project-instructions/v2/technical_research_project_instructions_v2.zip) | Research, architecture consulting, and technical teaching | Uploaded |
| AI Knowledge Atlas | `AI-Knowledge-Atlas-40-Project-Sources.zip` | **Latest authoritative Atlas instruction set**, confirmed by repository owner | Awaiting recovery of original ZIP bytes |
| Feature Extension Planning Council | [v1 sources](packages/feature-extension-planning-council/v1/README.md) | Feature scope, architecture, risk, phased delivery, and TPM handoff council | Sources uploaded |

## Canonical selection decisions

- **Retain the Meta-LLM Orchestrator v18 ZIP** as the progenitor, even if newer specialized instruction systems are added.
- **Retain AI-Knowledge-Atlas-40-Project-Sources.zip** as the sole authoritative latest Atlas package. Other Atlas v1/v2/compact or alias archives are not separate current releases and should not be imported as competing canonical entries.
- Archive contents, if available, should be verified before upload. No replacement or speculative reconstruction of the canonical Atlas ZIP.
- Distinct instruction systems may each have one latest canonical release; historical versions remain optional, clearly labeled, and separate.

## Loading a package

Download and extract an uploaded ZIP. Follow its own README for source-material setup and project or agent integration.

## Import limitations

The Atlas package is known by exact name, but its original binary content was not accessible through the currently available Project/Library file extraction interface. This README records the chosen authoritative archive; it **does not represent the Atlas ZIP as uploaded**. Add the original ZIP at `packages/ai-knowledge-atlas/latest/AI-Knowledge-Atlas-40-Project-Sources.zip` when its bytes are available.
