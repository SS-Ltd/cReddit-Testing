'''
This module is used to test the homepage and move to other connected modules.

'''

from login import login
from write_to_files import write_to_all_files

def home_page(driver) -> None:
    '''
    This function test the homepage of the website
    '''
    # TEST 1: Test the login functionality
    login(driver)

    write_to_all_files("Home page test completed")
