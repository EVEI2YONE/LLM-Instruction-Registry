"""Explicit immutable references; no guessed or mutable cross-agent session state."""
from __future__ import annotations
import re

REF = re.compile(r"^([A-Za-z0-9_.:-]{1,128})(?:@([1-9][0-9]{0,8}))?$")


def parse_ref(value: str, default_revision: int | None = None) -> tuple[str, int | None]:
    if not isinstance(value, str):
        raise ValueError("invalid immutable reference")
    m = REF.fullmatch(value)
    if not m:
        raise ValueError("invalid immutable reference")
    return m.group(1), int(m.group(2)) if m.group(2) else default_revision
