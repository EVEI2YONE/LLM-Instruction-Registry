# Pending authority-policy reconciliation

Status: **open decision; no authority rules changed in the foundations PR**.

Two existing authoritative sources differ:
- `governance/approval.json` requires a human for `investment`, `merge`, `production-deployment`, `irreversible-change`.
- `governance/capability-ownership/ownership-policies.json` requires `investment`, `scope-or-priority-policy-change`, `production`, `merge`, `irreversible-change`.

For an action implicated by either policy, a runtime MUST adopt the conservative combined restriction and block if the authorized human approval is missing. Treat `production` and `production-deployment` as overlapping but not assumed identical; resolve nomenclature explicitly. This is a temporary conflict-handling rule, not an authorization to rewrite the owner policies.

Before package migration: choose one canonical approval enumeration and a backward-compatible mapping, designate human owner, update both files in a separately reviewed governance change, add exact-revision approval tests, and release a versioned common-rules contract. No agent self-approval.
