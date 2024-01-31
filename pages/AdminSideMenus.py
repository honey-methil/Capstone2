from selenium.webdriver.common.by import By
from config.selenium_helper import Selenium_Helper


class AdminMenusPage(Selenium_Helper):
    # admin_menu_side_lbl = (By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']")

    ## Menus on the Side Panel
    admin_option = (
        By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']")

    pim_option = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")

    leave_option = (
        By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveModule']")

    time_option = (
        By.XPATH, "//a[@href='/web/index.php/time/viewTimeModule']")

    recruitment_option = (
        By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']")

    my_info__option = (
        By.XPATH, "//a[@href='/web/index.php/pim/viewMyDetails']")

    performance_option = (
        By.XPATH, "//a[@href='/web/index.php/performance/viewPerformanceModule']")

    dashboard_option = (
        By.XPATH, "//a[@href='/web/index.php/dashboard/index']")

    directory_option = (
        By.XPATH, "//a[@href='/web/index.php/directory/viewDirectory']")

    maintenance_option = (
        By.XPATH, "//a[@href='/web/index.php/maintenance/viewMaintenanceModule']")

    buzz_option = (
        By.XPATH, "//a[@href='/web/index.php/buzz/viewBuzz']")

    def __init__(self, driver):
        super().__init__(driver)

    def adminMenuOptions(self):
        # Admin - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.admin_option) == True  # Step 1

        # PIM - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.pim_option) == True  # Step 2

        # Leave - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.leave_option) == True  # Step 3

        # Time - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.time_option) == True  # Step 4

        # Recruitment - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.recruitment_option) == True  # Step 5

        # My Info - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.my_info__option) == True  # Step 6

        # Performance - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.performance_option) == True  # Step 7

        # Dashboard - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.dashboard_option) == True  # Step 8

        # Directory - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.directory_option) == True  # Step 9

        # Maintenance - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.maintenance_option) == True  # Step 10

        # Buzz - Validate option is displayed on Side Menu
        assert self.is_webelement_present(self.buzz_option) == True  # Step 11
