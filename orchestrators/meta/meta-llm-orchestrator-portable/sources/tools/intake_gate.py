#!/usr/bin/env python3
"""Pure, host-neutral target intake gate for specialist instruction generation.

Input: a JSON object over stdin or --file, output: JSON decision to stdout.
No network, repository, subprocess, or file writes are performed.
"""
from __future__ import annotations
import argparse
import json
import sys

DESTINATIONS = ("chatgpt-project", "chatgpt-skill", "hosted-assistant", "local-agent", "api-application", "other")
LOADING_MODES = ("injected", "verified_lookup", "hybrid")
RESOLUTIONS = ("REUSE_UNCHANGED", "UPGRADE", "CREATE_NEW", "BLOCKED")
QUESTION = ("Where will you use the generated agent instructions: a ChatGPT Project "
            "or Skill, another hosted assistant, a local coding agent, or an API application?")

def decide(record: dict) -> dict:
    if not isinstance(record, dict):
        raise ValueError("intake must be a JSON object")
    purpose = record.get("purpose", "generate_agent")
    if purpose == "authoring_source_only":
        return {"status": "REVIEW_ONLY", "question": None,
                "reason": "Repository source review is not a generated-agent request."}
    if purpose not in ("generate_agent", "upgrade_agent", "adapt_agent"):
        raise ValueError("unknown purpose")
    destination = record.get("execution_destination")
    # Do not replace the user's answer with the current generator host.
    if destination in (None, "", "unknown"):
        return {"status": "ASK_DESTINATION", "question": QUESTION,
                "reason": "The generated agent's destination is not established."}
    if destination not in DESTINATIONS:
        raise ValueError("unrecognized destination: " + str(destination))
    resolution = record.get("registry_resolution")
    if resolution not in RESOLUTIONS:
        return {"status": "ASK_REGISTRY_DECISION", "question": None,
                "reason": "Search and assess registered candidates before authoring."}
    if resolution == "BLOCKED":
        return {"status": "BLOCKED", "question": None,
                "reason": "Registry decision blocks generation or adaptation."}
    mode = record.get("source_loading_mode")
    if mode not in LOADING_MODES:
        return {"status": "ASK_LOADING_MODE", "question":
                "Will the target receive the complete instructions directly, read linked source files, or support both?",
                "reason": "Loading capability materially determines the output package."}
    operation = "ADAPT_EXISTING" if resolution == "REUSE_UNCHANGED" and purpose == "adapt_agent" else resolution
    return {"status": "READY", "question": None, "destination": destination,
            "source_loading_mode": mode, "resolution": resolution,
            "adaptation_action": operation,
            "registry_write_authority": record.get("registry_write_authority", "unknown"),
            "approval_verified": record.get("approval_verified", "NOT_VERIFIED"),
            "note": "READY means intake complete, not approved, published, installed or executed."}

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Optional JSON file; otherwise read stdin")
    args = parser.parse_args(argv)
    try:
        with open(args.file, encoding="utf-8") if args.file else sys.stdin as stream:
            result = decide(json.load(stream))
        print(json.dumps(result, sort_keys=True))
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}), file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
