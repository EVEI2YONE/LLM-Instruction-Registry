# Domain playbook
1. Inspect the current database schema, migration tooling, backups and deployment topology.
2. Propose forward/backward-compatible steps and data backfill procedures with ownership approval.
3. Assess lock duration, traffic, data size, recovery options and idempotence.
4. Add representative migration tests, invariants and rollback/run-forward strategies.
5. Record exact applied revisions and verify post-migration integrity before declaring success.

## Example
Add a credit transaction uniqueness constraint without breaking existing accounts.

## Required evidence
- [ ] migration-plan
- [ ] schema-change
- [ ] data-integrity-tests
- [ ] rollback-evidence
