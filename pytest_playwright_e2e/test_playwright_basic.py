import time

from playwright.sync_api import Page, expect


# to run test in headed mode use command: pytest test_playwright_basic::test_playwrightShortcut --headed
# to run from terminal on specific browser, use this command- pytest test_file.py --browser_name firefox
def test_playwright_basic(playwright):
    browser= playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page= context.new_page()
    page.goto("https://youtube.com")

def test_playwrightShortcut(page: Page):
    page.goto("https://youtube.com")

def test_login_page(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(10)

def test_verify_invalid_login_error_msg(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(10)

def test_verify_checkout_items(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct=page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(10)

def test_child_window_handle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as child_page:
        page.get_by_role("link", name= "Free Access to").click()
        new_page= child_page.value
        value= new_page.locator(".red").text_content()
        val= value.split("at")[1].strip()
        email = val.split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"

def test_hidden_btn(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name= "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    page.on("dialog", lambda d: d.accept())
    page.get_by_role("button", name="Confirm").click()

def test_handle_frames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    iframe_loc= page.frame_locator("#courses-iframe")
    iframe_loc.get_by_role("link", name="All Access plan")
    # Below is to verify text visible inside any locator. here in below code we are verifying inside entire body
    expect(iframe_loc.locator("body")).to_contain_text(" Happy Subscibers")

def test_selenium_practise(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index,row in enumerate(page.locator("th").all_text_contents()):
        if row=="Price":
            # cols = page.locator("tr>td").all_text_contents()
            rice_row=page.locator("tr").filter(has_text="Rice")
            print("price value is:"+rice_row.locator("td").nth(index).text_content())
            expect(rice_row.locator("td").nth(index)).to_have_text("37")
            # for c, col in enumerate(cols):
            #     if col == "Rice":
            #         page.locator("tr>td").nth()
            #         print(f"Rice price is:{cols[index+c]}")
            #         assert cols[index+c] == "37"
            #         break
            break

def test_selenium_practise_1(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).text_content() == "Price":
            print(f"price col value:{index}")
            row = page.locator("tr").filter(has_text="Rice")
            print("price value is:"+row.locator("td").nth(index).text_content())
            expect(row.locator("td").nth(index)).to_have_text("37")
            break

def test_mouse_hover(page: Page):
    page.locator("#mousehover").hover()
    page.get_by_role("link", name= "Top").click()







