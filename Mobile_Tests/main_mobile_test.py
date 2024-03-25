'''
This is the main test script for the mobile application.
'''
from my_imports import webdriver, AppiumOptions, thread, Dict, Any
from helper_functions import locate_element
from constants import DELAY_TIME

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

# Click on the login button
username = locate_element(driver, by_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
username.click()
thread.sleep(2)
# username.clear()
username.send_keys("test")

password = locate_element(driver, by_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
password.click()
thread.sleep(2)
# password.clear()
password.send_keys("test")

login = locate_element(driver, by_accessibility_id='Continue')
login.click()

# Verify that the login was successful
# If there is a profile icon, then the login was successful
profile = locate_element(driver, by_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]')
assert profile is not None, "Login was not successful"

# Click on the profile button
profile.click()

# Click on the settings button
settings = locate_element(driver, by_accessibility_id='Settings')
settings.click()

# thread.sleep(DELAY_TIME)

# Check that you are indeed in the settings page
# Check the account settings button
# account_settings = locate_element(
# driver, by_accessibility_id='Account Settings for u/ (username)')
# assert account_settings is not None, "Account settings button not found"

# Go to account settings
# account_settings.click()

# thread.sleep(5)

# Check that you are indeed in the account settings page
# title_element = locate_element(driver, by_accessibility_id='Account settings')
# print(title_element.is_displayed())
# assert title_element.is_displayed(), "Account settings page not found"

driver.swipe(100, 1000, 100, 100, 400)

thread.sleep(DELAY_TIME)

content_policy = locate_element(driver, by_accessibility_id='Content Policy')
assert content_policy is not None, "Content Policy button not found"

print("Before Clicking")
print(driver.contexts)
print(driver.context)


# Click on the content policy button
content_policy.click()
print("Clicked on the content policy button")
thread.sleep(DELAY_TIME)
print(driver.contexts)
print(driver.context)

# Check that another context has opened
assert "WEBVIEW_chrome" in driver.contexts, "Content Policy page not found"

print("Test completed successfully")
thread.sleep(20)
driver.quit()
