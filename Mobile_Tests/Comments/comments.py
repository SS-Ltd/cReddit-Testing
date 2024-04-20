'''
This file contains the test cases for the comments feature of the mobile app.
'''
from datetime import datetime
from my_imports import thread 
from constants import DELAY_TIME , SEE_TIME
from Paths import (COMMENT_CONTENT, COMMENT_DOWNVOTE, COMMENT_UPVOTE, COMMENT_REPLY, COMMENT_OPTIONS
                   , COMMENT_USERNAME, COMMENT_VOTES,POST_COMMENTS, COMMENT_CREATE, COMMENT_WRITE,COMMENT_POST
                   , COMMENT_EDIT,COMMENT_SAVE,COMMENT_GET_REPLY_NOTIFICATIONS,COMMENT_COPY_TEXT,COMMENT_COLAPSE_THREAD
                   , COMMENT_REPORT,COMMENT_BLOCK_ACCOUNT,COMMENT_SHARE,COMMENT_UNSAVE,COMMENT_DELETE)
from helper_functions import locate_element , end_text

def create_comment(driver)->str:
    '''
    This function tests creating a comment
    '''
    locate_element(driver, by_xpath=COMMENT_CREATE).click()
    comment_create = locate_element(driver, by_xpath=COMMENT_WRITE)
    thread.sleep(SEE_TIME)
    thread.sleep(3)
    comment_text = "This is a comment by the tester at the time of testing" + str(datetime.now())
    comment_create.send_keys(comment_text)
    thread.sleep(SEE_TIME)

    locate_element(driver, by_accessibility_id=COMMENT_POST).click()
    thread.sleep(SEE_TIME)

    end_text(driver)
    get_source = driver.page_source
    assert comment_text in get_source, 'Comment not found in source'
    return comment_text

def get_comment_votes(driver,up_down :bool = False)->int:
    '''
    This function tests the get comment votes feature
    '''
    comment_votes = driver.page_source
    comment_votes_position = comment_votes.find(COMMENT_VOTES)
    comment_votes = comment_votes[comment_votes_position + len(COMMENT_VOTES)+5:]
    comment_votes = comment_votes[:comment_votes.find(' ')-1]
    print(comment_votes)
    if comment_votes == 'Vote':
        return 0
    return int(comment_votes)

def up_down_vote_comment(driver):
    '''
    This function tests the up vote and down vote button
    '''
    # Not Working because the comment votes cannot be read
    # carefull that 0 votes is writen as vote no the number 0
    comment_votes = get_comment_votes(driver)
    print(str(comment_votes))

    comment_upvote = locate_element(driver,by_id=COMMENT_UPVOTE)
    comment_downvote = locate_element(driver,by_id=COMMENT_DOWNVOTE)
    comment_downvote.click()
    thread.sleep(DELAY_TIME)
    assert comment_votes - 2 == get_comment_votes(driver), 'Downvote failed'
    comment_votes = get_comment_votes(driver)
    comment_downvote.click()
    #check if the vote is 0
    thread.sleep(DELAY_TIME)
    assert comment_votes + 1 == get_comment_votes(driver), 'Downvote failed'
    comment_votes = get_comment_votes(driver)
    comment_upvote.click()
    thread.sleep(DELAY_TIME)
    assert comment_votes + 1 == get_comment_votes(driver), 'Upvote failed'
    comment_votes = get_comment_votes(driver)
    comment_upvote.click()
    thread.sleep(DELAY_TIME)
    #check if the vote is 0
    assert comment_votes - 1 == get_comment_votes(driver), 'Upvote failed'
    comment_votes = get_comment_votes(driver)

def edit_comment(driver):
    '''
    This function tests the edit comment feature
    '''
    comment_options = locate_element(driver,by_id=COMMENT_OPTIONS)
    comment_options.click()
    comment_edit = locate_element(driver,by_accessibility_id=COMMENT_EDIT)
    comment_edit.click()
    comment_create = locate_element(driver, by_xpath=COMMENT_WRITE)
    thread.sleep(SEE_TIME)
    comment_text = "This is a comment by the tester at the time of testing" + str(datetime.now())
    comment_create.send_keys(comment_text)
    thread.sleep(SEE_TIME)
    locate_element(driver, by_accessibility_id="Save").click()
    thread.sleep(SEE_TIME)
    end_text(driver)
    thread.sleep(5)
    get_source = driver.page_source
    assert comment_text in get_source, 'Comment not found in source'

def save_comment(driver):
    '''
    This function tests the save comment feature
    '''
    comment_options = locate_element(driver,by_id=COMMENT_OPTIONS)
    comment_options.click()
    comment_save = locate_element(driver,by_accessibility_id=COMMENT_SAVE)
    comment_save.click()
    thread.sleep(SEE_TIME)
    thread.sleep(1)
    assert locate_element(driver,by_accessibility_id='Comment Saved!') is not None, 'Comment not saved'


def delete_comment(driver):
    '''
    This function tests the delete comment feature
    '''
    comment_text = create_comment(driver)
    comment_options = locate_element(driver,by_id=COMMENT_OPTIONS)
    comment_options.click()
    comment_delete = locate_element(driver,by_accessibility_id=COMMENT_DELETE)
    comment_delete.click()
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    get_source = driver.page_source
    assert comment_text not in get_source, 'Comment found in source'

def copy_comment(driver):
    '''
    This function tests the copy comment feature
    '''
    comment_text = create_comment(driver)
    comment_options = locate_element(driver,by_id=COMMENT_OPTIONS)
    comment_options.click()
    comment_copy = locate_element(driver,by_accessibility_id=COMMENT_COPY_TEXT)
    comment_copy.click()
    thread.sleep(SEE_TIME)
    #get_source = driver.page_source
    clipboard_text = driver.get_clipboard_text()
    assert clipboard_text in comment_text, 'Comment not found in source'

def report_comment(driver):
    '''
    This function tests the report comment feature
    '''
    comment_options = locate_element(driver,by_id=COMMENT_OPTIONS)
    comment_options.click()
    comment_report = locate_element(driver,by_accessibility_id=COMMENT_REPORT)
    comment_report.click()
    thread.sleep(SEE_TIME)
    get_source = driver.page_source
    assert locate_element(driver,by_accessibility_id='Comment Reported!') is not None, 'Comment did not get Reported'

def unsave_comment(driver):
    '''
    This function tests the unsave comment feature
    '''
    comment_options = locate_element(driver,by_id=COMMENT_OPTIONS)
    comment_options.click()
    comment_unsave = locate_element(driver,by_accessibility_id=COMMENT_UNSAVE)
    comment_unsave.click()
    thread.sleep(SEE_TIME)
    #get_source = driver.page_source
    assert locate_element(driver,by_accessibility_id='Comment Unsaved!') is not None, 'Comment did not unsave'



def share_comment(driver):
    '''
    This function tests the share comment feature
    '''
    # Not Implemented
    comment_options = locate_element(driver,by_id=COMMENT_OPTIONS)
    comment_options.click()
    comment_share = locate_element(driver,by_accessibility_id=COMMENT_SHARE)
    comment_share.click()
    thread.sleep(SEE_TIME)
    get_source = driver.page_source
    assert locate_element(driver,by_accessibility_id='Comment Shared!') is not None, 'Comment not shared'

def comment(driver):
    '''
    This function tests the comments feature of the mobile app.
    '''
    #goto post
    post_comments = locate_element(driver, by_id=POST_COMMENTS)
    assert post_comments is not None, 'Post comments button not found'
    post_comments.click()
    thread.sleep(SEE_TIME)
    #locate comment
    create_comment(driver)
    thread.sleep(3)
    up_down_vote_comment(driver)
    edit_comment(driver)
    save_comment(driver)
    unsave_comment(driver)
    copy_comment(driver)
    delete_comment(driver)
    report_comment(driver)
    share_comment(driver)
