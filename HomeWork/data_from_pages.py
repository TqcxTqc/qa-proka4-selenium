from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://habr.com/")
harb_title = driver.title
print(harb_title)
driver.get("https://www.zone.ee/en/")
zone_title = driver.title
zone_url = driver.current_url
print(zone_title)
driver.back()
assert harb_title == "Publications / My feed / Habr", "Page is not found"
driver.refresh()
habr_url = driver.current_url
driver.forward()
assert habr_url != zone_url, "URL not changed"
