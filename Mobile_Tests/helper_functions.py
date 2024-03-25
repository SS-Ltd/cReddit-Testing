'''
This file contains all the helper functions that are used throughout the project
'''

from my_imports import webdriver, WebDriverWait, EC, AppiumBy
from constants import DELAY_TIME

def locate_element(driver: webdriver, *, by_accessibility_id=None, by_xpath=None) -> WebDriverWait:
    '''
    This function locates an element on the page
    '''
    if by_accessibility_id:
        return WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, by_accessibility_id))
        )
    if by_xpath:
        return WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((AppiumBy.XPATH, by_xpath))
        )
    return None
