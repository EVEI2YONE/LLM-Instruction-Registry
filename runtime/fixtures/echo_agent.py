"""Deterministic subprocess test agent. Never connect to a model/provider."""
import json
import sys

request = json.load(sys.stdin)
task = request["task"]
ctx = request["context"]
package = request["package"]
assert request["protocol"] == "local-agent-v1"
assert ctx["task_id"] == task["task_id"]
assert package["package_id"] == task["package_id"]
print(json.dumps({
    "protocol": "local-agent-result-v1", "task_id": task["task_id"],
    "status": "complete",
    "evidence": ["verified-fixture-process"],
    "artifacts": [{"artifact_id": "output-" + task["task_id"], "kind": "text",
                   "content": "completed " + task["objective"],
                   "visibility": "run", "status": "draft"}]
}))
