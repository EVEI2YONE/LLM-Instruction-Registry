"""Regression: extensive specialist evidence cannot be reduced to a summary."""
import unittest

from runtime.readiness_report_gate import Finding, ReadinessReport, ReportIncomplete, accept_readiness_report


FINDINGS = (
    Finding("ONBOARDING", "REQ-ONBOARD", "New users cannot complete the intended first-run path", "src:onboarding", "blocker"),
    Finding("MANAGEMENT", "REQ-MGMT", "Core project management actions are read-only", "src:management", "blocker", ("ONBOARDING",)),
    Finding("REVIEW", "REQ-REVIEW", "Review detail coverage is incomplete", "src:review", "gap", ("MANAGEMENT",)),
    Finding("STAGING", "REQ-STAGE", "Staging acceptance has no verified evidence", "src:release-gates", "blocker", ("REVIEW",)),
    Finding("QA", "REQ-QA", "Automated tests passed but manual acceptance is pending", "src:qa-run", "verified"),
)


def full_report(**changes):
    fields = dict(
        verdict="NO-GO",
        feature_coverage={x.requirement_id: x.disposition for x in FINDINGS},
        findings=FINDINGS,
        validation={"passed": ("automated",), "failed": (), "untested": ("staging", "manual")},
        backlog=("ONBOARDING", "MANAGEMENT", "REVIEW", "STAGING"),
        unresolved_decisions=("onboarding scope",),
        limitations=("No verified staging acceptance",),
    )
    fields.update(changes)
    return ReadinessReport(**fields)


class ReadinessReportGateTests(unittest.TestCase):
    def test_full_report_accepted(self):
        accept_readiness_report(FINDINGS, full_report())

    def test_summary_drops_material_findings(self):
        with self.assertRaisesRegex(ReportIncomplete, "dropped material finding"):
            accept_readiness_report(FINDINGS, full_report(findings=(FINDINGS[0],)))

    def test_evidence_mutation_rejected(self):
        altered = (Finding("ONBOARDING", "REQ-ONBOARD", "Minor", "src:fake", "blocker"),) + FINDINGS[1:]
        with self.assertRaisesRegex(ReportIncomplete, "altered impact"):
            accept_readiness_report(FINDINGS, full_report(findings=altered))

    def test_prerequisite_missing_from_backlog(self):
        with self.assertRaisesRegex(ReportIncomplete, "prerequisite"):
            accept_readiness_report(FINDINGS, full_report(backlog=("MANAGEMENT", "REVIEW", "STAGING")))

    def test_validation_untested_preserved(self):
        with self.assertRaisesRegex(ReportIncomplete, "missing validation class"):
            accept_readiness_report(FINDINGS, full_report(validation={"passed": [], "failed": []}))

    def test_feature_status_missing(self):
        with self.assertRaisesRegex(ReportIncomplete, "requirement coverage"):
            accept_readiness_report(FINDINGS, full_report(feature_coverage={}))

    def test_limitations_missing(self):
        with self.assertRaisesRegex(ReportIncomplete, "evidence limitations"):
            accept_readiness_report(FINDINGS, full_report(limitations=()))


if __name__ == "__main__":
    unittest.main()
