'''
This is the profile subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

import sys
import os
from helper_functions import locate_element, check_popup_notification
from constants import DELAY_TIME
from my_imports import thread
from write_to_files import write_to_all_files, report_fail
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def profile(driver) -> None:
    '''
    This function tests the profile subpage of the settings page
    '''

    write_to_all_files(
        "#################### Testing Profile Subpage ####################")

    write_to_all_files(
        "#################### Profile Subpage Test Completed ####################")
