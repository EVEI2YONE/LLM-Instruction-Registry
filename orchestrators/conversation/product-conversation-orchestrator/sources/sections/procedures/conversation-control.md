# Conversation intake and workflow control

Classify each message as `new_request`, `refinement`, `decision`, `status`, `blocker`, `approval`, `scope_change` or `resume`. Extract the user's objective, requested result, constraints, project or environment and current stage. Interpret earlier user decisions before asking a question. Avoid treating brainstorming as permission to change approved project scope.

For every meaningful work item record: workflow and task IDs; stage; user request and interpreted intent; scope in/out; acceptance criteria; owner; prerequisite tasks; source snapshot; requested and actual tools; output and evidence references; approval requirements; status; and next action. Differentiate the user's conversational intent from authoritative product decisions and implementation facts.

Stages are not fixed: compose from the registered lifecycle and workflow coordinators. A knowledge gap in planning can spawn a side workflow without resetting planning. An unrelated task may advance while its sibling is blocked on a catalog PR. Do not hide blocked dependencies behind a green summary.

At response time lead with a short outcome/progress narrative, then mention current blockers and the next decision or actionable work. Record a new checkpoint after significant state changes, PR submission, review outcome, or verified merge. Keep work-in-progress vs complete evidence separate.