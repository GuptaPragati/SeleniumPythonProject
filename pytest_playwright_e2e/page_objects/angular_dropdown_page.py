from playwright.sync_api import Page, expect


class AngularDropdownPage:
    def __init__(self, page: Page):
        self.page = page
        self.dropdown_field = ".select-container > input"
        self.preview_frame_loc = page.frame("previewFrame")

    def navigate(self):
        self.page.goto("https://stackblitz.com/edit/angular-dfy6hf?file=src%2Fapp%2Fapp.component.ts")

    def click_dropdown(self):
        dropdown= self.preview_frame_loc.locator(self.dropdown_field)
        dropdown.click()

    def select_dropdown(self, value):
        self.preview_frame_loc.locator(f"//ul[@class='select-menu box']/li[contains(., '{value}')]").click()

    def select_dropdwon_for_loop(self, value):
        list= self.preview_frame_loc.locator("ul[role='listbox'] > li")
        for c in list.all():
            if value in c.text_content():
                c.click()

    def verify_selected_option(self, value):
        expect(self.page.frame(self.preview_frame_loc).locator(self.dropdown_field)).to_have_value(value)