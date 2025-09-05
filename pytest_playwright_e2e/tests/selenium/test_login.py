import time

import pytest

from pytest_playwright_e2e.tests.selenium.base_test import BaseTest
from pytest_playwright_e2e.utils.json_parser import JsonParser

# class TestLogin(BaseTest):
#     @pytest.mark.parametrize("users", JsonParser.get_user_creds())
#     def test_login_feature(self, users):
#         self.login_page.login(users)





class TestLogin(BaseTest):
    """Updated login test using centralized page factory"""

    @pytest.mark.parametrize("users", JsonParser.get_user_creds())
    def test_login_feature(self, users):
        """Test login with parameterized user data"""
        # Using direct page access from base class
        self.login_page.login(users)
        time.sleep(3)
        # Verify we're on dashboard
        assert "dashboard" in self.get_current_url().lower()

    def test_login_with_invalid_credentials(self):
        """Test login with invalid credentials"""
        invalid_creds = {
            'user_email': 'invalid@test.com',
            'user_password': 'wrongpassword'
        }

        # Attempt login
        self.login_page.login(invalid_creds)

        # Should remain on login page or show error
        current_url = self.get_current_url()
        assert "login" in current_url.lower() or "client" in current_url.lower()
