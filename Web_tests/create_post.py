'''
This module checks the functionality of creating a post on the website.
'''

from my_imports import thread, By
from write_to_files import write_to_file
from helper_functions import locate_element
from constants import DELAY_TIME
from pynput.keyboard import Controller, Key

def create_post(driver):
    '''
    This function creates a post on the website
    '''
    # Click on the create post button
    locate_element(driver, by_id='navbar_create_post').click()
    thread.sleep(DELAY_TIME)

    # Check the url of the website
    assert driver.current_url == 'http://localhost:5173/submit', 'The url is incorrect'

    # Choose a community to post in
    locate_element(driver, by_id='create_post_community_dropdown_button').click()
    thread.sleep(1)
    locate_element(driver, by_xpath='//*[@id="create_post_community_dropdown_menu"]/ul[1]/li/div').click()
    thread.sleep(1)

    # Write the title of the post
    locate_element(driver, by_id='post_title').find_element(By.XPATH, './*').send_keys('Post Title')
    thread.sleep(1)

    # 1. Post
    
    # Write the body of the post
    # locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div').send_keys('Post Body')
    # thread.sleep(1)

    # 2. Image

    # Upload an image
    locate_element(driver, by_id='type_image').click()
    thread.sleep(1)
    locate_element(driver, by_id='post_drop_image').click()
    thread.sleep(DELAY_TIME)
    keyboard = Controller()

    keyboard.type(
        'C:\\Users\\abdal\\Pictures\\download.jpeg')
    thread.sleep(DELAY_TIME)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    thread.sleep(DELAY_TIME)

    # 3. URL
    # locate_element(driver, by_id='type_link').click()
    # locate_element(driver, by_id='url_content').send_keys('https://www.google.com')

    # 4. Poll
    # locate_element(driver, by_id='type_poll').click()
    # locate_element(driver, by_id='poll_content').send_keys('Poll Question')
    # locate_element(driver, by_id='input_option_1').send_keys('Option 1')
    # locate_element(driver, by_id='input_option_2').send_keys('Option 2')
    # locate_element(driver, by_id='add_option').click()
    # locate_element(driver, by_id='add_option').click()
    # locate_element(driver, by_id='delete_option_3').click()
    # locate_element(driver, by_id='input_option_3').send_keys('Option 3')
    # locate_element(driver, by_id='create_post_vote_dropdown_button').click()
    # locate_element(driver, by_id='vote_2_day').click()
    thread.sleep(1)

    # Submit the post
    locate_element(driver, by_id='submit_post').click()
    thread.sleep(DELAY_TIME)

    # Check that the post has been created
    # Check if the word comments is in the url
    assert 'comments' in driver.current_url, 'Post not created'

    print('Post created successfully')
