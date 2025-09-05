from pytest_playwright_e2e.core.selenium.page_factory import PageFactory


class SeleniumBaseTest:
    """
    Enhanced base test class with centralized page factory for Selenium
    """

    def setup_pages(self, driver):
        """
        Setup page factory with driver

        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.page_factory = PageFactory()
        self.page_factory.init_pages(driver)

    def __getattr__(self, name):
        """
        Dynamic page access - automatically create page properties on demand
        This allows direct access like self.any_page_name_page without explicit initialization
        """
        if name.endswith('_page'):
            page_name = name[:-5]  # Remove '_page' suffix
            if page_name in self.page_factory.get_available_pages():
                try:
                    page_obj = self.page_factory.get_page(page_name)
                    setattr(self, name, page_obj)  # Cache for future use
                    return page_obj
                except Exception as e:
                    print(f"Warning: Could not create {name}: {e}")
                    return None

        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def get_page(self, page_name: str):
        """
        Get any page object by name

        Args:
            page_name: Name of the page

        Returns:
            Page object instance
        """
        return self.page_factory.get_page(page_name)

    def navigate_to(self, url: str):
        """
        Navigate to URL

        Args:
            url: URL to navigate to
        """
        if self.driver:
            self.driver.get(url)

    def get_current_url(self) -> str:
        """Get current page URL"""
        return self.driver.current_url if self.driver else ""

    def get_page_title(self) -> str:
        """Get current page title"""
        return self.driver.title if self.driver else ""

    def refresh_page(self):
        """Refresh current page"""
        if self.driver:
            self.driver.refresh()

    def back(self):
        """Go back to previous page"""
        if self.driver:
            self.driver.back()

    def forward(self):
        """Go forward to next page"""
        if self.driver:
            self.driver.forward()


