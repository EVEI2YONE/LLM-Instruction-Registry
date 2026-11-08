"""Mock-only adapter used to test delegation contracts; does NOT spawn LLMs."""
from __future__ import annotations

from dataclasses import dataclass, field


class UnsupportedSpawn(RuntimeError):
    pass


@dataclass
class Adapter:
    runtime_id: str
    capabilities: dict[str, str]
    spawn_mode: str = "unavailable"
    handles: dict = field(default_factory=dict)

    def probe(self) -> dict:
        return {
            "runtime_id": self.runtime_id,
            "spawn_mode": self.spawn_mode,
            "features": dict(self.capabilities),
        }

    def spawn(self, task: dict, context_ref: str, sections: list[str]) -> dict:
        if self.spawn_mode != "mock":
            raise UnsupportedSpawn("no verified native/SDK/gateway child-agent adapter")
        if not task.get("task_id") or not task.get("idempotency_key"):
            raise ValueError("task identity and idempotency are required")
        if task.get("context_ref") != context_ref:
            raise ValueError("task context mismatch")
        required = task.get("required_capabilities", [])
        if any(self.capabilities.get(cap) != "verified-available" for cap in required):
            raise UnsupportedSpawn("required capability unavailable")
        for prev in self.handles.values():
            if prev["idempotency_key"] == task["idempotency_key"]:
                return prev
        result = {"task_id": task["task_id"], "status": "queued",
                  "idempotency_key": task["idempotency_key"],
                  "section_ids": list(sections), "mock_only": True}
        self.handles[task["task_id"]] = result
        return result

    def poll(self, handle: dict) -> dict:
        return dict(self.handles[handle["task_id"]])

    def cancel(self, handle: dict) -> dict:
        row = self.handles[handle["task_id"]]
        row["status"] = "cancelled"
        return dict(row)
