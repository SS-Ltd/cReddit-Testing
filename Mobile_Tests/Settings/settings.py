'''
This module checks the functionalities of the settings page of the mobile application.
'''

from my_imports import thread
from constants import DELAY_TIME
from helper_functions import locate_element

def settings(driver) -> None:
    '''
    This function checks the functionalities of the settings page of the mobile application.
    '''

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
    thread.sleep(10)

    print(driver.contexts)
    print(driver.context)

    # Check that another context has opened
    assert "WEBVIEW_chrome" in driver.contexts, "Content Policy page not found"
    print("Content Policy page found")

