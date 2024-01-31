from selenium.webdriver.common.by import By
from config.selenium_helper import Selenium_Helper


class LoginPage(Selenium_Helper):
    email_textfield = (By.XPATH, "//input[@name = 'username']")
    password_textfield = (By.XPATH, "//input[@name = 'password']")
    login_button = (By.XPATH, "//button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, usernametext, passwordtext):
        self.webelement_enter(self.email_textfield, usernametext)
        self.webelement_enter(self.password_textfield, passwordtext)
        self.webelement_click(self.login_button)



