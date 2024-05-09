'''
This module tests the content & moderation functionalities of the mobile application.
'''

from my_imports import webdriver, thread
from helper_functions import locate_element
from constants import DELAY_TIME
from Paths import MOD_TOOLS_QUEUES, MOD_TOOLS_RULES, MOD_TOOLS_SCHEDULED_POSTS
from Paths import QUEUES_COMMUNITY, QUEUES_NEEDS_REVIEW, QUEUES_POSTS_AND_COMMENTS, QUEUES_SORT, QUEUES_GOTO_COMMUNITY
from Paths import QUEUES_REVIEW_NEEDS_REVIEW, QUEUES_REVIEW_REMOVED, QUEUES_REVIEW_REPORTED, QUEUES_REVIEW_EDITED, QUEUES_REVIEW_UNMODERATED
from Paths import QUEUES_PAC_POSTS_AND_COMMENTS, QUEUES_PAC_POSTS_ONLY, QUEUES_PAC_COMMENTS_ONLY

def queues(driver: webdriver) -> None:
    '''
    This function tests the queues functionalities of the mobile application.
    '''
    # Click on the community queues
    community = locate_element(driver, by_accessibility_id=QUEUES_COMMUNITY)
    assert community is not None, "Community queues not found"
    community.click()
    print("Community queues clicked")

    # Click on the needs review
    needs_review = locate_element(driver, by_accessibility_id=QUEUES_NEEDS_REVIEW)
    assert needs_review is not None, "Needs review not found"
    needs_review.click()
    print("Needs review clicked")
    
    edited = locate_element(driver, by_accessibility_id=QUEUES_REVIEW_EDITED)
    assert edited is not None, "Edited not found"
    edited.click()
    print("Edited clicked")
    thread.sleep(DELAY_TIME)

    driver.swipe(1000, 375, 300, 375)

    pac = locate_element(driver, by_accessibility_id=QUEUES_POSTS_AND_COMMENTS)
    assert pac is not None, "Posts and comments not found"
    pac.click()
    print("Posts and comments clicked")

    po = locate_element(driver, by_accessibility_id=QUEUES_PAC_POSTS_ONLY)
    assert po is not None, "Posts only not found"
    po.click()
    print("Posts only clicked")

    sort = locate_element(driver, by_accessibility_id=QUEUES_SORT)
    assert sort is not None, "Sort not found"
    sort.click()
    print("Sort clicked")

    goto_community = locate_element(driver, by_accessibility_id=QUEUES_GOTO_COMMUNITY)
    assert goto_community is not None, "Goto community not found"
    goto_community.click()
    print("Goto community clicked")
    thread.sleep(DELAY_TIME)

    print("Queues functionalities checked")
    driver.back()

def rules(driver: webdriver) -> None:
    '''
    This function tests the rules functionalities of the mobile application.
    '''
    pass



def scheduled_posts(driver: webdriver) -> None:
    '''
    This function tests the scheduled posts functionalities of the mobile application.
    '''
    pass

def content(driver: webdriver) -> None:
    '''
    This function tests the content functionalities of the mobile application.
    '''

    # Click on the queues mod tool
    queue = locate_element(driver, by_accessibility_id=MOD_TOOLS_QUEUES)
    assert queue is not None, "Queues not found"
    queue.click()
    print("Queues clicked")
    queues(driver)

    # Click on the rules mod tool
    rule = locate_element(driver, by_accessibility_id=MOD_TOOLS_RULES)
    assert rule is not None, "Rules not found"    
    rule.click()
    print("Rules clicked")
    rules(driver)

    # Click on the scheduled posts mod tool
    scheduled = locate_element(driver, by_accessibility_id=MOD_TOOLS_SCHEDULED_POSTS)
    assert scheduled is not None, "Scheduled posts not found"
    scheduled.click()
    print("Scheduled posts clicked")
    scheduled_posts(driver)

    print("Content functionalities checked")