'''
This module checks the functionalities of the create post page of the mobile application.
'''

from my_imports import thread
from constants import DELAY_TIME
from helper_functions import locate_element, end_text
from Paths import CREATE_POST_TITLE, CREATE_POST_NEXT, CREATE_POST_BODY, CREATE_POST_ADD_LINK, CREATE_POST_LINK_BODY
from Paths import CREATE_POST_ADD_IMAGE, CREATE_POST_IMAGE
from Paths import CREATE_POST_ADD_POLL, CREATE_POST_DURATION_POLL, CREATE_POST_DURATION_POLL_5, CREATE_POST_DURATION_POLL_NEW
from Paths import CREATE_POST_POLL_OPTION_1, CREATE_POST_POLL_OPTION_2, CREATE_POST_POLL_ADD_OPTION, CREATE_POST_POLL_OPTION_3, CREATE_POST_CLOSE_POLL_3
from Paths import CREATE_POST_POST_TO
from Paths import CREATE_POST_POST
from Paths import NAVIGATION_BAR_HOME


def insert_link(driver) -> None:
    '''
    This function checks the functionalities of the insert link in the create post page of the mobile application.
    '''
    # Add a link
    add_link = locate_element(driver, by_accessibility_id=CREATE_POST_ADD_LINK)
    assert add_link is not None, "Add link button not found"
    add_link.click()
    thread.sleep(DELAY_TIME)

    # Check if the link field has opened
    link = locate_element(driver, by_id=CREATE_POST_LINK_BODY)
    assert link is not None, "Link field not opened"
    print("Link page opened")
    link.click()
    link.send_keys("https://www.google.com")
    end_text(driver)
    print("Link entered")
    thread.sleep(DELAY_TIME)

def insert_image(driver) -> None:
    '''
    This function checks the functionalities of the insert image in the create post page of the mobile application.
    '''
    # Add an image
    add_image = locate_element(driver, by_accessibility_id=CREATE_POST_ADD_IMAGE)
    assert add_image is not None, "Add image button not found"
    add_image.click()
    print("Image page opened")
    thread.sleep(DELAY_TIME)

    # Check if the image field has opened
    image = locate_element(driver, by_id=CREATE_POST_IMAGE)
    assert image is not None, "Image field not opened"
    image.click()
    print("Image entered")
    thread.sleep(DELAY_TIME)

def insert_poll(driver) -> None:
    '''
    This function checks the functionalities of the insert poll in the create post page of the mobile application.
    '''
    # Add a poll
    add_poll = locate_element(driver, by_accessibility_id=CREATE_POST_ADD_POLL)
    assert add_poll is not None, "Add poll button not found"
    add_poll.click()
    print("Poll page opened")
    thread.sleep(DELAY_TIME)

    # Check if the poll field has opened
    poll = locate_element(driver, by_accessibility_id=CREATE_POST_DURATION_POLL)
    assert poll is not None, "Poll field not opened"
    poll.click()
    print("Poll entered")
    thread.sleep(DELAY_TIME)
    # Choose 5 days
    poll_5 = locate_element(driver, by_accessibility_id=CREATE_POST_DURATION_POLL_5)
    assert poll_5 is not None, "5 days poll not found"
    poll_5.click()
    print("5 days poll entered")
    thread.sleep(DELAY_TIME)

    # Add options
    option1 = locate_element(driver, by_id=CREATE_POST_POLL_OPTION_1)
    assert option1 is not None, "Option 1 not found"
    option1.click()
    option1.send_keys("Test Option 1")
    end_text(driver)
    print("Option 1 entered")

    option2 = locate_element(driver, by_id=CREATE_POST_POLL_OPTION_2)
    assert option2 is not None, "Option 2 not found"
    option2.click()
    option2.send_keys("Test Option 2")
    end_text(driver)
    print("Option 2 entered")

    # Add a third option
    add_option = locate_element(driver, by_accessibility_id=CREATE_POST_POLL_ADD_OPTION)
    assert add_option is not None, "Add option button not found"
    add_option.click()
    print("Add option clicked")

    option3 = locate_element(driver, by_id=CREATE_POST_POLL_OPTION_3)
    assert option3 is not None, "Option 3 not found"

    close_option3 = locate_element(driver, by_accessibility_id=CREATE_POST_CLOSE_POLL_3)
    assert close_option3 is not None, "Close option 3 button not found"
    close_option3.click()

    # Check no more option 3
    option3 = locate_element(driver, by_id=CREATE_POST_POLL_OPTION_3)
    assert option3 is None, "Option 3 was not closed"

def create_post(driver) -> None:
    '''
    This function checks the functionalities of the create post page of the mobile application.
    '''

    # First try next on an empty post
    next_button = locate_element(driver, by_accessibility_id=CREATE_POST_NEXT)
    # assert next_button is not None, "Next button not found"
    # next_button.click()
    # thread.sleep(DELAY_TIME)

    # If nothing has happened, then empty fields validation has succeeded
    title = locate_element(driver, by_id=CREATE_POST_TITLE)
    assert title is not None, "Empty fields validation failed"
    title.click()
    title.send_keys("This is a test title")
    end_text(driver)
    print("Title entered")

    # Add temp body
    body = locate_element(driver, by_id=CREATE_POST_BODY)
    assert body is not None, "Body not found"
    body.click()
    body.send_keys("This is a test body")
    end_text(driver)
    print("Body entered")

    # Test1: inserting link
    # insert_link(driver)

    # Test2: inserting image
    # insert_image(driver)

    # Test4: Add Poll
    insert_poll(driver)

    # Next
    next_button.click()
    thread.sleep(DELAY_TIME)

    # Check if the next page has opened
    post_to = locate_element(driver, by_accessibility_id=CREATE_POST_POST_TO)
    assert post_to is not None, "Post with title only failed"
    # Select a random community at point(400, 400)
    driver.tap([(400, 400)])
    thread.sleep(DELAY_TIME)

    # Post
    post = locate_element(driver, by_accessibility_id=CREATE_POST_POST)
    assert post is not None, "Post button not found"
    post.click()
    print("Post button clicked")
    thread.sleep(DELAY_TIME)

    # Check if you are back in the homepage
    home_tab = locate_element(driver, by_accessibility_id=NAVIGATION_BAR_HOME)
    assert home_tab is not None, "Post failed"
    # assert home_tab is None, "Empty Link post was posted without a link"

    print("Create post page functionalities checked")
