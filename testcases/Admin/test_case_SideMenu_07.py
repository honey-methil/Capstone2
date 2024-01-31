from conftest import *
from pages.LoginPage import LoginPage
from pages.AdminSideMenus import AdminMenusPage
import time

from pages.ResetPasswordPage import ResetPasswordPage

"""
Test Case ID: TC_PIM_03
Test Objective:
    Main Menu validation on Admin Page
    URL = https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Pre Condition
    Launch URL and Login as 'Admin'

Steps
    Login as 'Admin'
    Validate below Menu options (on side pane) are displayed
        Admin
        PIM
        Leave
        Time
        Recruitment
        My Info
        Performance
        Dashboard
        Directory
        Maintenance
        Buzz

Expected
    User should be able to see the above mentioned Admin Page Menu Items on Admin Page
"""


@pytest.mark.usefixtures("browser_setup")
class Test_Login:
    admin_username = "Admin"
    admin_password = "admin123"

    # Opening a browser
    def setup_class(self):
        self.driver.get(BaseUrl)  # Launch URL
        self.login_page = LoginPage(self.driver)  # Login as Admin
        self.admin_side_menu_page = AdminMenusPage(self.driver)  # Validate Admin Options

    # Logging in
    # Middle we have a test case

    def test_admin_main_options(self):
        self.login_page.login(self.admin_username, self.admin_password)
        self.admin_side_menu_page.adminMenuOptions()

        # self.admin_options_page.adminTopOptions(self)
        time.sleep(5)

    # Closing the browser
    # Lastly we have the tear down class
    def teardown_class(self):
        self.driver.quit()
