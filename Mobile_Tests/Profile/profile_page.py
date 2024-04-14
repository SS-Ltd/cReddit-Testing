'''
This file contains the locators and functions for the Profile page.
'''

from my_imports import thread, Dict, Any
from constants import DELAY_TIME
from helper_functions import locate_element, end_text
from Paths import (PROFILE_WINDOW_PROFILE, PROFILE_WINDOW_PROFILE, HOME_PAGE_PROFILE_ICON, PROFILE_PAGE_ABOUT
                   , PROFILE_PAGE_BACK, PROFILE_PAGE_COMMENTS, PROFILE_PAGE_POSTS, PROFILE_PAGE_EDIT_PROFILE
                   , PROFILE_PAGE_SHARE, PROFILE_PAGE_SEARCH, PROFILE_PAGE_MENU)

def profile_page(driver):
    '''
    This function tests the profile page.
    '''
    # Click on the profile icon
    profile_icon = locate_element(driver, by_xpath=HOME_PAGE_PROFILE_ICON)
    profile_icon.click()
    # Check the profile window
    profile_window_profile = locate_element(driver, by_accessibility_id=PROFILE_WINDOW_PROFILE)
    assert profile_window_profile is not None, "Profile window not found"
    thread.sleep(2)
    profile_window_profile.click()
    thread.sleep(DELAY_TIME)

    # click on the about button
    about_button = locate_element(driver, by_accessibility_id=PROFILE_PAGE_ABOUT)
    assert about_button is not None, "About button not found"
    about_button.click()
    thread.sleep(DELAY_TIME)
    get_source = driver.page_source
    assert "About content here" in get_source, 'About not found in source'

    # click on the Posts button
    posts_button = locate_element(driver, by_accessibility_id=PROFILE_PAGE_POSTS)
    assert posts_button is not None, "Posts button not found"
    posts_button.click()
    thread.sleep(DELAY_TIME)
    get_source = driver.page_source
    assert "Baiulus" in get_source, 'Posts not found in source' # This is a post that already exists might need to change it

    # click on the Comments button
    comments_button = locate_element(driver, by_accessibility_id=PROFILE_PAGE_COMMENTS)
    assert comments_button is not None, "Comments button not found"
    comments_button.click()
    thread.sleep(DELAY_TIME)
    get_source = driver.page_source
    assert "This is a comment by the tester at the time of testing" in get_source, 'Comments not found in source' # This is a comment that already exists might need to change it

    # click on the Edit Profile button
    edit_profile_button = locate_element(driver, by_accessibility_id=PROFILE_PAGE_EDIT_PROFILE)
    assert edit_profile_button is not None, "Edit Profile button not found"
    edit_profile_button.click()
    thread.sleep(DELAY_TIME)
    assert "Edit Profile content here" in get_source, 'Edit Profile not found in source' #TODO: needs to be changed

    #confirm the rest here when implemeted
