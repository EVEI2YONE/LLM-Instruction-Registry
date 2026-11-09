# Registry lookup, proactive delegation and bounded fallback

Default to delegating bounded specialist work when independent expertise, reviews or parallel tasks would improve the result, **if** a real child interface is exposed and applicable policies permit it. This Skill expressly requests such delegation; do not require the user to type "spawn subagents" unless a higher-priority policy specifically requires separate user permission. Do not spawn for trivial work or unneeded overhead.

**Resolve first, regardless of execution mode.** Pin the live registry commit, match registered capabilities and retrieve the selected specialist's exact entrypoint, applicable manifest sections and transitive `requires` dependencies. Follow `sections/procedures/instruction-propagation.md` to deliver verified instruction content or child-accessible immutable references. Parent-only retrieval does not prove child inheritance.

**Check two separate gates.** Authorization: host rules, user permissions, tool scopes and action approval. Capability: exposed runtime tool implementing the logical `runtime/ADAPTER_CONTRACT.md` interface. Record one of:
- `POLICY_GATED_NOT_ATTEMPTED`: higher-priority policy requires direct authorization not given; do not infer tool absence.
- `TOOL_UNAVAILABLE`: authorized delegation has no callable native/gateway child tool.
- `SPAWN_FAILED`: attempted authorized child invocation failed; retain evidence.
- `CHILD_RUNNING` / `CHILD_COMPLETE`: real provider handle observed.
- `SEQUENTIAL_SPECIALIST`: no child spawned, but exact pinned specialist instructions were loaded and applied in a bounded parent execution.
- `BLOCKED_INSTRUCTIONS`: mandatory specialist source missing, inaccessible or unverifiable.

**Native child:** Construct `schemas/subagent-task.schema.json` task inputs: run/task ID, package/version, objective, context ref, idempotency key, required capabilities, permission scopes, limits, project and registry revisions, instruction section IDs/hashes, expected output and approval gates. Send the verified instruction text or accessible immutable refs *into the child*, explicitly. Capture provider child ID and verify the child received the required sections and used them. Never assume inheritance.

**Sequential specialist:** If spawn is disallowed, unavailable, or safely failed, *do not discard specialist behavior*. Load the same applicable instructions in the active parent context; execute one scoped phase labeled `SEQUENTIAL_SPECIALIST` with package/version, pinned registry SHA and loaded sections. Apply the specialist procedures subject to higher-priority controls. Cite project evidence and clearly report this was not an independent specialist review. Separate multiple specialist perspectives into bounded phases.

The parent validates all child/parent artifacts, ownership and source revisions. It cannot self-approve merges, actions requiring explicit approval, or irreversible changes. Do not equate parallel GitHub reads, roleplay or sequential phases with spawned children.
