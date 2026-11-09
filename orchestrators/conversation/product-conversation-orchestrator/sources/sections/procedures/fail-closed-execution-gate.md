# Fail-closed specialist execution gate (mandatory)

This gate must run **before the first substantive assessment, analysis, implementation, or release-readiness claim**, not after work has already begun. The parent may inspect enough metadata to select a specialist, but may not produce a specialist-scoped deliverable before the gate passes.

## Step 0: reconcile runtime capabilities and authorization

Read the active host capability declarations (including user-provided capability files such as `Capabilities.txt`) **before selecting execution mode**. Treat an explicit, applicable statement such as "You are unable to spawn subagents natively" as `native_spawn=verified-unavailable` for this session unless superseded by newer verified host evidence; do **not** claim ignorance or attempt a native child based solely on generic Codex documentation. Check whether any separately configured authenticated gateway is actually callable. Distinguish:
- `native_spawn=verified-available`: real native spawn exposed and allowed.
- `native_spawn=verified-unavailable`: active capability statement or runtime probe says no native spawn.
- `native_spawn=unknown`: no reliable evidence; **do not assume native spawn**.
- `delegation=policy-gated`: host requires explicit authorization not granted; never treat this as proof of tool absence.

Select `NATIVE_CHILD` only if *both* authorized and verified callable. Otherwise choose `SEQUENTIAL_SPECIALIST` if permitted, with a mandatory instruction load. Do not let `unknown` become `available`.

## Step 1: resolve instruction manifest before work

Select registered specialist(s) by live registry lookup pinned to an immutable commit. Fetch selected package `SKILL.md`, its versioned manifest, matching `read_when` sections and their transitive `requires` closure. Verify section file reads and expected hashes when possible. Record a compact receipt:
```json
{
  "execution_mode": "SEQUENTIAL_SPECIALIST",
  "runtime_capability_evidence": "Capabilities.txt: native spawn unavailable",
  "registry_commit": "<actual 40-hex SHA>",
  "package_id": "<registered specialist>",
  "package_version": "<manifest version>",
  "entrypoint_loaded": true,
  "required_sections": ["<section-id>"],
  "loaded_sections": ["<section-id>"],
  "instruction_status": "LOADED",
  "child_handle": null
}
```

**Fail closed** if the registry source is inaccessible, no suitable package is selected for specialist-scoped work, the entrypoint or required section is missing, or mandatory section dependency closure is incomplete. State `BLOCKED_INSTRUCTIONS`; do not proceed with a generic product assessment and call it specialist execution. Unrelated non-specialist work may proceed if transparently separated.

## Step 2: execute only after gate passes

- **Native child:** deliver actual verified instruction text or child-readable pinned refs. Require an observed handle, tool scope and a child instruction receipt before claiming child validation.
- **Sequential specialist:** load the same fetched instructions into the parent's active context and apply them in a bounded `SEQUENTIAL_SPECIALIST` phase. Record the phase, package version, loaded sections, source revision and parent-owned output. Explicitly report no independent child.
- **Gate not satisfied:** do not write an assessment conclusion or readiness verdict. Report blocked source/capability evidence and the precise next action.

## Step 3: require proof of propagation and application

A `LOADED` receipt is a **pre-execution assertion**, not evidence of delivery into the actual execution context or application of instructions. Before accepting a specialist-dependent result, record a second, independently inspectable evidence record: runtime/parent phase ID, exact package/version and registry SHA, mandatory entrypoint and section IDs actually delivered, an observable delivery or context trace reference, the output artifact reference, and task-specific behavioral requirements derived from the specialist instructions. For every required behavioral rule, record a corresponding check and a concrete output/tool evidence reference that supports it.

- For native children: compare the child handle to the provider-issued handle, inspect actual child context/tool trace for instruction delivery, and validate outputs against the selected instructions. A child attestation by itself is insufficient.
- For sequential fallback: inspect the parent execution/context trace showing the actual retrieved content was available at the start of the scoped phase, and map each relevant instruction requirement to the resulting deliverable. Merely naming the specialist, listing section IDs, or producing a generic readiness report does not pass.
- If the host does not expose evidence needed to verify delivery/application, report `PROPAGATION_NOT_VERIFIED` or `APPLICATION_NOT_VERIFIED`; do not turn an unverifiable assertion into a passing specialist claim. A blocked specialist verdict can be reported without inventing evidence.

Use `runtime/instruction_execution_gate.py` `assert_propagation_and_application` to check **structure and consistency** of supplied evidence before reporting a passing completion. This deterministic helper cannot authenticate provider traces or decide whether an artifact substantively satisfies the instructions; the orchestrator/reviewer must actually inspect those references.

## Step 4: validate claims

Before the final response, check both the pre-execution receipt **and** independent delivery/application evidence against the delivered output. `CHILD_COMPLETE` requires a real provider child handle plus attributable artifact and instruction receipt. `SEQUENTIAL_SPECIALIST` requires complete instruction closure and parent-owned evidence. A successful generic code/test run cannot substitute for this instruction gate.

Static regression tests exercise logical and evidence-shape gates, **not** actual model compliance or hosted child execution. See `runtime/instruction_execution_gate.py` and `scripts/test_instruction_execution_gate.py`.
