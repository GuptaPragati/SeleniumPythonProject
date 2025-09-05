from pytest_playwright_e2e.core.selenium.selenium_driver import SeleniumDriver


class FormPage(SeleniumDriver):
    """Form page for testing form interactions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Form elements
        self.name_input = "name"
        self.email_input = "email"
        self.phone_input = "phone"
        self.address_textarea = "address"
        self.gender_radio = "gender"
        self.hobbies_checkbox = "hobbies"
        self.submit_button = "submit"

    def navigate(self):
        """Navigate to form page"""
        self.driver.get("https://www.letskodeit.com/practice")

    def fill_form(self, form_data):
        """
        Fill complete form with data

        Args:
            form_data: Dictionary containing form field data
        """
        if 'name' in form_data:
            self.inputText(form_data['name'], self.name_input, "id")

        if 'email' in form_data:
            self.inputText(form_data['email'], self.email_input, "id")

        if 'phone' in form_data:
            self.inputText(form_data['phone'], self.phone_input, "id")

        if 'address' in form_data:
            self.inputText(form_data['address'], self.address_textarea, "id")

    def select_gender(self, gender):
        """Select gender radio button"""
        gender_xpath = f"//input[@value='{gender}']"
        self.elementClick(gender_xpath, "xpath")

    def select_hobbies(self, hobbies_list):
        """Select multiple hobbies"""
        for hobby in hobbies_list:
            hobby_xpath = f"//input[@value='{hobby}']"
            self.elementClick(hobby_xpath, "xpath")

    def submit_form(self):
        """Submit the form"""
        self.elementClick(self.submit_button, "id")
