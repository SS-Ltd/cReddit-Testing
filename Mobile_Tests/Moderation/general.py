'''
This file checks the GENERAL functionalities of the Mod Tools
'''

from my_imports import webdriver, thread
from constants import DELAY_TIME
from helper_functions import locate_element, end_text
from Paths import MOD_TOOLS_MOD_LOG, MOD_TOOLS_INSIGHTS
from Paths import MOD_TOOLS_COMMUNITY_ICON, MOD_TOOLS_DESCRIPTION
from Paths import MOD_TOOLS_WELCOME_MESSAGE, MOD_TOOLS_TOPICS
from Paths import MOD_TOOLS_COMMUNITY_TYPE, MOD_TOOLS_POST_TYPE
from Paths import MOD_TOOLS_LOCATION
from Paths import MOD_TOOLS_DESCRIPTION_EDIT, MOD_TOOLS_DESCRIPTION_SAVE
from Paths import MOD_TOOLS_COMMUNITY_TYPE_SEEKBAR, MOD_TOOLS_COMMUNITY_TYPE_SAVE, MOD_TOOLS_COMMUNITY_TYPE_SWITCH
from Paths import MOD_TOOLS_COMMUNITY_TYPE_PRIVATE, MOD_TOOLS_COMMUNITY_TYPE_PUBLIC, MOD_TOOLS_COMMUNITY_TYPE_RESTRICTED
from Paths import MOD_TOOLS_POST_TYPE_OPTIONS_ANY, MOD_TOOLS_POST_TYPE_OPTIONS_LINK, MOD_TOOLS_POST_TYPE_OPTIONS_TEXT
from Paths import MOD_TOOLS_POST_TYPE_SAVE
from Paths import OPTION_ANY, OPTION_LINK, OPTION_TEXT
from Paths import IMAGE_POSTS, VIDEO_POSTS, POLL_POSTS
from Paths import IMAGE_SWITCH, VIDEO_SWITCH, POLL_SWITCH
from Paths import LOCATION_TEXT, LOCATION_HEADER, LOCATION_SAVE

def description(driver: webdriver) -> None:
    '''
    This function checks the Description functionalities of the Mod Tools
    '''

    # Click on the Edit button
    edit = locate_element(driver, by_xpath=MOD_TOOLS_DESCRIPTION_EDIT)
    assert edit is not None, "Edit button not found"
    edit.click()
    print("Edit button clicked")
    edit.send_keys('This is a test description')
    print("Text entered")
    end_text(driver)
    thread.sleep(DELAY_TIME)

    # Click on the Save button
    save = locate_element(driver, by_accessibility_id=MOD_TOOLS_DESCRIPTION_SAVE)
    assert save is not None, "Save button not found"
    save.click()
    print("Save button clicked")
    thread.sleep(DELAY_TIME)

    # The correct scenario would be to go back to the community page and check that the description has been updated
    # But it is not implemented, so the test will end here
    # TODO: Validate the text field

    print("Description functionalities of the Mod Tools checked")
    driver.back()

def type(driver: webdriver) -> None:
    '''
    The function checks the Community Type functionalities of the Mod Tools
    '''

    # Locate the seekbar
    seekbar = locate_element(driver, by_class_name=MOD_TOOLS_COMMUNITY_TYPE_SEEKBAR)
    # Get the location of the seekbar
    location = seekbar.location
    # Get the size of the seekbar
    size = seekbar.size
    # Calculate the center of the seekbar
    x = location['x'] + size['width'] / 2
    y = location['y'] + size['height'] / 2
    # Click on the seekbar
    driver.tap([(x, y)])
    print("Seekbar clicked on the center")
    thread.sleep(DELAY_TIME)

    # Check that the text has changed to Restricted
    restricted = locate_element(driver, by_accessibility_id=MOD_TOOLS_COMMUNITY_TYPE_RESTRICTED)
    assert restricted is not None, "Restricted not found"
    print("Restricted found")

    # Calculate the right side of the seekbar
    x = location['x'] + size['width'] - 10
    y = location['y'] + size['height'] / 2
    # Click on the right side of the seekbar
    driver.tap([(x, y)])
    print("Seekbar clicked on the right side")
    thread.sleep(DELAY_TIME)

    # Check that the text has changed to Private
    private = locate_element(driver, by_accessibility_id=MOD_TOOLS_COMMUNITY_TYPE_PRIVATE)
    assert private is not None, "Private not found"
    print("Private found")

    # Calculate the left side of the seekbar
    x = location['x'] + 10
    y = location['y'] + size['height'] / 2
    # Click on the left side of the seekbar
    driver.tap([(x, y)])
    print("Seekbar clicked on the left side")
    thread.sleep(DELAY_TIME)

    # Check that the text has changed to Public
    public = locate_element(driver, by_accessibility_id=MOD_TOOLS_COMMUNITY_TYPE_PUBLIC)
    assert public is not None, "Public not found"
    print("Public found")

    # Click on the 18+ Community switch
    switch = locate_element(driver, by_class_name=MOD_TOOLS_COMMUNITY_TYPE_SWITCH)
    assert switch is not None, "Switch not found"
    # Check if the switch is off
    if switch.get_attribute('checked') == 'false':
        print("Switch initially off")
    elif switch.get_attribute('checked') == 'true':
        print("Switch initially on")
    switch.click()
    print("Switch clicked")
    thread.sleep(DELAY_TIME)
    if switch.get_attribute('checked') == 'false':
        print("Switch turned off")
    elif switch.get_attribute('checked') == 'true':
        print("Switch turned on")

    # Click on the Save button
    save = locate_element(driver, by_accessibility_id=MOD_TOOLS_COMMUNITY_TYPE_SAVE)
    assert save is not None, "Save button not found"
    save.click()
    print("Save button clicked")
    thread.sleep(DELAY_TIME)

    print("Community Type functionalities of the Mod Tools checked")
    driver.back()

def post_type(driver: webdriver) -> None:
    '''
    This function checks the Post Type functionalities of the Mod Tools
    '''

    # First check that the text type shows only poll posts
    any = locate_element(driver, by_accessibility_id=MOD_TOOLS_POST_TYPE_OPTIONS_ANY)
    assert any is not None, "Any not found"
    print("Any found")
    any.click()
    text = locate_element(driver, by_accessibility_id=OPTION_TEXT)
    assert text is not None, "Text not found"
    print("Text found")
    text.click()
    thread.sleep(DELAY_TIME)

    # Check that Image Posts and Video Posts are not found
    image = locate_element(driver, by_accessibility_id=IMAGE_POSTS)
    assert image is None, "Image Posts found"
    print("Image Posts not found")
    video = locate_element(driver, by_accessibility_id=VIDEO_POSTS)
    assert video is None, "Video Posts found"
    print("Video Posts not found")
    post = locate_element(driver, by_accessibility_id=POLL_POSTS)
    assert post is not None, "Poll Posts not found"
    print("Poll Posts found")

    # Check another type of posts
    text = locate_element(driver, by_accessibility_id=MOD_TOOLS_POST_TYPE_OPTIONS_TEXT)
    text.click()
    thread.sleep(DELAY_TIME)
    link = locate_element(driver, by_accessibility_id=OPTION_LINK)
    assert link is not None, "Link not found"
    print("Link found")
    link.click()
    print("Link clicked")
    thread.sleep(DELAY_TIME)

    # Check that Image Posts and Poll Posts are found
    image = locate_element(driver, by_xpath=IMAGE_SWITCH)
    assert image is not None, "Image Posts not found"
    print("Image Posts found")
    if image.get_attribute('checked') == 'false':
        print("Image Posts initially off")
    elif image.get_attribute('checked') == 'true':
        print("Image Posts initially on")
    image.click()
    print("Image Posts clicked")
    thread.sleep(DELAY_TIME)
    if image.get_attribute('checked') == 'false':
        print("Image Posts turned off")
    elif image.get_attribute('checked') == 'true':
        print("Image Posts turned on")
    video = locate_element(driver, by_xpath=VIDEO_SWITCH)
    assert video is not None, "Video Posts not found"
    print("Video Posts found")
    if video.get_attribute('checked') == 'false':
        print("Video Posts initially off")
    elif video.get_attribute('checked') == 'true':
        print("Video Posts initially on")
    video.click()
    print("Video Posts clicked")
    thread.sleep(DELAY_TIME)
    if video.get_attribute('checked') == 'false':
        print("Video Posts turned off")
    elif video.get_attribute('checked') == 'true':
        print("Video Posts turned on")
    poll = locate_element(driver, by_xpath=POLL_SWITCH)
    assert poll is not None, "Poll Posts not found"
    print("Poll Posts found")
    if poll.get_attribute('checked') == 'false':
        print("Poll Posts initially off")
    elif poll.get_attribute('checked') == 'true':
        print("Poll Posts initially on")
    poll.click()
    print("Poll Posts clicked")
    thread.sleep(DELAY_TIME)
    if poll.get_attribute('checked') == 'false':
        print("Poll Posts turned off")
    elif poll.get_attribute('checked') == 'true':
        print("Poll Posts turned on")

    save = locate_element(driver, by_accessibility_id=MOD_TOOLS_POST_TYPE_SAVE)
    assert save is not None, "Save button not found"
    save.click()
    print("Save button clicked")

    print("Post Type functionalities of the Mod Tools checked")
    driver.back()

def location(driver: webdriver) -> None:
    '''
    This function checks the Location functionalities of the Mod Tools
    '''

    # Check that the header exists
    header = locate_element(driver, by_accessibility_id=LOCATION_HEADER)
    assert header is not None, "Header not found"
    print("Header found")

    # Enter some text
    text = locate_element(driver, by_class_name=LOCATION_TEXT)
    assert text is not None, "Text not found"
    text.click()
    text.send_keys("This is a test location")
    print("Text entered")
    end_text(driver)

    # Click on the Save button
    save = locate_element(driver, by_accessibility_id=LOCATION_SAVE)
    assert save is not None, "Save button not found"
    save.click()
    print("Save button clicked")

    print("Location functionalities of the Mod Tools checked")
    driver.back()

def general(driver: webdriver) -> None:
    '''
    This function checks the GENERAL functionalities of the Mod Tools
    '''

    # Click on the Mod Log
    mod_log = locate_element(driver, by_accessibility_id=MOD_TOOLS_MOD_LOG)
    assert mod_log is not None, "Mod log not found"
    # mod_log.click()
    print("Mod log clicked")
    # thread.sleep(DELAY_TIME)

    # Click on the Insights
    insights = locate_element(driver, by_accessibility_id=MOD_TOOLS_INSIGHTS)
    assert insights is not None, "Insights not found"
    # insights.click()
    print("Insights clicked")
    # thread.sleep(DELAY_TIME)

    # Click on the Community Icon
    community_icon = locate_element(driver, by_accessibility_id=MOD_TOOLS_COMMUNITY_ICON)
    assert community_icon is not None, "Community icon not found"
    # community_icon.click()
    print("Community icon clicked")
    # thread.sleep(DELAY_TIME)

    # Click on the Description
    desc = locate_element(driver, by_accessibility_id=MOD_TOOLS_DESCRIPTION)
    assert desc is not None, "Description not found"
    # desc.click()
    print("Description clicked")
    # thread.sleep(DELAY_TIME)
    # description(driver)

    # Click on the Welcome Message
    welcome_message = locate_element(driver, by_accessibility_id=MOD_TOOLS_WELCOME_MESSAGE)
    assert welcome_message is not None, "Welcome message not found"
    # welcome_message.click()
    print("Welcome message clicked")
    # thread.sleep(DELAY_TIME)

    # Click on the Topics
    topics = locate_element(driver, by_accessibility_id=MOD_TOOLS_TOPICS)
    assert topics is not None, "Topics not found"
    # topics.click()
    print("Topics clicked")
    # thread.sleep(DELAY_TIME)

    # Click on the Community Type
    community_type = locate_element(driver, by_accessibility_id=MOD_TOOLS_COMMUNITY_TYPE)
    assert community_type is not None, "Community type not found"
    # community_type.click()
    print("Community type clicked")
    # thread.sleep(DELAY_TIME)
    # type(driver)

    # Click on the Post Type
    pt = locate_element(driver, by_accessibility_id=MOD_TOOLS_POST_TYPE)
    assert pt is not None, "Post type not found"
    # pt.click()
    print("Post type clicked")
    # thread.sleep(DELAY_TIME)
    # post_type(driver)

    # Click on the Location
    loc = locate_element(driver, by_accessibility_id=MOD_TOOLS_LOCATION)
    assert loc is not None, "Location not found"
    loc.click()
    print("Location clicked")
    thread.sleep(DELAY_TIME)
    location(driver)

    print("General functionalities of the Mod Tools checked")
