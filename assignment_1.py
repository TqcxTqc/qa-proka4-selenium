from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

FULL_NAME_INPUT = ("xpath", "//input[@id='userName']")
EMAIL_INPUT = ("xpath", "//input[@id='userEmail']")
CURRENT_ADDRESS_TEXTAREA = ("xpath", "//textarea[@id='currentAddress']")
PERMANENT_ADDRESS_TEXTAREA = ("xpath", "//textarea[@id='permanentAddress']")

full_name_field = driver.find_element(*FULL_NAME_INPUT)
full_name_field.clear()
full_name_field.send_keys("Automation QA")
assert "Automation QA" == full_name_field.get_attribute("value"), "Full name value is not correct"

email_field = driver.find_element(*EMAIL_INPUT)
email_field.clear()
email_field.send_keys("someEmail@mail.com")
assert "someEmail@mail.com" == email_field.get_attribute("value"), "Email value is not correct"

current_address = driver.find_element(*CURRENT_ADDRESS_TEXTAREA)
current_address.clear()
current_address.send_keys("Mahovica 32")
assert "Mahovica 32" == current_address.get_attribute("value"), "Current address value is not correct"

permanent_address = driver.find_element(*PERMANENT_ADDRESS_TEXTAREA)
permanent_address.clear()
permanent_address.send_keys("Dubrovnic 55")
assert "Dubrovnic 55" == permanent_address.get_attribute("value"), "Current address value is not correct"
