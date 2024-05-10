'''
This file contains the tests for the search functionality of the website
'''
from my_imports import thread, By, Keys
from write_to_files import write_to_file
from helper_functions import locate_element
from constants import DELAY_TIME
from paths import (SEARCH_BAR,SEARCH_FILTER_TIME,SEARCH_FILTER_TIME_MONTH,SEARCH_FILTER_TIME_NOW,SEARCH_FILTER_TIME_TODAY
                    ,SEARCH_FILTER_TIME_WEEK,SEARCH_FILTER_TIME_YEAR,SEARCH_FILTER_TIME_ALL_TIME,SEARCH_COMMUNITIES,SEARCH_COMMENTS,SEARCH_HASHTAGS
                    ,SEARCH_PEOPLE,SEARCH_POSTS,SEARCH_SAFE,SEARCH_SORT_BY,SEARCH_SORT_HOT,SEARCH_SORT_NEW,SEARCH_SORT_TOP
                    ,SETTINGS_PRIVACY_ADD_BLOCKED_USERS,SEARCH_CONTENT_MAP)

def search_auto_complete(driver):
    '''
    This function tests the search auto complete functionality of the website
    '''
    driver.get("https://creddit.tech/")
    # Click on the search button
    locate_element(driver, by_id=SEARCH_BAR).click()
    locate_element(driver, by_id=SEARCH_BAR).send_keys('apex')
    thread.sleep(DELAY_TIME)
    # Check the search bar
    search_list = locate_element(driver, by_xpath='//*[@id="root"]/div/div[1]/header/div/div[3]/div[1]/div[2]/div[1]')
    list_elements = search_list.find_elements(By.XPATH, "./*")
    list_elements = list_elements[1:]
    list_elements = list_elements[0:2:]
    found = False
    for element in list_elements:
        assert 'apex' in element.text, 'The search bar is not working'
        if 'apexlegends' in element.text:
            found = True
            element.click()
        assert 'https://creddit.tech/r/apexlegends/' in driver.current_url, 'The search bar is not working'
    assert found, 'The search bar is not working'

def search_listing(driver):
    '''
    This function tests the search listing functionality of the website
    '''
    # Check the search posts
    search_listing_types =[SEARCH_SORT_HOT,SEARCH_SORT_NEW,SEARCH_SORT_TOP]
    for search_type in search_listing_types:
        locate_element(driver, by_id=SEARCH_SORT_BY).click()
        thread.sleep(1)
        locate_element(driver, by_id=search_type).click()
        thread.sleep(DELAY_TIME)
        search_feed_has_items(driver)
        thread.sleep(DELAY_TIME)

def search_filter(driver):
    '''
    This function tests the search filter functionality of the website
    '''
    # Check the search posts
    search_filter_types =[SEARCH_FILTER_TIME_NOW,SEARCH_FILTER_TIME_TODAY
                          ,SEARCH_FILTER_TIME_WEEK,SEARCH_FILTER_TIME_MONTH
                          ,SEARCH_FILTER_TIME_YEAR,SEARCH_FILTER_TIME_ALL_TIME] 
    for search_type in search_filter_types:
        locate_element(driver, by_id=SEARCH_FILTER_TIME).click()
        thread.sleep(1)
        locate_element(driver, by_id=search_type).click()
        thread.sleep(DELAY_TIME)
        search_feed_has_items(driver)
        thread.sleep(DELAY_TIME)

def safe_search(driver):
    '''
    This function tests the safe search functionality of the website
    '''
    # Check the search posts
    locate_element(driver, by_id=SEARCH_SAFE).click()
    thread.sleep(DELAY_TIME)
    search_feed_has_items(driver)
    thread.sleep(DELAY_TIME)

    locate_element(driver, by_id=SEARCH_SAFE).click()
    thread.sleep(DELAY_TIME)
    search_feed_has_items(driver)
    thread.sleep(DELAY_TIME)

def search_feed_has_items(driver):
    '''
    This function checks if the search feed has items
    '''
    search_list = locate_element(driver,by_id=SEARCH_CONTENT_MAP)
    list_elements = search_list.find_elements(By.XPATH, "./*")
    found = False
    for element in list_elements:
        source = element.get_attribute('outerHTML')
        assert 'thebesttester' in source, 'The search bar is not working'
        if 'thebesttester' in source:
            found = True
            break
    assert found, 'The search bar is not working'

def search(driver):
    '''
    This function tests the search functionality of the website
    '''

    # Click on the search button
    thread.sleep(DELAY_TIME)
    search_auto_complete(driver)
    driver.get("https://creddit.tech/")
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=SEARCH_BAR).click()
    locate_element(driver, by_id=SEARCH_BAR).send_keys('thebesttester',Keys.ENTER)
    thread.sleep(DELAY_TIME)
    search_results_1 = [SEARCH_POSTS,SEARCH_COMMENTS,SEARCH_HASHTAGS]
    search_results_2 = [SEARCH_PEOPLE,SEARCH_COMMUNITIES]
    for search_result in search_results_1:
        locate_element(driver, by_id=search_result).click()
        search_listing(driver)
        search_filter(driver)

    for search_result in search_results_2:
        locate_element(driver, by_id=search_result).click()
        thread.sleep(DELAY_TIME)
        search_feed_has_items(driver)
        thread.sleep(DELAY_TIME)


    driver.get("https://creddit.tech/")
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=SEARCH_BAR).click()
    locate_element(driver, by_id=SEARCH_BAR).send_keys('thebesttester',Keys.ENTER)
    safe_search(driver)
