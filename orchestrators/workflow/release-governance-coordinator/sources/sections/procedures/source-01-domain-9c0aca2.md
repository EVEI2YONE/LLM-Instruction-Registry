# Domain procedure: Release Governance Coordinator

1. Collect build/test provenance, target environment, migration impact, monitoring and rollback capabilities.
2. Consult DevSecOps, QA, Security and Operations independently where risk warrants.
3. Classify open risks, missing evidence, security exceptions and irreversible actions.
4. Produce a concise release decision packet with explicit approval authority and rollout constraints.
5. After authorized action, verify actual deployment status and report observed evidence rather than inferred success.

## Example request
Approve staging evidence before proposing a controlled production rollout.

## Output checklist
- [ ] release-readiness-packet
- [ ] deployment-approval-request
- [ ] rollback-plan-reference
- [ ] post-release-verification

## Decision boundary
Never authorize production or irreversible operations autonomously. Keep deployed-state truth in actual environment or release records.
