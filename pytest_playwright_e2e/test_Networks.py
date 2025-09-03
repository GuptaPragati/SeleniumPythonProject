import time

from playwright.sync_api import Page, Playwright, expect

from utils.api_utils import ApiUtils

fake_order_response = {"data": [], "message":"No Orders"}

def intercept_response(route):
    route.fulfill(json=fake_order_response)

def intercept_url(route):
    route.continue_("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/682b3f385d3fd9ffa0f77147")

def test_mock_response(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", handler=intercept_url)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(10)
    order_text = page.locator(".mt-4").text_content()
    print(order_text)

    
def test_other_acc_order_details_not_visible(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", handler=intercept_url)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(10)
    msg= page.locator(".blink_me").text_content()
    print(msg)

def test_inject_session_token(playwright:Playwright):
    api_utils = ApiUtils()
    token =  api_utils.get_token(playwright)
    print(token)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(
        f"window.localStorage.setItem('token', '{token}');")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()