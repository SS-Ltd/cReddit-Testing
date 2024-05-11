'''
This module is used to test the homepage and move to other connected modules.
'''

from Registration.login import login
from settings import settings
from write_to_files import write_to_all_files
from create_post import create_post
from left_sidebar import left_sidebar
from post import post
from other_profile import profile
from my_profile import my_profile
from chats import chats
from create_community import create_community

def home_page(driver) -> None:
    '''
    This function test the homepage of the website
    '''
    # TEST 1: Test the login functionality
    # login(driver)

    # TEST 2: Test the settings page
    # settings(driver)

    # TEST 3: Create a community
    # create_community(driver)

    # TEST 4: Test the create post functionality
    # create_post(driver)

    # TEST 5: Test the Left SideBar
    # left_sidebar(driver)

    # TEST 6: TEST the post interactions
    # post(driver)

    # TEST 7: Test a random user profile
    # profile(driver)

    # TEST 8: Test my profile page
    # my_profile(driver)

    # TEST 9: Chats
    chats(driver)

    write_to_all_files("Home page test completed")
