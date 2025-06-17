import pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from Saucehelp.saucehelper import Sauce_helper
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
class InventoryPage(Sauce_helper):
    # locators
    inventory_container = (By.ID,"inventory_container")
    inventory_items = (By.CLASS_NAME,"inventory_item")
    page_title = (By.CLASS_NAME,"title")
    menu_button = (By.ID,"react-burger-menu-btn")
    logout_link = (By.ID,"logout_sidebar_link")
    add_to_cart_buttons = (By.CLASS_NAME,"btn_inventory")

    def __init__(self, driver):
        super().__init__(driver)


    def is_inventory_loaded(self):
        return self.get_element(self.inventory_container).is_displayed()

    def get_inventory_item_count(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(self.inventory_items))
        items = self.driver.find_elements(*self.inventory_items)
        return len(items)

    def get_page_title(self):
        return self.get_element(self.page_title).text

    def get_current_url(self):
        return self.driver.current_url

    def logout(self):
        self.webelement_click(self.menu_button)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logout_link))
        self.webelement_click(self.logout_link)


    def add_all_items_to_cart(self):
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        for button in buttons:
            button.click()

    def remove_all_items_from_cart(self):
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        for button in buttons:
            button.click()





