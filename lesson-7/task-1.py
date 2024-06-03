from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
driver.get("https://www.automationexercise.com/")
driver.add_cookie({
    "name": "username",
    "value": "user123"
})
driver.refresh()
cookie = driver.get_cookie("username")
assert cookie is not None and cookie["name"] == "username" and cookie["value"] == "user123", "No such cookie inserted "
print(cookie)

driver.quit()
