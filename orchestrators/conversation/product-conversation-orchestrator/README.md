# Product Conversation Orchestrator v1.3 (review candidate)

**Category:** conversation orchestrators. **Kind:** `conversation-orchestrator`. **Role:** orchestrator.

User-facing ChatGPT control plane for maintaining workflow progress across user conversations, selecting registered specialists, managing dependencies and knowledge-gap PRs, and resuming from verified merges. It composes rather than replaces `product-lifecycle-orchestrator`, workflow coordinators, specialists and `meta-llm-orchestrator`.

## Use

Install a validated ChatGPT Skill/host adapter separately, with explicitly granted repository tools. Start with a product request; the assistant maintains a visible ledger and proactively delegates suitable specialist tasks through verified, authorized child tools without requiring the user to say 'spawn'. If higher-priority policy requires explicit user permission, that gate still applies. The same pinned specialist instructions must be delivered to real child contexts (with reception evidence) or loaded into a separately attributed `SEQUENTIAL_SPECIALIST` parent phase when child tools are unavailable. Actual concurrent subagents and durable background work require a real configured runtime adapter. A GitHub link alone does not enable them.

## Governance

The uploaded conversation Skill was adapted into a lookup-first canonical source tree. Review the taxonomy expansion and verify registry ownership/approval before release. No self-approval, auto-merge, or claims of deployed workers. Merge remains human-controlled.

## Source

See `sources/SKILL.md` for entrypoint and `sources/manifest.json` for selective sections. This PR is a candidate until source archive, semantic tests, approval and installation checks are observed.
## Fail-closed execution gate (v1.2)

Specialist-dependent assessment cannot start before applicable capability declarations are reconciled, a runtime mode is selected, and the registered specialist entrypoint plus required section dependency closure have been loaded. If native spawning is explicitly unavailable (for example in Capabilities.txt), use a tailored `SEQUENTIAL_SPECIALIST` phase; if instructions cannot be loaded, report `BLOCKED_INSTRUCTIONS` and do not issue a specialist readiness verdict. Deterministic regression tests live in `scripts/test_instruction_execution_gate.py`; hosted end-to-end compliance remains NOT_RUN.

## Deliverable quality (v1.3)

For readiness and QA assessments, child/subagent completion and instruction receipts are prerequisites, not the final user deliverable. Reconcile a material findings ledger against the final report, leading with the verdict, requirement-to-feature status, evidence-backed impact and gaps, passed/failed/untested validation, dependency-prioritized backlog, limitations and unresolved decisions. A short progress summary must not replace the requested assessment. See `sources/sections/procedures/readiness-deliverable-acceptance.md` and `scripts/test_readiness_report_gate.py`. Behavioral evaluation remains NOT_RUN.
