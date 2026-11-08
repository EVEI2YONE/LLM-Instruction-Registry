# Lifecycle package inventory (new v1 instruction sets)
This catalog lists authored additions, not a claim that external runtimes expose the required tools.

| Package | Kind | Canonical path |
|---|---|---|
| Product Lifecycle Orchestrator | primary-orchestrator | `orchestrators/primary/product-lifecycle-orchestrator/` |
| Specialist Consultation Coordinator | workflow-orchestrator | `orchestrators/workflow/specialist-consultation-coordinator/` |
| Engineering Review Coordinator | workflow-orchestrator | `orchestrators/workflow/engineering-review-coordinator/` |
| Release Governance Coordinator | workflow-orchestrator | `orchestrators/workflow/release-governance-coordinator/` |
| Technical Product Manager | specialist | `specialists/product/technical-product-manager/` |
| Backlog and Story Refinement Specialist | specialist | `specialists/product/backlog-story-refinement-specialist/` |
| Business Feasibility Analyst | specialist | `specialists/business/business-feasibility-analyst/` |
| Market and Competitive Research Specialist | specialist | `specialists/business/market-competitive-research-specialist/` |
| UX Research and User Journey Specialist | specialist | `specialists/design/ux-research-journey-specialist/` |
| UI/UX Product Designer | specialist | `specialists/design/ui-ux-product-designer/` |
| Accessibility and Usability Reviewer | specialist | `specialists/design/accessibility-usability-reviewer/` |
| Solution and Cloud Resource Architect | specialist | `specialists/architecture/solution-cloud-resource-architect/` |
| Data Architecture Specialist | specialist | `specialists/architecture/data-architecture-specialist/` |
| Security Architecture Specialist | specialist | `specialists/architecture/security-architecture-specialist/` |
| API and Integration Design Specialist | specialist | `specialists/architecture/api-integration-design-specialist/` |
| Database and Migration Specialist | specialist | `specialists/engineering/database-migration-specialist/` |
| Integration Engineering Specialist | specialist | `specialists/engineering/integration-engineering-specialist/` |
| Pragmatic PR Reviewer | specialist | `specialists/quality/pragmatic-pr-reviewer/` |
| Test Automation Specialist | specialist | `specialists/quality/test-automation-specialist/` |
| Security and Compliance Reviewer | specialist | `specialists/security/security-compliance-reviewer/` |
| Product Analytics and Outcome Specialist | specialist | `specialists/product/product-analytics-specialist/` |
| Incident and Root Cause Analyst | specialist | `specialists/operations/incident-root-cause-analyst/` |
| Knowledge and Context Steward | specialist | `specialists/knowledge/knowledge-context-steward/` |
| Decision and Traceability Auditor | specialist | `specialists/quality/decision-traceability-auditor/` |

All packages contain `SKILL.md`, compiled guidance, domain-specific playbook, context/authority module, self-heal, manifest, sources README and their own archive. [Registry](../registry.json) indexes capability names.

Coordinate based on [capability ownership](../governance/capability-ownership/README.md); for authoritative product policies use target project governance. The primary orchestrator is not the Meta-LLM progenitor.

## Remaining existing packages — workflow-ready revisions

These packages preserve their original primary purpose; optional workflow integration is additive. The historical ZIP archives remain accessible.

| Package | Version change | Main update |
|---|---|---|
| ai-knowledge-atlas | v2.1 → updated | Optional workflow integration, pinned context, ownership and self-heal |
| ui-ux-design-system-architect | v1.1 → v1.2 | Design-system ownership, accessibility review and workflow-aware coordination |
| app-planning | v1 → updated | Optional workflow integration, pinned context, ownership and self-heal |
| backend-architecture-consultant | v1 → updated | Optional workflow integration, pinned context, ownership and self-heal |
| business-app-idea | v1 → updated | Optional workflow integration, pinned context, ownership and self-heal |
| coding-partner-mentor-teacher | v1 → updated | Optional workflow integration, pinned context, ownership and self-heal |
| feature-extension-planning-council | v1 → updated | Optional workflow integration, pinned context, ownership and self-heal |
| general-purpose-chatgpt-conversations | v2 → updated | Optional workflow integration, pinned context, ownership and self-heal |
| psychology-advice-research | v1 → updated | Optional workflow integration, pinned context, ownership and self-heal |
| solid-visual-architecture | v1 → updated | Optional workflow integration, pinned context, ownership and self-heal |
| technical-research-project-instructions | v2 → updated | Optional workflow integration, pinned context, ownership and self-heal |

**Provenance note:** Business App Idea and SOLID Visual Architecture previously exposed only a source README in their browsable source tree. Their new versioned packages include the historical ZIP as a nested, byte-preserved legacy artifact alongside newly browsable entrypoint, compiled, self-heal and workflow modules. Other packages have their full browsable source tree included directly in the new ZIP.
