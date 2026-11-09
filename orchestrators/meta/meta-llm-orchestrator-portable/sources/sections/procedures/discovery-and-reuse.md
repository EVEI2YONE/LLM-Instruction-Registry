# Discovery and reuse

Before new source authoring:
1. Resolve registry identity and approved lookup locations from a source locator; do not assume a URL grants tools, credentials, or latest-approval authority.
2. If connected repository or checkout access exists, read `registry.json` and pin one immutable commit; retrieve schema, relevant metadata, and candidate sources from the same commit. If the channel is inaccessible, mark discovery NOT_VERIFIED.
3. Inspect at most the closest candidates first: role, ID, version, functional inputs/outputs, boundaries, source availability, runtime compatibility, ownership, and actual approval evidence.
4. Produce a decision record with `registry_snapshot_commit`, `candidates_inspected`, `candidate_functional_fit`, `capability_gap`, `resolution`, `approval_verified`, `registry_operation`, and `registry_mutations`.
5. Choose REUSE_UNCHANGED for adequate behavior, including a new target-specific packaging adapter with no canonical upgrade. Choose UPGRADE only for an explicit requested semantic change or demonstrated gap. Choose CREATE_NEW only if no suitable match was verified. Otherwise choose BLOCKED or provisional.
6. Keep `available`, `approved`, `installed`, and `activated` distinct. Do not use age or presentation style as an invented feature gap.

For this source repository, the discovered legacy meta orchestrator is an existing implementation. This candidate explores a portable **alternative**, not an automatic replacement.