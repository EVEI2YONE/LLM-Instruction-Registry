# Meta-LLM-first instruction generation architecture

Status: **foundation policy, review required**. This is an authoring and migration contract, not an assertion that any existing specialist has been migrated, installed, or behaviorally tested.

## Authoring entrypoint

Use the [Meta-LLM Orchestrator](../orchestrators/meta/meta-llm-orchestrator/README.md) whenever creating, upgrading, repairing, or adapting specialist instructions for a target workspace. The [Product Lifecycle Orchestrator](../orchestrators/primary/product-lifecycle-orchestrator/README.md) remains responsible for routing work to existing agents, **not** instruction generation.

**Do not inspect and copy a similar published ZIP to author another specialist.** ZIPs are immutable historical release artifacts. Find candidates through [registry.json](../registry.json), inspect verified canonical browsable sources and manifests as needed, and retain provenance. This does not prohibit installing or directly using an existing registered specialist without regenerating it.

## Mandatory process for generation or revision

1. **Discover and pin.** Refresh the verified registry channel, resolve one immutable commit, and inspect only likely candidate packages. Evaluate function, boundaries, output ownership, version, source accessibility, and formal approval evidence. The presence of `status: available` is not independent formal approval, and missing access is NOT_VERIFIED rather than absence.
2. **Make a decision.** Record one of `REUSE_UNCHANGED`, `UPGRADE`, `CREATE_NEW`, or `BLOCKED`. Functional adequacy means reuse. `ADAPT_EXISTING` is a target packaging action, not a new specialist version. Evidence of a gap or explicit normative change is necessary for an upgrade; do not create duplicate package IDs.
3. **Identify the user's intended generated-agent execution environment.** The environment hosting the **Meta-LLM generator's own source files** is not necessarily the one using the **generated agent instructions**. If the target has not already been established, ask one concise destination question, for example: "Where will you use the generated agent instructions: a ChatGPT Project or Skill, another hosted assistant, a local coding agent, or an API application?" Reuse already stated answers; never ask redundantly.
4. **Resolve capabilities independently.** Record `execution_destination`, `source_loading_mode` (`injected`, `verified_lookup`, `hybrid` or `unknown`), `registry_operation`, `registry_write_authority`, `approval_source`, and target instruction size, file/tool/network, memory, child-agent, artifact and approval capabilities. Do not infer any from provider branding.
5. **Create or adapt one canonical tree.** Package-specific non-negotiables go into an always-loaded entrypoint; conditional behavior belongs to indexed sections with `read_when` and `requires`. Keep approved central governance referenced rather than duplicating it. Render target distributions from canonical source rather than independently maintaining platform-specific authorities.
6. **Tailor one delivery.** For injected prompt-only hosts assemble a self-contained bounded payload; for lookup-capable hosts include verified manifest-driven retrieval or manual dependency-closed reads; for native tools or child execution use only demonstrated install/invocation interfaces and approvals. When host capability or instruction limits are unknown, label a review candidate rather than install-ready.
7. **Validate independently.** Pin the canonical schema to the selected registry commit; check source and ZIP bytes, manifests, dependency closure, rule coverage and migration traceability. Report approval, schema, source inventory, instruction limits, packaging, installation, activation and behavioral evaluation as separate PASS/FAIL/NOT_RUN/BLOCKED outcomes. Never treat package creation as execution or owner approval.

## Existing specialist compatibility, before migration

**Do not change existing specialist sources, registry entries, historical ZIPs, package identities or released version references in this foundation change.** Registered legacy packages remain independently usable. A user who asks to *use* an existing specialist does not need the Meta-LLM generator; a user who asks to *create, modify, regenerate or retarget* its instructions does.

Future migrations require their own scope and reviewed PR(s). Inventory every registered package, map its normative source requirements and output contracts to the next canonical version, preserve old ZIP blobs, resolve owners/approval boundaries, validate all generated variants, and keep an evidence and rollback ledger. See [lookup-first rebuild plan](LOOKUP_FIRST_REBUILD_PLAN.md), [publishing rules](PUBLISHING.md), [workspace adapters](WORKSPACE_ADAPTERS.md), and [migration inventory](../migration/inventory.json).

## Regression acceptance scenarios

| Input | Required outcome |
|---|---|
| "Create a frontend specialist" without a destination | Registry-first discovery; avoid speculative version creation; ask one destination question before tailored output |
| Destination already established | Do not ask again; verify capabilities and tailor that target's instruction package |
| Existing specialist is functionally sufficient but needs hosted injection | `REUSE_UNCHANGED + ADAPT_EXISTING`; no canonical version increment or registry write |
| User just wants to use an existing registered specialist | Use the selected version directly if authorized; no regeneration |
| Similar ZIP proposed as an authoring template | Redirect to Meta-LLM, canonical source discovery and reuse decision |
| Registry or approval sources inaccessible | Mark NOT_VERIFIED/BLOCKED; do not fabricate approval or missing candidates |
| Legacy package migration is not approved | Preserve previous sources, ZIPs and registry without modification |
