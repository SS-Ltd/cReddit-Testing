'''
This module checks the functionalities of the home page of the mobile application.
'''

from my_imports import thread
from constants import DELAY_TIME
from paths import HOME_PAGE_PROFILE_ICON, PROFILE_SETTINGS
from helper_functions import locate_element
from Settings.settings import settings

def home_page(driver) -> None:
    '''
    This function checks the functionalities of the home page of the mobile application.
    '''
    # Click on the profile icon
    profile_icon = locate_element(driver, by_xpath=HOME_PAGE_PROFILE_ICON)
    profile_icon.click()
    thread.sleep(DELAY_TIME)
    print("Profile icon clicked")

    # Click on the settings
    settings_icon = locate_element(driver, by_accessibility_id=PROFILE_SETTINGS)
    settings_icon.click()
    thread.sleep(DELAY_TIME)
    print("Settings clicked")

    # Check the functionalities of the settings page
    settings(driver)

    print("Home page functionalities checked")
