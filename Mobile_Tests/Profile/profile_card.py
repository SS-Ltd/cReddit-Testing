'''
This file contains the locators and functions for the Profile Card
'''

from my_imports import thread, Dict, Any
from constants import DELAY_TIME
from helper_functions import locate_element, end_text
from Paths import (CREATE_YOUR_OWN_AVATAR, ABOUT_USER_BLOCK_ACCOUNT,ABOUT_USER_SEND_MESSAGE
                   , ABOUT_USER_VIEW_PROFILE,POST_USERNAME,PROFILE_PAGE_ABOUT,PROFILE_PAGE_BACK,POST_COMMENTS)



def profile_card(driver):
    '''
    This function tests the profile card
    '''
    # Click on the profile name
    thread.sleep(2)
    locate_element(driver, by_id=POST_COMMENTS).click()
    thread.sleep(2)
    locate_element(driver, by_id=POST_USERNAME).click()
    thread.sleep(2)
    # Check the profile window
    view_profile = locate_element(driver, by_accessibility_id=ABOUT_USER_VIEW_PROFILE)
    assert view_profile is not None, "View Profile not found"
    view_profile.click()
    thread.sleep(DELAY_TIME)
    # Check the profile window
    profile_window = locate_element(driver, by_accessibility_id=PROFILE_PAGE_ABOUT)
    assert profile_window is not None, "Profile window not found"
    thread.sleep(2)
    #go back
    back_button = locate_element(driver, by_accessibility_id=PROFILE_PAGE_BACK)
    back_button.click()
    thread.sleep(2)
    #
    send_message = locate_element(driver, by_accessibility_id=ABOUT_USER_SEND_MESSAGE)
    assert send_message is not None, "Send Message not found"
    send_message.click()
    thread.sleep(DELAY_TIME)
    # check message window
    #message_window = locate_element(driver, by_accessibility_id=#####)
    #assert message_window is not None, "Message window not found"
    #thread.sleep(2)
    #go back
    #back_button = locate_element(driver, by_accessibility_id=PROFILE_PAGE_BACK)
    #back_button.click()
    #thread.sleep(2)
    #
    block_account = locate_element(driver, by_accessibility_id=ABOUT_USER_BLOCK_ACCOUNT)
    assert block_account is not None, "Block Account not found"
    block_account.click()
    thread.sleep(DELAY_TIME)
    # check block account window
    #block_window = locate_element(driver, by_accessibility_id=#####)
    #assert block_window is not None, "Block Account window not found"
    #thread.sleep(2)
    #go back
    #back_button = locate_element(driver, by_accessibility_id=PROFILE_PAGE_BACK)
    #back_button.click()
    #thread.sleep(2)
