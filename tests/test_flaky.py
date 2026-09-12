"""Three flaky tests, each flaky for a different realistic reason.

The pipeline must be able to tell "this test is unreliable" apart from "this
code is broken". A single red run cannot do that; these fixtures exist to make
the difference visible.
"""

from __future__ import annotations

import datetime as dt
import random
import time

import pytest


def test_flaky_time_of_day() -> None:
    """Fails between 00:00 and 00:05 UTC. A classic 'works on my machine'."""
    now = dt.datetime.now(dt.timezone.utc)
    assert not (now.hour == 0 and now.minute < 5)


def test_flaky_random() -> None:
    """Fails roughly 30% of the time."""
    assert random.random() > 0.3


def test_flaky_slow_machine() -> None:
    """Fails when the machine is busy (CI runners, mostly)."""
    started = time.perf_counter()
    total = sum(range(200_000))
    assert total > 0
    assert time.perf_counter() - started < 0.002


@pytest.mark.parametrize("index", range(4))
def test_not_flaky_but_noisy(index: int) -> None:
    """A control: this one always passes, so the report can show the contrast."""
    assert index >= 0
