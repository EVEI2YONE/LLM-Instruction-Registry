# Technical Research Project Instructions v2

This package contains an enhanced, upload-ready instruction architecture for a ChatGPT Project that should behave as a technical researcher, consultant, and teacher.

## How to use

1. Extract this ZIP package.
2. Add the extracted markdown and JSON files to your ChatGPT Project as source material.
3. Use `00_compiled_instruction_set.md` as the main reference if your project only accepts one instruction file.
4. Use the modular files when you want clearer source organization and easier future updates.

## Source map

| Priority | Path | Purpose |
|---:|---|---|
| 00 | `00_compiled_instruction_set.md` | Combined project behavior contract. |
| 01 | `01_core/01_core_role_instruction_set.md` | Stable role, mission, priorities, and non-negotiable behavior. |
| 02 | `02_helpers/` | Reusable source, truthfulness, consulting, and teaching helpers. |
| 03 | `03_sub_roles/` | Specialized internal modes for research, consulting, teaching, and review. |
| 04 | `04_templates/` | Default answer templates and citation quality checklist. |
| 05 | `05_sources_to_update/` | Preferences, correction log, taxonomy, and unresolved questions. |
| 06 | `06_validation/` | Package and behavior validation tables. |
| 07 | `07_examples/` | Examples of intended behavior. |