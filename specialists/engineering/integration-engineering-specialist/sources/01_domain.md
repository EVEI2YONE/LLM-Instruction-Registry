# Domain procedure
1. Pin producer/consumer contracts, credentials boundary and integration sequence before editing code.
2. Implement minimal API/event adapters, idempotency, retry and timeout behavior required by approved scenarios.
3. Coordinate contract compatibility with backend, frontend and infrastructure owners.
4. Write integration and failure-path tests including duplicate events and partial outages.
5. Deliver scoped PR evidence, rollback notes and unresolved production dependencies.

## Representative task
Implement a billing webhook to update shared account credits without double-spending.

## Output validation
- [ ] integration-code
- [ ] contract-tests
- [ ] failure-evidence
- [ ] pr-handoff
