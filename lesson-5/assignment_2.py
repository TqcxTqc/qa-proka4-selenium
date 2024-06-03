import os
import time

from selenium import webdriver

DOWNLOADS_FOLDER = os.path.join(os.getcwd(), "downloads")

if not os.path.exists(DOWNLOADS_FOLDER):
    os.mkdir("downloads")

prefs = {
    "download.default_directory": os.path.join(os.getcwd(), "downloads")
}

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
driver.get("http://the-internet.herokuapp.com/download")

list_of_links = driver.find_elements("xpath", "//div[@class='example']//a")

for link in list_of_links:
    link.click()
    time.sleep(1)

assert len(os.listdir(DOWNLOADS_FOLDER)) == len(list_of_links), "Not all files are downloaded"
