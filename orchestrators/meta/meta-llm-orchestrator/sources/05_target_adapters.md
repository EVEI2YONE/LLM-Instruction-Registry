# Workspace-specific generation targets

| Target | Preferred output when verified | Common pitfalls | Required check |
|---|---|---|---|
| Online deployed chatbot | Versioned system/developer behavior, optional tool contracts, external state/store adapters, deploy instructions | Assuming filesystem, persistent memory or background jobs | Runtime config, tool APIs, hosting authorization, deployment evidence |
| Local Codex-style coding agent | Repo-scoped agent instructions (e.g., AGENTS.md only if supported), source modules, tests and git/PR procedure | Assuming automatic write, unrestricted shell or cross-repo permissions | Current checkout, available commands, sandbox, approvals, file conventions |
| Local Claude Code-style coding agent | Repository instructions (e.g., CLAUDE.md if supported), optional skills/subagents and scoped tool permissions | Assuming feature parity with Codex or automatic execution | Installed version, supported config, permissions and actual repo paths |
| Grok bot / hosted bot builder | Platform-native instruction text and verified action/knowledge definitions | Assuming native skill import, arbitrary script execution or filesystem | Provider configuration capabilities and permitted actions |
| ChatGPT Project / conversation workspace | Project instructions + organized project source files, optional skill only if supported, handoff guidance | Treating conversation memory as canonical repo or exceeding source attachment limits | Current Project file/access restrictions, connectors and upload paths |
| Generic or unknown LLM workspace | Plain Markdown core instructions, manifest, JSON contracts, portable ZIP and manual adaptation guide | Claiming compatibility or installation with unverified runtime | Capability report and explicit unsupported/unknown features |

Read `workspaces/` for concrete target-specific instructions. Do not introduce a platform-native filename merely because it is common; verify current target support first. Keep provider-specific logic outside the portable behavioral core.
