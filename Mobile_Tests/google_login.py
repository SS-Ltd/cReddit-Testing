'''
This file contains the function that logs into Gmail
'''
#from my_imports import webdriver, AppiumOptions, thread, Dict, Any
from appium import webdriver
from typing import Dict, Any
from appium.webdriver.common.touch_action import TouchAction
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from close_app import close_app
import time as thread
from helper_functions import locate_element
from constants import DELAY_TIME
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from helper_functions import locate_element
# from constants import DELAY_TIME

def gmail_login(driver: webdriver) -> None:
    '''
    This function logs into Gmail
    '''
    close_app(driver)


    # Click on the login button
    locate_element(driver, by_accessibility_id="Gmail").click()
    thread.sleep(2)

def search_for_email(driver, text :str) -> bool:
    '''
    This function searches for an email in the Gmail inbox
    if the email is found it clicks on it
    @param driver: The driver to use
    @param Text: The text to search for
    @return: True if the email was found, False otherwise
    '''
    a = driver.find_elements_by_xpath("//*[contains(@text, '" + text + "')]")
    for i in a:
        if  text in a.text:
            i.click()
            return True
    return False
