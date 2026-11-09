"""Cross-domain tests: deliverable acceptance must be task-specific, never release-specific."""
import unittest

from runtime.deliverable_acceptance_gate import (
    MaterialFinding, DeliveredFinding, Deliverable,
    DeliverableIncomplete, accept_deliverable,
)


class DeliverableAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.findings = (
            MaterialFinding("A", "artifact:research#a", "Evidence is incomplete",
                            "Limits confidence"),
            MaterialFinding("B", "artifact:design#b", "Tradeoff remains open",
                            "Requires authorized owner decision", ("A",)),
        )
        self.full = Deliverable("artifact:final", tuple(DeliveredFinding(
            f.id, f.source_ref, f.summary, f.significance, f.dependency_ids
        ) for f in self.findings))

    def test_research_deliverable_without_release_checklist_passes(self):
        accept_deliverable(self.findings, self.full)

    def test_design_review_without_verdict_or_qa_fields_passes(self):
        accept_deliverable(self.findings, self.full)

    def test_task_requested_criterion_requires_evidence(self):
        with self.assertRaisesRegex(DeliverableIncomplete, "task criterion"):
            accept_deliverable(self.findings, self.full, ("decision-owner",))

    def test_task_requested_criterion_with_evidence_passes(self):
        result = Deliverable(self.full.artifact_ref, self.full.findings,
                             ("decision-owner",), ("artifact:owner-record",))
        accept_deliverable(self.findings, result, ("decision-owner",))

    def test_summary_dropping_material_finding_fails(self):
        with self.assertRaisesRegex(DeliverableIncomplete, "omitted"):
            accept_deliverable(self.findings, Deliverable("artifact:summary",
                                                         self.full.findings[:1]))

    def test_rewriting_evidence_fails(self):
        altered = (DeliveredFinding("A", "invented:ref", "Evidence is incomplete",
                                    "Limits confidence"), self.full.findings[1])
        with self.assertRaisesRegex(DeliverableIncomplete, "source/impact changed"):
            accept_deliverable(self.findings, Deliverable("artifact:altered", altered))

    def test_optional_omission_requires_explicit_reason(self):
        with self.assertRaisesRegex(DeliverableIncomplete, "omitted"):
            accept_deliverable(self.findings, Deliverable("artifact:short",
                                                         self.full.findings[:1]))
        result = Deliverable("artifact:short", self.full.findings[:1],
                             excluded_findings=("B",),
                             exclusion_rationales=("User explicitly excluded architectural tradeoffs",))
        accept_deliverable(self.findings, result)


if __name__ == "__main__":
    unittest.main()
