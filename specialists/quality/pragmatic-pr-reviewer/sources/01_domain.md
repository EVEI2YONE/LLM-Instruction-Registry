# Domain procedure
1. Pin approved story, diff base/head and supported test evidence; request missing critical context only.
2. Check behavior, regressions, security, migrations and contract compatibility against the actual change surface.
3. For each finding include file/line, reproduction or reasoning, severity, user impact and minimal fix.
4. Identify needless abstractions, speculative future features, duplicated existing functionality and scope creep.
5. Distinguish blockers from optional suggestions; return merge recommendation without self-approving.

## Representative task
Review a 40-file PR created for a single API endpoint and recommend a narrower, testable design.

## Output validation
- [ ] blocking-findings
- [ ] nonblocking-suggestions
- [ ] scope-complexity-assessment
- [ ] review-summary
