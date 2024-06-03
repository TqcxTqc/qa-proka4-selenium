import os

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/upload-download")
driver.find_element("xpath", "//input[@id='uploadFile' and @type='file']").send_keys(os.path.join(os.getcwd(), "file_for_upload.txt"))
