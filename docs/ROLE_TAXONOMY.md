# Instruction package taxonomy

`kind` is execution responsibility; `role` is professional expertise. Neither implies tool access or human approval.

| Kind | Canonical root | Function |
|---|---|---|
| `primary-orchestrator` | `orchestrators/primary/<id>/` | User intent routing and workflow composition |
| `workflow-orchestrator` | `orchestrators/workflow/<id>/` | Specialist and stage coordination |
| `meta-orchestrator` | `orchestrators/meta/<id>/` | Generate and evolve instruction systems |
| `specialist` | `specialists/<domain>/<id>/` | Independent bounded domain execution |

Professional roles remain `progenitor`, `orchestrator`, `strategist`, `expert`, `curator`, and `generalist`. Multiple nonexclusive capability/domain facets support search without duplicating files. Workflow definitions live in `workflows/<group>/<id>/` and identify participants via capability; the [ownership matrix](../governance/capability-ownership/README.md) defines artifact participation. For prior path changes see [migration map](MIGRATION_MAP.md).
