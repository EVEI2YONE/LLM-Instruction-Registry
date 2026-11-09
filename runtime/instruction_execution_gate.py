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
        if receipt.output_owner == "parent":
            raise GateError("native child output cannot be labeled parent-owned")
    elif receipt.child_handle or receipt.child_instruction_receipt:
        raise GateError("sequential fallback cannot claim child execution")


def assert_valid_claim(receipt: ExecutionReceipt, claim: str) -> None:
    require_ready(receipt)
    if claim == "CHILD_COMPLETE":
        if receipt.mode != "NATIVE_CHILD":
            raise GateError("false child execution claim")
        if not receipt.child_handle or not receipt.child_instruction_receipt:
            raise GateError("child completion requires provider handle and instruction receipt")
    elif claim == "SEQUENTIAL_SPECIALIST":
        if receipt.mode != "SEQUENTIAL_SPECIALIST" or receipt.output_owner != "parent":
            raise GateError("false sequential specialist claim")
    else:
        raise GateError("unsupported completion claim")


@dataclass(frozen=True)
class InstructionEvidence:
    """Evidence of delivery and requirements checked against the resulting artifact.

    Recorded claims are not an independent observation of model behavior.
    The caller must supply observable refs from actual runtime/tool traces.
    """
    execution_id: str
    executor: str  # parent | child
    package_id: str
    package_version: str
    registry_commit: str
    delivered_section_ids: Tuple[str, ...]
    delivered_entrypoint: bool
    delivery_ref: str
    artifact_ref: str
    required_rule_ids: Tuple[str, ...]
    checked_rule_ids: Tuple[str, ...]
    rule_evidence_refs: Tuple[str, ...]


def assert_propagation_and_application(receipt: ExecutionReceipt, claim: str,
                                       evidence: InstructionEvidence) -> None:
    """Require traceable instruction delivery and criterion-by-criterion application.

    The caller must independently verify that refs are genuine, accessible and
    actually substantiate the rule checks. This function does not read a model's
    hidden reasoning or establish behavioral compliance by itself.
    """
    assert_valid_claim(receipt, claim)
    if (evidence.package_id != receipt.package_id
            or evidence.package_version != receipt.package_version
            or evidence.registry_commit != receipt.registry_commit):
        raise GateError("instruction propagation provenance mismatch")
    if not evidence.delivered_entrypoint:
        raise GateError("instruction propagation: missing entrypoint delivery")
    if not set(receipt.required_sections).issubset(set(evidence.delivered_section_ids)):
        raise GateError("instruction propagation: missing required section delivery")
    if not evidence.execution_id or not evidence.delivery_ref or not evidence.artifact_ref:
        raise GateError("instruction propagation: missing observable execution/delivery/artifact refs")
    if claim == "CHILD_COMPLETE":
        if evidence.executor != "child" or evidence.execution_id != receipt.child_handle:
            raise GateError("instruction propagation: wrong child execution handle")
    elif evidence.executor != "parent" or evidence.execution_id != "parent:" + receipt.package_id:
        raise GateError("instruction propagation: sequential phase not attributable to parent")
    if not evidence.required_rule_ids:
        raise GateError("instruction application: no scoped acceptance rules selected")
    if not set(evidence.required_rule_ids).issubset(set(evidence.checked_rule_ids)):
        raise GateError("instruction application: mandatory acceptance rules unchecked")
    if len(evidence.checked_rule_ids) != len(evidence.rule_evidence_refs):
        raise GateError("instruction application: missing criterion-specific evidence")
    if any(not x for x in evidence.rule_evidence_refs):
        raise GateError("instruction application: empty criterion-specific evidence")
