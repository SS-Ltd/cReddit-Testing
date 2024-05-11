'''
This module checks the functionality of creating a post on the website.
'''

from my_imports import thread, By
from write_to_files import write_to_file
from helper_functions import locate_element
from constants import DELAY_TIME
from pynput.keyboard import Controller, Key
from paths import CREATE_POST_RANDOM_COMMUNITY, CREATE_POST_BODY
from paths import CREATE_POST_URL, CREATE_POST_LINK, CREATE_POST_POST

def image(driver) -> None:
    '''
    Tests the create post -> image
    '''
    # Upload an image
    locate_element(driver, by_id='type_image').click()
    thread.sleep(1)
    locate_element(driver, by_id='post_drop_image').click()
    thread.sleep(DELAY_TIME)
    keyboard = Controller()

    keyboard.type(
        'C:\\Users\\abdal\\Pictures\\modric.jpg')
    thread.sleep(DELAY_TIME)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    thread.sleep(DELAY_TIME)

def poll(driver) -> None:
    '''
    Tests the create post -> poll
    '''
    locate_element(driver, by_id='type_poll').click()
    locate_element(driver, by_id='poll_content').send_keys('Poll Question')
    locate_element(driver, by_id='input_option_1').send_keys('Option 1')
    locate_element(driver, by_id='input_option_2').send_keys('Option 2')
    locate_element(driver, by_id='add_option').click()
    locate_element(driver, by_id='add_option').click()
    locate_element(driver, by_id='delete_option_3').click()
    locate_element(driver, by_id='input_option_3').send_keys('Option 3')
    locate_element(driver, by_id='create_post_vote_dropdown_button').click()
    locate_element(driver, by_id='vote_2_day').click()

def create_post(driver):
    '''
    This function creates a post on the website
    '''

    for i in range(4):
        # Click on the create post button
        locate_element(driver, by_id='navbar_create_post').click()
        thread.sleep(DELAY_TIME)

        # Check the url of the website
        assert '/submit' in driver.current_url, 'The url is incorrect'

        # Choose a community to post in
        locate_element(driver, by_id='create_post_community_dropdown_button').click()
        thread.sleep(1)
        random = locate_element(driver, by_xpath=CREATE_POST_RANDOM_COMMUNITY)
        # random/div/h1[1].text
        text = locate_element(random, by_xpath='./div/h1[1]')
        print("Text = ", text)
        print(text.text)
        text = text.text
        random.click()
        thread.sleep(1)

        # Write the title of the post
        locate_element(driver, by_id='post_title').find_element(By.XPATH, './*').send_keys('Xabi Alonso <3')
        thread.sleep(1)

        # 1. Post
        if i == 0:
            locate_element(driver, by_xpath=CREATE_POST_BODY).send_keys('Leverkusen X Madrid <3')
        elif i == 1:
            # 2. Image
            image(driver)
        elif i == 2:
            # 3. URL
            locate_element(driver, by_id=CREATE_POST_LINK).click()
            locate_element(driver, by_id=CREATE_POST_URL).send_keys('https://thinking-tester-contact-list.herokuapp.com')
        elif i == 3:
            # 4. Poll
            poll(driver)

        thread.sleep(DELAY_TIME)

        # Submit the post
        locate_element(driver, by_xpath=CREATE_POST_POST).click()
        thread.sleep(DELAY_TIME)

        # Check that the post has been created
        # Check if the word comments is in the url
        assert text in driver.current_url, 'Post not created'

        print('Post ' + str(i) + 'created successfully')

    print('All posts created successfully')
