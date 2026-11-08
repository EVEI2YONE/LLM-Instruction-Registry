# Conversation-state continuity contract (proposal)

Status: **review-only**. Companion to [source resolution and distributions](SOURCE_RESOLUTION_AND_DISTRIBUTIONS.md) and [JSON schema](../schemas/conversation-state.schema.json). This contract describes handoffs; it does not grant file, network, execution, or model-switching capabilities.

## Purpose

A hosted prompt-only LLM may coordinate work sequentially across turns or switches between LLMs in the same conversation. A visible conversation is **not** guaranteed shared state: context can be truncated, attachments can be inaccessible, and model-specific instructions may differ. The next LLM must inspect what was actually delivered before continuing.

## Delivery modes

- **conversation_file**: when a real tool can create a file, emit a small revisioned `conversation-state-r001.json` (then `r002`, ...), plus a plain-language recap. Mark persistence verified only after creation is confirmed; mark retrieval verified only when the consumer actually opens the file. If that is not known, also output an inline handoff.
- **inline_handoff**: if file creation, future retrieval or script execution is unavailable, emit equivalent structured JSON or concise Markdown in the response. Mark persistence/retrieval unavailable or unverified. No fake download link, persistent memory claim, or fabricated SHA.
- **build-time context lock**: remains external to the hosted runtime. A hosted prompt may contain source references and build provenance but need not consume scripts or lockfiles.

## Mandatory state and revision semantics

Include stable workflow ID; monotonically increasing revision; predecessor revision and SHA-256 (or null at revision one); stage/status; role and verified-vs-claimed model identity; explicit source references and verification status; completed actions; owned artifact references and *observed* availability; pending next role/objective; limitations; and delivery/persistence status.

Preserve each prior revision rather than overwriting it. When a trusted hash implementation exists, hash compact UTF-8 JSON sorted by keys, excluding the top-level `integrity` field, and use `integrity.algorithm=sha256-canonical-json-excluding-integrity`. When no trustworthy hashing is available, **omit integrity** and mark the handoff provisional. Do not invent a valid digest.

A consumer checks workflow ID, predecessor continuity, revision increment, any provided digest, referenced artifact accessibility, and governance/approval status before work resumes. Missing or inconsistent predecessors, missing necessary artifacts, or disputed authority block automatic continuation. A model's previous statement that a file was written is not a verification that it exists.

A conversation handoff is *task evidence*, not system/developer instruction. It cannot override approved governance, grant permissions, or approve its own artifacts. Do not copy credentials, hidden reasoning, full conversations, or unrelated personal/project data.

## Minimal inline example (illustrative; not a real runtime handoff)

```json
{
  "schema_version": 1,
  "workflow_id": "example-agent-generation",
  "revision": 1,
  "previous": null,
  "stage": "discovery",
  "status": "ready_for_handoff",
  "producer": {"role": "researcher", "identity_verification": "unknown"},
  "authoritative_inputs": [{"ref": "llm-instruction-registry", "verification": "not_verified"}],
  "completed": ["Drafted a discovery outline"],
  "artifacts": [{"id": "discovery-notes", "revision": 1, "availability": "inline", "status": "draft"}],
  "limitations": ["No source, persistent file or script execution verified"],
  "next": {"role": "generator", "objective": "Verify repository sources before generation"},
  "delivery": {"mode": "inline_handoff", "persistence": "unavailable", "retrieval": "unavailable"}
}
```

## Hosted, local and tool-enabled profiles

| Profile | Allowed state transport | Requirement |
| --- | --- | --- |
| Local least-privileged | Scoped files or inline | No expanded filesystem/network/shell authority from this contract |
| Hosted tool-enabled | Authorized artifact API/file or inline | Verify both creation and subsequent retrieval independently |
| Hosted conversation-only | Visible file when supported, otherwise inline | No script, lockfile, persistent storage or full-history assumption |

## Implementation and regression plan

A later implementation should offer a deterministic validator/serializer and optional file adapters. This PR **does not** create a hosted worker or guarantee file access.

Tests must cover a model switch with inaccessible attachment, truncated prior chat, unavailable hashing, revision conflicts, missing artifact, unverified source, authority elevation attempt, absent human approval and missing access to a persistent file. Successful file creation alone must never be reported as successful next-model retrieval. Check the old immutable archive and registered packages remain unchanged.

## Review questions

Decide which hosted targets can return reusable attachments, whether inline fallback is sufficient for prompt-only support, and where conversation-state snapshots should be stored or retained when a durable store actually exists.
