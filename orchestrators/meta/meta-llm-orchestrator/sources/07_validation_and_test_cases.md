# Validation and test matrix

Before publication, enforce (1) source/ZIP equality and CRC, (2) manifest and registry paths, (3) entrypoint/README/self-heal presence, (4) workspace adaptation, (5) authority/approval boundaries and (6) truthful tool/deployment claims.

| Scenario | Expected routing |
|---|---|
| User asks for a single debugging specialist | Reuse direct specialist; no mandatory SDLC |
| User asks to build a product from ideation | Primary orchestrator -> Organization-to-MVP -> approved SDLC |
| User asks for workflow with shared reviewers | Workflow with explicit responsibilities and independent QA |
| Local Codex checkout with shell access verified | Repo instructions + tests/PR only within permissions |
| Local agent without network | Offline evidence; no claims of current remote facts |
| ChatGPT Project with limited upload slots | Compact validated source package within current limits |
| Hosted chatbot with only system prompts | Portable prompt/integration spec, not fake local skill install |
| Grok bot action capabilities unknown | Provider-neutral instructions and explicit capability validation |
| Existing package same capability | Extend/version rather than creating a duplicate agent |
| ZIP missing or not byte-equivalent | Block availability/registry entry |
| Existing user correction reveals systemic issue | Self-heal report and regression change |
| Product owner approval unavailable | Return approval request; no self-authorization |

Run `python3 scripts/search_registry.py validate`, all unit tests, ZIP CRC/source comparisons, link checks and workspace-specific smoke tests. Mark tests not executed as UNVERIFIED; do not treat this guide as evidence of a deployed runtime.
