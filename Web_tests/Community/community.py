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
    