import pytest


@pytest.fixture(scope='module', autouse=True)
def module_data():
    print("\n    > Module setup")

    yield

    print("\n   > Module teardown")


@pytest.fixture(scope='class')
def suite_data():
    print("\n   > Suite setup")

    yield

    print("\n   > Suite teardown")


@pytest.fixture(scope='function')
def case_data():
    print("\n    > Case setup")

    yield

    print("\n   > Case teardown")