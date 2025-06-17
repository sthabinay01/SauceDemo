from selenium.webdriver.common.by import By
from Saucehelp.saucehelper import Sauce_helper

class LoginPage(Sauce_helper):
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_msg = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.webelement_enter(self.username_input, username)

    def enter_password(self, password):
        self.webelement_enter(self.password_input, password)

    def click_login(self):
        self.webelement_click(self.login_button)

    def get_error_message(self):
        return self.get_element(self.error_msg).text

    def get_username_placeholder(self):
        return self.get_element(self.username_input).get_attribute("placeholder")

    def get_password_placeholder(self):
        return self.get_element(self.password_input).get_attribute("placeholder")

    def get_login_button_text(self):
        return self.get_element(self.login_button).get_attribute("value")

    def is_login_page_displayed(self):
        return self.get_element(self.username_input).is_displayed()

