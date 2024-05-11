'''
This file contains the messages tests
'''

from my_imports import thread, By, Keys
from write_to_files import write_to_file
from helper_functions import locate_element
from constants import DELAY_TIME
from paths import (NOTIFICATIONS,MESSAGES,MESSAGES_COMPOSE,MESSAGES_COMPOSE_MESSAGE,MESSAGES_COMPOSE_SEND,MESSAGES_COMPOSE_SUBJECT
                   , MESSAGES_COMPOSE, MESSAGES_COMPOSE_MESSAGE,MESSAGES_COMPOSE_SEND,MESSAGES_COMPOSE_SUBJECT
                   , MESSAGES_INBOX_ITEMS,MESSAGES_INBOX,MESSAGES_ALL,MESSAGES_SENT,MESSAGES_COMPOSE_USERNAME
                   , MESSAGES_MESSAGES,MESSAGES_POST_REPLIES,MESSAGES_UNREAD,MESSAGES_USERNAME_MENTIONS
                   , MESSAGES_MESSAGES_ITEMS,MESSAGES_POST_REPLIES_ITEMS,MESSAGES_UNREAD_ITEMS,MESSAGES_USERNAME_MENTIONS_ITEMS)
def logout(driver):
    '''
    This function logs out
    '''
    locate_element(driver, by_id="navbar_profile").click()
    thread.sleep(1)
    locate_element(driver, by_id="profile_logout").click()
    thread.sleep(1)

def messages(driver):
    '''
    This function tests the messages page of the website
    '''
    # Click on the messages tab
    locate_element(driver, by_id=NOTIFICATIONS).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_xpath=MESSAGES).click()
    thread.sleep(DELAY_TIME)
    # Compose a message
    locate_element(driver, by_xpath=MESSAGES_COMPOSE).click()
    thread.sleep(DELAY_TIME)
    # Compose a message
    locate_element(driver, by_xpath=MESSAGES_COMPOSE_USERNAME).send_keys("RadiantSamurai")
    locate_element(driver, by_xpath=MESSAGES_COMPOSE_SUBJECT).send_keys("Test")
    locate_element(driver, by_xpath=MESSAGES_COMPOSE_MESSAGE).send_keys("This is a test message")
    locate_element(driver, by_xpath=MESSAGES_COMPOSE_SEND).click()
    thread.sleep(DELAY_TIME)
    # Check the sent messages
    locate_element(driver, by_xpath=MESSAGES_SENT).click()
    messages = locate_element(driver, by_id="sent")
    messages = messages.find_elements(By.XPATH, "./*")
    assert len(messages) > 0, 'There are no sent messages sent'

    locate_element(driver, by_xpath=MESSAGES_INBOX).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_xpath=MESSAGES_ALL).click()
    # Check the inbox messages
    locate_element(driver, by_xpath=MESSAGES_INBOX).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_xpath=MESSAGES_ALL).click()
    messages = locate_element(driver, by_id=MESSAGES_INBOX_ITEMS)
    messages = messages.find_elements(By.XPATH, "./*")
    assert len(messages) > 0, 'There are no messages in the ALL inbox'
    thread.sleep(DELAY_TIME)
    # Check the unread messages
    locate_element(driver, by_xpath=MESSAGES_UNREAD).click()
    thread.sleep(DELAY_TIME)
    messages = locate_element(driver, by_id=MESSAGES_UNREAD_ITEMS)
    messages = messages.find_elements(By.XPATH, "./*")
    assert len(messages) > 0, 'There are no messages in the UNREAD inbox'
    thread.sleep(DELAY_TIME)
    # Check the username mentions
    locate_element(driver, by_xpath=MESSAGES_USERNAME_MENTIONS).click()
    thread.sleep(DELAY_TIME)
    messages = locate_element(driver, by_id=MESSAGES_USERNAME_MENTIONS_ITEMS)
    messages = messages.find_elements(By.XPATH, "./*")
    assert len(messages) > 0, 'There are no messages in the USERNAME MENTIONS inbox'
    thread.sleep(DELAY_TIME)
    # Check the post replies
    locate_element(driver, by_xpath=MESSAGES_POST_REPLIES).click()
    thread.sleep(DELAY_TIME)
    messages = locate_element(driver, by_id=MESSAGES_POST_REPLIES_ITEMS)
    messages = messages.find_elements(By.XPATH, "./*")
    assert len(messages) > 0, 'There are no messages in the POST REPLIES inbox'
    thread.sleep(DELAY_TIME)
    # Check the messages
    locate_element(driver, by_xpath=MESSAGES_MESSAGES).click()
    thread.sleep(DELAY_TIME)
    messages = locate_element(driver, by_id=MESSAGES_MESSAGES_ITEMS)
    messages = messages.find_elements(By.XPATH, "./*")
    assert len(messages) > 0, 'There are no messages in the MESSAGES inbox'
    thread.sleep(DELAY_TIME)
   


    driver.get("https://creddit.tech")
    logout(driver)
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_xpath='//*[@id="navbar_login_button"]').click()
    locate_element(driver, by_xpath='//*[@id="login_username"]').send_keys("RadiantSamurai")
    locate_element(driver, by_xpath='//*[@id="login_password"]').send_keys("12345678Mm")
    locate_element(driver, by_xpath='//*[@id="login_submit"]').click()
    thread.sleep(DELAY_TIME)
    # Check the inbox messages
    locate_element(driver, by_id=NOTIFICATIONS).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_xpath=MESSAGES).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_xpath=MESSAGES_INBOX).click()
    thread.sleep(DELAY_TIME)
    messages = locate_element(driver, by_id=MESSAGES_INBOX_ITEMS)
    messages = messages.find_elements(By.XPATH, "./*")
    assert len(messages) > 0, 'There are no messages in the inbox'
