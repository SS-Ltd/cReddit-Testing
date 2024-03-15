'''
This module contains the function firefox, which prepares an instance of a firefox browser.
'''
from my_imports import webdriver, Options, FirefoxService, WebDriver
from constants import FIREFOX_DRIVER_PATH, FIREFOX_BINARY_PATH

def firefox() -> WebDriver:
    '''
    This function prepares an instance of a firefox browser.
    Its return value is the driver.
    '''
    options = Options()
    options.binary_location = FIREFOX_BINARY_PATH
    service = FirefoxService(FIREFOX_DRIVER_PATH)
    driver: WebDriver = webdriver.Firefox(options, service=service)
    driver.maximize_window()

    return driver
