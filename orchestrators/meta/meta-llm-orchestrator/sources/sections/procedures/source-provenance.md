# Verify sources, knowledge and authority

Read when about to assert that an instruction came from an authoritative source, cite knowledge, use common governance, or make a change affecting approvals.

Pin the instruction-registry commit and target project revision independently. Identify exact files and owners, current versions, applicable source hierarchy, source freshness and accessibility. Approved project requirements own product intent; ADRs/interfaces own reviewed design; actual code SHAs and tests support implementation and verification. A newer draft does not automatically override approved artifacts, and conversation memory is not source authority.

Domain and world knowledge should be referenced by catalog entry IDs at pinned catalog SHAs. Search a curated index before opening entries, preserve approval/provisional/deprecated states, and record `catalog@sha:entry-id` in evidence. If an external catalog cannot be reached, report `not_verified` rather than inventing a negative finding. Do not create an index merely because a document proposes one; verify the catalog's actual interface.

Central governance under `governance/` is authoritative only at an approved pinned version. The current `governance/common-rules.md` is a **draft v0**, not a deployed globally injected runtime policy. Until it is approved and installed, always retain safety, ownership and evidence non-negotiables in the agent entrypoint or verified runner configuration.

Existing `governance/approval.json` and `governance/capability-ownership/ownership-policies.json` are not reconciled. Conservatively block/escalate any action requiring human approval under either list, including merges, investment, production and scope/priority authority changes. Never infer approvals or weaken the policy based on a generated package.
