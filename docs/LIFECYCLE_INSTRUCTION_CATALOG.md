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
