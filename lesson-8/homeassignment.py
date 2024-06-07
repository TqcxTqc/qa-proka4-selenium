from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1020,1020")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")

GRID_TAB_LOCATOR = ("xpath", "//a[@id='demo-tab-grid']")

grid_tile_locator = lambda row_id, text: ("xpath", f"//div[@id='{row_id}']//li[contains(text(),'{text}')]")

with webdriver.Chrome(options=options) as driver:
    driver.get("https://demoqa.com/selectable")

    wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

    wait.until(EC.element_to_be_clickable(GRID_TAB_LOCATOR), "Tab is not clickable").click()
    tile_one = wait.until(EC.element_to_be_clickable(grid_tile_locator("row1", "One")))
    tile_five = wait.until(EC.element_to_be_clickable(grid_tile_locator("row2", "Five")))
    tile_nine = wait.until(EC.element_to_be_clickable(grid_tile_locator("row3", "Nine")))

    selected_tiles = [("Tile One", tile_one), ("Tile Five", tile_five), ("Tile Nine", tile_nine)]

    for name, tile in selected_tiles:
        tile.click()
        assert "active" in tile.get_attribute("class"), f"{name} is not selected"

    for name, tile in selected_tiles:
        tile.click()
        assert "active" not in tile.get_attribute("class"), f"{name} still selected"
