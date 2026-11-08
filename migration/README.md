# Full-registry migration ledger

The inventory includes **all 49 registered packages**, including every specialist and every orchestrator. No pilot subset is excluded. This foundation stage intentionally marks every item pending.

Run `python3 scripts/migration_inventory.py --verify migration/inventory.json` to detect drift. As the staged full-catalog migration proceeds, replace the static baseline with a version-aware ledger tracking source and archive revisions, per-package validation, source provenance, and approvals. The current inventory is a frozen pre-migration baseline and should not be rewritten to hide incomplete conversions.

No migrated package is published by adding only a pending row.
