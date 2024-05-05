'''
This file contains the tests for the community page.
'''
import sys
import os
from enum import Enum
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper_functions import locate_element , check_logged_in, check_logged_out , element_dissapeared
from my_imports import WebDriverWait, EC, By, TimeoutException, thread 
from constants import DELAY_TIME,EMAIL, PASSWORD, USERNAME, SEE_TIME,CREDDIT_PASSWORD
from write_to_files import write_to_all_files, report_fail, report_success

def community(driver)->str:
    '''
    This function tests the community page of the website
    '''
    community_link = "https://creddit.tech/r/Carlotta.Kreiger61"
    driver.get(community_link)
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    print(locate_element(driver, by_id="community-header__info__community__name").text)
    assert locate_element(driver, by_id="community-header__info__community__name").text == "r/Carlotta.Kreiger61", report_fail("The community name was not found")
    
    locate_element(driver, by_id="community-header__info__community__create-post__icon").click()
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    assert "https://creddit.tech/submit" in driver.current_url , report_fail("The create post button was not found")

    # Test the join button
    driver.get(community_link)
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    get_source = driver.page_source
    locate_element(driver, by_id="community-header__info__community__join__button").click()
    driver.refresh()
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    source_after_click = driver.page_source
    assert get_source.count("Joined") != source_after_click.count("Joined"), report_fail("The join button was not found")

    # Test the mute button
    get_source = driver.page_source
    locate_element(driver, by_id="community-header__info__community__mute__button").click()
    driver.refresh()
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    source_after_click = driver.page_source
    assert get_source.count("Muted") != source_after_click.count("Muted"), report_fail("The mute button was not found")

    # Test the unmute button
    get_source = driver.page_source
    locate_element(driver, by_id="community-header__info__community__mute__button").click()
    driver.refresh()
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    source_after_click = driver.page_source
    assert get_source.count("Muted") != source_after_click.count("Muted"), report_fail("The unmute button was not found")

    # Test the leave button
    get_source = driver.page_source
    locate_element(driver, by_id="community-header__info__community__join__button").click()
    driver.refresh()
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    source_after_click = driver.page_source
    assert get_source.count("Joined") != source_after_click.count("Joined"), report_fail("The leave button was not found")

    # Test the community Listing hot
    driver.get(community_link)
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id="commfeed_category_dropdown").click()
    locate_element(driver, by_id="commfeed_category_hot").click()
    # TODO: assert on the listing
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)

    # Test the community Listing new
    driver.get(community_link)
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id="commfeed_category_dropdown").click()
    locate_element(driver, by_id="commfeed_category_new").click()
    # TODO: assert on the listing
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)

    # Test the community Listing top
    driver.get(community_link)
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id="commfeed_category_dropdown").click()
    locate_element(driver, by_id="commfeed_category_top").click()
    # TODO: assert on the listing
    thread.sleep(SEE_TIME)
    thread.sleep(DELAY_TIME)