"""Module with fixtures for tests"""

import pytest


@pytest.fixture(scope='module', autouse=True)
def module_data():
    """Fixture for module"""
    print("\n    > Module setup")
    print(module_data.__doc__)

    yield

    print("\n   > Module teardown")


@pytest.fixture(scope='class', autouse=True)
def suite_data():
    """Fixture for testsuite"""
    print("\n   > Suite setup")
    print(suite_data.__doc__)

    yield

    print("\n   > Suite teardown")


@pytest.fixture(scope='function', autouse=True)
def case_data():
    """Fixture for testcase"""
    print("\n    > Case setup")
    print(case_data.__doc__)

    yield

    print("\n   > Case teardown")
