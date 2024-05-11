'''
This Module is supposed to test the Profile page of another user.
'''

from constants import DELAY_TIME, SITE_NAME
from my_imports import thread
from helper_functions import locate_element
from paths import PROFILE_USERNAME, PROFILE_FEED, PROFILE_FIRST_COMMENT
from paths import PROFILE_MAINFEED_CATEGORY_DROPDOWN
from paths import PROFILE_MAINFEED_CATEGORY_NEW, PROFILE_MAINFEED_CATEGORY_HOT, PROFILE_MAINFEED_CATEGORY_TOP
from paths import PROFILE_FOLLOW, PROFILE_CHAT, PROFILE_USER_DROPDOWN
from paths import PROFILE_USER_DROPDOWN_SHARE, PROFILE_USER_DROPDOWN_SEND, PROFILE_USER_DROPDOWN_BLOCK, PROFILE_USER_DROPDOWN_REPORT

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

def test_usercard(driver) -> None:
    '''
    This function is supposed to test the UserCard of the Profile page.
    '''

    # Locate the follow button and click on it
    follow_button = locate_element(driver, by_id=PROFILE_FOLLOW)
    assert follow_button is not None, "The follow button is not present"
    follow_button.click()
    # thread.sleep(DELAY_TIME)
    # Check the p tag inside the follow_button
    # assert locate_element(follow_button, by_xpath=".//p").text == "Unfollow", "The follow button is not working"

    thread.sleep(DELAY_TIME)

    # Click on the follow button again
    # follow_button.click()
    # thread.sleep(DELAY_TIME)
    # Check that the button text is now "Follow"
    # assert locate_element(follow_button, by_xpath=".//p").text == "Follow", "The follow button is not working"

    # Locate the chat button and click on it
    chat_button = locate_element(driver, by_id=PROFILE_CHAT)
    assert chat_button is not None, "The chat button is not present"
    chat_button.click()
    thread.sleep(DELAY_TIME)
    # Check that the url contains the correct path
    assert "chat" in driver.current_url, "The Chat URL is incorrect"
    # Go back to the profile page
    driver.back()
    thread.sleep(DELAY_TIME)

    # Locate the user dropdown button and click on it
    user_dropdown = locate_element(driver, by_id=PROFILE_USER_DROPDOWN)
    assert user_dropdown is not None, "The user dropdown button is not present"
    user_dropdown.click()
    thread.sleep(1)

    # Locate the share button and click on it
    share_button = locate_element(driver, by_xpath=PROFILE_USER_DROPDOWN_SHARE)
    assert share_button is not None, "The share button is not present"
    share_button.click()
    # NOT IMPLEMENTED YET
    print("Share Clicked")

    # Locate the send button and click on it
    send_button = locate_element(driver, by_xpath=PROFILE_USER_DROPDOWN_SEND)
    assert send_button is not None, "The send button is not present"
    send_button.click()
    # NOT IMPLEMENTED YET
    print("Send Clicked")

    # Locate the block button and click on it
    block_button = locate_element(driver, by_xpath=PROFILE_USER_DROPDOWN_BLOCK)
    assert block_button is not None, "The block button is not present"
    block_button.click()
    thread.sleep(DELAY_TIME)
    # Check that an unblock button has appeared
    follow_button = locate_element(driver, by_id=PROFILE_FOLLOW)
    assert locate_element(follow_button, by_xpath=".//p").text == "UnBlock", "The block button is not working"
    # Click on the unblock button
    follow_button.click()

    # Locate the user dropdown button and click on it
    user_dropdown = locate_element(driver, by_id=PROFILE_USER_DROPDOWN)
    assert user_dropdown is not None, "The user dropdown button is not present"
    user_dropdown.click()
    thread.sleep(1)

    # Locate the report button and click on it
    report_button = locate_element(driver, by_xpath=PROFILE_USER_DROPDOWN_REPORT)
    assert report_button is not None, "The report button is not present"
    report_button.click()
    # NOT IMPLEMENTED YET
    print("Report Clicked")

def test_feed(driver) -> None:
    '''
    This function tests the feed of the profile page
    '''
    # Locate the username and check that it contains the correct username
    username = locate_element(driver, by_xpath=PROFILE_USERNAME)
    assert username.text == "u/Edwina54", "The username is incorrect"

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
    post_a = locate_element(post, by_xpath=".//div/p")
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
    assert "Edwina54" in comment_p.text, "The comment is incorrect"
    thread.sleep(DELAY_TIME)


def profile(driver) -> None:
    '''
    This function is supposed to test the Profile page of the website.
    '''

    # Go to a random user's profile
    driver.get(SITE_NAME + "user/Edwina54/")
    thread.sleep(DELAY_TIME)

    # Test1: Test the feed
    test_feed(driver)

    # Test2: Test the user card
    test_usercard(driver)
