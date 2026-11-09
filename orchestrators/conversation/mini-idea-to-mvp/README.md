# Mini conversational Idea-to-MVP workflows (v0.1.0 review candidate)

Four ZIPs: **Idea Discovery & MVP Scope**, **Visual Experience & Prototype Studio**, **MVP Builder & Validation**, and optional **Mini Product Conversation Controller**. They compose existing registry instructions; they do not supersede registered specialist authority.

## Package map

| ZIP | Job | Handoff |
|---|---|---|
| `idea-discovery-mvp-scope_v0.1.0.zip` | Shape an uncertain idea into an opportunity hypothesis and an explicitly approved MVP scope. | Idea → approved MVP scope |
| `visual-experience-prototype-studio_v0.1.0.zip` | Turn approved product scenarios into distinctive design directions, an accessible responsive system and prototype-ready screens. | Scope → selected visual system and prototype/spec |
| `mvp-builder-validation_v0.1.0.zip` | Build one working end-to-end MVP slice, validate its behavior and compare implementation against approved visuals. | Approved design → tested runnable MVP |
| `mini-product-conversation-controller_v0.1.0.zip` | Route one conversation among discovery, visual studio and builder while tracking decisions and verified handoffs. | Conversation routing and ledger |

## Workflow

1. Use controller to route conversation; maintain a small decision/evidence ledger.
2. Discovery explores three options, converges on a small end-to-end MVP and obtains scope approval.
3. Visual studio proposes differentiated aesthetics, collects a direction choice, specifies tokens, responsive screens and accessibility requirements.
4. Builder implements vertical slices, runs actual tests, checks visual fidelity and presents release evidence.
5. Human approval is needed for investment, merges, production deployments or irreversible changes.

## Specialists and sources

Read [SOURCE_CROSSWALK.md](SOURCE_CROSSWALK.md) for every source workflow/specialist, version and pinned entrypoint. Snapshot: `0aaf031e693c7e280a8b3bd4be86cb531e167d90`. Upstream registry status 'available' is NOT formal approval. These new packages are review candidates; model behavior, hosting compatibility and actual delegated agent execution are NOT_RUN.

## Installation and limitations

Extract ZIPs, load applicable SKILL.md and workflow.md, and fetch the pinned source specialist instructions (including manifest dependency closure) before executing any specialist. Do not assume a ZIP supplies a tool, a subagent runner or durable background state. If source instructions are inaccessible, report BLOCKED_INSTRUCTIONS. Without real child runners, specialist passes must be sequential. No approval or deployment is claimed by packaging alone.
