# Contributing instruction sets

The canonical publication layout is `instruction-sets/<plural-role>/<id>/`. Role folders are `progenitors`, `curators`, `experts`, `strategists`, `orchestrators`, and `generalists`.

Consult [publishing instructions](docs/PUBLISHING.md) and [role taxonomy](docs/ROLE_TAXONOMY.md) first. Assign one primary `role` and additional nonexclusive `capabilities` and `domains` for agentic search. Retain stable IDs, validate real ZIPs, publish full browsable sources, and update registry and category/root READMEs together.

The ZIP inside each package must have one `<id>/` top-level directory. **For new packages**, safely extract and repackage the actual content; renaming a ZIP is insufficient. **For pure folder relocations**, preserve the existing validated binary blob and sources byte-for-byte. Check moved blob SHA identities before completing the PR.

Do not fabricate archives, tests or metadata. Packages without a real ZIP and source README remain pending and unregistered. Use branches and reviewable PRs; never merge without explicit user authorization. [Executive Product Repository Review](instruction-sets/strategists/executive-product-repo-review/README.md) is such a pending source-only package.

Maintain meaningful `aliases` and `use_cases` for search, plus one primary role and multiple useful capability/domain facets. Consult the [agent discovery protocol](docs/AGENTIC_SEARCH.md) and run `python3 scripts/search_registry.py validate` plus the search unit tests before publishing. Source paths and metadata must describe actual capabilities, not claimed tool availability.

Do not rerun legacy `scripts/rebuild_registry.py` when `packages/` is absent.
