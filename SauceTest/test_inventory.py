import pytest

from SaucePages.inventory_page import InventoryPage
from SaucePages.login_page import LoginPage


@pytest.mark.usefixtures("driver")
class TestInventory:

    def test_inventory_page_and_logout(self, driver):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory_page = InventoryPage(driver)

        # Verify current URL
        assert "inventory" in driver.current_url, "URL should contain 'inventory' after login"

        # Verify page title
        assert inventory_page.get_page_title() == "Products", "Page title should be 'Products'"

        # Verify 6 inventory items
        item_count = inventory_page.get_inventory_item_count()
        assert item_count == 6, f"Expected 6 items, but found {item_count}"

        # Perform logout
        inventory_page.logout()

        # Verify redirected back to login
        assert "saucedemo.com" in driver.current_url
        assert "login" in driver.current_url or driver.find_element("id", "login-button").is_displayed(), "Should return to login page after logout"

