"""Deterministic material-finding retention gate for product readiness reporting.

Validates a structured report against independently supplied specialist findings.
It does not determine whether findings are true or whether prose faithfully explains
an evidence reference; reviewers must inspect the source and final artifact.
"""
from dataclasses import dataclass
from typing import Tuple


class ReportIncomplete(ValueError):
    pass


@dataclass(frozen=True)
class Finding:
    id: str
    requirement_id: str
    impact: str
    evidence_ref: str
    disposition: str  # blocker | gap | verified
    dependency_ids: Tuple[str, ...] = ()


@dataclass(frozen=True)
class ReadinessReport:
    verdict: str
    feature_coverage: dict
    findings: Tuple[Finding, ...]
    validation: dict
    backlog: Tuple[str, ...]
    unresolved_decisions: Tuple[str, ...]
    limitations: Tuple[str, ...]


def accept_readiness_report(specialist_findings: Tuple[Finding, ...],
                            report: ReadinessReport) -> None:
    if not report.verdict:
        raise ReportIncomplete("READINESS_REPORT_INCOMPLETE: missing verdict")
    expected = {f.id: f for f in specialist_findings}
    if len(expected) != len(specialist_findings):
        raise ReportIncomplete("duplicate specialist finding identifiers")
    actual = {f.id: f for f in report.findings}
    for key, finding in expected.items():
        if key not in actual:
            raise ReportIncomplete("READINESS_REPORT_INCOMPLETE: dropped material finding " + key)
        rendered = actual[key]
        if rendered != finding:
            raise ReportIncomplete("READINESS_REPORT_INCOMPLETE: altered impact, evidence, requirement, or dependencies " + key)
        if finding.requirement_id not in report.feature_coverage:
            raise ReportIncomplete("READINESS_REPORT_INCOMPLETE: missing requirement coverage " + finding.requirement_id)
        if finding.disposition in {"blocker", "gap"}:
            if key not in report.backlog:
                raise ReportIncomplete("READINESS_REPORT_INCOMPLETE: actionable backlog missing " + key)
            for dep in finding.dependency_ids:
                if dep not in report.backlog:
                    raise ReportIncomplete("READINESS_REPORT_INCOMPLETE: missing prerequisite " + dep)
    for status in ("passed", "failed", "untested"):
        if status not in report.validation:
            raise ReportIncomplete("READINESS_REPORT_INCOMPLETE: missing validation class " + status)
    if not report.limitations:
        raise ReportIncomplete("READINESS_REPORT_INCOMPLETE: missing evidence limitations")
    if report.unresolved_decisions is None:
        raise ReportIncomplete("READINESS_REPORT_INCOMPLETE: unresolved decisions not accounted for")
