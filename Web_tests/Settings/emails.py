'''
This is the notifications subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

import sys
import os
from enum import Enum
from helper_functions import check_checkbox
from constants import DELAY_TIME
from my_imports import thread
from write_to_files import write_to_all_files
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Button(Enum):
    '''
    This class is used to define the buttons in the notifications subpage
    '''
    CHAT_REQUESTS = (0, "Chat Requests")
    NEW_FOLLOWERS = (1, "New Followers")
    UNSUBSCRIBE = (2, "Unsubscribe from all emails")


# Constant XPATHS to identify the buttons
BUTTONS = [
    'settings-emails-chat-requests-toggle-button',
    'settings-emails-new-followers-toggle-button',
    'settings-emails-unsubscribe-from-all-emails-toggle-button'
]

def emails(driver) -> None:
    '''
    This function tests the notifications subpage of the settings page
    '''

    write_to_all_files(
        "#################### Testing Notifications Subpage ####################")

    # Test the chat requests button
    check_checkbox(driver, by_id=BUTTONS[Button.CHAT_REQUESTS.value[0]], name=Button.CHAT_REQUESTS.value[1])
    thread.sleep(DELAY_TIME)

    # Test the new followers button
    check_checkbox(driver, by_id=BUTTONS[Button.NEW_FOLLOWERS.value[0]], name=Button.NEW_FOLLOWERS.value[1])
    thread.sleep(DELAY_TIME)

    # Test the unsubscribe button
    check_checkbox(driver, by_id=BUTTONS[Button.UNSUBSCRIBE.value[0]], name=Button.UNSUBSCRIBE.value[1])
    thread.sleep(DELAY_TIME)

    write_to_all_files(
        "#################### Notifications Subpage Test Completed ####################")
