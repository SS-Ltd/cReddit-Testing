'''
This is the feed subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper_functions import locate_element
from constants import DELAY_TIME
from my_imports import thread
from write_to_files import write_to_all_files, report_fail

def mature(driver) -> None:
    '''
    This function tests the mature feed option
    '''
    # Locate the feed option
    mature_button = locate_element(
        driver, by_xpath='//*[@id="root"]/div[2]/div[3]/div[3]/div/div[1]/div[2]/label/div')
    assert mature_button is not None, report_fail("Mature feed option not found")
    mature_button.click()

def feed(driver) -> None:
    '''
    This function tests the feed subpage of the settings page
    '''

    write_to_all_files(
        "#################### Testing Feed Subpage ####################")

    # Test the 18+ feed option
    mature(driver)

    write_to_all_files(
        "#################### Feed Subpage Test Completed ####################")
