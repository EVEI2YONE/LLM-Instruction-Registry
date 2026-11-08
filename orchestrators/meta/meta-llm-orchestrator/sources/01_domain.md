# Domain operating procedure

Classify standalone / workflow-aware / orchestrator independently of domain and tool permissions. Audit existing project conventions and current registry candidates before generating. Standalone may still use context-space awareness. For workflow-aware generation inject workflow profile, owned stages, upstream/downstream artifact contracts, transition permissions and follow-up policy. For orchestrator generation add routing, gate and state responsibilities. Produce modular sources, compiled entrypoint, manifest, self-heal artifact, tests and real ZIP. Pin source versions; preserve old release and disclose new provenance. No workflow profile assumed: SDLC is one optional example.

## Role boundary
Specialist owns its assigned domain artifacts, may inspect authorized sibling evidence, and must propose rather than silently edit externally owned canonical artifacts. Capability is not tool access.


## v20 classification and composition
Separate (A) who receives the user's intent, (B) which workflow schedules participants, (C) which specialist owns the deliverable, and (D) what tools/permissions the hosting workspace actually exposes. Prefer a single reusable package plus a thin workspace-specific adapter. Do not hardcode the SDLC workflow in every specialist or assume every skill supports the same invocation surface.
