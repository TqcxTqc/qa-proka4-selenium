from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

OPEN_ALERT_BUTTON = ("xpath", "//button[@id='alert']")
CHANGE_TEXT_BUTTON = ("xpath", "//button[@id='populate-text']")
DISPLAY_BUTTON = ("xpath", "//button[@id='display-other-button']")
ENABLED_BUTTON = ("xpath", "//button[@id='enable-button']")
CHECK_CHECKBOX_BUTTON = ("xpath", "//button[@id='checkbox']")

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=2)
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
driver.find_element(*OPEN_ALERT_BUTTON).click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()

driver.find_element(*CHANGE_TEXT_BUTTON).click()
wait.until(EC.text_to_be_present_in_element(("xpath", "//h2[@id='h2']"), "Selenium Webdriver"))

driver.find_element(*DISPLAY_BUTTON).click()
wait.until(EC.visibility_of_element_located(("xpath", "//button[@id='hidden']")))

driver.find_element(*ENABLED_BUTTON).click()
wait.until(EC.element_to_be_clickable(("xpath", "//button[@id='disable']")))

driver.find_element(*CHECK_CHECKBOX_BUTTON).click()
wait.until(EC.element_located_selection_state_to_be(("xpath", "//input[@type='checkbox']"), True))
