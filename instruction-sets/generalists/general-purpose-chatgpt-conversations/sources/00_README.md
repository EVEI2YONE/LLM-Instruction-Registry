# Efficient Conversation Research Project v2

This package is source material for a ChatGPT Project designed for efficient, friendly, topic-enhancing conversation with credible-source research when needed.

## How to use

1. Extract the ZIP package.
2. Add the extracted files as ChatGPT Project source material.
3. Use `00_compiled_instruction_set.md` as the primary instruction reference.
4. Keep the supporting files available so the Project can reinforce tone, research behavior, templates, source quality, and self-heal updates.

## Operating priority

| Priority | Source | Use |
|---:|---|---|
| 00 | `00_compiled_instruction_set.md` | Combined behavior contract. |
| 01 | `01_core/01_core_role_instruction_set.md` | Stable identity, tone, and response defaults. |
| 02 | `02_helpers/` | Conversation pacing, research triggers, and source filtering. |
| 03 | `03_sub_roles/` | Internal roles for conversation, advice, research, synthesis, token budget, and self-heal. |
| 04 | `04_templates/` | Reusable answer and source-review formats. |
| 05 | `05_handoffs/` | Phased workflow for complex or researched turns. |
| 06 | `06_sources_to_update/` | Preferences, source quality, correction log, and self-heal rules. |
| 07 | `07_tables/` | Expected artifacts and validation checks. |
| 99 | `99_manifest.json` | Inventory and validation flags. |

## Intended behavior

The Project should usually respond in 1-4 short paragraphs, avoid excessive emojis, add one useful tidbit or practical angle when helpful, and ask at most one follow-up question. It should research before answering current, niche, disputed, or high-stakes questions, filter candidate sources for credibility, and summarize findings by importance with compact citations.