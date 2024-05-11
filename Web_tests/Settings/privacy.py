'''
This is the safety & privacy subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

from helper_functions import locate_element, check_popup_notification
from constants import DELAY_TIME
from my_imports import thread, WebDriver, By
from paths import SETTINGS_PRIVACY_ADD_BLOCKED_USERS

def users_block(driver: WebDriver) -> None:
    '''
    This function tests blocking people functionality
    '''
    input_field = locate_element(driver, by_id='safety-block-user-input')
    assert input_field is not None, "Block user input field not found"
    driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.clear()
    # First check with an invalid username
    input_field.send_keys('Test User')
    locate_element(driver, by_xpath=SETTINGS_PRIVACY_ADD_BLOCKED_USERS).click()
    # Check with a failed notification
    check_popup_notification(driver, False)
    thread.sleep(DELAY_TIME)
    input_field.clear()
    input_field.send_keys('Chat0')
    locate_element(driver, by_xpath=SETTINGS_PRIVACY_ADD_BLOCKED_USERS).click()
    check_popup_notification(driver, True)
    # Check that the user has been added to the list of blocked users
    users = driver.find_elements(By.XPATH, '//*[contains(text(), "Chat0")]')
    print("users: \n", users)
    # check if users is not empty
    assert users, "User not found in blocked users list"
    for user in users:
        # Go up two divs (to the grandparent)
        grandparent = user.find_element(By.XPATH, '../..')
        # Find a button within the grandparent's children
        button = grandparent.find_element(By.XPATH, './/button')
        assert button is not None, "Remove user from blocked list button not found"
        # Click on the button
        button.click()
        check_popup_notification(driver)
        thread.sleep(DELAY_TIME)

    # Check that the user has been removed from the list of blocked users
    users = driver.find_elements(By.XPATH, '//*[contains(text(), "Chat0")]')
    assert not users, "User found in blocked users list"


def communities_mute(driver) -> None:
    '''
    This function tests muting communities functionality
    '''
    input_field = locate_element(driver, by_id='safety-mute-community-input')
    assert input_field is not None, "Mute community input field not found"
    driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.clear()
    input_field.send_keys('Test Community')
    locate_element(driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[1]/button').click()
    # Check with invalid community
    check_popup_notification(driver, False)
    thread.sleep(DELAY_TIME)
    input_field.clear()
    input_field.send_keys('Chat_Community0')
    locate_element(driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[1]/button').click()
    check_popup_notification(driver, True)
    # Check that the community has been added to the list of muted communities
    communities = driver.find_elements(By.XPATH, '//*[contains(text(), "Chat_Community0")]')
    # check if communities is not empty
    assert communities is not None, "Community not found in muted communities list"
    for community in communities:
        # Go up two divs (to the grandparent)
        grandparent = community.find_element(By.XPATH, '../..')
        # Find a button within the grandparent's children
        button = grandparent.find_element(By.XPATH, './/button')
        assert button is not None, "Remove community from muted list button not found"
        # Click on the button
        button.click()
        check_popup_notification(driver)
        thread.sleep(DELAY_TIME)

    # Check that the community has been removed from the list of muted communities
    communities = driver.find_elements(By.XPATH, '//*[contains(text(), "Chat_Community0")]')
    assert not communities, "Community found in muted communities list"

def privacy(driver) -> None:
    '''
    This function tests the account subpage of the settings page
    '''

    users_block(driver)
    # thread.sleep(DELAY_TIME)

    communities_mute(driver)
    # thread.sleep(DELAY_TIME)
