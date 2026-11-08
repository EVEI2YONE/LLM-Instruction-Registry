"""Conservative policy enforcement until approval rules are reconciled."""
from __future__ import annotations
import json
from pathlib import Path

# Until authenticated human approval is implemented in the runner, all
# consequential actions are blocked, even if a client supplies approval_ref.
BLOCKED_ACTIONS = {
    "investment", "merge", "production", "production-deployment",
    "irreversible-change", "scope-or-priority-policy-change",
    "release-production", "approve", "delete-approved",
}


def check_permissions(repo: str | Path, permissions: list[str]) -> None:
    root = Path(repo)
    approval = json.loads((root / "governance" / "approval.json").read_text(encoding="utf8"))
    ownership = json.loads((root / "governance" / "capability-ownership" /
                            "ownership-policies.json").read_text(encoding="utf8"))
    human_only = set(approval["human_required_for"]) | set(ownership["human_only_approvals"]) | BLOCKED_ACTIONS
    if set(permissions) & human_only:
        raise PermissionError("consequential actions need a verified human approval gateway")
    if not permissions or not all(isinstance(p, str) and p for p in permissions):
        raise ValueError("permissions must be non-empty strings")
