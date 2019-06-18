"""Module with testsuite of tests for JSON API tests"""


class TestSuite:
    """Testsuite for drag$drop tests on custom menu page"""
    def test_login(self, login, drag_drop):
        """add product test positive scenario"""
        login
        expected_result, current_result = drag_drop
        assert expected_result == current_result
