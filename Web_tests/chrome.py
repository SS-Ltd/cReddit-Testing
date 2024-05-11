'''
This module contains a function that prepares an instance of a chrome browser.
'''
from my_imports import webdriver, ChromeDriverManager, ChromeService, WebDriver, ChromeOptions

def chrome() -> WebDriver:
    '''
    This function prepares an instance of a chrome browser.
    Its return value is the driver.
    '''

    option = ChromeOptions()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)

    return driver
