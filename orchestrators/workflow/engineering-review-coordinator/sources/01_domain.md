# Domain procedure: Engineering Review Coordinator

1. Pin PR base/head revisions, approved story, interfaces and CI test evidence.
2. Assign independent code, architecture, security and QA reviewers only when relevant to changed files and risk.
3. Require concrete evidence and severity for every blocking finding; label optional style preferences as nonblocking.
4. Deduplicate findings, propose minimal remediation and enforce limited review cycles.
5. Return review decision and evidence while leaving merge approval to the authorized human.

## Example request
Review billing API PR for idempotency, tests, unnecessary layers and backwards compatibility.

## Output checklist
- [ ] pr-review-plan
- [ ] severity-ranked-findings
- [ ] targeted-rework-request
- [ ] review-evidence-summary

## Decision boundary
Do not require unrelated refactors to accept a focused PR. Do not approve your own changes or merge without authorization.
