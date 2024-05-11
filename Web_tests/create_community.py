'''
This module tests the create community functionality of the website.
'''

from my_imports import thread
from constants import DELAY_TIME
from helper_functions import locate_element
from paths import LEFT_SIDE_BAR_CREATE_COMMUNITY, LEFT_SIDE_BAR_CREATE_COMMUNITY_CARD
from paths import LEFT_SIDE_BAR_CREATE_COMMUNITY_ALREADY_EXISTS


def create_community(driver) -> None:
    """
    This function test the create community functionality
    """

    thread.sleep(DELAY_TIME)
    # Locate the create community button
    create = locate_element(driver, by_xpath=LEFT_SIDE_BAR_CREATE_COMMUNITY)
    assert create is not None, "Create community button not found"
    create.click()
    thread.sleep(DELAY_TIME)

    assert (
        locate_element(
            driver, by_id=LEFT_SIDE_BAR_CREATE_COMMUNITY_CARD) is not None
    ), "Create community page not displayed"

    # Enter community name
    community_name = locate_element(driver, by_id="community-name")
    assert community_name is not None, "Community name not found"
    community_name.send_keys("")
    driver.execute_script("arguments[0].blur()", community_name)
    text = locate_element(driver, by_xpath='//*[@id="card-content"]/div[1]/div/div[2]/p')
    assert text is not None, "Empty field error not displayed"
    print(text.text)
    community_name.send_keys("7aree2aInMunich")
    driver.execute_script("arguments[0].blur()", community_name)
    text = locate_element(driver, by_xpath='//*[@id="card-content"]/div[1]/div/div[2]/p')
    assert text is None, "Empty field error not displayed"
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id="Public-community-type").click()
    # locate_element(driver, by_id="ismature-switch-btn").click()
    locate_element(driver, by_id="name-create-community").click()
    thread.sleep(DELAY_TIME)

    # Check that the community already exists
    assert (
        locate_element(
            driver, by_xpath=LEFT_SIDE_BAR_CREATE_COMMUNITY_ALREADY_EXISTS
        ) is not None
    ), "Community already exists error not displayed"
    community_name.clear()
    community_name.send_keys("7aree2aInMunich44")
    locate_element(driver, by_id="name-create-community").click()
    thread.sleep(DELAY_TIME)

    # Check that the community was created
    assert (
        "r/7aree2aInMunich3" in driver.current_url
    ), "Community was not created"
    print("Community created successfully")
    thread.sleep(DELAY_TIME)
    driver.back()
    thread.sleep(DELAY_TIME)
