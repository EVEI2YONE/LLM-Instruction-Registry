# Capability ownership resolution
[Global model](../governance/capability-ownership/README.md) defines Owner, Contributor, Consultant, Reviewer and human Approver. Each workflow has a local `responsibilities.json` that binds artifact ownership to **capability IDs** and decision authority to human/project roles. The `registry.json` is a discovery index, not proof of a tool's availability or actual approval authority.

Agents must not silently create duplicate PRDs/ADRs, merge, deploy or infer authority. Resolve human identities from project-level owners and check approvals against pinned revisions. Conflicts are escalated to human decision makers.
