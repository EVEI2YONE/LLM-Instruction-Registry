# Full-registry migration ledger

The inventory includes **all 49 registered packages**, including every specialist and every orchestrator. No pilot subset is excluded. The baseline retains all 49 package records; Meta-LLM Orchestrator v21 has now been versioned and the other 48 remain pending.

Run `python3 scripts/migration_inventory.py --verify migration/inventory.json` to detect drift. As the staged full-catalog migration proceeds, replace the static baseline with a version-aware ledger tracking source and archive revisions, per-package validation, source provenance, and approvals. The frozen baseline versions and original archives are retained. The verification command permits only explicitly recorded migrations and checks old/new archives.

No migrated package is published by adding only a pending row.
