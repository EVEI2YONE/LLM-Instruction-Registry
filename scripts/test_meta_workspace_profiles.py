"""Meta-LLM v20 workspace adaptability and packaging checks."""
import json
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "orchestrators/meta/meta-llm-orchestrator"
REQUIRED = [
  "online-hosted-chatbot.md", "codex-local.md", "claude-code-local.md",
  "grok-bot.md", "chatgpt-project.md", "generic-portable.md"
]
class MetaWorkspaceTests(unittest.TestCase):
    def test_workspace_profiles(self):
        for name in REQUIRED:
            self.assertTrue((META / "sources/workspaces" / name).is_file())
        manifest = json.loads((META / "sources/99_manifest.json").read_text())
        self.assertEqual("v20", manifest["version"])
        self.assertTrue(manifest["self_heal_required"])

    def test_meta_archive_matches_sources(self):
        p = META / "meta-llm-orchestrator_v20.zip"
        with zipfile.ZipFile(p) as z:
            self.assertIsNone(z.testzip())
            src = META / "sources"
            expected = { "meta-llm-orchestrator/" + x.relative_to(src).as_posix(): x
                         for x in src.rglob("*") if x.is_file() }
            self.assertEqual(set(expected), set(z.namelist()))
            for n, f in expected.items():
                self.assertEqual(f.read_bytes(), z.read(n))
if __name__ == "__main__":
    unittest.main()
