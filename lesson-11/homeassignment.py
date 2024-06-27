from selenium import webdriver
from selenium.webdriver import ChromeOptions
from table_handler import TableHandler
from time import sleep

options = ChromeOptions()
options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://practice-automation.com/tables/")
table = TableHandler(driver)

table.check_amount_of_entries(25)
table.get_cell_content(2, 2)
table.get_column_content(3)
table.sort_by_descending(3)
table.search_record_in_table(column_number=2, record_value="Brazil")
