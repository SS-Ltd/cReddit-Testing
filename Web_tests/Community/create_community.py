'''
This file contains the test cases for creating a community.
'''


import sys
import os
from enum import Enum
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper_functions import locate_element , check_logged_in, check_logged_out , element_dissapeared
from my_imports import WebDriverWait, EC, By, TimeoutException, thread 
from constants import DELAY_TIME,EMAIL, PASSWORD, USERNAME, SEE_TIME,CREDDIT_PASSWORD
from write_to_files import write_to_all_files, report_fail, report_success
def generate_new_community_name()->str:
    '''
    This function generates a new community name
    '''
    x = "Community" + str(thread.time())
    x = x.replace(".","")
    x = x.replace(" ","")
    x = x[0:20]
    return x

def create_community(driver) -> None:
    '''
    This function tests the create community functionality of the website
    '''
    create_community_xpaths = '//*[@id="root"]/div/div[3]/div/div[1]/div/div[6]/div[1]/span[2]'
    locate_element(driver, by_xpath=create_community_xpaths).click()
    thread.sleep(SEE_TIME)
    assert locate_element(driver, by_id="community-name"), report_fail("The community name textbox was not found")
    #duplicate community name

    locate_element(driver, by_id="community-name").send_keys("peak.community") 
    thread.sleep(SEE_TIME)
    
    locate_element(driver, by_id="name-create-community").click()
    thread.sleep(SEE_TIME)
    
    assert driver.current_url == "https://creddit.tech/", report_fail("The community was  created")
    thread.sleep(SEE_TIME)

    #check close button
    locate_element(driver, by_xpath='/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/button').click()
    thread.sleep(5)
    thread.sleep(SEE_TIME)
    
    #check the cancel button 
    locate_element(driver, by_xpath=create_community_xpaths).click()
    thread.sleep(SEE_TIME)
    
    assert locate_element(driver, by_id="cancel-create-community") , report_fail("The cancel button was not found")
    locate_element(driver, by_id="cancel-create-community").click() 
    thread.sleep(SEE_TIME)

    #check the create community correct senario
    locate_element(driver, by_xpath=create_community_xpaths).click() 
    thread.sleep(SEE_TIME)

    community_name = generate_new_community_name()
    assert locate_element(driver, by_id="community-name"), report_fail("The community name textbox was not found")
    locate_element(driver, by_id="community-name").send_keys(community_name) 
    thread.sleep(SEE_TIME)

    assert locate_element(driver, by_id="Private-community-type"), report_fail("The community is Private button was not found")
    locate_element(driver, by_id="Private-community-type").click()
    thread.sleep(SEE_TIME)

    assert locate_element(driver, by_id="Restricted-community-type"), report_fail("The Restricted is public button was not found")
    locate_element(driver, by_id="Restricted-community-type").click()
    thread.sleep(SEE_TIME)

    assert locate_element(driver, by_id="Public-community-type"), report_fail("The Public is public button was not found")
    locate_element(driver, by_id="Public-community-type").click()
    thread.sleep(SEE_TIME)

    assert locate_element(driver, by_id="ismature-switch-btn"), report_fail("The is mature button was not found")
    locate_element(driver, by_id="ismature-switch-btn").click()
    thread.sleep(SEE_TIME)

    assert locate_element(driver, by_id="name-create-community"), report_fail("The create community button was not found")
    locate_element(driver, by_id="ismature-switch-btn").click()
    thread.sleep(SEE_TIME)
    
    assert locate_element(driver, by_id="name-create-community"), report_fail("The create community button was not found")
    locate_element(driver, by_id="name-create-community").click()
    thread.sleep(SEE_TIME)

    assert element_dissapeared(driver, by_id="name-create-community"), report_fail("The community was not created")
    thread.sleep(SEE_TIME)

    assert driver.current_url == "https://creddit.tech/r/"+community_name, report_fail("The community was not created")