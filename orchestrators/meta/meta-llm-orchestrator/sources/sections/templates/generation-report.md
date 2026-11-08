# Generation decision and release report

Read when about to summarize a new instruction package, delivery plan, source migration or release for human review.

Use this shape, keeping each field compact and evidence-backed:

- **Request / scope:** Input goal, expected output artifact, representative use cases and exclusions.
- **Registry decision:** Reuse, extend, new, or blocked; candidate packages compared, exact repo/commit, selected ID/kind/role, owner and explanation.
- **Target runtime:** Authoring environment vs execution environment; native instruction surface, verified capabilities, unknown capabilities, adapters and expected fallback.
- **Instruction partition:** Critical always-rules, section IDs, procedure/contract/template split, shared-rule pin and source-to-section traceability.
- **Knowledge and source provenance:** Target project revision, relevant catalogs at pinned SHAs, approved/provisional/unverified evidence.
- **Deliverables:** Canonical source root, versioned ZIP path, generated target bundles, test/validation record, source hashes and output artifacts.
- **Orchestration integration:** Required child-agent capabilities, handoff schema, context/artifact references, task limits, independent reviewer/human approval checkpoints.
- **Validation:** Static tests, actual model/runner integration results versus NOT_RUN, missing sections, packaging integrity, known risks.
- **Review action:** PR link/status and exact requested approvals, remaining dependencies, rollback version, next owner.

Never write a vague success statement without tool proof; do not present installed/deployed status when only files were generated.
