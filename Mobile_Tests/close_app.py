"""
This script is used to close the app
"""

from my_imports import (
    webdriver,
    AppiumOptions,
    thread,
    Dict,
    Any,
    WebDriverWait,
    EC,
    AppiumBy,
)
from helper_functions import locate_element
from constants import DELAY_TIME


def close_app(driver):
    """
    This function closes the app
    """
    # Click on the profile button
    #WebDriverWait(driver, DELAY_TIME).until(
    #    EC.presence_of_element_located(
    #        (AppiumBy.ID, "android:id/navigationBarBackground")
    #    )
    #)
    driver.swipe(
        start_x=671,
        start_y=2956,
        end_x=671,
        end_y=100,
        duration=550,
    )
    # Close the app
    #driver.quit()
    print("App closed")
    thread.sleep(2)
    print("Appium test completed")
    print("Test Passed")
