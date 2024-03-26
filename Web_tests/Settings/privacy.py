'''
This is the safety & privacy subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

import sys
import os
from helper_functions import locate_element, check_popup_notification
from constants import DELAY_TIME
from my_imports import thread, WebDriver, By
from write_to_files import write_to_all_files, report_fail
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def users_block(driver: WebDriver) -> None:
    '''
    This function tests blocking people functionality
    '''
    write_to_all_files("Testing Block People")
    input_field = locate_element(driver, by_id='safety-block-user-input')
    assert input_field is not None, report_fail("Block user input field not found")
    driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.clear()
    input_field.send_keys('Test User')
    locate_element(driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[2]/button').click()
    check_popup_notification(driver)
    thread.sleep(DELAY_TIME)
    input_field.clear()
    # Check that the user has been added to the list of blocked users
    users = driver.find_elements(By.XPATH, '//*[contains(text(), "Test User")]')
    # check if users is not empty
    assert users, report_fail("User not found in blocked users list")
    for user in users:
        # Go up two divs (to the grandparent)
        grandparent = user.find_element(By.XPATH, '../..')
        # Find a button within the grandparent's children
        button = grandparent.find_element(By.XPATH, './/button')
        assert button is not None, report_fail("Remove user from blocked list button not found")
        # Click on the button
        button.click()
        check_popup_notification(driver)
        thread.sleep(DELAY_TIME)

    # Check that the user has been removed from the list of blocked users
    users = driver.find_elements(By.XPATH, '//*[contains(text(), "Test User")]')
    assert not users, report_fail("User found in blocked users list")

    write_to_all_files("Blocking users functionality works as expected")

def communities_mute(driver) -> None:
    '''
    This function tests muting communities functionality
    '''
    write_to_all_files("Testing Block Communities")
    input_field = locate_element(driver, by_id='safety-mute-community-input')
    assert input_field is not None, report_fail("Mute community input field not found")
    driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.clear()
    input_field.send_keys('Test Community')
    locate_element(driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[8]/button').click()
    check_popup_notification(driver)
    thread.sleep(DELAY_TIME)
    input_field.clear()
    # Check that the community has been added to the list of muted communities
    communities = driver.find_elements(By.XPATH, '//*[contains(text(), "Test Community")]')
    # check if communities is not empty
    assert communities, report_fail("Community not found in muted communities list")
    for community in communities:
        # Go up two divs (to the grandparent)
        grandparent = community.find_element(By.XPATH, '../..')
        # Find a button within the grandparent's children
        button = grandparent.find_element(By.XPATH, './/button')
        assert button is not None, report_fail("Remove community from muted list button not found")
        # Click on the button
        button.click()
        check_popup_notification(driver)
        thread.sleep(DELAY_TIME)

    # Check that the community has been removed from the list of muted communities
    communities = driver.find_elements(By.XPATH, '//*[contains(text(), "Test Community")]')
    assert not communities, report_fail("Community found in muted communities list")

    write_to_all_files("Muting communities functionality works as expected")

def privacy(driver) -> None:
    '''
    This function tests the account subpage of the settings page
    '''

    write_to_all_files(
        "#################### Testing Safety & Privacy Subpage ####################")

    users_block(driver)
    # thread.sleep(DELAY_TIME)

    communities_mute(driver)

    write_to_all_files(
        "#################### Safety & Privacy Subpage Test Completed ####################")
