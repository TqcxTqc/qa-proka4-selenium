import os
import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ACCEPT_COOKIES_LOCATOR = ("xpath", "//button[@widget-attachpoint='agree']")
ADD_TO_CART_LOCATOR = ("xpath", "//div[@class='c-product__controls']//div[@widget-attachpoint='addToCart']")

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
driver.get("https://kaup24.ee/ru/kosmetika-parfyumeriya/parfyumeriya/duhi-dlya-muzhchin/muzhskaya-parfyumeriya-boss-bottled-hugo-boss-edt?id=46946")
wait.until(EC.visibility_of_element_located(ACCEPT_COOKIES_LOCATOR)).click()
wait.until(EC.visibility_of_element_located(ADD_TO_CART_LOCATOR)).click()
if not os.path.exists(os.path.join(os.getcwd(), "cookies")):
    os.mkdir("cookies")
    pickle.dump(driver.get_cookies(), open(os.path.join(os.getcwd(), "cookies", "cookies.pkl"), "wb"))

driver.delete_all_cookies()
driver.refresh()

cookies = pickle.load(open(os.path.join(os.getcwd(), "cookies", "cookies.pkl"), "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.get("https://kaup24.ee/ru/cart")
driver.quit()
