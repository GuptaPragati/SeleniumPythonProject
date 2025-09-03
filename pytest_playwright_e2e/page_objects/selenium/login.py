from pytest_playwright_e2e.core.selenium.selenium_driver import SeleniumDriver
from pytest_playwright_e2e.page_objects.selenium.dashboard import DashboardPage


class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.email_input_id = "userEmail"
        self.password_input_id = "userPassword"
        self.login_btn_id = "login"

    def login(self, user_creds):
        self.inputText(user_creds['user_email'], self.email_input_id, "id")
        self.inputText(user_creds['user_password'], self.password_input_id, "id")
        self.elementClick(self.login_btn_id, "id")
        return DashboardPage(self.driver)