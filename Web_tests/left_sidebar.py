"""
This module is used to test the left sidebar of the website.
"""

from my_imports import thread, EC, By, WebDriverWait
from constants import DELAY_TIME, SITE_NAME
from helper_functions import locate_element, check_hyperlink
from paths import LEFT_SIDE_BAR_HOME, LEFT_SIDE_BAR_POPULAR, LEFT_SIDE_BAR_ALL
from paths import LEFT_SIDE_BAR_RECENT, LEFT_SIDE_BAR_RECENT_COMMUNITY, LEFT_SIDE_BAR_RECENT_COMMUNITY_TEXT
from paths import LEFT_SIDE_BAR_COMMUNITY, LEFT_SIDE_BAR_CREATE_COMMUNITY, LEFT_SIDE_BAR_CREATE_COMMUNITY_CARD
from paths import LEFT_SIDE_BAR_CREATE_COMMUNITY_ALREADY_EXISTS, LEFT_SIDE_BAR_COMMUNITY_RANDOM



def recent(driver) -> None:
    '''
    This community checks whether the user can go to a recent community.
    '''
    # Locate the recent communities
    dropdown_recent = locate_element(driver, by_id=LEFT_SIDE_BAR_RECENT)
    assert dropdown_recent is not None, "Recent communities not found"
    # dropdown_recent.click()
    # thread.sleep(1)
    recent_community = locate_element(
        driver, by_id=LEFT_SIDE_BAR_RECENT_COMMUNITY)
    if recent_community is None:
        dropdown_recent.click()
        thread.sleep(1)
        recent_community = locate_element(
            driver, by_id=LEFT_SIDE_BAR_RECENT_COMMUNITY)
    assert recent_community is not None, "Recent communities not displayed"
    url = recent_community.get_attribute("href")
    print("url = ", url)

    # Get the test inside the span
    recent_community_text = locate_element(
        driver, by_xpath=LEFT_SIDE_BAR_RECENT_COMMUNITY_TEXT)
    assert recent_community_text is not None, "Recent community text not found"
    text = recent_community_text.text
    print("text = ", recent_community_text.text)
    driver.get(url)
    thread.sleep(DELAY_TIME)
    # Check the URL
    assert text in driver.current_url, "Recent community URL is incorrect"
    driver.back()
    thread.sleep(DELAY_TIME)

def community(driver) -> None:
    '''
    This function checks the community functionality
    '''
    # Locate the community button
    random_community = locate_element(driver, by_xpath=LEFT_SIDE_BAR_COMMUNITY_RANDOM)
    assert random_community is not None, "Community button not found"

    # Click the community
    random_community.click()
    thread.sleep(DELAY_TIME)

    # Check the URL
    assert 'r/' in driver.current_url, "Community URL is incorrect"
    print("Community URL is correct")

    # Go back
    driver.back()
    thread.sleep(DELAY_TIME)

def left_sidebar(driver) -> None:
    """
    This function test the left sidebar of the website
    """

    # Locate the all button
    all = locate_element(driver, by_id=LEFT_SIDE_BAR_ALL)
    assert all is not None, "All button not found"
    all.click()
    thread.sleep(DELAY_TIME)
    # Check the URL
    assert "all" in driver.current_url, "All URL is incorrect"
    # Go Back
    driver.back()
    thread.sleep(DELAY_TIME)

    # Locate the popular button
    popular = locate_element(driver, by_id=LEFT_SIDE_BAR_POPULAR)
    assert popular is not None, "Popular button not found"
    popular.click()
    thread.sleep(DELAY_TIME)
    # Check the URL
    assert "popular" in driver.current_url, "Popular URL is incorrect"

    # Locate the home button
    home = locate_element(driver, by_id=LEFT_SIDE_BAR_HOME)
    assert home is not None, "Home button not found"
    home.click()
    thread.sleep(DELAY_TIME)
    # Check the URL
    assert SITE_NAME == driver.current_url, "Home URL is incorrect"

    # Check Recent Communities
    recent(driver)

    # Locate the recent communities to minimize the thing
    dropdown_recent = locate_element(driver, by_id=LEFT_SIDE_BAR_RECENT)
    assert dropdown_recent is not None, "Recent communities not found"
    dropdown_recent.click()
    thread.sleep(1)

    # Check Community
    community(driver)

    # Check Resources
    # check_hyperlink(
    #     driver,
    #     "https://www.redditinc.com/",
    #     by_id="sidebar_resources_about_reddit",
    #     name="About Reddit",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://accounts.reddit.com/adsregister?dest=https%3A%2F%2Fads.reddit.com%2F&referrer=https%3A%2F%2Fwww.reddit.com%2F&utm_source=web3x_consumer&utm_name=left_nav_cta",
    #     by_id="sidebar_resources_advertise",
    #     name="Advertise",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://support.reddithelp.com/hc/en-us",
    #     by_id="sidebar_resources_help",
    #     name="Help Center",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://www.redditinc.com/blog",
    #     by_id="sidebar_resources_blog",
    #     name="Blog",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://www.redditinc.com/careers",
    #     by_id="sidebar_resources_careers",
    #     name="Careers",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://www.redditinc.com/press",
    #     by_id="sidebar_resources_press",
    #     name="Press",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://www.reddit.com/best/communities/1/",
    #     by_id="sidebar_resources_communties",
    #     name="Best of Reddit",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://www.reddit.com/posts/2023/global/",
    #     by_id="sidebar_resources_best_of_reddit",
    #     name="Reddit Premium",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://www.reddit.com/topics/a-1/",
    #     by_id="sidebar_resources_topics",
    #     name="Topics",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://www.redditinc.com/policies/content-policy",
    #     by_id="sidebar_resources_content_policy",
    #     name="Content Policy",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://www.reddit.com/policies/privacy-policy",
    #     by_id="sidebar_resources_privacy_policy",
    #     name="Privacy Policy",
    # )
    # check_hyperlink(
    #     driver,
    #     "https://www.redditinc.com/policies/user-agreement",
    #     by_id="sidebar_resources_agreement",
    #     name="User Agreement",
    # )
