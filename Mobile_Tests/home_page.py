'''
This module checks the functionalities of the home page of the mobile application.
'''

from my_imports import thread
from constants import DELAY_TIME
from Paths import HOME_PAGE_PROFILE_ICON, PROFILE_SETTINGS
from Paths import NAVIGATION_BAR_CREATE_POST
from Paths import SUBREDDIT_PAGE_JOIN
from Paths import PROFILE_WINDOW_CREATE_COMMUNITY
from helper_functions import locate_element
from settings import settings
from post import post
from create_community import create_community
from search import search
from Moderation.mod import mod

def home_page(driver) -> None:
    '''
    This function checks the functionalities of the home page of the mobile application.
    '''

    # Check Moderation Tools
    # mod(driver)

    # Check search
    search(driver)

    # Click on the profile icon
    # profile_icon = locate_element(driver, by_xpath=HOME_PAGE_PROFILE_ICON)
    # profile_icon.click()
    # thread.sleep(DELAY_TIME)
    # print("Profile icon clicked")

    # # Click on the settings
    # settings_icon = locate_element(driver, by_accessibility_id=PROFILE_SETTINGS)
    # settings_icon.click()
    # thread.sleep(DELAY_TIME)
    # print("Settings clicked")

    # # Check the functionalities of the settings page
    # settings(driver)

    # # Post
    # post(driver)

    # Check a random community
    # click on coordinates (x, y) = (400, 400)
    # driver.tap([(400, 400)])
    # thread.sleep(DELAY_TIME)

    # # Check if Join button is displayed, if it is, then the community page is displayed
    # join_button = locate_element(driver, by_accessibility_id=SUBREDDIT_PAGE_JOIN)
    # assert join_button is not None, "Community page not displayed"
    # print("Community page displayed")

    # Create a Community
    # create = locate_element(driver, by_accessibility_id=PROFILE_WINDOW_CREATE_COMMUNITY)
    # create.click()
    # thread.sleep(DELAY_TIME)
    # print("Create community clicked")
    # create_community(driver)

    print("Home page functionalities checked")
