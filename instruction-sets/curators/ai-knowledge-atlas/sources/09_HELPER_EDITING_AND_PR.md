# 09 Helper Editing And Pr

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `02_helpers/05_editing_and_integration.md`

# Helper — Change authoring, implementation and integration

## Before writing
Confirm requested branch, actual branch SHA, allowed repository, authorized action and proposed file set. Use PR rather than direct main changes when possible. Scope batches to independent coherent improvements. Preserve unrelated user changes.

## Documentation changes
For new topics, justify a distinct canonical entry and add needed catalog links. For extensions, preserve correct content and explain changes. Use precise terms, scope, assumptions, inputs/outputs/contracts, alternatives, failure modes, security, evaluation, primary references and related entries where useful. Avoid template filler.

## Code and implementation references
Do not infer runnable examples from the directory name `implementations/`. Label samples `pseudocode`, `illustrative and untested`, `locally tested`, or `reproduced experiment` with evidence. Keep minimal dependencies; include run instructions, environment versions, fixed inputs, expected behavior and tests when warranted. Do not execute paid services without permission.

## Integration
Update all required README catalogs (root/category/nested), cross references and terminology. Ensure no duplicate headings or orphan entries. Provide change list with exactly changed paths. Do not say PR created until a tool confirms its URL and branch.

---

## Original source: `02_helpers/13_change_review_and_pr_protocol.md`

# Helper — GitHub branch, diff, PR and concurrency discipline

1. Read repository current default branch, target SHA, contributor instructions and branch policy.
2. Compute intended file list from the accepted gaps and dependencies. Avoid modifying unrelated application repos.
3. Recheck HEAD just before writing; isolate edits in one branch per coherent batch. If HEAD moved, compare changes before applying patches.
4. Make document changes, add indexes and related links, include typed examples or code only under scoped authorization.
5. Inspect diff for accidental mass changes, duplicated content, invented citations, stale relative paths, private information and unsupported claims.
6. Run applicable checks. Record their command/outcome, including explicit `not_run` for unavailable checks.
7. Create PR only if authorized, with concise summary, taxonomy rationale, evidence classification, exact test results, open questions and review needs.
8. Do not claim PR exists until exact URL is returned by the actual repository tool. Never silently merge or treat a PR as released knowledge.

## Required PR comment distinctions
- Repository code modifications versus instruction-package modifications.
- New documentation versus tested implementation.
- Newly verified facts versus derived engineering synthesis.
- Remaining source-review tasks versus checks performed.
