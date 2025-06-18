import pytest
import json
from SaucePages.login_page import LoginPage
import conftest



@pytest.mark.usefixtures("driver")
class TestLogin:

    def load_validdata():
        with open('TestData/valid_data.json') as f:
            data = json.load(f)
        return [(entry['username'],entry['password']) for entry in data]

    @pytest.mark.parametrize("username, password", load_validdata())
    def test_valid_login(self, driver,username,password):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        assert "inventory" in driver.current_url, "User should be redirected to inventory page on successful login"

    def test_invalid_login(self, driver):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.enter_username("invalid_user")
        login_page.enter_password("invalid_pass")
        login_page.click_login()
        error_message = login_page.get_error_message()
        assert "do not match" in error_message, f"Unexpected error message: {error_message}"

    def test_username_placeholder(self, driver):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        placeholder = login_page.get_username_placeholder()
        assert placeholder.lower() == "username", f"Username placeholder should be 'Username', got '{placeholder}'"

    def test_password_placeholder(self, driver):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        placeholder = login_page.get_password_placeholder()
        assert placeholder.lower() == "password", f"Password placeholder should be 'Password', got '{placeholder}'"

    def test_login_button_text(self, driver):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        button_text = login_page.get_login_button_text()
        assert button_text.lower() == "login", f"Login button text should be 'Login', got '{button_text}'"


