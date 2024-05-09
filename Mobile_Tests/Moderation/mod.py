'''
This file contains the function that checks the functionalities of the moderation tools of the mobile application.
'''

from my_imports import webdriver, thread
from helper_functions import locate_element
from Paths import SEARCH_ICON, SEARCH_TEXT, SEARCH_SEARCH_FOR, SEARCH_RESULT, SEARCH_COMMUNNITY
from Paths import COMMUNITY_MOD_TOOLS
from constants import DELAY_TIME
from Moderation.general import general
from Moderation.content import content

def goto_mod(driver: webdriver) -> None:
    '''
    This function goes to the moderation tools of the mobile application.
    '''

    # Click on the search icon
    search_icon = locate_element(driver, by_id=SEARCH_ICON)
    assert search_icon is not None, "Search icon not found"
    search_icon.click()
    print("Search icon clicked")
    # thread.sleep(DELAY_TIME)

    # Search for a subreddit
    search_text = locate_element(driver, by_id=SEARCH_TEXT)
    assert search_text is not None, "Search text not found"
    search_text.click()
    thread.sleep(2)
    search_text.clear()
    search_text.send_keys("Noelia_Dicki")
    print("Search text entered")
    # thread.sleep(DELAY_TIME)

    # Click on the search button
    # The search button has accessibility ID that starts with the text "Search for"
    search_button = locate_element(driver, by_accessibility_id=SEARCH_SEARCH_FOR + ' Noelia_Dicki')
    assert search_button is not None, "Search button not found"
    search_button.click()
    print("Search button clicked")
    # thread.sleep(DELAY_TIME)

    # Locate the communities tab
    community = locate_element(driver, by_accessibility_id=SEARCH_COMMUNNITY)
    assert community is not None, "Community not found"
    community.click()
    print("Community clicked")
    # thread.sleep(DELAY_TIME)

    # Locate the search result
    search_result = locate_element(driver, by_id=SEARCH_RESULT)
    assert search_result is not None, "Search result not found"
    search_result.click()
    print("Search result found")
    # thread.sleep(DELAY_TIME)

    # Locate the mod tools icon
    mod_tools = locate_element(driver, by_accessibility_id=COMMUNITY_MOD_TOOLS)
    assert mod_tools is not None, "Mod tools not found"
    mod_tools.click()
    # print("Mod tools clicked")

def mod(driver: webdriver) -> None:
    '''
    This function checks the functionalities of the moderation tools of the mobile application.
    '''

    # First go to mod tools from the homepage
    goto_mod(driver)

    # Check the general functionalities of the mod tools
    # general(driver)

    # Check the content functionalities of the mod tools
    content(driver)

    print("Moderation tools checked")