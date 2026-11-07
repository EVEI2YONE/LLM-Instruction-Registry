# LLM Instruction Registry

Central registry of authoritative, reusable LLM instruction-set ZIP packages.

## Canonical packages

| Instruction system | Authoritative package | Role | Repository status |
|---|---|---|---|
| Meta-LLM Instruction Architect | [`meta_llm_orchestrator_instruction_set_v18.zip`](packages/meta-llm-orchestrator/v18/meta_llm_orchestrator_instruction_set_v18.zip) | **Progenitor** instruction architecture; retain as the foundational system | Uploaded |
| Technical Research Project Instructions v2 | [`technical_research_project_instructions_v2.zip`](packages/technical-research-project-instructions/v2/technical_research_project_instructions_v2.zip) | Research, architecture consulting, and technical teaching | Uploaded |
| AI Knowledge Atlas | `AI-Knowledge-Atlas-40-Project-Sources.zip` | **Latest authoritative Atlas instruction set**, confirmed by repository owner | Awaiting recovery of original ZIP bytes |

## Canonical selection decisions

- **Retain the Meta-LLM Orchestrator v18 ZIP** as the progenitor, even if newer specialized instruction systems are added.
- **Retain AI-Knowledge-Atlas-40-Project-Sources.zip** as the sole authoritative latest Atlas package. Other Atlas v1/v2/compact or alias archives are not separate current releases and should not be imported as competing canonical entries.
- Archive contents, if available, should be verified before upload. No replacement or speculative reconstruction of the canonical Atlas ZIP.
- Distinct instruction systems may each have one latest canonical release; historical versions remain optional, clearly labeled, and separate.

## Loading a package

Download and extract an uploaded ZIP. Follow its own README for source-material setup and project or agent integration.

## Import limitations

The Atlas package is known by exact name, but its original binary content was not accessible through the currently available Project/Library file extraction interface. This README records the chosen authoritative archive; it **does not represent the Atlas ZIP as uploaded**. Add the original ZIP at `packages/ai-knowledge-atlas/latest/AI-Knowledge-Atlas-40-Project-Sources.zip` when its bytes are available.

## Coding Partner / Mentor / Teacher

The [Coding Partner v1 instruction package](packages/coding-partner-mentor-teacher/v1/README.md) provides a practical software-engineering assistant configuration with concise recommendations, debugging workflows, design reviews, mentorship examples, and self-heal guidance.

- [Download the v1 ZIP](packages/coding-partner-mentor-teacher/v1/coding_partner_mentor_teacher_instruction_set_v1.zip)
- [Browse editable source files](packages/coding-partner-mentor-teacher/v1/sources/)
- Primary prompt: `packages/coding-partner-mentor-teacher/v1/sources/00_compiled_instruction_prompt.md`
