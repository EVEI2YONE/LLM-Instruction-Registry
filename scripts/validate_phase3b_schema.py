#!/usr/bin/env python3
"""Validate every registered package against the canonical lookup manifest schema."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parent.parent
schema=json.loads((ROOT/"schemas/lookup-package.schema.json").read_text())
validator=Draft202012Validator(schema)
registry=json.loads((ROOT/"registry.json").read_text())["instruction_sets"]
for entry in registry:
    manifest=json.loads((ROOT/entry["sources"]/"manifest.json").read_text())
    errors=list(validator.iter_errors(manifest))
    if errors:
        raise ValueError(entry["id"]+": "+str(errors[0]))
print("PASS: validated "+str(len(registry))+" canonical package manifests against repo schema")
