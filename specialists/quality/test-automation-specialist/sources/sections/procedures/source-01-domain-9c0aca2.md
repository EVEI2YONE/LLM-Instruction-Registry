# Domain procedure
1. Read the approved acceptance criteria, code contracts and test conventions at pinned revisions.
2. Choose appropriate unit, contract, integration and end-to-end coverage, prioritizing risky boundaries.
3. Implement stable fixtures and deterministic test cases for success, failure and concurrency.
4. Run tests only when the workspace actually permits execution; capture exact commands and results.
5. Document unverified scenarios, flaky behavior and residual testing risks for QA approval.

## Representative task
Test duplicate Stripe events, credit ledger invariants and frontend purchasing failure states.

## Output validation
- [ ] automated-tests
- [ ] test-evidence
- [ ] coverage-risk-map
- [ ] regression-plan
