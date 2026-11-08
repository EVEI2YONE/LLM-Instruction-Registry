# Configuring execution targets (foundation; not predeployed)

## Local-machine setup

Prerequisites: Python 3.11+, an authorized local checkout, provider SDK/process command supplied by the machine owner, explicit tool permissions and a project-scoped directory. Never commit secrets.

1. Clone the registry at an exact SHA; use `python3 scripts/search_registry.py search --query "..." ` to choose a package.
2. Probe available runtime APIs and persist an environment-specific capabilities report using `schemas/runtime-capabilities.schema.json`. Do not fabricate a successful native-spawn probe.
3. For current legacy packages, read the selected published entrypoint and the minimal necessary sources. After migration, use `python3 scripts/lookup_sections.py lookup <package-id> "task words"` and `show` to retrieve verified sections.
4. Implement the adapter described by `ADAPTER_CONTRACT.md` for the installed provider SDK, CLI or process. Use `reference_adapter.py` only for simulated tests.
5. Configure a state DB under the project's restricted directory using `runtime/state_store.py`. This is a local reference store; the application still must enforce authentication, context minimization, and tool authorization.
6. Bind a real worker and run adapter conformance tests before claiming dynamic local spawning.

## Hosted chat-agent setup

1. Verify whether the hosted chat product exposes a callable native subagent API and durable storage. Do not infer from the product name.
2. If native child creation is absent, deploy an operator-controlled HTTPS service implementing `gateway.openapi.json` with identity, project isolation, queue/workers, audit records, scopes, protected secrets, artifact storage, human approval callbacks and cancellation.
3. Configure the provider's **actual** tools/functions/actions to call that service. A URL pasted into chat is not a configured integration.
4. Allow the hosted conversation to reference the registry at pinned SHAs via its verified repository connector or through the gateway's controlled package resolver.
5. Test read-only retrieval, delegated task execution, artifact visibility, concurrent writes, conflict handling, approval gates and cancellation with the authenticated provider setup.
6. Only publish a verified adapter-capability report after integration tests pass. Without a gateway/native child API, disclose single-agent mode.

## Publication and ownership

- Registry: reusable instructions and section manifests.
- Target project: code, product documents, approved decisions.
- Runtime operator: credentials, execution engine, context/artifact state, queue, access controls, billing, health and audit logs.
- Humans: policy approval, merges, investment and production deployment.

A successful foundation CI is **not** evidence of a deployed local model worker or hosted gateway.
