'''
This is the safety & privacy subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

import sys
import os
from helper_functions import locate_element
from constants import DELAY_TIME
from my_imports import thread
from write_to_files import write_to_all_files, report_fail
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def people(driver) -> None:
    '''
    This function tests blocking people functionality
    '''

    write_to_all_files("Testing Block People")
    input_field = locate_element(driver, by_id='safety-block-user-input')
    assert input_field is not None, report_fail("Block user input field not found")
    driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.clear()
    input_field.send_keys('Test User')
    # This doesnt really do anything for now
    # Will continue the tests later, probably on the actual reddit website

def communities(driver) -> None:
    '''
    This function tests muting communities functionality
    '''

    write_to_all_files("Testing Block Communities")
    input_field = locate_element(driver, by_id='safety-mute-community-input')
    assert input_field is not None, report_fail("Mute community input field not found")
    driver.execute_script("arguments[0].scrollIntoView();", input_field)
    input_field.clear()
    input_field.send_keys('Test Community')
    # This doesnt really do anything for now
    # Will continue the tests later, probably on the actual reddit website

def privacy(driver) -> None:
    '''
    This function tests the account subpage of the settings page
    '''

    write_to_all_files(
        "#################### Testing Safety & Privacy Subpage ####################")

    people(driver)
    thread.sleep(DELAY_TIME)

    communities(driver)

    write_to_all_files(
        "#################### Safety & Privacy Subpage Test Completed ####################")
