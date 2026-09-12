"""The few tests in this repository that actually work.

Their job is to give the CI something green to report. The interesting fixture
here is `test_flaky.py` -- three unreliable tests plus a control -- and the
repository's own workflow deliberately does not run that file:

    it exists so the *pipeline* can practise telling "flaky" apart from
    "broken". A repo whose own gate is red on every push cannot be used as a
    practice target, and the roadmap does require all three practice
    repositories to have a green CI. So the flakiness is kept in the file and
    excluded from this repository's gate, on purpose, with this comment.
"""

from __future__ import annotations

from legacy_py2_notes import legacy_has_key


def test_legacy_has_key_finds_present_key() -> None:
    assert legacy_has_key({"a": 1}, "a") is True


def test_legacy_has_key_reports_absent_key() -> None:
    assert legacy_has_key({"a": 1}, "b") is False


def test_importing_the_god_module_does_not_explode() -> None:
    import god_module

    assert god_module.step_01(2) > 0
