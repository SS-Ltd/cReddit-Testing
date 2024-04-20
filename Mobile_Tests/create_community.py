'''
This module checks the create community functionalities of the mobile application.
'''

from my_imports import thread
from constants import DELAY_TIME
from helper_functions import locate_element, end_text
from Paths import SUBREDDIT_PAGE_JOIN
from Paths import CREATE_COMMUNITY_NAME, CREATE_COMMUNITY_BUTTON
from Paths import CREATE_COMMUNITY_ALREADY_EXISTS, CREATE_COMMUNITY_TYPE, CREATE_COMMUNITY_TYPE_PRIVATE, CREATE_COMMUNITY_18
from Paths import CREATE_COMMUNITY_TYPE_PRIVATE_DESC

def check_success(driver) -> bool:
    '''
    This module checks if the creation was successful
    '''
    # Check if Join button is displayed, if it is, then the community page is displayed
    join_button = locate_element(driver, by_accessibility_id=SUBREDDIT_PAGE_JOIN)
    assert join_button is not None, "Community page not displayed"
    print("Community page displayed")
    return True

def create_community(driver) -> None:
    '''
    This function checks the create community functionalities of the mobile application.
    '''

    # Try to create a community with empty fields
    create = locate_element(driver, by_accessibility_id=CREATE_COMMUNITY_BUTTON)
    create.click()
    thread.sleep(DELAY_TIME)
    print("Create community clicked")

    # check_success(driver)

    # Create a community with a name that already exists
    name = locate_element(driver, by_id=CREATE_COMMUNITY_NAME)
    name.click()
    name.send_keys("test")
    end_text(driver)
    print("Name entered")
    thread.sleep(DELAY_TIME)

    already_exists = locate_element(driver, by_accessibility_id=CREATE_COMMUNITY_ALREADY_EXISTS)
    assert already_exists is not None, "Community already exists"
    print("Community already exists")

    # Create a community with a name that does not exist
    name = locate_element(driver, by_id=CREATE_COMMUNITY_NAME)
    name.click()
    name.clear()
    name.send_keys("test1")
    end_text(driver)
    print("Name entered")
    thread.sleep(DELAY_TIME)

    # Make the community private
    community_type = locate_element(driver, by_id=CREATE_COMMUNITY_TYPE)
    community_type.click()
    thread.sleep(DELAY_TIME)
    private = locate_element(driver, by_accessibility_id=CREATE_COMMUNITY_TYPE_PRIVATE)
    private.click()
    thread.sleep(DELAY_TIME)
    print("Community type selected")
    desc = locate_element(driver, by_accessibility_id=CREATE_COMMUNITY_TYPE_PRIVATE_DESC)
    assert desc is not None, "Description not found"

    # 18+ option
    mature = locate_element(driver, by_id=CREATE_COMMUNITY_18)
    mature.click()
    thread.sleep(DELAY_TIME)

    create = locate_element(driver, by_accessibility_id=CREATE_COMMUNITY_BUTTON)
    create.click()
    thread.sleep(DELAY_TIME)
    print("Create community clicked")

    check_success(driver)
