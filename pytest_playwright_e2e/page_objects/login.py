from .dashboard import DashboardPage

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.get_by_placeholder("email@example.com")
        self.password_input = page.get_by_placeholder("enter your passsword")
        self.login_btn = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self, user_creds):
        self.email_input.fill(user_creds['user_email'])
        self.password_input.fill(user_creds['user_password'])
        self.login_btn.click()
        return DashboardPage(self.page)