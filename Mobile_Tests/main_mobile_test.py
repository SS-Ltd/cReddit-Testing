'''
This is the main test script for the mobile application.
'''
from my_imports import webdriver, AppiumOptions, thread, Dict, Any
from helper_functions import locate_element
from constants import DELAY_TIME
from Paths import START_USERNAME, START_PASSWORD, START_LOGIN, HOME_PAGE_TABS_HOME
from home_page import home_page
from Registration.login import login

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",
    "appPackage": "com.example.reddit_clone",
    "appActivity": "com.example.reddit_clone.MainActivity",
    "language": "en",
    "locale": "US"
}

URL = "http://localhost:4724"

print("Starting the Appium Test")
driver = webdriver.Remote(URL, options=AppiumOptions().load_capabilities(cap))
# Check if the app is launched
print(driver.current_activity)
#gmail_login(driver)

print("App launched")

# Test the login functionality
login(driver)
# Click on the login button
username = locate_element(driver, by_xpath=START_USERNAME)
username.click()
thread.sleep(2)
# username.clear()
username.send_keys("Clement33")

password = locate_element(driver, by_xpath=START_PASSWORD)
password.click()
thread.sleep(2)
# password.clear()
password.send_keys("1")

login_element = locate_element(driver, by_accessibility_id=START_LOGIN)
login_element.click()

# Verify that the login was successful
# Check the bottom tabs, one of them is an enough indication that the login was successful
# Check the home tab (tab 1 of 5)
home_tab = locate_element(driver, by_accessibility_id=HOME_PAGE_TABS_HOME)
assert home_tab.is_displayed(), "Login was not successful"
print("Login was successful")

# TEST FUNCTIONALITIES HERE
# TODO: Test Settings
home_page(driver)

print("Test completed successfully")
thread.sleep(DELAY_TIME)
driver.quit()
