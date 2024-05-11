'''
This file contains the tests for the chat functionality of the app.
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

def chat(driver):