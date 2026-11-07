# Feature Extension Planning Council Instruction Set

This package is an agent-facing instruction architecture for a reusable Feature Extension Planning Council. It helps research, evaluate, architect, and plan software extensions so the final output can be handed directly to a Technical Project Manager and a development team.

## How to use

1. Extract this ZIP.
2. Add the extracted files as source material to the target ChatGPT Project, agent, or internal planning assistant.
3. Use `00_compiled_instruction_set.md` as the top-level reference.
4. Keep the folder structure intact so the receiving agent can distinguish core behavior, helper methods, council sub-roles, templates, handoff formats, registries, examples, and validation tables.

## Operating priority

| Priority | Source | Use |
|---:|---|---|
| 00 | `00_compiled_instruction_set.md` | Complete behavior contract. |
| 01 | `01_core/01_core_role_instruction_set.md` | Stable mission and non-negotiable rules. |
| 02 | `02_general_helpers/02_general_helper_instruction_sets.md` | Reusable research, architecture, schema, and validation helpers. |
| 03 | `03_sub_roles/` | Council member roles and specialist responsibilities. |
| 04 | `04_templates/` | Reusable outputs for plans, schemas, pseudocode, and handoff packages. |
| 05 | `05_handoffs/` | TPM/development-team handoff format. |
| 06 | `06_sources_to_update/` | Registries, decision logs, risks, open questions, and corrections. |
| 07 | `07_tables/` | Required validation tables. |
| 08 | `08_examples/` | Example invocation and output skeletons. |

## Core assumption

When asked to research or plan a feature extension, the council should produce a practical development plan with enough architecture, pseudocode, schemas, acceptance criteria, sequencing, risk analysis, and team handoff detail for immediate TPM/development-team intake.