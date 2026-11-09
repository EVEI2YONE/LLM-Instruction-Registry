# Mandatory instruction propagation: native children and sequential fallback

## Resolve the same instructions for either route

1. Pin an immutable registry commit and project revision. Identify the registered specialist's ID/version, status/approval evidence and canonical source path.
2. Retrieve its exact `SKILL.md` and applicable manifest sections according to `read_when`, including transitive `requires` dependencies. Verify content SHA-256 against manifest when possible; record the section IDs, digests and any unverifiable integrity separately. A role label alone does not load an instruction set.
3. Compose a least-privilege task envelope: objective, scope, relevant artifact/context refs, project/registry SHAs, package/version, instruction content or verified immutable refs, tool permissions, acceptance criteria, output ownership and approval gates.

## Native child execution (when both authorized and exposed)

4. Proactively invoke an actual child tool for beneficial specialist scopes. **Explicitly deliver the resolved mandatory instruction bytes to the child**, or immutable refs the child demonstrably can read; never assume that loading instructions in the parent makes them appear in children.
5. Capture the provider-issued child handle, its tool/permission scope and loaded instruction section provenance. Ask the child to report consumed package/version, registry SHA and section IDs/hashes, along with grounded artifact evidence. Independently compare the claim to its task payload and tool trace.
6. Poll/collect only through supported runtime operations and reconcile before presenting an independent specialist finding. Unsupported cancel, poll or resume capabilities must be reported as unavailable, not simulated.

## Parent-run sequential specialist execution

4. When no native child is callable, higher-priority policy forbids spawning, or an actual spawn safely failed, **load the exact same resolved specialist entrypoint and applicable sections in the parent's current working context**.
5. Open a distinct `SEQUENTIAL_SPECIALIST` work phase with the package ID/version, pinned registry revision, loaded section IDs and scoped question. Follow the specialist's applicable instructions subject to higher-priority policies; produce a grounded deliverable, then close the phase.
6. For multiple specialist roles, use separate attributed parent-run phases and reconcile disagreements. Disclose that no independent child executed or reviewed the work.

## Verifying instruction application

For each selected specialist, derive explicit observable task requirements from the *actual loaded instruction content*. Record what sections were delivered to the executing context and which output/artifact evidence demonstrates each applicable requirement. A self-reported instruction receipt, role label, or well-written generic assessment is not enough. If the runtime does not expose a trustworthy delivery trace, mark propagation unverified; if the output has no checkable rule-level evidence, mark application unverified. Require an actual child execution trace for independent-agent claims; for parent sequential phases, disclose the parent as the executor.

## Failure classifications

- `POLICY_GATED_NOT_ATTEMPTED`: higher-priority host policy requires direct permission; report this as an authorization gate, **not** a runtime deficiency.
- `TOOL_UNAVAILABLE`: delegation is permitted but no callable child API is exposed. Follow with `SEQUENTIAL_SPECIALIST` only after loading actual specialist instructions.
- `SPAWN_FAILED`: attempted child execution failed; preserve provider error, avoid duplicate side effects and choose safe fallback only where applicable.
- `BLOCKED_INSTRUCTIONS`: mandatory specialist instructions cannot be retrieved or verified. Do not claim to have followed specialist instructions; unrelated or transparently generic work can continue.
- `CHILD_COMPLETE` is valid only with an observed provider handle, verified instruction reception and attributable output.

This Skill requests proactive delegation for appropriate tasks **without requiring the user to explicitly say "spawn"** if the active instructions and tool scopes allow it. It cannot override a higher-priority explicit-consent policy, manufacture execution tools, approve merges or promote parent-only work into independent specialist evidence.
