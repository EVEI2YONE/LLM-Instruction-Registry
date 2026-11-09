"""Task-agnostic deliverable retention checks for independently sourced findings.

No release, architecture, feature, QA or other domain-specific schema is required.
Authoritative task-specific criteria come from the caller, not this module.
"""
from dataclasses import dataclass
from typing import Tuple


class DeliverableIncomplete(ValueError):
    pass


@dataclass(frozen=True)
class MaterialFinding:
    id: str
    source_ref: str
    summary: str
    significance: str
    dependency_ids: Tuple[str, ...] = ()


@dataclass(frozen=True)
class DeliveredFinding:
    id: str
    source_ref: str
    summary: str
    significance: str
    dependency_ids: Tuple[str, ...] = ()


@dataclass(frozen=True)
class Deliverable:
    artifact_ref: str
    findings: Tuple[DeliveredFinding, ...]
    satisfied_criteria: Tuple[str, ...] = ()
    criterion_evidence_refs: Tuple[str, ...] = ()
    excluded_findings: Tuple[str, ...] = ()
    exclusion_rationales: Tuple[str, ...] = ()


def accept_deliverable(sources: Tuple[MaterialFinding, ...], result: Deliverable,
                       required_criteria: Tuple[str, ...] = ()) -> None:
    """Compare complete independent source ledger with delivered material.

    This structural gate cannot verify the semantic truth of source citations;
    an independent reviewer must inspect the actual source and output artifacts.
    """
    if not result.artifact_ref:
        raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: missing actual artifact reference")
    wanted = {f.id: f for f in sources}
    if len(wanted) != len(sources):
        raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: duplicate source finding ID")
    seen = {f.id: f for f in result.findings}
    if len(seen) != len(result.findings):
        raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: duplicate output finding ID")
    exclusions = dict(zip(result.excluded_findings, result.exclusion_rationales))
    if len(result.excluded_findings) != len(result.exclusion_rationales):
        raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: exclusion lacks rationale")
    if len(exclusions) != len(result.excluded_findings):
        raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: duplicate exclusions")
    for id, src in wanted.items():
        if id in exclusions:
            if id in seen or not exclusions[id].strip():
                raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: invalid exclusion " + id)
            continue
        actual = seen.get(id)
        if actual is None:
            raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: material finding omitted " + id)
        if actual != DeliveredFinding(src.id, src.source_ref, src.summary,
                                      src.significance, src.dependency_ids):
            raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: material source/impact changed " + id)
    if any(id not in wanted for id in exclusions):
        raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: unjustified exclusion")
    if len(result.satisfied_criteria) != len(result.criterion_evidence_refs):
        raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: criterion evidence misaligned")
    proof = dict(zip(result.satisfied_criteria, result.criterion_evidence_refs))
    if len(proof) != len(result.satisfied_criteria):
        raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: duplicate criterion")
    for item in required_criteria:
        if not proof.get(item):
            raise DeliverableIncomplete("DELIVERABLE_INCOMPLETE: unsatisfied task criterion " + item)
