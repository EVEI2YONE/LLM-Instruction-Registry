# Domain playbook
1. Identify data entities, use cases, invariants, retention and authority of record.
2. Compare relational, document, event and analytical storage based on access patterns.
3. Design consistency boundaries, schema evolution, cross-service synchronization and lineage.
4. Evaluate privacy, security and operational recovery implications.
5. Return versioned schemas, migration impacts, data-quality checks and approval decisions.

## Example
Separate billing ledger, credit balances and analytics aggregates without duplicate authority.

## Required evidence
- [ ] logical-data-model
- [ ] ownership-and-lineage-map
- [ ] schema-evolution-plan
- [ ] data-risk-review
