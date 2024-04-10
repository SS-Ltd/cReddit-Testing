'''
This module is used to test the homepage and move to other connected modules.
'''

from Registration.login import login
from settings import settings
from write_to_files import write_to_all_files
from create_post import create_post
from left_sidebar import left_sidebar

def home_page(driver) -> None:
    '''
    This function test the homepage of the website
    '''
    # TEST 1: Test the login functionality
    # login(driver)

    # TEST 2: Test the settings page
    # settings(driver)

    # TEST 3: Test the create post functionality
    # create_post(driver)

    # TEST 4: Test the Left SideBar
    left_sidebar(driver)

    write_to_all_files("Home page test completed")
