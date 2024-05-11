'''
This file contains the tests for the moderation page.
'''

from my_imports import thread, By, Keys
from write_to_files import write_to_file
from helper_functions import locate_element
from constants import DELAY_TIME
from paths import (MOD_QUEUES_EDITED,MOD_EXIT_MOD_TOOLS,MOD_QUEUES,MOD_QUEUES_UNMODERATED,MOD_QUEUES_OPTIONS_LIST
                   , MOD_QUEUES_REPORTED,MOD_SCHEDULED_POST,MOD_USER_MANAGMENT,MOD_USER_MANAGMENT_APPROVE_USER
                   , MOD_USER_MANAGMENT_APPROVE_USER_APPROVE,MOD_USER_MANAGMENT_APPROVE_USER_CANCEL
                   , MOD_USER_MANAGMENT_APPROVE_USER_USERNAME,MOD_USER_MANAGMENT_APPROVED,MOD_USER_MANAGMENT_APPROVED_REMOVE
                   , MOD_USER_MANAGMENT_BANNED,MOD_USER_MANAGMENT_BANNED_BAN_USER,MOD_USER_MANAGMENT_BANNED_BAN_USER_CANCEL
                   , MOD_USER_MANAGMENT_BANNED_BAN_USER_CONFIRM,MOD_USER_MANAGMENT_BANNED_BAN_USER_DAYS
                   , MOD_USER_MANAGMENT_BANNED_BAN_USER_PERMENANT,MOD_USER_MANAGMENT_BANNED_BAN_USER_REASON 
                   , MOD_USER_MANAGMENT_BANNED_BAN_USER_USER,MOD_USER_MANAGMENT_BANNED_EDIT,MOD_USER_MANAGMENT_BANNED_EDIT_CANCEL
                   , MOD_USER_MANAGMENT_BANNED_EDIT_CONFIRM,MOD_USER_MANAGMENT_BANNED_EDIT_DAYS,MOD_USER_MANAGMENT_BANNED_EDIT_NOTE
                   , MOD_USER_MANAGMENT_BANNED_EDIT_PERMENANT,MOD_USER_MANAGMENT_BANNED_EDIT_REASON,MOD_USER_MANAGMENT_BANNED_UNBAN
                   , MOD_USER_MANAGMENT_MODERATORS,MODERATION_TAB,MOD_MAPPED_MOD,MOD_MAPPED_USERS
                   , MOD_USER_MANAGMENT_BANNED_BAN_USER_NOTE)

def moderation(driver):
    '''
    This function tests the moderation page of the website
    '''
    # Click on the moderation tab
    locate_element(driver, by_xpath=MODERATION_TAB).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=MOD_QUEUES).click()
    locate_element(driver, by_xpath=MOD_QUEUES_UNMODERATED).click()
    thread.sleep(DELAY_TIME)
    # Unmoderated Queue
    get_source = driver.page_source
    mod_queue_options = driver.find_elements(By.ID,MOD_QUEUES_OPTIONS_LIST)
    mod_queue_options_approve = mod_queue_options[0].find_elements(By.XPATH, "./*")
    mod_queue_options_approve[0].click()
    thread.sleep(DELAY_TIME)
    get_source2 = driver.page_source
    assert get_source.count("Approved") < get_source2.count("Approved"), 'The approve button is not working' 
    
    mod_queue_options_remove = mod_queue_options[1].find_elements(By.XPATH, "./*")
    mod_queue_options_remove[1].click()
    thread.sleep(DELAY_TIME)
    get_source3 = driver.page_source
    assert get_source2.count("Removed") < get_source3.count("Removed"), 'The remove button is not working'
    
    mod_queue_options_lock = mod_queue_options[2].find_elements(By.XPATH, "./*")
    mod_queue_options_lock[2].click()
    thread.sleep(DELAY_TIME)
    get_source4 = driver.page_source
    assert get_source3.count("Locked") < get_source4.count("Locked"), 'The lock button is not working'

    # Edited Queue
    locate_element(driver, by_xpath=MOD_QUEUES_EDITED).click()
    thread.sleep(DELAY_TIME)
    posts = locate_element(driver, by_id=MOD_MAPPED_MOD)
    posts = posts.find_elements(By.XPATH, "./*")
    assert len(posts) > 0, 'There are no posts in the edited queue'

    # Reported Queue
    locate_element(driver, by_xpath=MOD_QUEUES_REPORTED).click()
    thread.sleep(DELAY_TIME)
    # nothing to check yet

    # user moderator
    locate_element(driver, by_id=MOD_USER_MANAGMENT).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=MOD_USER_MANAGMENT_MODERATORS).click()
    thread.sleep(DELAY_TIME)
    mods = locate_element(driver, by_id=MOD_MAPPED_USERS)
    mods = mods.find_elements(By.XPATH, "./*")
    assert len(mods) > 0, 'There are no moderators'

    # unApprove user
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_APPROVED).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_APPROVED_REMOVE).click()
    assert locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div[1]/div') is not None, 'The remove button is not working'

    # approve user
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_APPROVED).click()
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_APPROVE_USER).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=MOD_USER_MANAGMENT_APPROVE_USER_USERNAME).click()
    locate_element(driver, by_id=MOD_USER_MANAGMENT_APPROVE_USER_USERNAME).send_keys('thebesttester')
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_APPROVE_USER_APPROVE).click()
    thread.sleep(DELAY_TIME)
    get_source5 = driver.page_source
    assert get_source5.count('thebesttester') > 0, 'The approve user button is not working'

    # ban user
    locate_element(driver, by_id=MOD_USER_MANAGMENT_BANNED).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=MOD_USER_MANAGMENT_BANNED_BAN_USER).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=MOD_USER_MANAGMENT_BANNED_BAN_USER_USER).click()
    locate_element(driver, by_id=MOD_USER_MANAGMENT_BANNED_BAN_USER_USER).send_keys('thebesttester')
    locate_element(driver, by_id=MOD_USER_MANAGMENT_BANNED_BAN_USER_DAYS).click()
    locate_element(driver, by_id=MOD_USER_MANAGMENT_BANNED_BAN_USER_DAYS).send_keys('1')
    locate_element(driver, by_id=MOD_USER_MANAGMENT_BANNED_BAN_USER_NOTE).click()
    locate_element(driver, by_id=MOD_USER_MANAGMENT_BANNED_BAN_USER_NOTE).send_keys('testing')
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_BAN_USER_PERMENANT).click()
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_BAN_USER_REASON).click()
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_BAN_USER_REASON).send_keys(Keys.DOWN, Keys.ENTER)
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=MOD_USER_MANAGMENT_BANNED_BAN_USER_CONFIRM).click()
    thread.sleep(DELAY_TIME)
    get_source6 = driver.page_source
    assert get_source6.count('thebesttester') > 0, 'The ban user button is not working'

    #edit ban
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_EDIT).click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_EDIT_DAYS).click()
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_EDIT_DAYS).send_keys('2')
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_EDIT_PERMENANT).click()
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_EDIT_REASON).click()
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_EDIT_REASON).send_keys(Keys.DOWN, Keys.ENTER)
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_EDIT_NOTE).click()
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_EDIT_NOTE).send_keys('testing')
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_EDIT_CONFIRM).click()
    thread.sleep(DELAY_TIME)
    assert locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div[1]/div').text == 'User banned' , 'The edit ban button is not working'

    # unban user
    locate_element(driver, by_xpath=MOD_USER_MANAGMENT_BANNED_UNBAN).click()
    thread.sleep(DELAY_TIME)
    assert locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div[1]/div').text == 'User unbanned' , 'The edit ban button is not working'

    # scheduled post
    locate_element(driver, by_id=MOD_SCHEDULED_POST).click()
    thread.sleep(DELAY_TIME)
    posts = locate_element(driver, by_id=MOD_MAPPED_MOD)
    posts = posts.find_elements(By.XPATH, "./*")
    assert len(posts) > 0, 'There are no scheduled posts'

    # schedule post
    # not implemented yet