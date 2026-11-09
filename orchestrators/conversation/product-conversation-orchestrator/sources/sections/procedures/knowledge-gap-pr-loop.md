# Knowledge gap -> PR -> merge verification -> resume

1. Detect a missing, stale or contradictory authoritative fact. Pin the specific current catalog/version; inaccessible sources are `not_verified`, not missing. Record the exact blocked question and dependent deliverables.
2. Look for an existing catalog entry, owner and active PR before creating work. A one-off product decision is not a generalizable catalog gap.
3. Gather source evidence using an appropriate curator or verified specialist. For AI research, inspect `ai-knowledge-atlas`; for broader consultation consider `catalog-grounded-consultant`. Keep sources, dates, limitations and citation provenance.
4. Prepare the minimum catalog-only change and tests; identify the correct repository, owner and reviewer. If repo tools and user authorization permit, submit a dedicated draft PR. Do not expand unrelated scope or silently modify product code.
5. Set dependent task `blocked_on_merge` with PR link, head SHA, target branch, expected catalog section, approval owner and resume criterion. Continue unrelated tasks.
6. Human approval is required for merge. After the user says it merged, independently fetch PR and verify `merged=true`, target branch, actual merge commit, updated catalog content and approval requirements.
7. Refresh and pin a new approved authoritative snapshot, rerun affected knowledge lookup and tests, update handoff and resume only previously blocked tasks. Rejected, closed-unmerged, outdated or conflicting PRs stay blocked.

Downstream agents may request a PR or supply a patch, but the conversation orchestrator coordinates review and submission. A PR created by an assistant is not an approved or merged change.