'''
This Module checks the functionalities of the posts in the mobile application
'''

from my_imports import thread
from constants import DELAY_TIME, SEE_TIME
from helper_functions import locate_element, end_text
from Paths import NAVIGATION_BAR_CREATE_POST, POST_COMMENTS, POST_VOTES
from Paths import POST_UPVOTE, POST_DOWNVOTE, POST_SHARE
from create_post import create_post

def get_post_votes(driver)->int:
    '''
    This function tests the get comment votes feature
    '''
    post_votes = driver.page_source
    # print("POST VOTES")
    # print('-----------------------------------------------------------------------------------')
    # print(post_votes)
    post_votes_position = post_votes.find(POST_VOTES)
    # print("POST VOTES POSITION")
    # print('-----------------------------------------------------------------------------------')
    # print(post_votes_position)
    post_votes = post_votes[post_votes_position + len(POST_VOTES)+5:]
    # print("POST VOTES")
    # print('-----------------------------------------------------------------------------------')
    # print(post_votes)
    post_votes = post_votes[:post_votes.find('&')]
    # print("POST VOTES")
    # print('-----------------------------------------------------------------------------------')
    # print(post_votes)
    # print(post_votes)
    if post_votes == 'Vote':
        return 0
    return int(post_votes)

def post(driver) -> None:
    '''
    This function checks the functionalities of the posts in the mobile application
    '''

    # Create a Post
    # create = locate_element(driver, by_accessibility_id=NAVIGATION_BAR_CREATE_POST)
    # create.click()
    # thread.sleep(DELAY_TIME)
    # print("Create post clicked")
    # create_post(driver)

    # Check the post
    # To Be Implemented

    # Post interactions
    post_comments = locate_element(driver, by_id=POST_COMMENTS)
    assert post_comments is not None, 'Post comments button not found'
    post_comments.click()
    thread.sleep(SEE_TIME)

    # Check the votes of the comment
    post_votes = get_post_votes(driver)
    print(post_votes)

    # Upvote the post
    upvote = locate_element(driver, by_id=POST_UPVOTE)
    assert upvote is not None, 'Upvote button not found'
    upvote.click()
    thread.sleep(DELAY_TIME)

    # Check the votes of the comment
    post_votes_updated = get_post_votes(driver)
    print(post_votes_updated)
    assert post_votes_updated == post_votes + 1, 'Upvote not successful'

    # Downvote the post
    downvote = locate_element(driver, by_id=POST_DOWNVOTE)
    assert downvote is not None, 'Downvote button not found'
    downvote.click()
    thread.sleep(DELAY_TIME)

    # Check the votes of the comment
    post_votes_updated = get_post_votes(driver)
    print(post_votes_updated)
    assert post_votes_updated == post_votes - 1, 'Downvote not successful'

    # Share the post
    share = locate_element(driver, by_id=POST_SHARE)
    assert share is not None, 'Share button not found'
    # share.click()
    # thread.sleep(DELAY_TIME)
