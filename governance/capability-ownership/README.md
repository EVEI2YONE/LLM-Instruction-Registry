# Capability ownership and authority
The registry defines *reusable* roles and authority limits; the product repository names the real accountable owners and approved artifacts. Workflow-local responsibilities assign capabilities at execution time. Never infer a person's approval from an AI role.

## Responsibility model
- **owner**: exactly one accountable capability for preparing or maintaining an artifact; ownership does not confer permission to approve changes.
- **contributor**: scoped implementation / drafting work.
- **consultant**: supplies alternatives, risks and evidence, without editing owner artifacts by default.
- **reviewer**: independently verifies outputs, cannot be the sole author of the artifact being reviewed.
- **approver**: actual human or external project-defined authority; an AI capability must never impersonate this actor.

## Resolution order
1. Check target product's verified owners, CODEOWNERS, ADR owners and policy; do not override project authority.
2. Load [global policy](ownership-policies.json) and [responsibility model](responsibility-model.json).
3. Resolve the selected workflow's `responsibilities.json`; then use `registry.json` capabilities to pick available package versions.
4. Require pinned context, artifact IDs, evidence, independence for reviews and explicit human approval where necessary.
5. Conflicting owners, missing capability, stale revisions and unresolved disagreement block or escalate. Never silently reassign authority.

[Schema](capability-ownership.schema.json) · [Workflow index](../../workflows/README.md) · [Approval policy](../approval.json)
