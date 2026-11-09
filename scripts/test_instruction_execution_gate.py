"""Regression checks for fail-closed orchestration preflight and false claims."""
import unittest
from runtime.instruction_execution_gate import (
    ExecutionReceipt, InstructionEvidence, GateError, choose_mode, require_ready, assert_valid_claim, assert_propagation_and_application
)

COMMIT = "7d68443e5d8e3a02c9f91439fd82687d38ca8af1"


def receipt(**kwargs):
    base = dict(
        native_spawn="verified-unavailable", delegation_authorized=True,
        mode="SEQUENTIAL_SPECIALIST", registry_commit=COMMIT,
        package_id="frontend-engineering-specialist", package_version="v1.2",
        entrypoint_loaded=True, required_sections=("core", "quality"),
        loaded_sections=("core", "quality"), instruction_status="LOADED",
    )
    base.update(kwargs)
    return ExecutionReceipt(**base)


class ExecutionGateTests(unittest.TestCase):
    def test_explicit_capability_forces_sequential_even_if_delegation_authorized(self):
        self.assertEqual("SEQUENTIAL_SPECIALIST", choose_mode("verified-unavailable", True))
        require_ready(receipt())
        assert_valid_claim(receipt(), "SEQUENTIAL_SPECIALIST")

    def test_unknown_native_capability_does_not_imply_spawn(self):
        self.assertEqual("SEQUENTIAL_SPECIALIST", choose_mode("unknown", True))
        with self.assertRaisesRegex(GateError, "mode contradicts"):
            require_ready(receipt(native_spawn="unknown", mode="NATIVE_CHILD"))

    def test_missing_specialist_entrypoint_fails_closed(self):
        with self.assertRaisesRegex(GateError, "BLOCKED_INSTRUCTIONS"):
            require_ready(receipt(entrypoint_loaded=False))

    def test_missing_required_section_fails_closed(self):
        with self.assertRaisesRegex(GateError, "mandatory section"):
            require_ready(receipt(loaded_sections=("core",)))

    def test_unverified_instruction_status_fails_closed(self):
        with self.assertRaisesRegex(GateError, "BLOCKED_INSTRUCTIONS"):
            require_ready(receipt(instruction_status="MISSING"))

    def test_false_child_completion_rejected(self):
        with self.assertRaisesRegex(GateError, "false child"):
            assert_valid_claim(receipt(), "CHILD_COMPLETE")

    def test_missing_child_propagation_receipt_rejected(self):
        with self.assertRaisesRegex(GateError, "provider handle"):
            assert_valid_claim(receipt(
                native_spawn="verified-available", mode="NATIVE_CHILD",
                child_handle="provider:123", output_owner="child",
                child_instruction_receipt=False
            ), "CHILD_COMPLETE")

    def test_real_child_requires_handle_and_verified_receipt(self):
        r = receipt(native_spawn="verified-available", mode="NATIVE_CHILD",
                    child_handle="provider:123", output_owner="child",
                    child_instruction_receipt=True)
        assert_valid_claim(r, "CHILD_COMPLETE")

    def test_policy_gate_does_not_claim_unavailable_tool(self):
        self.assertEqual("SEQUENTIAL_SPECIALIST", choose_mode("verified-available", False))
        require_ready(receipt(native_spawn="verified-available", delegation_authorized=False))

    def test_sequential_cannot_sneak_child_handle(self):
        with self.assertRaisesRegex(GateError, "cannot claim child"):
            require_ready(receipt(child_handle="fabricated"))


if __name__ == "__main__":
    unittest.main()

    
class PropagationAndApplicationTests(unittest.TestCase):
    def evidence(self, **overrides):
        base = dict(
            execution_id="parent:frontend-engineering-specialist",
            executor="parent",
            package_id="frontend-engineering-specialist",
            package_version="v1.2",
            registry_commit=COMMIT,
            delivered_section_ids=("core", "quality"),
            delivered_entrypoint=True,
            delivery_ref="trace:parent-loaded-content",
            artifact_ref="artifact:readiness-report",
            required_rule_ids=("verify-release-gates", "cite-repo-evidence"),
            checked_rule_ids=("verify-release-gates", "cite-repo-evidence"),
            rule_evidence_refs=("artifact:readiness-report#release-gates",
                                "artifact:readiness-report#file-references"),
        )
        base.update(overrides)
        return InstructionEvidence(**base)

    def test_sequential_delivery_and_application_accepts_complete_trace(self):
        assert_propagation_and_application(receipt(), "SEQUENTIAL_SPECIALIST",
                                           self.evidence())

    def test_sequential_missing_instruction_delivery_fails(self):
        with self.assertRaisesRegex(GateError, "missing required section delivery"):
            assert_propagation_and_application(receipt(), "SEQUENTIAL_SPECIALIST",
                                               self.evidence(delivered_section_ids=("core",)))

    def test_loaded_receipt_alone_not_enough(self):
        with self.assertRaisesRegex(GateError, "missing observable"):
            assert_propagation_and_application(receipt(), "SEQUENTIAL_SPECIALIST",
                                               self.evidence(delivery_ref=""))

    def test_sequential_generic_assessment_without_rule_checks_fails(self):
        with self.assertRaisesRegex(GateError, "mandatory acceptance rules unchecked"):
            assert_propagation_and_application(receipt(), "SEQUENTIAL_SPECIALIST",
                                               self.evidence(checked_rule_ids=("verify-release-gates",),
                                                             rule_evidence_refs=("artifact:readiness-report#release-gates",)))

    def test_rule_check_without_evidence_fails(self):
        with self.assertRaisesRegex(GateError, "empty criterion-specific evidence"):
            assert_propagation_and_application(receipt(), "SEQUENTIAL_SPECIALIST",
                                               self.evidence(rule_evidence_refs=("artifact:a", "")))

    def test_wrong_package_or_commit_fails(self):
        with self.assertRaisesRegex(GateError, "provenance mismatch"):
            assert_propagation_and_application(receipt(), "SEQUENTIAL_SPECIALIST",
                                               self.evidence(registry_commit="0"*40))

    def test_false_sequential_child_attribution_fails(self):
        with self.assertRaisesRegex(GateError, "not attributable to parent"):
            assert_propagation_and_application(receipt(), "SEQUENTIAL_SPECIALIST",
                                               self.evidence(executor="child"))

    def test_child_propagation_requires_matching_real_handle(self):
        child = receipt(native_spawn="verified-available", mode="NATIVE_CHILD",
                        child_handle="provider:actual", child_instruction_receipt=True,
                        output_owner="child")
        with self.assertRaisesRegex(GateError, "wrong child execution handle"):
            assert_propagation_and_application(child, "CHILD_COMPLETE",
                                               self.evidence(executor="child", execution_id="provider:wrong"))
        assert_propagation_and_application(child, "CHILD_COMPLETE",
                                           self.evidence(executor="child", execution_id="provider:actual"))

    def test_missing_entrypoint_delivery_fails(self):
        with self.assertRaisesRegex(GateError, "missing entrypoint"):
            assert_propagation_and_application(receipt(), "SEQUENTIAL_SPECIALIST",
                                               self.evidence(delivered_entrypoint=False))
