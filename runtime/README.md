# Runtime adapters and shared execution

This directory contains portable **contracts and reference implementation** for local and hosted execution. The repository itself does not run agent models, host a gateway, share session memory across providers or grant permission to spawn child agents.

Read:
- [Architecture](../docs/LOCAL_AND_HOSTED_AGENT_RUNTIME.md)
- [Adapter protocol](ADAPTER_CONTRACT.md)
- [Execution setup](EXECUTION_SETUP.md)
- [Gateway OpenAPI contract](gateway.openapi.json)
- [Portable adapter profiles](../adapters/README.md)
- [Context and artifacts](CONTEXT_AND_ARTIFACT_CONTRACT.md)
- [Runtime capability schema](../schemas/runtime-capabilities.schema.json)
- [Delegation schema](../schemas/subagent-task.schema.json)
- [Context schema](../schemas/context-envelope.schema.json)
- [Artifact schema](../schemas/artifact-record.schema.json)

For real local execution, implement or configure a provider adapter, using authorized credentials and a scoped filesystem. Hosted environments require platform tools or an external authenticated gateway. A reference in-process adapter is for correctness tests, **not** a deployed hosted subagent system.
