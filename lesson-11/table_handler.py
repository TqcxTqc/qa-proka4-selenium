from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class TableHandler:
    _DROPDOWN_LOCATOR = ("xpath", "//select[@name='tablepress-1_length']")
    _TABLE_LOCATOR = ("xpath", "//table[@id='tablepress-1']")
    _ROWS_LOCATOR = ("xpath", ".//tbody//tr[contains(@class,'row')]")
    _CELLS_LOCATOR = ("xpath", ".//td[contains(@class,'column')]")
    _TABLE_HEADER = ("xpath", ".//th[contains(@class, 'column')]")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    @property
    def _table(self) -> WebElement:
        return self.driver.find_element(*self._TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self._ROWS_LOCATOR)

    def check_amount_of_entries(self, amount_of_entries):
        dropdown = Select(self.driver.find_element(*self._DROPDOWN_LOCATOR))
        dropdown.select_by_value(str(amount_of_entries))
        if len(self._rows) != amount_of_entries:
            raise AssertionError(
                f"Amount of entries are not equal: expected -> {amount_of_entries} / actual-> {len(self._rows)}")
        else:
            return len(self._rows)

    def sort_by_descending(self, header_number):
        headers = self._table.find_elements(*self._TABLE_HEADER)

        if 0 < header_number <= len(headers):
            headers[header_number - 1].click()
        else:
            raise IndexError("Header number out of range.")

    def get_cell_content(self, row_number, column_number):
        row = self._rows[row_number - 1]
        cell = row.find_elements(*self._CELLS_LOCATOR)[column_number - 1]
        return cell.text

    def get_column_content(self, column_number):
        return [self.get_cell_content(row + 1, column_number) for row in range(len(self._rows))]

    def get_row_content(self, row_number):
        row = self._rows[row_number - 1]
        return [cell.text for cell in row.find_elements(*self._CELLS_LOCATOR)]

    def search_record_in_table(self, column_number, record_value):
        column_record = self.get_column_content(column_number)

        if record_value in column_record:
            return self.get_row_content(column_record.index(record_value) + 1)
