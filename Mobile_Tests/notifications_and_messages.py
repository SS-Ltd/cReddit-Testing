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
                   , START_PASSWORD,START_USERNAME,START_LOGIN,SEARCH_BAR,SEARCH_ICON,COMMENTS_BACK)
from search import send_keys_slowly
from Comments.comments import create_comment

def notifications_and_messages(driver):
    '''
    This function tests the notifications of the mobile app
    '''
    #notifications = locate_element(driver, by_accessibility_id='26\nInbox\nTab 5 of 5')
    #notifications.click()
    thread.sleep(5)
    # logout
    # Click on the profile icon
    logout(driver,"Curt37")
    # Click on the right side bar
    thread.sleep(7)
    username = locate_element(driver, by_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')
    username.click()
    thread.sleep(2)
    # username.clear()
    username.send_keys("RadiantSamurai")

    password = locate_element(driver, by_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
    password.click()
    thread.sleep(2)
    # password.clear()
    password.send_keys("12345678Mm")
    end_text(driver)
    thread.sleep(2)
    locate_element(driver, by_accessibility_id=START_LOGIN).click()
    thread.sleep(5)
    locate_element(driver, by_accessibility_id='Best').click()
    thread.sleep(2)
    locate_element(driver, by_accessibility_id='New').click()
    thread.sleep(5)

    post = locate_element(driver,by_xpath='(//android.widget.Button[@content-desc="post comment"])[1]')
    post.click()
    thread.sleep(5)
    send_text = create_comment(driver)
    thread.sleep(5)
    locate_element(driver, by_xpath=COMMENTS_BACK).click()

    notifications = locate_element(driver, by_accessibility_id='28\nInbox\nTab 5 of 5')
    notifications.click()
    thread.sleep(5)
    # Click on the notifications button
    three_dots = locate_element(driver, by_xpath=NOTIFICATIONS_RIGHT_THREE_DOTS)
    three_dots.click()
    thread.sleep(5)
    # Click on the new message button
    new_message = locate_element(driver, by_accessibility_id=MESSAGES_NEW_MESSAGE)
    new_message.click()
    thread.sleep(5)
    # Click on the username button
    username_field = locate_element(driver, by_id=MESSAGE_USERNAME)
    username_field.click()
    thread.sleep(5)
    # Enter the username
    username_field.send_keys("Curt37")
    thread.sleep(1)
    # Click on the subject
    subject_field = locate_element(driver, by_id=MESSAGES_SUBJECT)
    subject_field.click()
    thread.sleep(1)
    messege_text = "This is a test message" + str(thread.time())
    subject_field.send_keys(messege_text)
    thread.sleep(1)

    # Click on the message field
    message_field = locate_element(driver, by_id=MESSAGES_MESSAGE)
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
    username = locate_element(driver, by_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')
    username.click()
    thread.sleep(2)
    # username.clear()
    username.send_keys("Curt37")

    password = locate_element(driver, by_xpath='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
    password.click()
    thread.sleep(2)
    # password.clear()
    password.send_keys("1")
    end_text(driver)
    thread.sleep(2)
    locate_element(driver, by_accessibility_id=START_LOGIN).click()
    thread.sleep(10)

    # check the notificaations 
    notifications = locate_element(driver, by_accessibility_id='43\nInbox\nTab 5 of 5')#update again
    notifications.click()
    thread.sleep(5)
    page_source = driver.page_source

    assert "u/RadiantSamurai commented on your post" in page_source, "Notification not found"

    # check messages
    locate_element(driver, by_accessibility_id=MESSAGES).click()
    page_source = driver.page_source

    assert messege_text in page_source, "Message not found"
    print("success")

