"""Module with testsuite of tests for JSON API tests"""
from LoginPage import LoginPage


class TestSuite:
    """Testsuite for base page tests"""

    def test_login_positive(self, get_driver, cmdopt_url):
        """login test positive scenario"""
        login_page = LoginPage(get_driver, cmdopt_url)
        login_page.navigate()
        login_page.login("admin", "admin")
        assert "Dashboard" in login_page.get_title()

    def test_login_negative(self, get_driver, cmdopt_url):
        """login test negative scenario"""
        login_page = LoginPage(get_driver, cmdopt_url)
        login_page.navigate()
        login_page.login("admin", "admin1")
        assert "No match for Username and/or Password." in login_page.get_alert()
