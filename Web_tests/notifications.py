'''
This module checks the notifications functionality of the website.
'''

from my_imports import webdriver, thread, By
from constants import DELAY_TIME
from helper_functions import locate_element
from paths import CHAT_CREATE_CHAT, CHAT_INPUT_TEXT, CHAT_SEARCHBAR_INPUT, CHAT_SEARCHBAR_USER, CHAT_SEND_MESSAGE, CREATE_POST_POST, LANDING_CREATE_CHANNEL, NAVBAR_CHAT, PROFILE_FOLLOW
import random

usernames = ['notifications0', 'notifications1', 'notifications2', 'notifications3', 'notifications4', 'notifications5', 'notifications6', 'notifications7', 'notifications8', 'notifications9']
password = 'ABcd1234'

def send_keys_slowly(element, text, delay=0.1):
    for character in text:
        element.send_keys(character)
        thread.sleep(delay)

def notifications(driver: webdriver) -> None:
    '''
    This function tests the notifications functionality of the website.
    '''

    # Logout
    locate_element(driver, by_xpath='//*[@id="navbar_profile"]').click()
    locate_element(driver, by_xpath='//*[@id="profile_logout"]').click()
    thread.sleep(DELAY_TIME)

    # Login
    user1 = random.choice(usernames)
    print(f"Logging in with user: {user1}")
    locate_element(driver, by_xpath='//*[@id="navbar_login_button"]').click()
    locate_element(driver, by_xpath='//*[@id="login_username"]').send_keys(user1)
    locate_element(driver, by_xpath='//*[@id="login_password"]').send_keys(password)
    locate_element(driver, by_xpath='//*[@id="login_submit"]').click()
    thread.sleep(DELAY_TIME)

    # Go to a specific community
    driver.get('https://creddit.tech/submit/r/Chat_Community0')
    
    # Post a post there
    locate_element(driver, by_id='post_title').find_element(By.XPATH, './*').send_keys("Test Notifications")
    locate_element(driver, by_xpath=CREATE_POST_POST).click()
    thread.sleep(DELAY_TIME)

    # Save post url
    post_url = driver.current_url

    # Post a comment
    locate_element(driver, by_id='add_comment').send_keys("Test Notifications")
    locate_element(driver, by_id='submit_comment').click()
    thread.sleep(DELAY_TIME)

    # Logout
    locate_element(driver, by_xpath='//*[@id="navbar_profile"]').click()
    locate_element(driver, by_xpath='//*[@id="profile_logout"]').click()
    thread.sleep(DELAY_TIME)

    # Login
    user2 = random.choice(usernames)
    print(f"Logging in with user: {user2}")
    locate_element(driver, by_xpath='//*[@id="navbar_login_button"]').click()
    locate_element(driver, by_xpath='//*[@id="login_username"]').send_keys(user2)
    locate_element(driver, by_xpath='//*[@id="login_password"]').send_keys(password)
    locate_element(driver, by_xpath='//*[@id="login_submit"]').click()
    thread.sleep(DELAY_TIME)

    # Go to the post
    driver.get(post_url)

    # Upvote the post
    locate_element(driver, by_xpath="//span[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('upvote') + 1) = 'upvote']").click()

    # Downvote the post
    # locate_element(driver, by_xpath="//span[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('downvote') + 1) = 'downvote']").click()

    # Upvote the comment of user1
    locate_element(driver, by_xpath="//span[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('upvote_comment') + 1) = 'upvote_comment']").click()

    # Post a comment
    locate_element(driver, by_id='add_comment').send_keys("Test Notifications")
    locate_element(driver, by_id='submit_comment').click()
    thread.sleep(DELAY_TIME)

    # Go to user's profile
    driver.get('https://creddit.tech/user/' + user1)

    # Follow the user
    locate_element(driver, by_id=PROFILE_FOLLOW).click()
    thread.sleep(DELAY_TIME)

    # Go to Chat page
    locate_element(driver, by_id=NAVBAR_CHAT).click()
    thread.sleep(DELAY_TIME)

    # Create a chat with user1
    locate_element(driver, by_id=LANDING_CREATE_CHANNEL).click()
    print(f"Creating a chat with user: {user1}")
    input_field = locate_element(driver, by_id=CHAT_SEARCHBAR_INPUT)
    input_field.click()
    send_keys_slowly(input_field, user1)
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=CHAT_SEARCHBAR_USER).click()
    locate_element(driver, by_id=CHAT_CREATE_CHAT).click()
    thread.sleep(DELAY_TIME)

    # Enter that chat
    chat_threads = driver.find_elements(By.CSS_SELECTOR, "[data-testid='open-threads']")
    chat_threads[1].click()

    # Send a message
    input_field = locate_element(driver, by_xpath=CHAT_INPUT_TEXT)
    input_field.send_keys('Test Notifications')
    locate_element(driver, by_css=CHAT_SEND_MESSAGE).click()
    thread.sleep(DELAY_TIME)

    # Logout
    driver.get('https://creddit.tech/')
    locate_element(driver, by_xpath='//*[@id="navbar_profile"]').click()
    locate_element(driver, by_xpath='//*[@id="profile_logout"]').click()
    thread.sleep(DELAY_TIME)

    # Login with user1
    locate_element(driver, by_xpath='//*[@id="navbar_login_button"]').click()
    locate_element(driver, by_xpath='//*[@id="login_username"]').send_keys(user1)
    locate_element(driver, by_xpath='//*[@id="login_password"]').send_keys(password)
    locate_element(driver, by_xpath='//*[@id="login_submit"]').click()
    thread.sleep(DELAY_TIME)

    # Go to the notifications page
    locate_element(driver, by_id='navbar_bell').click()
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_xpath='//*[@id="root"]/div/div[1]/header/div/div[3]/div[2]/div[2]/div[2]/div[2]/div/div[6]/button').click()

    # Check that the notifications are present
    # Define the base xpath
    base_xpath = '//*[@id="root"]/div/div[3]/div/div[3]/div/div[3]/div'

    # Find all descendant p elements
    p_elements = driver.find_elements(By.XPATH, base_xpath + '//p')
    print(f"Found {len(p_elements)} p elements")
    # print the text in each of the p elements
    for el in p_elements:
        print(el.text)

    # Filter the elements that contain the notification text
    notification_text = f'u/{user2}'
    notifications = [el for el in p_elements if notification_text in el.text]

    # Check if there are 5 notifications
    if len(notifications) >= 5:
        print("Found 5 notifications")
    else:
        print(f"Found {len(notifications)} notifications, not 5")

    print("Notifications test completed")
    thread.sleep(DELAY_TIME)
