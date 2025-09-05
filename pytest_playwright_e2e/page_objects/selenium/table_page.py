from pytest_playwright_e2e.core.selenium.selenium_driver import SeleniumDriver


class TablePage(SeleniumDriver):
    """Table page for testing table interactions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.table_xpath = "//table[@id='product']"
        self.table_headers_xpath = "//table[@id='product']//th"
        self.table_rows_xpath = "//table[@id='product']//tr"

    def navigate(self):
        """Navigate to table page"""
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    def get_table_headers(self):
        """Get all table headers"""
        headers = self.getElements(self.table_headers_xpath, "xpath")
        return [header.text for header in headers]

    def get_table_data(self):
        """Get all table data"""
        rows = self.getElements(self.table_rows_xpath, "xpath")[1:]  # Skip header row
        table_data = []

        for row in rows:
            cells = row.find_elements("tag name", "td")
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)

        return table_data

    def get_cell_value(self, row_index, col_index):
        """Get specific cell value by row and column index"""
        cell_xpath = f"//table[@id='product']//tr[{row_index + 2}]/td[{col_index + 1}]"
        element = self.getElement(cell_xpath, "xpath")
        return element.text if element else None

    def find_row_by_column_value(self, column_name, value):
        """Find row containing specific value in given column"""
        headers = self.get_table_headers()
        if column_name not in headers:
            return None

        col_index = headers.index(column_name)
        table_data = self.get_table_data()

        for i, row in enumerate(table_data):
            if row[col_index] == value:
                return dict(zip(headers, row))
        return None

