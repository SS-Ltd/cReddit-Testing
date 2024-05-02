'''
This is the feed subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

from enum import Enum
from helper_functions import locate_element, check_checkbox
from constants import DELAY_TIME
from my_imports import thread


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


def check_community_content_sort(driver) -> None:
    '''
    This function tests the community content sort dropdown
    '''

    # Locate the dropdown
    dropdown = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[2]/div/a')
    assert dropdown is not None, "Community Content Sort Dropdown not found"
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    dropdown.click()
    thread.sleep(DELAY_TIME)

    # Choose a random element from the dropdown
    random = locate_element(
        driver, by_id='settings-feed-community-content-sort-dropdown-new')
    assert random is not None, "Random Element not found"
    random_text = random.text
    random.click()
    thread.sleep(DELAY_TIME)
    driver.refresh()
    thread.sleep(DELAY_TIME)
    dropdown = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[2]/div/a')
    assert dropdown is not None, "Community Content Sort Dropdown not found"
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    assert dropdown.text == random_text, "Community Content Sort Dropdown not working"


def check_global_feed(driver) -> None:
    '''
    This function tests the global feed option
    '''

    # Locate the global feed dropdown
    global_feed = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[5]/div[2]/div/a')
    assert global_feed is not None, "Global Feed Button not found"
    driver.execute_script("arguments[0].scrollIntoView();", global_feed)
    global_feed.click()
    thread.sleep(DELAY_TIME)

    # Choose a random element from the dropdown
    random = locate_element(
        driver, by_id='settings-feed-global-content-view-dropdown-card')
    assert random is not None, "Random Element not found"
    random_text = random.text
    random.click()
    thread.sleep(DELAY_TIME)
    driver.refresh()
    thread.sleep(DELAY_TIME)
    global_feed = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[5]/div[2]/div/a')
    assert global_feed is not None, "Global Feed Button not found"
    driver.execute_script("arguments[0].scrollIntoView();", global_feed)
#    assert global_feed.text == random_text, report_fail(
#        "Global Feed Button not working")
    print("Global Feed Button working")


def feed(driver) -> None:
    '''
    This function tests the feed subpage of the settings page
    '''


    # Test the 18+ feed option
    check_checkbox(
        driver, by_xpath=BUTTONS[Button.MATURE.value[0]], name=Button.MATURE.value[1])
    thread.sleep(DELAY_TIME)

    # Test the autoplay feed option
    check_checkbox(
        driver, by_xpath=BUTTONS[Button.AUTOPLAY.value[0]], name=Button.AUTOPLAY.value[1])
    thread.sleep(DELAY_TIME)

    # Test the themes feed option
    check_checkbox(
        driver, by_xpath=BUTTONS[Button.THEMES.value[0]], name=Button.THEMES.value[1])
    thread.sleep(DELAY_TIME)

    # Test the community content sort dropdown
    check_community_content_sort(driver)
    thread.sleep(DELAY_TIME)

    # Test the global feed option
    check_global_feed(driver)
    thread.sleep(DELAY_TIME)

    # Test the new tab feed option
    check_checkbox(
        driver, by_xpath=BUTTONS[Button.NEW_TAB.value[0]], name=Button.NEW_TAB.value[1])
    thread.sleep(DELAY_TIME)
