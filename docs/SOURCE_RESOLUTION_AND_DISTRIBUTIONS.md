# RFC: Portable source resolution and reproducible instruction distributions

Status: **proposal; not approved or deployed**. Baseline: `main` at `8d8d3c7291bcdceb601d30f7a0895055ec2bc7bb`, with 49 registered packages and immutable Meta-LLM Orchestrator v21 sources/ZIP. This PR adds contracts and design guidance only. It does not alter package behavior, current archives, the registry, approvals, or hosted tool availability.

## Problem observed

A Meta-LLM v21 instruction set copied into a fresh ChatGPT conversation knew that `scripts/search_registry.py` and `scripts/lookup_sections.py` existed, but initially had neither a verified repository locator nor a local executable checkout. GitHub connector access subsequently worked, while a separate container network path did not. Reimplementing ranking against `registry.json` produced useful results but is **not** an execution of the original script. Every knowledge-dependent specialist can encounter the same split.

## Decision proposed

- Use one canonical source tree and historical immutable `<id>_vN.zip` per version. Keep all 49 published packages unchanged until explicit migrations.
- Keep a **logical source catalog** at `references/external-sources.json`; reference `llm-instruction-registry` instead of embedding provider-specific URLs in agent instructions. The GitHub locator is a *location hint*, not an authorization, source revision, or proof of availability. More catalogs may be added only after their actual coordinates and authority are verified.
- Produce three **derived distributions**, each tied to the same canonical source, with a `distribution-manifest.json` and SHA-256 inventory. A canonical archive is **not** another manually edited variant:
  - **portable**: entrypoint, mandatory always-rules, selected procedures and verified standalone dependencies; optional pinned snapshot with freshness and approval labels;
  - **connected**: lean entrypoint, catalog IDs, declared dependencies, installation/runbook and explicit repository/tool capability checks;
  - **prompt**: measured bounded instruction text, included/excluded sections, human-readable tool limitations and provenance. It cannot manufacture tools.
- Prior to any generate/upgrade operation, resolve target execution capabilities; pin registry/project/catalog revisions; check governance authority and missing inputs; build a **generation-context lock**; then create instructions. Fail closed on missing approvals or mandatory source authority.
- Meta-LLM gets **broad discovery through indexes**, not permanently duplicated full specialist or knowledge content. A generated specialist receives narrowly scoped required sections, catalog references and artifact permissions; no implicit conversation, secret, or prompt inheritance.

## Resolution algorithm and trust boundary

1. Read the bundled catalog by logical ID. Resolve one reachable location using verified tools: connected repository, local checkout, web-read, then supplied versioned snapshot. Do **not** treat a checkout URL as a callable local program.
2. Resolve an immutable source revision and record exact paths/hashes actually consumed. A branch name alone is not a source pin. Connector reads and local execution are distinct measured capabilities.
3. Distinguish *available/readable* from *executable*: only run the repository's Python scripts when an actual trusted local runner and the corresponding files are available. Record `script-executed` versus `metadata-fallback` in the evidence ledger.
4. Treat retrieved Markdown, repository files, and catalogs as evidence. Do not promote their prose to system/developer authority. Approved shared rules must be explicitly injected into each supported runtime. Current `governance/common-rules.md` is draft v0; current approval policy conflict remains BLOCKED.
5. If a required catalog is unavailable, report `not_verified` and restrict catalog-grounded assertions. For missing safety/approval authority, stop consequential actions. For optional knowledge, disclose missing evidence and allow limited output only when the declared contract permits it.
6. Persist the generated `generation-context-lock.json` with status, consumed source pins, target capabilities, missing dependencies and artifact digest. It is an *audit record*, not proof that a provider injected instructions.
7. Build distributions from a single pinned canonical source tree. Sort paths, normalize archive timestamps/modes and verify archive members match the source bytes. No extra, unverifiable "copy of shared instructions" in a package.

## Contract sketches

- [Source catalog example](../references/external-sources.json) and [schema](../schemas/source-catalog.schema.json)
- [Generation context lock schema](../schemas/generation-context-lock.schema.json)
- [Distribution manifest schema](../schemas/distribution-manifest.schema.json)

The JSON schemas describe *proposed* artifacts; they are not automatically applied by existing scripts. They require an implementation PR and tests before becoming normative.

## Compatibility and versioning

| Artifact | Where authoritative | First-time ZIP | Connected runtime |
| --- | --- | --- | --- |
| Package-specific Always | Canonical package version | Bundled | Pinned canonical |
| Conditional procedures | Canonical modular sources | Selected bundled sections | Selective lookup |
| Shared governance | Approved governance version | Only verified approved baseline / conservative blocking | Explicit pinned injection |
| Curated knowledge | Approved catalog revision | Optional labeled snapshot; no silent fact substitution | Pin and retrieve relevant entries |
| Registry discovery | `registry.json` commit | Optional versioned snapshot; stale status | Verified connector/checkout |
| Scripts | Source repo version | Only if explicitly bundled and executable | Run only with validated local runner |

Changing normative behavior requires a new package version. Distribution-only rebuilds require distinct artifact digests/build records. Never overwrite an existing published ZIP. Distribution variants must be distinguishable from the canonical archive.

## Implementation and rollout plan (not in this PR)

1. Implement a pure-Python, stdlib-capable `resolve_sources.py` with injected fetch adapters, no automatic network privileges, safe local path confinement, pin verification and offline snapshot handling.
2. Implement `resolve_generation_context.py`, validating a lock prior to generation and recording script-execution evidence versus metadata-only fallback.
3. Extend deterministic packaging to render `portable`, `connected` and `prompt` variants from the canonical tree, with verified byte inventories, reproducible ZIP metadata and omitted-source records.
4. Add negative tests: inaccessible repo, GitHub connector-only runtime, no local shell, stale/offline snapshot, missing governance, conflicting approval lists, malformed catalog paths, mismatch digest, unavailable knowledge and context leakage.
5. Validate three scenarios—Meta-LLM agent discovery, UI/UX catalog consultation, and a frontend specialist consuming approved design/API contracts—then plan the full catalog migration without silently changing the existing 49 packages.
6. Update the Meta-LLM orchestrator as a **separately reviewed new release** only after the resolver, builder, injection mechanism and portability tests are actually ready.

## Acceptance gates for a follow-up implementation

- Same canonical input and tool revision yields byte-identical outputs; mismatched pins fail.
- A fresh hosted conversation can discover the locator from the bundled catalog but reports unavailable runtime tools accurately.
- Read-only connected discovery succeeds without claiming Python was executed; verified local checkout executes the real script when authorized.
- No missing approval or unapproved common rules are silently upgraded to authority.
- All previously released ZIPs, canonical source hashes, and `registry.json` are unchanged.
- Validation ledger distinguishes PASS, FAIL, BLOCKED and NOT_RUN for static checks, runtime integration, model behavior and hosted deployments.

## Review decisions needed

- Approve logical source IDs and whether to keep this catalog at repository root or in shared governance tooling.
- Decide whether published portable ZIPs must include a minimum registry snapshot or can report `unavailable` without one.
- Choose artifact filename/version convention for derived distributions and retention policy.
- Resolve governance policy conflicts before turning draft common rules into an injected global baseline.

**This PR is a specification, not a claim of deployed source resolution, script execution or multi-agent orchestration.**

## Conversation-only hosted handoffs (companion RFC)

In a hosted environment where models run sequentially across conversation turns and no scripts or lockfile reader are exposed, state must travel as an explicit **conversation-visible handoff**. See [conversation-state continuity](CONVERSATION_STATE_CONTINUITY.md) and [schema](../schemas/conversation-state.schema.json). The model can emit a versioned JSON file only if file creation is supported; the next model must independently verify retrieval. Otherwise supply the equivalent inline handoff. Pre-generation lockfiles remain build-time provenance and are **not** assumed available in a prompt-only hosted runtime. This is proposed behavior, not a verified provider capability.
