from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

SLIDER_LOCATOR = ("xpath", "(//div[@id='ex26Slider']/div[contains(@class,'slider-handle')])[1]")

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=2)
driver.get("http://seiyria.com/bootstrap-slider/#example-26")
wait.until(EC.visibility_of_element_located(SLIDER_LOCATOR))


def move_slider(slider, current_position_attr, max_val_attr, min_val_attr, target_position, step):
    slider = driver.find_element(*slider)
    slider_max_value = int(slider.get_attribute(max_val_attr))
    slider_min_value = int(slider.get_attribute(min_val_attr))
    current_position = int(slider.get_attribute(current_position_attr))

    if not slider_min_value < target_position < slider_max_value:
        raise ValueError("Target position is not valid")

    if target_position != current_position:
        offset = abs((current_position - target_position) // step)
        if target_position < current_position:
            slider.send_keys(Keys.ARROW_LEFT * offset)
        else:
            slider.send_keys(Keys.ARROW_RIGHT * offset)


move_slider(slider=SLIDER_LOCATOR, current_position_attr="aria-valuenow", max_val_attr="aria-valuemax",
            min_val_attr="aria-valuemin", target_position=-100, step=1)
