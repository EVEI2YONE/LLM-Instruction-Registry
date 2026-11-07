# Revision Notes

## v1 synthesis goals

- Merge the app-planning workflow with the LLM Instructions Orchestrator role.
- Separate reusable behavior into organized files instead of one large instruction prompt.
- Preserve mode commands and required output sections.
- Strengthen stack and modular design enforcement.
- Add explicit self-heal behavior for future corrections.
- Add Antigravity IDE and Claude handoff guidance as separate reusable artifacts.
- Include validation files so future package revisions can check their own completeness.

## Key refinements made

- Converted broad role descriptions into a stable core role file.
- Promoted mode commands into a dedicated mode registry.
- Split workflow, output structure, stack defaults, modularity rules, and handoffs into separate source files.
- Added backend modular structure to complement the frontend structure.
- Added conflict-aware worktree rules for Claude decomposition.
- Added artifact completion and final validation checklists.
- Added self-heal behavior as a first-class instruction file.