"""The other half of the circular import."""

from __future__ import annotations

NAME = "b"


def describe() -> str:
    from .messy_circular_a import describe as describe_a

    return f"b sees {describe_a()}"
