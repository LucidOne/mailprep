import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--hitl", action="store_true", default=False, help="Human/Hardware in the Loop"
    )

def pytest_collection_modifyitems(config, items):
    if config.getoption("--hitl"):
        return
    skip_hitl = pytest.mark.skip(reason="Human/Hardware in the Loop tests require the `--hitl` option")
    for item in items:
        if "hitl" in item.keywords:
            item.add_marker(skip_hitl)
