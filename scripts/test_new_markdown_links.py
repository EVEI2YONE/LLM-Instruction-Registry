"""Check links in new entrypoints and documents without requiring network access."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = [
    "README.md", "CONTRIBUTING.md", "docs/PUBLISHING.md",
    "docs/ROLE_TAXONOMY.md", "docs/WORKFLOW_ARCHITECTURE.md",
    "docs/CAPABILITY_OWNERSHIP.md", "docs/WORKSPACE_ADAPTERS.md",
    "docs/LIFECYCLE_INSTRUCTION_CATALOG.md",
    "orchestrators/README.md", "orchestrators/primary/product-lifecycle-orchestrator/README.md",
    "orchestrators/meta/meta-llm-orchestrator/README.md", "workflows/README.md",
    "governance/README.md", "governance/capability-ownership/README.md",
    "templates/README.md", "knowledge/README.md"
]

class EntryPointLinkTests(unittest.TestCase):
    def test_local_links(self):
        registry = json.loads((ROOT / "registry.json").read_text())
        new = {x["id"] for x in registry["instruction_sets"] if x["version"] == "v1"
               and x["id"] in {
                   "product-lifecycle-orchestrator", "specialist-consultation-coordinator",
                   "engineering-review-coordinator", "release-governance-coordinator",
                   "technical-product-manager", "backlog-story-refinement-specialist",
                   "business-feasibility-analyst", "market-competitive-research-specialist",
                   "ux-research-journey-specialist", "ui-ux-product-designer",
                   "accessibility-usability-reviewer", "solution-cloud-resource-architect",
                   "data-architecture-specialist", "security-architecture-specialist",
                   "api-integration-design-specialist", "database-migration-specialist",
                   "integration-engineering-specialist", "pragmatic-pr-reviewer",
                   "test-automation-specialist", "security-compliance-reviewer",
                   "product-analytics-specialist", "incident-root-cause-analyst",
                   "knowledge-context-steward", "decision-traceability-auditor"}}
        docs = DOCS + [x["readme"] for x in registry["instruction_sets"] if x["id"] in new]
        for path in docs:
            p = ROOT / path
            with self.subTest(file=path):
                self.assertTrue(p.is_file())
                for dest in re.findall(r'\[[^\]]+\]\(([^)]+)\)', p.read_text(encoding="utf-8")):
                    loc = dest.split("#", 1)[0].split("?", 1)[0]
                    if not loc or re.match(r"^(https?:|mailto:|data:)", loc):
                        continue
                    self.assertTrue((p.parent / loc).exists(), f"{path} -> {dest}")
if __name__ == "__main__":
    unittest.main()
