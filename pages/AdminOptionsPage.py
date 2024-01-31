import time

from selenium.webdriver.common.by import By
from config.selenium_helper import Selenium_Helper


class AdminOptionsPage(Selenium_Helper):
    admin_menu_side_lbl = (By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']")

    ## Main Options on the top
    user_management_option = (
        By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'User Management')]")

    job_option = (By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Job')]")

    organization_option = (
        By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Organization')]")

    qualifications_option = (
        By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Qualifications')]")

    nationalities_option = (
        By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Nationalities')]")

    corporate_branding_option = (
        By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Corporate Branding')]")

    configuration_option = (
        By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Configuration')]")

    def __init__(self, driver):
        super().__init__(driver)

    def adminTopOptions(self):
        # Click on 'Admin' side menu
        self.webelement_click(self.admin_menu_side_lbl)  # Step 1
        time.sleep(5)

        # Validate title of the page as 'OrangeHRM'
        assert self.driver.title == 'OrangeHRM'  # Step 2

        # User Management - Validate option is displayed on Top Menu
        assert self.is_webelement_present(self.user_management_option) == True  # Step 3

        # Job - Validate option is displayed on Top Menu
        assert self.is_webelement_present(self.job_option) == True  # Step 4

        # Organization - Validate option is displayed on Top Menu
        assert self.is_webelement_present(self.organization_option) == True  # Step 5

        # Qualifications - Validate option is displayed on Top Menu
        assert self.is_webelement_present(self.qualifications_option) == True  # Step 7

        # Nationalities - Validate option is displayed on Top Menu
        assert self.is_webelement_present(self.nationalities_option) == True  # Step 8

        # Corporate Branding - Validate option is displayed on Top Menu
        assert self.is_webelement_present(self.corporate_branding_option) == True  # Step 9

        # Configuration - Validate option is displayed on Top Menu
        assert self.is_webelement_present(self.configuration_option) == True  # Step 10

        """
        User Management - Validate option is displayed on Top Menu
        Job - Validate option is displayed on Top Menu
        Organization - Validate option is displayed on Top Menu
        Qualifications - Validate option is displayed on Top Menu
        Nationalities - Validate option is displayed on Top Menu
        Corporate Branding - Validate option is displayed on Top Menu
        Configuration - Validate option is displayed on Top Menu      
        """
