import hub_worker


def test_package_imports() -> None:
    assert hub_worker.__version__
