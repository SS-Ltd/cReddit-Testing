'''
This is the feed subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

import sys
import os
from enum import Enum
from helper_functions import locate_element, check_popup_notification
from constants import DELAY_TIME
from my_imports import thread, Select
from write_to_files import write_to_all_files, report_fail
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Button(Enum):
    '''
    This class is used to define the buttons in the feed subpage
    '''
    MATURE = (0, "Mature")
    AUTOPLAY = (1, "Autoplay")
    THEMES = (2, "Themes")
    NEW_TAB = (3, "New Tab")


# Constant XPATHS to identify the buttons
BUTTONS = [
    '//*[@id="root"]/div/div[4]/div[3]/div/div[1]/div[2]/label/input',
    '//*[@id="root"]/div/div[4]/div[3]/div/div[2]/div[2]/label/input',
    '//*[@id="root"]/div/div[4]/div[3]/div/div[3]/div[2]/label/input',
    '//*[@id="root"]/div/div[4]/div[3]/div/div[6]/div[2]/label/input'
]


def check_checkbox(driver, button: Button) -> None:
    '''
    This function checks the button
    '''
    # Locate the button
    button_element = locate_element(driver, by_xpath=BUTTONS[button.value[0]])
    assert button_element is not None, report_fail(
        button.value[1] + " Button not found")
    driver.execute_script("arguments[0].scrollIntoView();", button_element)
    selected = button_element.is_selected()
    driver.execute_script("arguments[0].click();", button_element)
    # check_popup_notification(driver)
    thread.sleep(DELAY_TIME)
    driver.refresh()
    thread.sleep(DELAY_TIME)
    button_element = locate_element(driver, by_xpath=BUTTONS[button.value[0]])
    assert button_element is not None, report_fail(
        button.value[1] + " Button not found")
    driver.execute_script("arguments[0].scrollIntoView();", button_element)
    assert button_element.is_selected() != selected, report_fail(
        button.value[1] + " Button not working")


def check_community_content_sort(driver) -> None:
    '''
    This function tests the community content sort dropdown
    '''

    # Locate the dropdown
    dropdown = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[2]/div/a')
    assert dropdown is not None, report_fail("Community Content Sort Dropdown not found")
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    dropdown.click()
    thread.sleep(DELAY_TIME)

    # Choose a random element from the dropdown
    random = locate_element(
        driver, by_id='undefined-new')
    assert random is not None, report_fail("Random Element not found")
    random_text = random.text
    random.click()
    thread.sleep(DELAY_TIME)
    driver.refresh()
    thread.sleep(DELAY_TIME)
    dropdown = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[2]/div/a')
    assert dropdown is not None, report_fail("Community Content Sort Dropdown not found")
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    assert dropdown.text == random_text, report_fail("Community Content Sort Dropdown not working")

def check_global_feed(driver) -> None:
    '''
    This function tests the global feed option
    '''

    # Locate the global feed dropdown
    global_feed = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[5]/div[2]/div/a')
    assert global_feed is not None, report_fail("Global Feed Button not found")
    driver.execute_script("arguments[0].scrollIntoView();", global_feed)
    global_feed.click()
    thread.sleep(DELAY_TIME)

    # Choose a random element from the dropdown
    random = locate_element(
        driver, by_id='undefined-compact')
    assert random is not None, report_fail("Random Element not found")
    random_text = random.text
    random.click()
    thread.sleep(DELAY_TIME)
    driver.refresh()
    thread.sleep(DELAY_TIME)
    global_feed = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[5]/div[2]/div/a')
    assert global_feed is not None, report_fail("Global Feed Button not found")
    driver.execute_script("arguments[0].scrollIntoView();", global_feed)
    assert global_feed.text == random_text, report_fail("Global Feed Button not working")


def feed(driver) -> None:
    '''
    This function tests the feed subpage of the settings page
    '''

    write_to_all_files(
        "#################### Testing Feed Subpage ####################")

    # Test the 18+ feed option
    # check_checkbox(driver, Button.MATURE)
    # thread.sleep(DELAY_TIME)

    # Test the autoplay feed option
    # check_checkbox(driver, Button.AUTOPLAY)
    # thread.sleep(DELAY_TIME)

    # Test the themes feed option
    # check_checkbox(driver, Button.THEMES)
    # thread.sleep(DELAY_TIME)

    # Test the community content sort dropdown
    # check_community_content_sort(driver)

    # Test the global feed option
    check_global_feed(driver)

    # Test the new tab feed option
    # check_checkbox(driver, Button.NEW_TAB)
    # thread.sleep(DELAY_TIME)

    write_to_all_files(
        "#################### Feed Subpage Test Completed ####################")
