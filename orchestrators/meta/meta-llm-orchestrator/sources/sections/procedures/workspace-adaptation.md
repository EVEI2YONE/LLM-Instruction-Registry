# Render a package for a verified workspace

Read when about to convert a portable package into a target-specific instruction, skill, repository-agent file, chatbot prompt, or upload bundle.

Start with the recorded `runtime-capabilities` report. Do **not** infer target behavior from the author's current chat features. Select exactly one adapter under `adapters/` and read it only after the target is known. Check available source read interfaces, source count and context budgets, tool schemas, authentic project/repo access, permission grants, secret handling, native skill conventions, scheduling and state.

For local coding agents, prefer a pinned checkout, addressable `SKILL.md` sections, and an operator-configured SDK or process adapter when actual child execution is required. Generate native files (e.g. `AGENTS.md` or `CLAUDE.md`) only when installed target/version supports that filename and semantics. Do not silently create permanent global host configuration.

For hosted chat agents, distinguish source reference, actual external tool registration and native subagent creation. If hosted tools are absent, generate prompt-only instructions with explicit manual retrieval limitations. If there is a callable tool, generate the precise action/API contract, identity/project isolation requirements, and operator deployment runbook. Cross-agent context/artifact persistence must use approved external storage, not assumed conversational memory.

Produce a portability report listing source ref, rendered target, section availability, shared-rule injection mechanism, permissible actions, capable/unsupported/unknown features, test method, and install/deploy actor. If a target enforces upload limits, compile from canonical modules into `dist/<target>/` rather than flattening/mutating the canonical source. A generated artifact is *not* proof of installation or successful execution.
