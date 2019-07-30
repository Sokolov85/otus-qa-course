"""Module with fixtures for tests"""
import pytest
from selenium import webdriver
from LoginPage import LoginPage


def pytest_addoption(parser):
    """Addoption fixture: browser type, url, headless option"""
    parser.addoption(
        "--browser_type", action="store", default="ie", help="browser option"
    )
    parser.addoption(
        "--url", action="store", default="http://demo23.opencart.pro/admin", help="url option"
    )


@pytest.fixture
def cmdopt_browser(request):
    """browser type option"""
    return request.config.getoption("--browser_type")


@pytest.fixture
def cmdopt_url(request):
    """url options"""
    return request.config.getoption("--url")


@pytest.fixture
def username():
    """username fixture"""
    return "ssokolov1"


@pytest.fixture
def automate_key():
    """automate_key fixture"""
    return "vqP7yCNgq3RMksBhrXkK"


@pytest.fixture
def get_driver(request, cmdopt_browser, username, automate_key):
    """Fixture to create, return and close driver"""
    driver = None
    if cmdopt_browser == "ie":
        desiredcapabilities = {
            'browser': 'IE',
            'browser_version': '11.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Sample Test'
        }
    elif cmdopt_browser == "firefox":
        desiredcapabilities = {
            'browser': 'Firefox',
            'browser_version': '69.0 beta',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Sample Test'
        }
    elif cmdopt_browser == "chrome":
        desiredcapabilities = {
            'browser': 'Chrome',
            'browser_version': '62.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Sample Test'
        }
    else:
        return "unsupported browser"
    driver = webdriver.Remote(
            command_executor='http://{}:{}@hub.browserstack.com:80/wd/hub'.format(username, automate_key),
            desired_capabilities=desiredcapabilities)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver


@pytest.fixture
def login_positive(get_driver, cmdopt_url):
    """fixture to test positive scenario"""
    login_page = LoginPage(get_driver, cmdopt_url)
    login_page.navigate()
    login_page.login("demo", "demo")
    current_result = login_page.get_title()
    expected_result = "Панель состояния"
    return expected_result, current_result


@pytest.fixture
def login_negative(get_driver, cmdopt_url):
    """fixture to test negative scenario"""
    login_page = LoginPage(get_driver, cmdopt_url)
    login_page.navigate()
    login_page.login("demo", "demon1")
    current_result = login_page.get_alert()
    expected_result = "Такой логин и/или пароль не существует!"
    return expected_result, current_result


@pytest.fixture
def empty_form(get_driver, cmdopt_url):
    """fixture to empty login form scenario"""
    login_page = LoginPage(get_driver, cmdopt_url)
    login_page.navigate()
    login_page.login("", "")
    current_result = login_page.get_alert()
    expected_result = "Такой логин и/или пароль не существует!"
    return expected_result, current_result
