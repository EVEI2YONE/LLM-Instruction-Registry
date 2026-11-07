# Claude Handoff Guidance

Claude receives the validated architecture, implementation artifacts, task artifacts, and research findings after Antigravity IDE has reconciled them with the actual project context.

## Claude responsibilities

- Break implementation work into smaller actionable tasks.
- Partition work into subagent/worktree-friendly execution packets.
- Preserve approved stack and modular boundaries unless explicitly told to revise them.
- Use research artifacts to avoid redundant discovery work.
- Ground integration subtasks in actual references and implementation artifacts.

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