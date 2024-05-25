import time

from selenium import webdriver

# Header Locators
HEADER_LINKS = ("xpath", "//ul/li[contains(@class,'nav-item')]")
SIGN_IN_BUTTON = ("xpath", "//button[text()=' Sign in ']")
START_FOR_FREE = ("xpath", "//button[text()='Start for free']")

# Main block Locators
TITLE_EXPLORE_ALL_TRACKS = ("xpath", "//h2[contains(text(),'Explore all tracks')]")
TOP_TRACKS_AREA_BUTTON = ("xpath", "//a[contains(@click-event-context,'top_tracks')]")
DATA_ANALYSIS_BUTTON = ("xpath", "//a[contains(@click-event-context,'frontend')]")
CARD_INTRODUCTION_PYTHON_TITLE = ("xpath", "//a[@aria-label='Introduction to Python']//h5")
KOTLIN_CORE_CERTIFICATE_LABEL = ("xpath", "//a[@aria-label='Kotlin Core']//span[contains(@class,'badge')]")
PYTHON_OOP_RATING_NUMBER = ("xpath", "//a[@aria-label='Python OOP']//div[text()='4.6']")
CARD_SQL_PROJECTS_COUNT = ("xpath", "//a[@aria-label='Introduction to SQL']//span[contains(text(),'projects')]")
CARD_SQL_LEARNING_COUNTER = (
    "xpath", "//a[@aria-label='Introduction to SQL']//div[contains(text(),'already learning')]")
CARD_ANDROID_HOURS = ("xpath", "//a[@aria-label='Android Developer with Kotlin']//span[contains(text(),'hours')]")
TOPIC_ANDROID = ("xpath", "//a[contains(@click-event-context, 'android')]")
TOPIC_BACKEND = ("xpath", "//a[contains(@click-event-context, 'backend')]")
TOPIC_PYTHON = ("xpath", "//a[contains(@click-event-context, 'python')]")
TOPIC_JAVA = ("xpath", "//a[contains(@click-event-context, 'java') and text()='Java ']")

# Footer Locators
BLOG_LINK = ("xpath", "//footer//a[@click-event-target='blog']")
RESOURCES_TEXT = ("xpath", "//footer//div[text()='Resources']")
GOOGLE_PLAY_BUTTON = ("xpath", "//footer//a[@click-event-target='google-play']")
APP_STORE_BUTTON = ("xpath", "//footer//a[@click-event-target='app-store']")
PRICING_LINK = ("xpath", "//footer//a[@click-event-target='pricing']")
FULL_CATALOG_BUTTON = ("xpath", "//footer//a[@click-event-target='full_catalog']")
SUBSCRIPTION_TEXT = ("xpath", "//footer//div[text()='Subscription']")
SUPPORT_TEXT = ("xpath", "//footer//div[text()='Support']")
SOCIAL_YOUTUBE = ("xpath", "//footer//a[@click-event-target='YouTube']")
SOCIAL_DISCORD = ("xpath", "//footer//a[@click-event-target='Discord']")
HELP_CENTER_LINK = ("xpath", "//footer//a[@click-event-target='help-center']")
CATEGORY_JAVA = ("xpath", "//footer//a[@click-event-target='Java']")
CATEGORY_PYTHON = ("xpath", "//footer//a[@click-event-target='Python']")
HYPERSKILL_ICON = ("xpath", "//a[@click-event-target='logo']")

driver = webdriver.Chrome()

all_locators = [HEADER_LINKS, SIGN_IN_BUTTON, START_FOR_FREE, TITLE_EXPLORE_ALL_TRACKS, TOP_TRACKS_AREA_BUTTON,
                DATA_ANALYSIS_BUTTON, CARD_INTRODUCTION_PYTHON_TITLE, KOTLIN_CORE_CERTIFICATE_LABEL,
                CARD_SQL_PROJECTS_COUNT, CARD_SQL_LEARNING_COUNTER, CARD_ANDROID_HOURS, TOPIC_ANDROID, TOPIC_BACKEND,
                TOPIC_PYTHON, TOPIC_JAVA, BLOG_LINK, RESOURCES_TEXT, GOOGLE_PLAY_BUTTON, APP_STORE_BUTTON, PRICING_LINK,
                FULL_CATALOG_BUTTON, SUBSCRIPTION_TEXT, SUPPORT_TEXT, SOCIAL_YOUTUBE, SOCIAL_DISCORD, HELP_CENTER_LINK,
                CATEGORY_JAVA, CATEGORY_PYTHON, HYPERSKILL_ICON, PYTHON_OOP_RATING_NUMBER
                ]

driver.get("https://hyperskill.org/tracks")
time.sleep(3)

for locator in all_locators:
    driver.find_element(*locator)
    time.sleep(1)
