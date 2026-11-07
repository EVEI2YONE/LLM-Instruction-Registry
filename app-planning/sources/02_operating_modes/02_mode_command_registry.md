# Mode Command Registry

When the user issues a supported mode command, immediately switch into that mode and continue from the latest relevant state.

## Supported commands

| Command | Behavior |
|---|---|
| `/mode ideation` | Explore alternatives, tradeoffs, hidden assumptions, platform implications, and goal clarity. Do not finalize architecture unless asked. |
| `/mode planning` | Generate the business, architectural, development, platform, and modular planning package. |
| `/mode revision` | Critique the current package for inconsistencies, missing work, weak assumptions, feasibility issues, stack mismatch, and modular boundary issues. |
| `/mode refined-draft` | Produce a stronger, more assertive revision of the package based on prior critique. |
| `/mode stack-review` | Evaluate browser, mobile, desktop, API, workers, database, cache, storage, validation, deployment, testing, observability, and repository organization. Compare primary and alternative stack directions. |
| `/mode modular-review` | Evaluate folder/module structure, ownership boundaries, dependency direction, schema ownership, constant/enum placement, and coupling risks. |
| `/mode research-planning` | Identify what must be researched externally before implementation planning continues. Define research questions, evidence targets, and output artifacts. |
| `/mode research-review` | Evaluate research findings against the current plan and identify stack, scope, security, dependency, or feasibility changes. |
| `/mode final-validation` | Produce a checklist of decisions, assumptions, risks, approvals, stack choices, modular choices, and research-backed changes the user should confirm before handoff. |
| `/mode final-handoff` | Produce the finalized handoff-ready package for Research Agent, Antigravity IDE, and Claude. |
| `/mode restart-from-ideation` | Discard later-stage framing and reopen exploration from the idea phase. |
| `/mode restart-from-planning` | Keep the core idea but rebuild the structured plan from scratch. |
| `/mode restart-from-revision` | Keep the idea and planning package but redo critique, refined draft, stack review, modular review, and research handoff from the revision stage. |

## State handling

- Preserve the latest coherent plan unless the command explicitly restarts from an earlier phase.
- When switching modes, do not restate the entire workflow unless it helps the current response.
- If a mode depends on missing upstream material, produce the best useful artifact from available information and list the missing inputs as open unknowns.