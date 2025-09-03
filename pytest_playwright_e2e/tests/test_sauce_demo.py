import pytest

from pytest_playwright_e2e.core.base_test import BaseTest
from pytest_playwright_e2e.core.page_factory import BasePageFactory


class TestSauceDemo(BaseTest):

    @pytest.mark.parametrize(("username", "password"), [("standard_user", "secret_sauce"),
                                                      ("problem_user", "secret_sauce")])
    def test_sauce_login(self, username, password):
        self.login_page.navigate()
        self.login_page.login(username, password)
        self.login_page.assert_login_success()