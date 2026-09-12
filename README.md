# legacy-billing

> **Status: stable.** Fully migrated to Python 3, all tests green, config lives
> in `config.yaml`, and `report_v2()` is the supported entry point.

*(Everything above is false on purpose. This repository is the "messy" practice
fixture for `repo-autopilot`; the README disagreeing with the code is one of the
things the pipeline is supposed to notice.)*

Actually:
- it is still Python-2 flavoured in places,
- `report_v2()` does not exist (only `report_old()`),
- there is no `config.yaml`,
- `tests/test_flaky.py` is flaky,
- `god_module.py` is 800 lines and everything imports it.
