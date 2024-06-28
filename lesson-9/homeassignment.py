from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")

driver = webdriver.Chrome(options=options)


def page_actions_after_switch(current_window, element_to_interract):
    assert current_window == driver.current_window_handle, "Window is not switched"
    driver.find_element("xpath", element_to_interract).click()
    return driver.title


driver.get("https://hyperskill.org/login")
hyperskill_window = driver.current_window_handle
driver.switch_to.new_window("tab")

driver.get("https://www.avito.ru/")
avito_window = driver.current_window_handle
driver.switch_to.new_window("tab")

driver.get("https://test.k6.io/")
k6_window = driver.current_window_handle

driver.switch_to.window(hyperskill_window)
print(page_actions_after_switch(hyperskill_window, "//a[normalize-space()='Reset password']"))

driver.switch_to.window(k6_window)
print(page_actions_after_switch(k6_window, "//a[text()='/contacts.php']"))

driver.switch_to.window(avito_window)
print(page_actions_after_switch(avito_window, "//a[@data-marker='header/login-button']"))
