from conftest import *
from pages.LoginPage import LoginPage
from pages.AdminOptionsPage import AdminOptionsPage
import time

from pages.ResetPasswordPage import ResetPasswordPage

"""
Test Case ID: TC_PIM_02
Test Objective:
    Header validation on Admin Page
    URL = https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Pre Condition
    Launch URL and Login as 'Admin'

Steps
    Login as 'Admin'
    Click on 'Admin' side menu
    Validate title of the page as 'OrangeHRM'
    Validate below options are displayed on Top Menu
        User Management
        Job
        Organization
        Qualifications
        Nationalities
        Corporate Banking
        Configuration

Expected
    User should be able to see the above mentioned Admin Page Headers on Admin Page
"""


@pytest.mark.usefixtures("browser_setup")
class Test_Login:
    admin_username = "Admin"
    admin_password = "admin123"

    # Opening a browser
    def setup_class(self):
        self.driver.get(BaseUrl)  # Launch URL
        self.login_page = LoginPage(self.driver)  # Login as Admin
        self.admin_options_page = AdminOptionsPage(self.driver)  # Validate Admin Options

    # Logging in
    # Middle we have a test case

    def test_admin_main_options(self):
        self.login_page.login(self.admin_username, self.admin_password)
        self.admin_options_page.adminTopOptions()

        # self.admin_options_page.adminTopOptions(self)
        time.sleep(5)

    # Closing the browser
    # Lastly we have the tear down class
    def teardown_class(self):
        self.driver.quit()
