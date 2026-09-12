"""Half of a circular import. `b` imports `a`, `a` imports `b`."""

from __future__ import annotations


def describe() -> str:
    from .messy_circular_b import NAME

    return f"a sees {NAME}"
