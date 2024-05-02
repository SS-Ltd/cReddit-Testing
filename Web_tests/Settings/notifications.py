'''
This is the notifications subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

from enum import Enum
from helper_functions import check_checkbox
from constants import DELAY_TIME
from my_imports import thread


class Button(Enum):
    '''
    This class is used to define the buttons in the notifications subpage
    '''
    MENTIONS = (0, "Mentions")
    COMMENTS = (1, "Comments")
    UPVOTES_POSTS = (2, "Upvotes on Posts")
    REPLIES = (4, "Replies")
    POSTS_FOLLOWED = (6, "Posts of Followed Users")


# Constant XPATHS to identify the buttons
BUTTONS = [
    'settings-notifications-mentions-of-username-toggle-button',
    'settings-notifications-comments-on-your-posts-toggle-button',
    'settings-notifications-upvotes-on-your-posts-toggle-button',
    'settings-notifications-upvotes-on-your-comments-toggle-button',
    'settings-notifications-replies-to-your-comments-toggle-button',
    'settings-notifications-new-followers-toggle-button',
    'settings-notifications-posts-you-follow-toggle-button',
    'settings-notifications-comments-you-follow-toggle-button'
]

def notifications(driver) -> None:
    '''
    This function tests the notifications subpage of the settings page
    '''

    # Test the mentions button
    check_checkbox(driver, by_id=BUTTONS[Button.MENTIONS.value[0]],
                   name=Button.MENTIONS.value[1])
    thread.sleep(DELAY_TIME)

    # Test the comments button
    check_checkbox(driver, by_id=BUTTONS[Button.COMMENTS.value[0]],
                   name=Button.COMMENTS.value[1])
    thread.sleep(DELAY_TIME)

    # Test the upvotes on posts button
    check_checkbox(driver, by_id=BUTTONS[Button.UPVOTES_POSTS.value[0]],
                   name=Button.UPVOTES_POSTS.value[1])
    thread.sleep(DELAY_TIME)

    # Test the replies button
    check_checkbox(driver, by_id=BUTTONS[Button.REPLIES.value[0]],
                   name=Button.REPLIES.value[1])
    thread.sleep(DELAY_TIME)


    # Test the posts of followed users button
    check_checkbox(driver, by_id=BUTTONS[Button.POSTS_FOLLOWED.value[0]],
                   name=Button.POSTS_FOLLOWED.value[1])
    thread.sleep(DELAY_TIME)
