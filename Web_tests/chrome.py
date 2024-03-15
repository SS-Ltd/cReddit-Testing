'''
This module contains a function that prepares an instance of a chrome browser.
'''
from my_imports import webdriver, ChromeDriverManager, ChromeService, WebDriver

def chrome() -> WebDriver:
    '''
    This function prepares an instance of a chrome browser.
    Its return value is the driver.
    '''
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    return driver
