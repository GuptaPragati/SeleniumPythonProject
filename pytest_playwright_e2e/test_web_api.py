import json

import pytest
from playwright.sync_api import Playwright, expect
from playwright.sync_api import Page

from .page_objects.login import LoginPage
from .utils.api_utils import ApiUtils

with open('data/creds.json') as f:
    creds = json.load(f)
    cred_list = creds['user_creds']


# use command to run smoke test cases tag: pytest -m smoke
# to run a test which contains login_info in the test name then use command : pytest -k login_info
# to run test cases in parallel mode, install plugin- pip install pytest-xdist and then use command: pytest -n 3
# to generate report, install plugin - pip install pytest-html and then use command: pytest -n 2 --html=report.html
# to capture screenshots and logs use command: pytest --tracing on , pytest --browser_name chrome -m smoke -n 3 --tracing on --html=report.html

@pytest.mark.smoke
@pytest.mark.parametrize('user_creds', cred_list)
def test_e2e_login_info(playwright: Playwright, launch_browser, user_creds):
    print(user_creds)
    api_utils = ApiUtils()
    order_id= api_utils.create_order(playwright, user_creds)
    loginPage = LoginPage(launch_browser)
    loginPage.navigate()
    dashPage= loginPage.login(user_creds)
    orderHistory = dashPage.openOrders()
    orderDetails=orderHistory.verify_and_select_order(order_id)
    orderDetails.verify_order_msg("Thank you for Shopping With Us")
    # context.close() # to free up the memory