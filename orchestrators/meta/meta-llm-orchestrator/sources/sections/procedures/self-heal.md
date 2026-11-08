# Correction, gap closure and self-heal

Read when a generated agent behaves incorrectly, repeats instructions, misses a mandatory lookup, violates source precedence, confuses environments, leaks context or claims unverified execution.

Collect actual request, observed output, expected behavior, exact source package/section version, target capabilities and evidence. Classify: wrong package routing, bad `read_when`, missing `requires`, authority conflict, stale knowledge/catalog pointer, incorrect generated adapter, insufficient context, artifact ownership/concurrency, unsupported tool claim or packaging/integrity defect.

Diagnose once at the earliest authoritative layer: shared governance, package Always, conditional section, manifest lookup, runtime adapter, schema or external catalog. Do not duplicate fixes across every package. For an isolated user-specific issue, avoid global behavior changes without evidence. Preserve approved policy and prior released versions.

Propose a minimal patch to a new version, with a negative regression test demonstrating the original failure and a positive test showing the intended behavior. Re-render the entrypoint from the revised manifest when triggers change; verify every affected cross-package dependency and generated distribution. Subject changes to the package owner, reviewer, and human gates when required. Record blocked or unverified actions truthfully.

Never make an unreviewed self-edit to an already published ZIP or silently change a product repository just because the instruction system failed.
