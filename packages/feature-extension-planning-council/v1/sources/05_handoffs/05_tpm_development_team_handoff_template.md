# TPM and Development Team Handoff Template

## Handoff Summary

- Extension:
- Planning owner:
- Target release:
- Recommended delivery model:
- Confidence level:

## Epic Map

| Epic | Goal | Owner function | Dependencies | Exit criteria |
|---|---|---|---|---|
| Epic 1: Discovery and constraints | Validate platform/API assumptions | Product + Tech Lead | Access to docs/sandbox | Constraints documented |
| Epic 2: Architecture foundation | Establish contracts and module boundaries | Engineering | Discovery outputs | Skeleton builds and tests |
| Epic 3: Core extension behavior | Implement primary user workflow | Engineering + Design | Foundation | Acceptance tests pass |
| Epic 4: Security and reliability | Harden permissions, privacy, logging, errors | Security + Engineering | Core behavior | Security review complete |
| Epic 5: Release and operations | Deploy, monitor, support, roll back | DevOps + TPM | Hardened candidate | Release checklist complete |

## Work Breakdown

| Work item | Description | Type | Suggested owner | Dependencies | Acceptance criteria |
|---|---|---|---|---|---|
|  |  | Research / Design / Backend / Frontend / QA / DevOps |  |  |  |

## Milestones

| Milestone | Target outcome | Required artifacts | Go/no-go gate |
|---|---|---|---|
| M0 | Discovery complete | Research notes, decision records | Architecture risks understood |
| M1 | Build foundation | Repo structure, interfaces, CI | Build/test pipeline green |
| M2 | MVP complete | Working core workflow | Functional acceptance passes |
| M3 | Release candidate | Hardened build | Security, QA, rollout approvals |
| M4 | Production rollout | Released extension | Monitoring and support ready |

## Risks and Decisions

| ID | Risk/Decision | Impact | Mitigation/Decision owner | Due date |
|---|---|---|---|---|
| R-001 |  |  |  |  |

## Open Questions

| Question | Blocking? | Owner | Needed by | Resolution path |
|---|---:|---|---|---|
|  | Yes/No |  |  |  |

## Acceptance Criteria

- [ ] Functional requirements map to tests.
- [ ] Non-functional requirements have measurable thresholds.
- [ ] Interfaces and schemas are documented.
- [ ] Security and privacy review items are identified.
- [ ] Rollout and rollback strategy are defined.
- [ ] TPM can convert handoff into epics, milestones, and sprint-ready tasks.