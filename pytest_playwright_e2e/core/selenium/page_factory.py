import importlib
from typing import Dict, Any


class PageFactory:
    """
    Centralized Page Factory for Selenium framework
    Manages all page objects and provides easy access
    """

    def __init__(self):
        self._page_cache: Dict[str, Any] = {}
        self._driver = None
        self._page_mapping = {}
        self._initialize_page_mapping()

    def _initialize_page_mapping(self):
        """Initialize the mapping of page names to their classes"""
        self._page_mapping = {
            'login': ('pytest_playwright_e2e.page_objects.selenium.login', 'LoginPage'),
            'dashboard': ('pytest_playwright_e2e.page_objects.selenium.dashboard', 'DashboardPage'),
            'radio_checkboxes': ('pytest_playwright_e2e.page_objects.selenium.radio_checkboxes', 'RadioCheckboxesPage'),
            'dropdown': ('pytest_playwright_e2e.page_objects.selenium.dropdown', 'DropdownPage'),
            'form': ('pytest_playwright_e2e.page_objects.selenium.form_page', 'FormPage'),
            'table': ('pytest_playwright_e2e.page_objects.selenium.table_page', 'TablePage'),
            'alert': ('pytest_playwright_e2e.page_objects.selenium.alert_page', 'AlertPage'),
            'window': ('pytest_playwright_e2e.page_objects.selenium.window_page', 'WindowPage'),
        }

    def init_pages(self, driver):
        """
        Initialize page factory with driver

        Args:
            driver: Selenium WebDriver instance
        """
        self._driver = driver
        self._page_cache.clear()
        return self

    def get_page(self, page_name: str):
        """
        Get page object by name with lazy loading and caching

        Args:
            page_name: Name of the page (e.g., 'login', 'dashboard', 'radio_checkboxes')

        Returns:
            Page object instance
        """
        if not self._driver:
            raise ValueError("Page Factory not initialized. Call init_pages(driver) first.")

        page_name = page_name.lower()

        # Return cached page if exists
        if page_name in self._page_cache:
            return self._page_cache[page_name]

        # Create new page instance
        page_instance = self._create_page_instance(page_name)
        if page_instance:
            self._page_cache[page_name] = page_instance
            return page_instance
        else:
            available_pages = ', '.join(self.get_available_pages())
            raise ValueError(f"Page '{page_name}' not found. Available pages: {available_pages}")

    def _create_page_instance(self, page_name: str):
        """Create page instance dynamically"""
        if page_name not in self._page_mapping:
            return None

        module_path, class_name = self._page_mapping[page_name]

        try:
            # Import the module dynamically
            module = importlib.import_module(module_path)
            # Get the class from module
            page_class = getattr(module, class_name)
            # Create instance with driver
            return page_class(self._driver)
        except (ImportError, AttributeError) as e:
            print(f"Warning: Could not create page '{page_name}': {e}")
            return None

    def get_available_pages(self) -> list:
        """Get list of all available pages"""
        return list(self._page_mapping.keys())

    def refresh_pages(self):
        """Clear cache and reinitialize pages"""
        self._page_cache.clear()

    def add_custom_page(self, page_name: str, module_path: str, class_name: str):
        """
        Add custom page to the factory

        Args:
            page_name: Name to reference the page
            module_path: Full module path
            class_name: Class name in the module
        """
        self._page_mapping[page_name.lower()] = (module_path, class_name)

    def get_driver(self):
        """Get current driver instance"""
        return self._driver
