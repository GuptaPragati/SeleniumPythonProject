from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[placeholder='Username']")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("input#login-button")
        self.products_header = page.locator("//span[text()='Products']")
        self.error_message = page.locator("[data-test='error']")  # Example

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_failed(self):
        expect(self.error_message).to_be_visible()

    def assert_login_success(self):
        assert self.products_header.is_visible(), "User is unable to login"