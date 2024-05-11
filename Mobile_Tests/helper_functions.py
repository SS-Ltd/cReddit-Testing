'''
This file contains all the helper functions that are used throughout the project
'''

from my_imports import webdriver, WebDriverWait, EC, AppiumBy, thread
from constants import DELAY_TIME
from Paths import OPEN_RIGHT_SIDE_BAR,LOGOUT,LAST_LOGOUT
def locate_element(driver: webdriver, *, by_accessibility_id=None, by_xpath=None, by_class_name=None, by_id = None) -> WebDriverWait:
    '''
    This function locates an element on the page
    '''
    try:
        if by_id:
            return WebDriverWait(driver, DELAY_TIME).until(
                EC.presence_of_element_located((AppiumBy.ID, by_id))
            )
        if by_accessibility_id:
            return WebDriverWait(driver, DELAY_TIME).until(
                EC.presence_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, by_accessibility_id))
            )
        if by_xpath:
            return WebDriverWait(driver, DELAY_TIME).until(
                EC.presence_of_element_located((AppiumBy.XPATH, by_xpath))
            )
        if by_class_name:
            return WebDriverWait(driver, DELAY_TIME).until(
                EC.presence_of_element_located(
                    (AppiumBy.CLASS_NAME, by_class_name))
            )
    except Exception as e:
        print(e)
    return None

def end_text(driver: webdriver) -> None:
    '''
    clicks the correct button after typing text
    '''
    driver.hide_keyboard()

    thread.sleep(2)

def check_hyperlink(driver, hyperlink: str) -> None:
    '''
    This function checks the functionalities of the hyperlink on the settings page.
    '''

    print(f"Checking {hyperlink} hyperlink")

    button = locate_element(driver, by_accessibility_id=hyperlink)
    assert button is not None, f"{hyperlink} button not found"

    print("Before Clicking")
    print(driver.contexts)
    print(driver.context)

    # Click on the hyperlink
    button.click()
    print(f"Clicked on the {hyperlink} hyperlink")
    thread.sleep(10)

    print(driver.contexts)
    print(driver.context)

    # Check that another context has opened
    assert "WEBVIEW_chrome" in driver.contexts, f"{hyperlink} page not found"
    print(f"{hyperlink} page found")

    # Go back to the settings page
    driver.back()
    thread.sleep(DELAY_TIME)

    print(f"Back to the settings page from {hyperlink}")

    # Swipe randomly
    driver.swipe(100, 1000, 100, 100, 200)
    thread.sleep(DELAY_TIME)

def logout(driver,username):
    '''
    This function logs out the user
    '''
    # Click on the profile icon
    profile_icon = locate_element(driver, by_accessibility_id=OPEN_RIGHT_SIDE_BAR)
    profile_icon.click()
    thread.sleep(DELAY_TIME)
    # Click on the username button
    username_button = locate_element(driver, by_accessibility_id="u/"+username)
    username_button.click()
    thread.sleep(DELAY_TIME)
    # Click on the logout button
    logout_button = locate_element(driver, by_xpath=LOGOUT)
    logout_button.click()

    thread.sleep(DELAY_TIME)
    logout_button = locate_element(driver, by_accessibility_id=LAST_LOGOUT)
    logout_button.click()
