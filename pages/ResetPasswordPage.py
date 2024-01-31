import time

from selenium.webdriver.common.by import By
from config.selenium_helper import Selenium_Helper


class ResetPasswordPage(Selenium_Helper):
    # forgot_password_link = (By.XPATH, "//a[@href='http://www.orangehrm.com']")
    forgot_password_link = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")

    username_textfield = (By.XPATH, "//input[@name='username']")
    reset_password_button = (By.XPATH, "//button[@type='submit']")

    password_sent_lbl = (By.XPATH, "//h6[@class = 'oxd-text oxd-text--h6 orangehrm-forgot-password-title']")

    def __init__(self, driver):
        super().__init__(driver)

    def resetpassword(self, usernametext):
        # Step 1
        self.webelement_click(self.forgot_password_link)  # Click on Forgot Password Link

        # Step 2
        assert self.webelement_state(self.username_textfield) == True  # Username textbox is visible

        # Step 3
        self.webelement_enter(self.username_textfield, usernametext)  # Provide your username

        # Step 4
        self.webelement_click(self.reset_password_button)  # Click on Reset password
        # time.sleep(5)

        # Step 5
        # Get successful message saying "Reset Password link sent successfully"
        print(self.webelement_text(self.password_sent_lbl))
        assert self.webelement_text(self.password_sent_lbl) == "Reset Password link sent successfully"
