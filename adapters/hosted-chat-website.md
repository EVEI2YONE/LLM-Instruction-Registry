# Hosted chat agent adapter profile

Entrypoint: provider-native instructions and registered callable tools; verify current connector permissions, tool invocation, durable state and subagent support at runtime. For file-limited platforms, generated compact bundles must list missing/unavailable sections explicitly.

Dynamic execution: if genuine native child-agent API exists, bind it through a verified adapter. Otherwise require an authenticated external gateway implementing `runtime/gateway.openapi.json`, configured as an actual provider tool. An arbitrary repository link, system prompt or Markdown file cannot spawn platform-native child agents.

Shared context and artifacts: store outside the hosted chat session in a project-scoped gateway/data service or expose explicit supported native object refs. Avoid leaking full history, secrets or unrelated project material. Persist approved decisions and exact source revisions.

Fallback: no tool or gateway means single-agent mode only, with transparent limitations. Cross-platform subagent provisioning, external-service deployment and connector configuration are not automatic. See [setup](../runtime/EXECUTION_SETUP.md).
