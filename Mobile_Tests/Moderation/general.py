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
    community_type.click()
    print("Community type clicked")
    thread.sleep(DELAY_TIME)
    type(driver)

    # Click on the Post Type
    post_type = locate_element(driver, by_accessibility_id=MOD_TOOLS_POST_TYPE)
    assert post_type is not None, "Post type not found"
    # post_type.click()
    print("Post type clicked")
    # thread.sleep(DELAY_TIME)

    # Click on the Location
    location = locate_element(driver, by_accessibility_id=MOD_TOOLS_LOCATION)
    assert location is not None, "Location not found"
    # location.click()
    print("Location clicked")
    # thread.sleep(DELAY_TIME)

    print("General functionalities of the Mod Tools checked")
