'''
This file contains all the helper functions that are used throughout the project
'''

from my_imports import webdriver, WebDriverWait, EC, AppiumBy, thread
from constants import DELAY_TIME


def locate_element(driver: webdriver, *, by_accessibility_id=None, by_xpath=None, by_class_name=None) -> WebDriverWait:
    '''
    This function locates an element on the page
    '''
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
    return None

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
