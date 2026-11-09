# Tool-enforced specialist execution (local reference)

This is a **trusted local process boundary** layered on top of `runtime/instruction_execution_gate.py`. It is not a ChatGPT-installed action, hosted execution gateway, deployed worker, or proof that a ChatGPT conversation cannot answer outside the adapter.

## Contract

1. `prepare_specialist(task, native_available, delegation_authorized)` reads the live checkout's registry record, entrypoint and mandatory section/dependency closure, checks SHA-256 against the canonical manifest, snapshots the actual bytes, and issues a short-lived, one-use HMAC-authenticated token bound to task identity/objective, package/version, registry revision, project revision, execution mode, accepted-rule IDs and instruction digest.
2. `execute_specialist(task, token)` rejects absent/modified/used/expired tokens before calling an **operator-configured** runner. Runner receives the complete verified instruction snapshot and chosen mode, not only source names. A native result must expose a child handle; a sequential result must not. Runner must provide an observable delivery reference.
3. `accept_specialist_result(task, token)` calls an **independent operator-configured verifier** which checks artifact content and real provider delivery traces against the task's requirements. Missing evidence/requirements blocks acceptance.

## Important security boundaries

- The reference adapter uses **process-local** token state and secret keys; tokens cannot be shared across processes or recovered on restart. It is not a multi-tenant production service.
- The registry root must be an operator-controlled checkout **verified externally at the claimed immutable commit**. Merely supplying a 40-character SHA is not evidence that local bytes came from that commit. No model-provided repo location, evaluator, runner, verification result, or HMAC key should be trusted.
- The verifier callback must evaluate actual artifact bytes and delivery traces. A model-supplied Boolean, file name, or arbitrary evidence reference is **not** sufficient. Existing tests use fixture callbacks to test enforcement logic, not real LLM quality or identity.
- Sequential mode means a verified instruction snapshot is passed to the configured **parent-model execution adapter**. It does not magically inject instructions into an existing ChatGPT context. An installed ChatGPT tool or gateway must arrange this.
- The protected execution route needs to be the **only authorized specialist-execution route** for strong enforcement; a regular ChatGPT conversation can still produce prose without using it. Deployment requires authentication, authorization, approved project scopes, audit retention and existing human approval boundaries.
- This reference is intentionally non-networked. A hosted deployment should integrate with the existing `runtime/gateway.py` security boundary and document new API methods in `runtime/gateway.openapi.json` before describing the gateway as enforcing this contract.

## Little Wins regression

Run from repository root:

```bash
python3 -m unittest scripts.test_enforced_specialist_adapter
```

The fixture simulates the request to assess `EVEI2YONE/Little_Wins`, verifies no assessment runner call before preparation, detects missing entrypoint/section/dependency/hash, selects sequential mode when native spawning is absent, and refuses output acceptance if required instructions are not evidenced. This is **not** the full end-to-end ChatGPT behavioral retest.

## Required deployment follow-up

Expose the three guarded operations through a real trusted API/tool integration, bind user/project/run authorization and an actual provider execution adapter, persist token state and audit logs, then run the Little Wins assessment end-to-end from the ChatGPT site with no `Capabilities.txt`. Until that happens, the website's existing behavior remains an unresolved integration gap.
