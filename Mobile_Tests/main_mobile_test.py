'''
This is the main test script for the mobile application.
'''
import time as thread
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5556",
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

print("App launched")
thread.sleep(2)

# Click on the login button
username = driver.find_element(
    AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
username.click()
thread.sleep(2)
# username.clear()
username.send_keys("test")

thread.sleep(5)

password = driver.find_element(
    AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
password.click()
thread.sleep(2)
# password.clear()
password.send_keys("test")

login = driver.find_element(
    AppiumBy.ACCESSIBILITY_ID, 'LOGIN')
login.click()

thread.sleep(10)
# driver.quit()
