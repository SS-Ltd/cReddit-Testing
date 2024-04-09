'''
This module checks the functionalities of the settings page of the mobile application.
'''

from my_imports import thread
from constants import DELAY_TIME
from helper_functions import locate_element
from Paths import SETTINGS_CONTENT_POLICY, SETTINGS_PRIVACY_POLICY, SETTINGS_USER_AGREEMENT, SETTINGS_HELP_CENTER, SETTINGS_VISIT_REDDIT_MOBILE

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


def settings(driver) -> None:
    '''
    This function checks the functionalities of the settings page of the mobile application.
    '''

    # Check that you are in the settings page
    temp = locate_element(driver, by_class_name='android.widget.ScrollView')
    assert temp is not None, "Settings page not found"
    print("Settings page found")

    driver.swipe(100, 1000, 100, 100, 400)

    thread.sleep(DELAY_TIME)

    # Check the functionalities of the hyperlinks
    check_hyperlink(driver, SETTINGS_CONTENT_POLICY)
    check_hyperlink(driver, SETTINGS_PRIVACY_POLICY)
    check_hyperlink(driver, SETTINGS_USER_AGREEMENT)
    check_hyperlink(driver, SETTINGS_HELP_CENTER)
    check_hyperlink(driver, SETTINGS_VISIT_REDDIT_MOBILE)
