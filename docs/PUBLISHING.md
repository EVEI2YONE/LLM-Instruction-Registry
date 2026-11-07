# Publishing instruction sets by role

Follow [CONTRIBUTING](../CONTRIBUTING.md), [role taxonomy](ROLE_TAXONOMY.md), the current registry, root catalog and any existing package README.

1. Inspect current catalog and active PRs. Choose a stable package `id`, **one primary role** (`progenitor`, `curator`, `expert`, `strategist`, `orchestrator`, or `generalist`), capabilities and domains. Role classifies responsibility; capabilities describe search facets.
2. Publish to `instruction-sets/<plural-role>/<id>/`; add explanatory package README, actual versioned ZIP, full browsable `sources/` and sources README. The ZIP's internal root remains `<id>/`.
3. For a new ZIP, safely extract the original, reject unsafe paths and symlinks, normalize under `<id>/`, **repack** (not rename), test CRC and compare extracted content to the original. For a pure folder move, preserve the existing ZIP blob without unnecessary repackaging.
4. Use real binary GitHub objects (e.g. `create_blob` with base64 bytes and Git Data tree commits) or an authenticated git push; text file APIs do not safely upload raw ZIPs. Validate actual blob and individual source file presence on the PR branch.
5. Update exactly one canonical `registry.json` record per available package: `id`, `name`, `description`, `version`, `role`, `capabilities`, `domains`, `tags`, `status`, `readme`, `archive`, `sources`.
6. Update category README, root catalog and crosslinks. Verify that registered paths exist and migration preserves moved blob SHAs. Document old→new locations; do not leave stale known links.
7. Incomplete source-only packages may have pending documentation but must not have fabricated available releases.
8. Open or update a reviewable PR based on current `main`; never merge without explicit authorization. State file count, verification scope and known limitations. No claim of post-upload ZIP integrity unless verified.

## Search index maintenance gate

Include informative `aliases` and `use_cases` for every available release, in addition to role, capabilities and domains. On additions, renames or role changes, validate the catalog and expected search results:

```sh
python3 scripts/search_registry.py validate
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/search_registry.py search --query "coding mentor"
```

See [agent discovery protocol](AGENTIC_SEARCH.md). Document newly ambiguous aliases and add appropriate regressions. Do not claim local tests passed unless run; CI status is a separate verification gate.

Do not rerun the legacy one-time `scripts/rebuild_registry.py` migration.
