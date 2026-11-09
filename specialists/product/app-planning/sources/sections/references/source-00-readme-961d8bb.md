# App Planning Instruction Set v1

This package is an upload-ready source-material set for a ChatGPT Project focused on app planning, product shaping, architecture planning, research handoff, Antigravity IDE preparation, and Claude worktree decomposition.

## How to use

1. Extract this ZIP.
2. Add the extracted files as source material to the target ChatGPT Project.
3. Use `00_compiled_instruction_set.md` as the primary reference if the project supports one core instruction file.
4. Keep the foldered files as separate source material when the project supports multiple files.
5. Preserve the source and validation files; they help future revisions stay consistent.

## Operating priority

| Priority | Source | Purpose |
|---:|---|---|
| 00 | `00_compiled_instruction_set.md` | Full combined behavior contract. |
| 01 | `01_core/01_core_role_instruction_set.md` | Stable identity, mission, and non-negotiable behavior. |
| 02 | `02_operating_modes/` | Mode commands and state transition rules. |
| 03 | `03_planning_workflow/` | End-to-end planning sequence and required output sections. |
| 04 | `04_stack_and_modularity/` | Default stack, modular boundaries, dependency rules, and schemas. |
| 05 | `05_handoffs/` | Research Agent, Antigravity IDE, and Claude handoff guidance. |
| 06 | `06_templates/` | Reusable output templates. |
| 07 | `07_validation/` | Validation and completion checklists. |
| 08 | `08_sources/` | Source inventory and revision notes. |
| 09 | `09_self_heal/` | Durable correction and self-heal behavior. |

## Intended behavior

The project should help transform rough app ideas into coherent, stack-aligned, modular, research-backed, handoff-ready planning packages. It should not jump straight into implementation unless explicitly asked. It should first refine the idea, generate a structured plan, critique the plan, strengthen it, review stack and modularity, prepare research questions, and then produce downstream handoff artifacts.