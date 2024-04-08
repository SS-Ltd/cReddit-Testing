'''
This module is used to test the homepage and move to other connected modules.
'''

from Registration.login import login
from settings import settings
from write_to_files import write_to_all_files

def home_page(driver) -> None:
    '''
    This function test the homepage of the website
    '''
    # TEST 1: Test the login functionality
    # login(driver)

    # TEST 2: Test the settings page
    settings(driver)

    write_to_all_files("Home page test completed")