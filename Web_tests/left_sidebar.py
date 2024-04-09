'''
This module is used to test the left sidebar of the website.
'''

from my_imports import thread
from constants import DELAY_TIME
from helper_functions import locate_element, check_hyperlink


def create_community(driver) -> None:
    '''
    This function test the create community functionality
    '''

    locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[3]/div/div[1]/div/div[5]/div').click()
    thread.sleep(DELAY_TIME)

    locate_element(driver, by_id='sidebar_communities').click()
    if locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div/div[1]/div/div[6]/div') is None:
        locate_element(driver, by_id='sidebar_communities').click()
    locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div/div[1]/div/div[6]/div').click()

    assert locate_element(
        driver, by_id='community-card') is not None, "Create community page not displayed"

    # Enter community name
    community_name = locate_element(driver, by_id='community-name')
    assert community_name is not None, "Community name not found"
    community_name.send_keys("")
    driver.execute_script("arguments[0].blur()", community_name)
    assert locate_element(
        driver, by_xpath='//*[@id="card-content"]/div[1]/div/div[2]/p') is not None, "Empty field error not displayed"
    community_name.send_keys("Test Community")
    thread.sleep(DELAY_TIME)
    assert locate_element(
        driver, by_xpath='//*[@id="card-content"]/div[1]/div/div[2]/p') is None, "Empty field error displayed"
    locate_element(driver, by_id='Public-community-type').click()
    thread.sleep(1)
    locate_element(driver, by_id='ismature-switch-btn').click()
    thread.sleep(1)
    locate_element(driver, by_id='name-create-community').click()
    thread.sleep(DELAY_TIME)


def left_sidebar(driver) -> None:
    '''
    This function test the left sidebar of the website
    '''

    # Locate the recent communities
    # recent_communities = locate_element(driver, by_id='sidebar_recent')
    # assert recent_communities is not None, "Recent communities not found"
    # recent_communities.click()
    # thread.sleep(1)

    # dropdown = locate_element(
    #     driver, by_id='sidebar_recent_icon0')
    # assert dropdown is None, "Recent communities not displayed"

    # recent_communities.click()
    # thread.sleep(1)

    # dropdown = locate_element(
    #     driver, by_id='sidebar_recent_icon0')
    # assert dropdown is not None, "Recent communities not displayed"

    # Create a community
    # create_community(driver)

    # Check Resources
    check_hyperlink(driver, 'https://www.redditinc.com/', by_id='sidebar_resources_about_reddit', name="About Reddit")
    check_hyperlink(driver, 'https://accounts.reddit.com/adsregister?dest=https%3A%2F%2Fads.reddit.com%2F&referrer=https%3A%2F%2Fwww.reddit.com%2F&utm_source=web3x_consumer&utm_name=left_nav_cta', by_id='sidebar_resources_advertise', name="Advertise")
    check_hyperlink(driver, 'https://support.reddithelp.com/hc/en-us', by_id='sidebar_resources_help_center', name="Help Center")
