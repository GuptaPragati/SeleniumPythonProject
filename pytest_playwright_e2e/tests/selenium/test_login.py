import pytest

from pytest_playwright_e2e.tests.selenium.base_test import BaseTest
from pytest_playwright_e2e.utils.json_parser import JsonParser


class TestLogin(BaseTest):
    @pytest.mark.parametrize("users", JsonParser.get_user_creds())
    def test_login_feature(self, users):
        self.login_page.login(users)