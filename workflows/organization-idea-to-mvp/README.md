# Organization-to-MVP: top-down organization workflow
This is a workflow-specific guide distinct from the technical SDLC. Start with organizational intent and opportunity investment, NOT automatically with coding. Reuse approved existing organizational/project artifacts and their ownership before creating anything.

| Stage | Lead and collaborators | Exit gate |
|---|---|---|
| Organizational intent | organizational-strategy-specialist | strategic objectives, constraints, sponsor |
| Portfolio opportunity | organizational-strategy-specialist | candidate investment, comparison and evidence |
| Ideation | business-app-idea; product-delivery-specialist | user problem and value proposition |
| Opportunity validation | product-delivery-specialist; technical-research-project-instructions; AI specialist when needed | research, customer/technical evidence and risk |
| Product definition | app-planning; product-delivery-specialist | thesis, requirements, success criteria |
| MVP scope & investment | idea-to-mvp-orchestrator + accountable human | must-have/later/cut, budget and MVP learning gate approved |
| MVP design | architecture-delivery-specialist; UI/UX design system; AI specialist when needed | reviewed UX, interfaces, architecture and eval contracts |
| MVP build | frontend-engineering-specialist; backend-engineering-specialist; conditional AI specialist | integrated PRs and verified contract/test evidence |
| MVP acceptance | qa-verification-specialist; product-delivery-specialist | product/QA evidence, learn/iterate/stop decision |

Each stage checks current artifact ID/revision, owner, exit evidence and next downstream consumer. Independent work may run concurrently but shared interfaces require approved version. Context moves across threads through durable handoffs, not assumed memory. Existing PRDs/strategy/ADRs win over new duplicated documents; resolve conflicting drafts with owners. Use SDLC for release/operations and reference the same canonical artifacts. Other future workflows add a sibling directory/profile.
