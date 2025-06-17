import pytest
from SaucePages.login_page import LoginPage
from SaucePages.inventory_page import InventoryPage
from SaucePages.cart_page import CartPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
class TestCart:

    def test_add_and_remove_all_items(self, driver):
        driver.get("https://www.saucedemo.com/")

        # Login
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        # Inventory Page
        inventory = InventoryPage(driver)
        assert inventory.is_inventory_loaded()

        # Add all items
        inventory.add_all_items_to_cart()

        # Go to cart and verify 6 items are added
        cart = CartPage(driver)
        cart.go_to_cart()

        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 6

        # Go back to inventory page
        driver.back()

        # Remove all items
        inventory.remove_all_items_from_cart()

        # Go to cart again and verify cart is empty
        cart.go_to_cart()
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 0


