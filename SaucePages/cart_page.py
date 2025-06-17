from selenium.webdriver.common.by import By
from Saucehelp.saucehelper import Sauce_helper
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CartPage(Sauce_helper):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_items = (By.CLASS_NAME, "cart_item")
    checkout_button = (By.ID, "checkout")
    continue_shopping_button = (By.ID, "continue-shopping")
    remove_buttons = (By.XPATH, "//button[text()='Remove']")

    # Navigate to cart
    def go_to_cart(self):
        self.webelement_click(self.cart_icon)

    # Get number of items in the cart
    def get_cart_items_count(self):
        return self.get_elements_count(self.cart_items)

    # Click checkout
    def click_checkout(self):
        self.webelement_click(self.checkout_button)

    # Click continue shopping
    def click_continue_shopping(self):
        self.webelement_click(self.continue_shopping_button)

    # Remove all items from cart
    def remove_all_items(self):
        self.click_remove(self.remove_buttons)




