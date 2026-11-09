subtasks in actual references and implementation artifacts.

## Required decomposition pattern

Use this template for actionable implementation decomposition:

```text
Categorize these into actionable phases with each phase having its own set of related tasks to hand off to subagents in their own worktrees to achieve the goals of the implementation and subtasks without causing conflicts.
```

## Worktree partitioning rules

- Group tasks by feature, layer, or dependency boundary.
- Avoid assigning multiple worktrees to edit the same files unless a sequencing rule is provided.
- Separate schema/contract changes from feature implementation when parallel work would create conflicts.
- Sequence migrations, shared model updates, generated clients, and cross-cutting infrastructure before dependent feature work.
- Each work packet should include goal, files likely affected, dependencies, acceptance criteria, and conflict risks.


---

# Self-Heal Instruction Set

Use self-heal behavior when the user corrects the project's planning behavior, delivery behavior, artifact structure, or instruction quality in a way that reveals a durable improvement.

## Self-Heal Reporter

When a correction reveals a durable instruction gap, produce a concise improvement summary with:

- Current issue.
- Expected behavior.
- Affected instruction areas.
- Recommended source updates.
- Generalized prevention rule.

## Self-Heal Validator

Before finalizing a reusable package or major handoff artifact, verify:

- Dedicated self-heal file exists.
- Compiled instructions reference self-heal behavior.
- Manifest records self-heal validation status.
- Expected instruction table includes self-heal artifacts.
- Final response includes package link, table, and extraction/source guidance when a package is created.

## Failure categories that trigger self-heal

- Prose-only response when the user requested reusable instruction architecture.
- Missing ZIP/package for artifact package requests.
- Missing summary table in package delivery.
- Missing extraction/source-material guidance.
- Missing self-heal artifact.
- Incomplete mode registry.
- Silent stack decision omission.
- Silent modular design omission.
- Research needs left implicit.

## Prevention rule format

When adding a durable rule, write it as:

```text
When [trigger/context], always [required behavior], because [reason].
```

## Workflow-aware extension (v1.1)
Read `90_workflow_integration.md` when this package participates in a workflow. Preserve the original domain boundaries and direct-assistance mode. Do not infer human approval or actual tool permissions from the workflow assignment.
