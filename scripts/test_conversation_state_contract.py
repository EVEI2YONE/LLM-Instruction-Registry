"""Static contract assertions for proposed conversation continuity; no runtime claims."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

class ConversationStateContractTests(unittest.TestCase):
    def test_schema_has_revision_and_delivery_gates(self):
        schema = json.loads((ROOT / "schemas/conversation-state.schema.json").read_text(encoding="utf8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertTrue({"previous", "revision", "delivery", "artifacts", "authoritative_inputs"}.issubset(schema["required"]))
        self.assertEqual(set(schema["properties"]["delivery"]["properties"]["mode"]["enum"]), {"inline_handoff", "conversation_file"})
        self.assertIn("unavailable", schema["properties"]["delivery"]["properties"]["retrieval"]["enum"])
        self.assertNotIn("integrity", schema["required"])

    def test_guidance_does_not_assume_persistence(self):
        text = (ROOT / "docs/CONVERSATION_STATE_CONTINUITY.md").read_text(encoding="utf8")
        self.assertIn("retrieval verified only when the consumer actually opens the file", text)
        self.assertIn("omit integrity", text)
        self.assertIn("inline_handoff", text)

if __name__ == "__main__":
    unittest.main()
