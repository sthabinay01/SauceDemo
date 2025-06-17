from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Sauce_helper:

    def __init__(self, driver):
        self.driver = driver

    def webelement_enter(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    # for clicking buttons
    def webelement_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    # for count
    def get_elements_count(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        elements = self.driver.find_elements(*locator)
        return len(elements)

    # for removing
    def click_remove(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        elements = self.driver.find_elements(*locator)
        for element in elements:
            element.click()

    # for getting value locator
    def get_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
