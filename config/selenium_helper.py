from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *


class Selenium_Helper:

    # Driver
    def __init__(self, driver):
        self.driver = driver

    # Method to enter in web element
    def webelement_enter(self, locator, text):
        wait = WebDriverWait(self.driver, timeout=20, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        element = wait.until(ec.visibility_of_element_located(locator))
        element.send_keys(text)

    # Method to click on web element
    def webelement_click(self, locator):
        wait = WebDriverWait(self.driver, timeout=20, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        element = wait.until(ec.visibility_of_element_located(locator))
        element.click()

    # Method to find state of the textbox
    def webelement_state(self, locator):
        wait = WebDriverWait(self.driver, timeout=20, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        element = wait.until(ec.visibility_of_element_located(locator))
        return element.is_displayed()

    # Method to find text of the element
    def webelement_text(self, locator):
        wait = WebDriverWait(self.driver, timeout=20, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        element = wait.until(ec.visibility_of_element_located(locator))
        return element.text

    # Method to find if Element present
    def is_webelement_present(self, locator):
        wait = WebDriverWait(self.driver, timeout=20, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        element = wait.until(ec.visibility_of_element_located(locator))
        if element is not None:
            print("Element Found")
            return True
        else:
            print("Element not found")
            return False
