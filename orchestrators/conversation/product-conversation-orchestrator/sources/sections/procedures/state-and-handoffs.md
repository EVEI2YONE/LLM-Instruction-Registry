# Workflow state and conversation handoffs

After meaningful changes produce a small versioned record, or a durable file only when actual write/read is observed. Minimum record:
```json
{
  "workflow_id": "example",
  "revision": 1,
  "previous": null,
  "stage": "planning",
  "status": "provisional",
  "producer_role": "conversation-orchestrator",
  "authoritative_inputs": [],
  "intent": {},
  "scope": {"in": [], "out": []},
  "decisions": [],
  "tasks": [],
  "artifacts": [],
  "approvals": [],
  "blockers": [],
  "next": {"owner": "user", "action": "review stage plan"}
}
```
Each task should include ID, parent/dependencies, specialist and pinned version when assigned, status, owner, output refs, acceptance criteria and verified evidence. Each artifact has one owner, revision, visibility, digest if verified, producer and provenance. Preserve required `governance/handoff.schema.json` fields when emitting formal cross-workflow handoff records.

A chat transcript is not a persistence guarantee. If a file tool exists, persist a numbered state artifact and confirm its exact path. Include concise inline continuation anyway unless later file retrieval was tested. Before resuming verify prior revision, artifact availability, required approvals and fresh external PR/commit state. Contradictions, inaccessible predecessor or unclear approvals block automatic continuation. Never copy unrelated sensitive messages or private reasoning into handoffs.