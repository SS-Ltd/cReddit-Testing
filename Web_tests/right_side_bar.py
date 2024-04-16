'''
This file contains the test cases for the right side bar of the website.
'''

from datetime import datetime
from my_imports import thread 
from constants import DELAY_TIME , SEE_TIME
from paths import (RIGHT_SIDE_BAR_CLEAR, RIGHT_SIDE_BAR_COMMUNITY_NAME, RIGHT_SIDE_BAR_POST_TITLE)
from helper_functions import locate_element
from write_to_files import report_success

def test_right_side_bar(driver):
    '''
    This function tests the right side bar of the website
    '''
    
    # Test the right side bar
    right_side_bar_community_name = locate_element(driver, by_xpath='//*[contains(@id, "'+RIGHT_SIDE_BAR_COMMUNITY_NAME+'")]')
    right_side_bar_community_name_text = right_side_bar_community_name.text
    print(right_side_bar_community_name_text)
    right_side_bar_community_name.click()
    thread.sleep(SEE_TIME)
    assert right_side_bar_community_name_text in driver.current_url, 'Community name not found in URL'

    driver.back()
    thread.sleep(SEE_TIME)

    right_side_bar_post_title = locate_element(driver, by_xpath='//*[contains(@id, "'+RIGHT_SIDE_BAR_POST_TITLE+'")]')
    right_side_bar_post_title_text = right_side_bar_post_title.text
    print(right_side_bar_post_title_text)
    right_side_bar_post_title.click()
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    getsourse = driver.page_source
    assert right_side_bar_community_name_text in driver.current_url, 'Post title not found in URL'
    assert right_side_bar_post_title_text in getsourse, 'Post title not found in source'

    driver.back()
    thread.sleep(SEE_TIME)

    right_side_bar_clear = locate_element(driver, by_xpath='//*[contains(@id, "'+RIGHT_SIDE_BAR_CLEAR+'")]')
    right_side_bar_clear.click()
    thread.sleep(SEE_TIME)

    getsourse = driver.page_source

    assert "RECENT POSTS" not in getsourse, 'Right side bar clear failed'
    report_success('Right side bar test passed')
