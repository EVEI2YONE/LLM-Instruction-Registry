"""Deterministic pre-execution gate for a registry-selected specialist.

This checks evidence supplied by the caller. It cannot observe whether a model truly
followed its instructions; that requires end-to-end runtime evaluation.
"""
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class ExecutionReceipt:
    native_spawn: str  # verified-available | verified-unavailable | unknown
    delegation_authorized: bool
    mode: str  # NATIVE_CHILD | SEQUENTIAL_SPECIALIST
    registry_commit: str
    package_id: str
    package_version: str
    entrypoint_loaded: bool
    required_sections: Tuple[str, ...]
    loaded_sections: Tuple[str, ...]
    instruction_status: str  # LOADED | MISSING
    child_handle: Optional[str] = None
    child_instruction_receipt: bool = False
    output_owner: str = "parent"


class GateError(ValueError):
    """A specialist-scoped task is not authorized to execute or claim completion."""


def choose_mode(native_spawn: str, delegation_authorized: bool) -> str:
    if native_spawn not in {"verified-available", "verified-unavailable", "unknown"}:
        raise GateError("invalid runtime capability evidence")
    if native_spawn == "verified-available" and delegation_authorized:
        return "NATIVE_CHILD"
    return "SEQUENTIAL_SPECIALIST"


def require_ready(receipt: ExecutionReceipt) -> None:
    """Fail before specialist work when source closure or execution mode is invalid."""
    import re
    if receipt.mode != choose_mode(receipt.native_spawn, receipt.delegation_authorized):
        raise GateError("execution mode contradicts verified runtime capability/policy")
    if not re.fullmatch(r"[0-9a-f]{40}", receipt.registry_commit):
        raise GateError("registry snapshot must be an immutable commit SHA")
    if not receipt.package_id or not receipt.package_version or not receipt.entrypoint_loaded:
        raise GateError("BLOCKED_INSTRUCTIONS: registered entrypoint or version missing")
    if receipt.instruction_status != "LOADED":
        raise GateError("BLOCKED_INSTRUCTIONS: instruction status is not LOADED")
    required = set(receipt.required_sections)
    loaded = set(receipt.loaded_sections)
    if not required.issubset(loaded):
        raise GateError("BLOCKED_INSTRUCTIONS: mandatory section/dependency closure incomplete")
    if receipt.mode == "NATIVE_CHILD":
        if not receipt.child_handle or not receipt.child_instruction_receipt:
            raise GateError("native child requires a provider handle and instruction receipt")
        if receipt.output_owner == "parent":
            raise GateError("native child output cannot be labeled parent-owned")
    elif receipt.child_handle or receipt.child_instruction_receipt:
        raise GateError("sequential fallback cannot claim child execution")


def assert_valid_claim(receipt: ExecutionReceipt, claim: str) -> None:
    require_ready(receipt)
    if claim == "CHILD_COMPLETE":
        if receipt.mode != "NATIVE_CHILD":
            raise GateError("false child execution claim")
    elif claim == "SEQUENTIAL_SPECIALIST":
        if receipt.mode != "SEQUENTIAL_SPECIALIST" or receipt.output_owner != "parent":
            raise GateError("false sequential specialist claim")
    else:
        raise GateError("unsupported completion claim")
