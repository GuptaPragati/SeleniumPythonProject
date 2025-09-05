from pytest_playwright_e2e.core.selenium.selenium_driver import SeleniumDriver


class WindowPage(SeleniumDriver):
    """Window page for testing window/tab operations"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.open_window_button = "openwindow"
        self.open_tab_button = "opentab"

    def navigate(self):
        """Navigate to window handling page"""
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    def open_new_window(self):
        """Click to open new window"""
        self.elementClick(self.open_window_button, "id")

    def open_new_tab(self):
        """Click to open new tab"""
        self.elementClick(self.open_tab_button, "id")

    def get_all_window_handles(self):
        """Get all window handles"""
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        """Switch to specific window"""
        self.driver.switch_to.window(window_handle)

    def switch_to_new_window(self):
        """Switch to the newest opened window"""
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

    def close_current_window(self):
        """Close current window"""
        self.driver.close()

    def switch_to_main_window(self, main_window_handle):
        """Switch back to main window"""
        self.driver.switch_to.window(main_window_handle)
