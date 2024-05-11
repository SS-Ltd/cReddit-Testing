'''
This file contains the tests for the notifications and messages of the mobile app.
'''

from my_imports import (
    webdriver,
    AppiumOptions,
    thread,
    Dict,
    Any,
    WebDriverWait,
    EC,
    AppiumBy,
)
from helper_functions import locate_element,logout,end_text
from constants import DELAY_TIME
from Paths import (OPEN_RIGHT_SIDE_BAR, NOTIFICATIONS, MESSAGES,NOTIFICATIONS_DISABLE_UPDATES,NAVIGATION_BAR_CHAT
                   , NOTIFICATIONS_HIDE_NOTIFICATION,NAVIGATION_BAR_COMMUNITIES,NAVIGATION_BAR_HOME
                   , NAVIGATION_BAR_CREATE_POST,NAVIGATION_BAR_INBOX,NOTIFICATIONS_MENU_CLOSE,NOTIFICATIONS_RIGHT_THREE_DOTS
                   , NOTIFICATIONS_THREE_DOTS_LOCATION,NOTIFICATIONS_TURN_OFF_NOTIFICATION,MESSAGE_USERNAME
                   , MESSAGES_MARK_ALL_READ,MESSAGES_MESSAGE,MESSAGES_SEND,MESSAGES_NEW_MESSAGE,MESSAGES_SUBJECT
                   , START_PASSWORD,START_USERNAME,START_LOGIN,SEARCH_BAR,SEARCH_ICON)
from search import send_keys_slowly
from Comments.comments import create_comment

def notifications_and_messages(driver):
    '''
    This function tests the notifications of the mobile app
    '''
    # logout
    # Click on the profile icon
    logout(driver,"Curt37")
    # Click on the right side bar
    thread.sleep(5)
    username = locate_element(driver, by_xpath=START_USERNAME)
    username.click()
    thread.sleep(2)
    # username.clear()
    username.send_keys("RadiantSamurai")

    password = locate_element(driver, by_xpath=START_PASSWORD)
    password.click()
    thread.sleep(2)
    # password.clear()
    password.send_keys("12345678Mm")
    end_text(driver)
    thread.sleep(2)
    locate_element(driver, by_accessibility_id=START_LOGIN).click()
    thread.sleep(10)
    search_icon = locate_element(driver, by_accessibility_id=SEARCH_ICON)
    search_icon.click()
    send_text = "this notificataion test" + str(thread.time())
    text = "Curt37"
    search_bar = locate_element(driver, by_id=SEARCH_BAR)
    search_bar.click()
    search_bar.clear()
    send_keys_slowly(search_bar, text)
    thread.sleep(DELAY_TIME)
    print("Search bar clicked")

    # Locate the search button that contains accessibility id starting with 'Search for'
    search_for = locate_element(driver, by_xpath="//android.widget.Button[starts-with(@content-desc, 'Search for')]")
    search_for.click()
    thread.sleep(DELAY_TIME)
    people = locate_element(driver, by_accessibility_id='People\nTab 4 of 5')
    people.click()

    locate_element(driver, by_accessibility_id='u/Curt37').click()
    thread.sleep(5)

    posts = driver.find_elements_by_xpath("//*[contains(@ID, '" + 'post' + "')]")
    for i in posts:
        if 'Curt37' in i.get_attribute('outerHTML'):
            i.click()
            break

    thread.sleep(5)
    send_text = create_comment(driver)
    notifications = locate_element(driver, by_accessibility_id=NAVIGATION_BAR_INBOX)
    notifications.click()
    thread.sleep(5)
    # Click on the notifications button
    three_dots = locate_element(driver, by_accessibility_id=NOTIFICATIONS_RIGHT_THREE_DOTS)
    three_dots.click()
    thread.sleep(5)
    # Click on the new message button
    new_message = locate_element(driver, by_accessibility_id=MESSAGES_NEW_MESSAGE)
    new_message.click()
    thread.sleep(5)
    # Click on the username button
    username_field = locate_element(driver, by_accessibility_id=MESSAGE_USERNAME)
    username_field.click()
    thread.sleep(5)
    # Enter the username
    username_field.send_keys("Curt37")
    thread.sleep(1)
    # Click on the subject
    subject_field = locate_element(driver, by_accessibility_id=MESSAGES_SUBJECT)
    subject_field.click()
    thread.sleep(1)
    messege_text = "This is a test message" + str(thread.time())
    subject_field.send_keys(messege_text)
    thread.sleep(1)

    # Click on the message field
    message_field = locate_element(driver, by_accessibility_id=MESSAGES_MESSAGE)
    message_field.click()
    thread.sleep(1)
    message_field.send_keys("lets goooooo")
    thread.sleep(1)
    # Click on the send button
    send_button = locate_element(driver, by_accessibility_id=MESSAGES_SEND)
    send_button.click()

    logout(driver,"RadiantSamurai")
    # Click on the right side bar
    thread.sleep(5)
    username = locate_element(driver, by_xpath=START_USERNAME)
    username.click()
    thread.sleep(2)
    # username.clear()
    username.send_keys("Curt37")

    password = locate_element(driver, by_xpath=START_PASSWORD)
    password.click()
    thread.sleep(2)
    # password.clear()
    password.send_keys("1")
    end_text(driver)
    thread.sleep(2)
    locate_element(driver, by_accessibility_id=START_LOGIN).click()
    thread.sleep(10)

    # check the notificaations 
    notifications = locate_element(driver, by_accessibility_id=NAVIGATION_BAR_INBOX)
    notifications.click()
    thread.sleep(5)
    page_source = driver.page_source

    assert send_text in page_source, "Notification not found"

    # check messages
    locate_element(driver, by_accessibility_id=MESSAGES).click()
    page_source = driver.page_source

    assert messege_text in page_source, "Message not found"
    print("success")

