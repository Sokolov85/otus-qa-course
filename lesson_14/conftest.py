"""Module with fixtures for tests"""
import datetime
import logging
import urllib.parse
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
from selenium.webdriver.firefox.options import Options as Firefox_options
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from browsermobproxy import Server
from pages import LoginPage
from pages import AdminPage
from pages import ProductPage



def log():
    """Function for logging"""
    log_timestamp = str(datetime.datetime.now())[0:-4].replace('-', '.').replace(' ', '_').replace(':', '.')
    logger = logging.getLogger("WebTestApp")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_timestamp + "_logging.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("-----------------------------")
    logger.info("Program started")


class MyListener(AbstractEventListener):
    """event_firing_webdriver listener"""
    def __init__(self):
        self.log_timestamp = str(datetime.datetime.now())[0:-4].replace('-', '.').replace(' ', '_').replace(':', '.')
        self.log_filename = self.log_timestamp + '_file.log'
        self.logfile = open(self.log_filename, 'w')

        log()
        self.logger = logging.getLogger("WebTestApp")

    def _write_log_(self, entry):
        """Function for write information in logfile"""
        self.logfile.write(entry + '\n')

    def before_navigate_to(self, url, driver):
        print("Before navigate to {}".format(url))
        self._write_log_("Before navigate to {}".format(url))
        self.logger.info("Before navigate to {}".format(url))

    def after_navigate_to(self, url, driver):
        print("After navigate to {}".format(url))
        self._write_log_("After navigate to {}".format(url))
        self.logger.info("After navigate to {}".format(url))

    def before_find(self, by, value, driver):
        print("Before find {} {}".format(by, value))
        self._write_log_("Before find {} {}".format(by, value))
        self.logger.info("Before find {} {}".format(by, value))

    def after_find(self, by, value, driver):
        print("After find {} {}".format(by, value))
        self._write_log_("After find {} {}".format(by, value))
        self.logger.info("After find {} {}".format(by, value))

    def before_click(self, element, driver):
        print("Before click {}".format(element))
        self._write_log_("Before click {}".format(element.get_attribute("class")))
        self.logger.info("Before click {}".format(element.get_attribute("class")))

    def after_click(self, element, driver):
        print("After click")
        self._write_log_("After click")
        self.logger.info("After click")

    def before_execute_script(self, script, driver):
        print("Before execute script {}".format(script))
        self._write_log_("Before execute script {}".format(script))
        self.logger.info("Before execute script {}".format(script))

    def after_execute_script(self, script, driver):
        print("After execute script {}".format(script))
        self._write_log_("After execute script {}".format(script))
        self.logger.info("After execute script {}".format(script))

    def before_close(self, driver):
        print("Before close")
        self._write_log_("Before close")
        self.logger.info("Before close")

    def after_close(self, driver):
        print("After close")
        self._write_log_("After close")
        self.logger.info("After close")

    def before_quit(self, driver):
        print("Before quit")
        self._write_log_("Before quit")
        self.logger.info("Before quit")

    def after_quit(self, driver):
        print("After quit")
        self._write_log_("After quit")
        self.logger.info("After quit")

    def on_exception(self, exception, driver):
        screenshot_timestamp = str(datetime.datetime.now())[0:-4].replace('-', '.').replace(' ', '_').replace(':', '.')
        screenshot_filename = screenshot_timestamp + 'exception_screenshot.png'
        print("On exception {}".format(exception))
        self._write_log_("On exception {}".format(exception))
        driver.save_screenshot('screenshots/' + screenshot_filename)


def pytest_addoption(parser):
    """Addoption fixture: browser type, url, headless option"""
    parser.addoption(
        "--browser_type", action="store", default="ie", help="browser option"
    )
    parser.addoption(
        "--url", action="store", default="http://127.0.0.1/opencart/admin/", help="url option"
    )
    parser.addoption(
        "--window_option", action="store", default="window", help="window option"
    )
    parser.addoption(
        "--waits", action="store", default="no_wait", help="wait option"
    )
    parser.addoption(
        "--wait_time", action="store", default=10, help="wait time option"
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
def cmdopt_window(request):
    """window option"""
    return request.config.getoption("--window_option")


@pytest.fixture
def cmdopt_waits(request):
    """wait option"""
    return request.config.getoption("--waits")


@pytest.fixture
def cmdopt_wait_time(request):
    """wait time option"""
    return request.config.getoption("--wait_time")


@pytest.fixture
def get_driver(request, cmdopt_browser, cmdopt_window):
    """Fixture to create, return and close driver"""
    server = Server("C:\\Program Files (x86)\\browsermob-proxy\\bin\\browsermob-proxy", {"port": 9090})
    server.start()
    proxy = server.create_proxy()
    url = urllib.parse.urlparse(proxy.proxy).path
    driver = None
    if cmdopt_browser == "ie":
        driver = webdriver.Ie()
    elif cmdopt_browser == "firefox":
        if cmdopt_window == "headless":
            options = Firefox_options()
            options.add_argument("--headless")
            options.add_argument('--proxy-server={}'.format(url))
            driver = webdriver.Firefox(firefox_options=options)
        else:
            options = Firefox_options()
            options.add_argument('--proxy-server={}'.format(url))
            driver = webdriver.Firefox()
        proxy.new_har()
        request.addfinalizer(driver.quit)
    elif cmdopt_browser == "chrome":
        if cmdopt_window == "headless":
            options = Chrome_options()
            options.headless = True
            options.add_argument('--proxy-server={}'.format(url))
            driver = webdriver.Chrome(chrome_options=options)
            proxy.new_har()
            request.addfinalizer(driver.quit)
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server={}'.format(url))
            d = DesiredCapabilities.CHROME
            d['loggingPrefs'] = {'browser': 'ALL'}
            driver = webdriver.Chrome(desired_capabilities=d, chrome_options=chrome_options)
            proxy.new_har()
            ef_driver = EventFiringWebDriver(driver, MyListener())

            def fin():
                log_timestamp = str(datetime.datetime.now())[0:-4].replace('-', '.').replace(' ', '_').replace(':', '.')
                browserlog_filename = log_timestamp + '_browser_log_file.log'
                browserlogfile = open(browserlog_filename, 'w')
                print('-------------------------')
                for i in ef_driver.get_log('browser'):
                    print(i)
                    browserlogfile.write(str(i) + '\n')
                print(proxy.har)
                server.stop()
                ef_driver.quit

            request.addfinalizer(fin)
            return ef_driver
    else:
        return "unsupported browser"

    return driver


@pytest.fixture
def add_waits(get_driver, cmdopt_wait_time):
    """fixture for add waits"""
    driver = get_driver
    if cmdopt_waits == "waits":
        driver.implicitly_wait(cmdopt_wait_time)
    else:
        pass
    return driver


@pytest.fixture
def login_param():
    """fixture for storage login&password"""
    login = "admin"
    password = "admin"
    return login, password


@pytest.fixture()
def product_dataset():
    """fixture for storage product data"""
    product_name = 'Phone_1'
    product_meta_tag_title = 'Phone_1'
    product_model = 'Phone_1'
    return product_name, product_meta_tag_title, product_model


@pytest.fixture()
def product_dataset_more():
    """fixture for storage product data"""
    product_name = 'Phone_2'
    product_meta_tag_title = 'Phone_2'
    product_model = 'Phone_2'
    return product_name, product_meta_tag_title, product_model


@pytest.fixture
def login(add_waits, cmdopt_url, login_param):
    """fixture to login"""
    login_page = LoginPage(add_waits, cmdopt_url)
    login_page.navigate()
    login, password = login_param
    login_page.login(login, password)
    login_page.close_modal_window()
    return login_page.get_url()


@pytest.fixture
def login_negative(get_driver, cmdopt_url):
    """fixture to test negative scenario"""
    login_page = LoginPage(get_driver, cmdopt_url)
    login_page.navigate()
    login_page.login("admin", "admin1")
    current_result = login_page.get_alert_loginpage()
    expected_result = "No match for Username and/or Password."
    return expected_result, current_result


@pytest.fixture
def go_to_product_page(add_waits, login):
    """fixture to add product test"""
    admin_page = AdminPage(add_waits, login)
    admin_page.navigate()
    admin_page.close_modal_window()
    admin_page.choose_catalog()
    admin_page.choose_product()
    return admin_page.get_url()


@pytest.fixture
def add_product(add_waits, go_to_product_page, product_dataset):
    """fixture to add product test"""
    product_page = ProductPage(add_waits, go_to_product_page)
    product_page.navigate()
    product_name, product_meta_tag_title, product_model = product_dataset
    product_page.add_product(product_name, product_meta_tag_title, product_model)
    current_result = product_page.get_alert()
    expected_result = "Success: You have modified products!"
    return expected_result, current_result


@pytest.fixture
def modify_product(add_waits, go_to_product_page, product_dataset_more):
    """fixture to modify product test"""
    product_page = ProductPage(add_waits, go_to_product_page)
    product_page.navigate()
    product_name, product_meta_tag_title, product_model = product_dataset_more
    product_page.add_product(product_name, product_meta_tag_title, product_model)
    product_page.modify_product()
    current_result = product_page.get_alert()
    expected_result = "Success: You have modified products!"
    return expected_result, current_result


@pytest.fixture
def delete_product(add_waits, go_to_product_page, product_dataset_more):
    """fixture to delete product test"""
    product_page = ProductPage(add_waits, go_to_product_page)
    product_page.navigate()
    product_name, product_meta_tag_title, product_model = product_dataset_more
    product_page.add_product(product_name, product_meta_tag_title, product_model)
    product_page.delete_product()
    current_result = product_page.get_alert()
    expected_result = "Success: You have modified products!"
    return expected_result, current_result
