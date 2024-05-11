'''
This module will contain the tests for the search functionality of the mobile app.
'''

from my_imports import webdriver, thread
from helper_functions import locate_element
from constants import DELAY_TIME
from Paths import SEARCH_ICON, SEARCH_BAR
from Paths import SEARCH_AUTOFILL_COMMUNITY, SEARCH_AUTOFILL_PEOPLE
from Paths import SEARCH_COMMUNITY_HEADER, SEARCH_PEOPLE_HEADER

def send_keys_slowly(element, text, delay=0.5):
    for character in text:
        element.send_keys(character)
        thread.sleep(delay)


def search(driver: webdriver) -> None:
    '''
    This function will test the search functionality of the mobile app.
    '''

    # Locate the search icon.
    search_icon = locate_element(driver, by_accessibility_id=SEARCH_ICON)
    search_icon.click()
    print("Search icon clicked")

    # Locate the search bar.
    search_bar = locate_element(driver, by_id=SEARCH_BAR)
    search_bar.click()
    send_keys_slowly(search_bar, "cha")
    thread.sleep(DELAY_TIME)
    print("Search bar clicked")

    # Locate the autofilled community
    search_autofill_community = locate_element(driver, by_accessibility_id=SEARCH_AUTOFILL_COMMUNITY)
    search_autofill_community.click()
    print("Autofilled community clicked")

    # Locate the community header
    search_community_header = locate_element(driver, by_xpath=SEARCH_COMMUNITY_HEADER)
    print("Community header located")
    print(search_community_header.get_attribute('content-desc'))
    assert search_community_header.get_attribute('content-desc') == "r/Chat_Community0", "Community header text is not as expected"

    driver.back()

    # Locate the autofilled people
    search_autofill_people = locate_element(driver, by_accessibility_id=SEARCH_AUTOFILL_PEOPLE)
    search_autofill_people.click()
    print("Autofilled people clicked")

    # Locate the people header
    search_people_header = locate_element(driver, by_xpath=SEARCH_PEOPLE_HEADER)
    print("People header located")
    print(search_people_header.get_attribute('content-desc'))
    assert search_people_header.get_attribute('content-desc') == "chat13", "People header text is not as expected"

    print("Search functionality passed")
