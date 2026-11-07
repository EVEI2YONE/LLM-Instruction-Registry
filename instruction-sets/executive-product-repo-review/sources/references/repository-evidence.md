# Repository evidence guide

## Scan order (high-signal first)
1. Product README, positioning, target users, onboarding and usage guides.
2. Screens, demos, UI navigation, user-facing copy and documented journeys.
3. Changelog/release notes and declared roadmap.
4. Route/module inventory and integration entrypoints *only to verify product capability*.
5. Issues, customer requests, PR descriptions, backlog and discussions when available; distinguish maintainer opinions from customers.
6. Tests and deployment docs only as weak evidence of operational readiness, not customer quality.

## Evidence ledger
| Claim / capability | Source (path/issue) | Status: observed/inferred/hypothesis/unknown | User outcome | Caveat |
|---|---|---|---|---|

Status guidance:
- **Observed:** documentation/UI/code supports existence; still not evidence of quality or usage.
- **Inferred:** plausible strategy, segment or motivation from product signals.
- **Hypothesis:** prospective value or adoption awaiting validation.
- **Unknown:** inaccessible, absent, contradictory or requiring telemetry/customer evidence.

Separate: implemented; advertised but unverified; prototype/flagged; proposed; deprecated. Do not assume all implemented capabilities are exposed or functional. Report gaps in access or unexamined repository regions. Prioritize decisions over exhaustive file enumeration.

## Product context questions
Who is end user, economic buyer and administrator? Who suffers the pain? Which use case gets the user to first value? Is the offering single-purpose, workflow, platform or marketplace? Why would users return? What is the switching cost? What might create trust or compliance concerns? What distribution route is plausible? What competitor or current workaround is being replaced?
