'''
This Module is supposed to test the Profile page of the website.
'''

from constants import DELAY_TIME, SITE_NAME
from my_imports import thread
from helper_functions import locate_element
from paths import PROFILE_USERNAME, PROFILE_FEED, PROFILE_FIRST_COMMENT
from paths import PROFILE_MAINFEED_CATEGORY_DROPDOWN
from paths import PROFILE_MAINFEED_CATEGORY_NEW, PROFILE_MAINFEED_CATEGORY_HOT, PROFILE_MAINFEED_CATEGORY_TOP

def sort_feed(driver, feed: str) -> None:
    '''
    This function is supposed to sort the feed by the given feed type.
    '''
    # Locate the mainfeed_category_dropdown and click on it
    dropdown = locate_element(driver, by_id=PROFILE_MAINFEED_CATEGORY_DROPDOWN)
    assert dropdown is not None, "The dropdown is not present"
    dropdown.click()
    thread.sleep(DELAY_TIME)
    
    category = None
    # Locate the mainfeed_category_ and click on it
    if feed == "New":
        category = locate_element(driver, by_id=PROFILE_MAINFEED_CATEGORY_NEW)
    elif feed == "Hot":
        category = locate_element(driver, by_id=PROFILE_MAINFEED_CATEGORY_HOT)
    elif feed == "Top":
        category = locate_element(driver, by_id=PROFILE_MAINFEED_CATEGORY_TOP)
    assert category is not None, "The " + feed + " button is not present"
    category.click()
    thread.sleep(DELAY_TIME)
    # Check that the first p element in dropwdown contains the text "New"
    dropdown = locate_element(driver, by_id=PROFILE_MAINFEED_CATEGORY_DROPDOWN)
    dropdown_p = locate_element(dropdown, by_xpath=".//p")
    print(dropdown_p.text)
    assert dropdown_p.text == feed, "The dropdown is not sorted by " + feed


def profile(driver) -> None:
    '''
    This function is supposed to test the Profile page of the website.
    '''

    # Go to a random user's profile
    driver.get(SITE_NAME + "user/Taya_Shanahan38/")
    thread.sleep(DELAY_TIME)

    # Locate the username and check that it contains the correct username
    username = locate_element(driver, by_xpath=PROFILE_USERNAME)
    assert username.text == "u/Taya_Shanahan38", "The username is incorrect"

    # Sort the content by new
    sort_feed(driver, "New")

    # Locate the user's overview, posts, and comments
    buttons = locate_element(driver, by_id=PROFILE_FEED)
    
    # Click on the second button of buttons  (path is buttons/button[0])
    posts = locate_element(buttons, by_xpath=".//button[2]").click()
    thread.sleep(DELAY_TIME)
    # Check that the url contains the correct path
    assert "submitted" in driver.current_url, "The Posts URL is incorrect"

    # Sort the content by hot
    sort_feed(driver, "Hot")
    # Check that there is an actual post
    # Locate an element that contains mainfeed in its id
    post = locate_element(driver, by_xpath="//*[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('community') + 1) = 'community']")
    # Locate post/a/p and check that it is starts with "r/"
    post_a = locate_element(post, by_xpath=".//a/p")
    print(post_a.text)
    assert post_a.text.startswith("r/"), "The post is incorrect"
    
    # Click on the third button of buttons  (path is buttons/button[1])
    buttons = locate_element(driver, by_id=PROFILE_FEED)
    comments = locate_element(buttons, by_xpath=".//button[3]").click()
    thread.sleep(DELAY_TIME)
    # Check that the url contains the correct path
    assert "comments" in driver.current_url, "The Comments URL is incorrect"
    # Sort the content by top
    sort_feed(driver, "Top")
    # Locate the div with id = 'mainfeed' and check that it contains a p tag in its descendents that contains the text "Taya_Shanahan38"
    comment_p = locate_element(driver, by_xpath=PROFILE_FIRST_COMMENT)
    print(comment_p.text)
    assert "Taya_Shanahan38" in comment_p.text, "The comment is incorrect"
    thread.sleep(DELAY_TIME)

