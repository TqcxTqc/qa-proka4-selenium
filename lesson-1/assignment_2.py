from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

USERNAME_INPUT = ("xpath", "//input[@id='username']")
PASSWORD_INPUT = ("xpath", "//input[@id='password']")
LOGIN_BUTTON = ("xpath", "//button[@type='submit']")
LOGOUT_BUTTON = ("xpath", "//a[contains(@class, 'secondary')]")
SUB_HEADER = ("xpath", "//h4")

username_field = driver.find_element(*USERNAME_INPUT)
username_field.clear()
username_field.send_keys("tomsmith")
password_field = driver.find_element(*PASSWORD_INPUT)
password_field.clear()
password_field.send_keys("SuperSecretPassword!")
login_button = driver.find_element(*LOGIN_BUTTON)
login_button.click()
assert "Welcome to the Secure Area. When you are done click logout below." == driver.find_element(*SUB_HEADER).text

try:
    logout_button = driver.find_element(*LOGOUT_BUTTON)
    if logout_button.is_displayed():
        print("Logout button are visible, we are logged in")
        login_button.is_displayed()
except Exception as e:
    print("Login button is not visible")
