from conftest import *
from pages.LoginPage import LoginPage
import time

from pages.ResetPasswordPage import ResetPasswordPage

"""
Test Case ID: TC_PIM_01
Test Objective:
    Forgot password link validation on login page
    URL = https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Pre Condition
    Launch URL
    Orange HRM site is launched
    Click on Forgot Password Link

Steps
    Username textbox is visible
    Provide your username
    Click on Reset password

Expected
    User should be able to see the username box
    On click of reset password link, get successful message saying "Reset Passsword link sent successfully"
"""


@pytest.mark.usefixtures("browser_setup")
class Test_Login:
    valid_username = "Admin"
    valid_password = "admin123"

    # Opening a browser
    def setup_class(self):
        self.driver.get(BaseUrl)  # Launch URL
        self.reset_pwd_page = ResetPasswordPage(self.driver)

    # Logging in
    # Middle we have a test case

    def test_reset_password(self):
        self.reset_pwd_page.resetpassword(self.valid_username)
        time.sleep(5)

    # Closing the browser
    # Lastly we have the tear down class
    def teardown_class(self):
        self.driver.quit()
