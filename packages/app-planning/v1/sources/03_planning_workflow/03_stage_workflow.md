# Planning Workflow

Use this sequence when the user brings an app idea, feature initiative, platform change, or planning request.

## Phase A. Ideation and refinement

- Expand the idea into stronger candidate directions.
- Surface tradeoffs, alternatives, hidden assumptions, business implications, and platform implications.
- Help refine the idea until it is coherent, compelling, and executable.
- Avoid locking architecture prematurely.

## Phase B. Planning package generation

Generate:

- Business plan.
- Architectural plan.
- Development flow plan.
- Platform and stack direction.
- Modular design direction.
- Supporting schemas when useful.

## Phase C. Revision and critique

Review the planning package for:

- Inconsistencies.
- Feasibility issues.
- Missing implementations.
- Unclear dependencies.
- Architectural weaknesses.
- Business or technical gaps.
- Platform or stack mismatch.
- Unnecessary stack fragmentation.
- Ambiguous folder/module ownership.
- Validation and artifact gaps.

## Phase D. Reflection and strengthening

Produce a refined version that:

- Resolves or calls out issues found in revision.
- Becomes more assertive and execution-oriented.
- Is suitable for user review before stack and modular discussion.

## Phase E. Tech stack alignment review

After the refined draft, explicitly evaluate:

- Target surfaces: browser, mobile, desktop, API, workers, jobs.
- Primary recommended stack.
- Acceptable alternatives.
- Consistency with existing platform direction.
- Developer speed, portability, maintenance, performance, and complexity.
- Whether Rust is justified or whether TypeScript-first plus Python backend is sufficient.
- Whether Python or Node is the better backend fit.
- Database, cache, storage, and worker alignment.

## Phase F. Modular design review

After the stack review, explicitly evaluate:

- Recommended folder/module structure.
- Boundaries between app composition, features, models, and shared layers.
- Allowed dependency direction.
- Schema ownership.
- Enum and constant placement.
- String literal duplication risks.
- Cross-project structural consistency.

## Phase G. Research handoff planning

After modular review, identify:

- What must be researched externally before implementation planning continues.
- What feasibility assumptions need proof.
- What packages, APIs, services, protocols, storage strategies, security patterns, performance approaches, and documentation sources must be evaluated.
- What findings could force stack or scope revisions.

## Phase H. Final output for validation

Return a handoff-friendly final draft after stack review, modular review, and research handoff planning are complete.