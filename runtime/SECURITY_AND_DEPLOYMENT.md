# Operational boundary and reproducible setup

**Status:** Implemented and CI-tested local reference gateway with process-backed child tasks. No real model/SDK adapter, public gateway deployment, or hosted chatbot tool installation is provided by this repository. These require operator credentials, infrastructure and separate conformance evidence.

## Local developer smoke test

From the repository root:

```sh
python3 scripts/search_registry.py validate
python3 scripts/migration_inventory.py --verify migration/inventory.json
python3 -m unittest discover -s scripts -p 'test_lookup_foundations.py' -v
python3 -m unittest discover -s scripts -p 'test_runtime_integration.py' -v
```

The integration test launches a real child Python process using a deterministic fixture, uses authenticated HTTP on an ephemeral localhost port, exercises project/run isolation, parallel tasks, dependencies, artifact fan-in and rejection cases. It does not prove actual LLM inference.

## Configure a local worker

The worker executable is an **operator-controlled fixed JSON-stdin / JSON-stdout program**. It receives a task, scoped context and the **selected package only**. Worker stdout uses protocol `local-agent-result-v1`, a matching task_id, status `complete|blocked|failed`, evidence list and draft artifact proposals. For a real LLM, adapt a permitted local CLI or installed provider SDK in the worker executable. Never pass arbitrary executable names from user requests; never invoke via shell.

Example development-only setup (replace `dev-token-replace-me` with a long random secret; never commit it):

```sh
export AGENT_GATEWAY_TOKENS_JSON='{"dev-token-replace-me":{"projects":["demo"],"run_ids":["run-demo"],"scopes":["read","write","delegate"]}}'
export AGENT_WORKER_ARGV_JSON='["python3","runtime/fixtures/echo_agent.py"]'
export AGENT_STATE_DB='./demo-state.sqlite3'
python3 -m runtime.gateway
```

The sample executable is a **fixture**, not a trained agent. Requests need their own matching run-scoped context snapshot before submitting child tasks.

## Hosted website

A hosted chatbot needs either a verified provider-native child API or a configured tool/action invoking an operator-hosted gateway. A pasted GitHub URL or these files do not automatically grant tools or spawn abilities.

The provided Dockerfile is a reproducible **reference packaging recipe only**. Its HTTP listener is not TLS; do not publish it directly on the Internet. For proxy deployment, configure token bindings, a real worker executable, persistent database volume and `AGENT_GATEWAY_HOST=0.0.0.0` together with `GATEWAY_ALLOW_PROXY_BIND=yes` inside a private network, behind TLS-terminating reverse proxy and external identity controls. Run the service as a non-root user.

## Known boundaries

- Local bearer token bindings enforce project, API scope and run scope, not enterprise SSO, OAuth, policy-as-code or dynamic token issuance.
- SQLite queue/reference store is suitable for one instance; it is not a distributed queue or a scalable cross-machine multi-tenant database.
- Cancellation changes durable task status, but a running process may continue until timeout; consequential tools must use idempotency and enforce cancellation at their own boundary.
- Restart blocks orphaned running tasks for human reconciliation rather than falsely marking success.
- All consequential policy actions are blocked until human approval service and policy reconciliation are implemented; an arbitrary approval string is not accepted as proof.
- Artifact content is bounded and content-addressed, with per-project and per-run controls. Operator must add encryption-at-rest, key rotation, retention/deletion and backups for sensitive or production data.
- Host-specific SDK/website integration is **NOT_RUN** unless operator actually configures and verifies it. Never label it passed from fixture tests.
