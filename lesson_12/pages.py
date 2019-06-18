"""Module contains Page-object classes"""
from locators import MainPageLocators
from locators import ConctructorPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    """Base page class"""
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def _wait_element_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException) as err:
            raise err
            return False

    def _get_title_(self):
        return self.driver.title

    def _click_close_modal_window_button_(self):
        self._wait_element_(*MainPageLocators.CLOSE_MODAL_WINDOW).click()

    def get_title(self):
        """public method to get page title"""
        return self._get_title_()

    def navigate(self):
        """Public method to page navigate"""
        self.driver.get(self.url)
        self.driver.maximize_window()

    def close_modal_window(self):
        """public method to close modal window"""
        self._click_close_modal_window_button_()

    def _get_url_(self):
        return self.driver.current_url

    def _get_token_(self):
        text = self.get_url()
        start = (text.find('token=') + 6)
        return str(text[start:])

    def get_url(self):
        """public method to get window url"""
        return self._get_url_()

    def get_token(self):
        """public method to get token"""
        return self._get_token_()


class LoginPage(BasePage):
    """Login page class"""
    def _get_alert_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.alert_is_present())
            element = self.driver.find_element(by, value)
            return element.text
        except NoAlertPresentException as err:
            raise err
            return False

    def _set_username_(self, username, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            self.driver.find_element(by, value).send_keys(username)
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _set_password_(self, password, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            self.driver.find_element(by, value).send_keys(password)
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def _click_login_button_(self, by, value, delay=5):
        try:
            WebDriverWait(self.driver, delay).until(EC.text_to_be_present_in_element((by, value), "Войти"))
            self.driver.find_element(by, value).click()
        except (NoSuchElementException, TimeoutException) as err:
            raise err

    def get_alert(self):
        """public method to get page alert"""
        return self._get_alert_(*MainPageLocators.ALERT)

    def login(self, username, password):
        """public method to login"""
        self._set_username_(username, *MainPageLocators.INPUT_USERNAME)
        self._set_password_(password, *MainPageLocators.INPUT_PASSWORD)
        self._click_login_button_(*MainPageLocators.BUTTON_LOGIN)


class ConstuctorPage(BasePage):
    """Constructor page class"""
    def navigate(self):
        """Public method to page navigate"""
        token = self.get_token()
        self.driver.get(ConctructorPageLocators.CONSTRUCTOR_PAGE_URL + token)
        self.driver.maximize_window()

    def _get_element_y_coordinates_(self, by, value):
        element = self.driver.find_element(by, value)
        element_y_coordinates = element.location['y']
        return element_y_coordinates

    def get_element_y_coordinates_before_dnd(self):
        """Public method to get y coordinate before d&d"""
        return self._get_element_y_coordinates_(*ConctructorPageLocators.PRODUCT_ITEM_1)

    def get_element_y_coordinates_after_dnd(self):
        """Public method to get y coordinate after d&d"""
        return self._get_element_y_coordinates_(*ConctructorPageLocators.PRODUCT_ITEM_2)

    def dnd(self):
        """Public method to drag&drop"""
        source_element = self.driver.find_element(*ConctructorPageLocators.PRODUCT_ITEM_1)
        dest_element = self.driver.find_element(*ConctructorPageLocators.PRODUCT_ITEM_2)
        ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()
