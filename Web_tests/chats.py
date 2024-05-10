'''
This module checks the chats functionality in its entirety
'''

from my_imports import thread, webdriver, By
import random
from constants import DELAY_TIME, SITE_NAME
from helper_functions import locate_element
from paths import NAVBAR_CHAT, LANDING_CREATE_CHANNEL, ADD_CHAT
from paths import CHAT_SEARCHBAR_INPUT, CHAT_SEARCHBAR_USER, CHAT_CREATE_CHAT
from paths import CHAT_INPUT_TEXT, CHAT_SEND_MESSAGE, CHAT_GROUP_INPUT

usernames = ['chat10', 'chat11', 'chat12', 'chat13', 'chat14', 'chat15', 'chat16', 'chat17', 'chat18', 'chat19']
password = 'ABcd1234'

def send_keys_slowly(element, text, delay=0.1):
    for character in text:
        element.send_keys(character)
        thread.sleep(delay)

def logout(driver: webdriver) -> None:
    '''
    This function logs out
    '''
    locate_element(driver, by_xpath='//*[@id="navbar_profile"]').click()
    locate_element(driver, by_xpath='//*[@id="profile_logout"]').click()
    thread.sleep(DELAY_TIME)

def login(driver: webdriver, user: str) -> None:
    '''
    This function logs in with a given username
    '''
    locate_element(driver, by_xpath='//*[@id="navbar_login_button"]').click()
    locate_element(driver, by_xpath='//*[@id="login_username"]').send_keys(user)
    locate_element(driver, by_xpath='//*[@id="login_password"]').send_keys(password)
    locate_element(driver, by_xpath='//*[@id="login_submit"]').click()
    thread.sleep(DELAY_TIME)

def goto_chat_page(driver: webdriver) -> None:
    '''
    This function navigates you to the chats page
    '''
    locate_element(driver, by_id=NAVBAR_CHAT).click()
    thread.sleep(DELAY_TIME)
    assert 'chat' in driver.current_url, "Chat button is not working"

def select_a_chat_thread(driver: webdriver, user: str) -> str:
    '''
    This function selects a random chat thread, or creates one if none exist
    It returns the username of the selected chat thread
    '''

    # Pick a random user to create a chat with
    random_user = random.choice(usernames)
    while random_user == user:
        random_user = random.choice(usernames)
    # Wait for the element to load (adjust timeout if needed)
    chat_threads = driver.find_elements(By.CSS_SELECTOR, "[data-testid='open-threads']")
    if len(chat_threads) == 1:
        print("No chat threads found, creating a new one")
        # Create a new chat thread with another user
        locate_element(driver, by_id=LANDING_CREATE_CHANNEL).click()
        print(f"Creating a chat with user: {random_user}")
        input_field = locate_element(driver, by_id=CHAT_SEARCHBAR_INPUT)
        input_field.click()
        send_keys_slowly(input_field, random_user)
        thread.sleep(DELAY_TIME)
        locate_element(driver, by_id=CHAT_SEARCHBAR_USER).click()
        locate_element(driver, by_id=CHAT_CREATE_CHAT).click()
        thread.sleep(DELAY_TIME)
        # Check if the chat thread is created
        chat_threads = driver.find_elements(By.CSS_SELECTOR, "[data-testid='open-threads']")
        if len(chat_threads) == 1:
            print("Chat thread was not created")
            return None
    chat_threads.pop(0)
    for chat_thread in chat_threads:
        # Get username from the first paragraph with class "text-white"
        username_element = locate_element(chat_thread, by_css="p.text-white.text-sm")
        username = username_element.text

        # Get message from the second paragraph with class "text-gray-400"
        message_element = locate_element(chat_thread, by_css="p.text-gray-400.text-sm")
        message = message_element.text

        # Get timestamp from the second paragraph with class "text-gray-500"
        timestamp_element = locate_element(chat_thread, by_css="p.text-gray-500.text-xs")
        timestamp = timestamp_element.text

        # Print the extracted information for each chat thread
        print(f"Username: {username}")
        print(f"Message: {message}")
        print(f"Timestamp: {timestamp}")
        print("-" * 30)  # Separator for better readability

    # Click on a random thread from chat_threads and see what happens
    random_chat_thread = random.choice(chat_threads)
    # username of the chat thread
    username_element = locate_element(random_chat_thread, by_css="p.text-white.text-sm")
    username = username_element.text
    print(f"Selecting chat thread with user: {username}")
    random_chat_thread.click()
    thread.sleep(DELAY_TIME)
    return username

def send_a_message(driver: webdriver, msg: str) -> str:
    '''
    This function sends a message in the chat thread
    This function returns the sent message
    '''
    input_field = locate_element(driver, by_xpath=CHAT_INPUT_TEXT)
    assert input_field is not None, "Input field not found"
    input_field.send_keys(msg)
    button = locate_element(driver, by_css=CHAT_SEND_MESSAGE)
    assert button is not None, "Send button not found"
    button.click()

    # Check if the message is sent
    thread.sleep(DELAY_TIME)
    driver.refresh()
    thread.sleep(DELAY_TIME)
    chat_threads = driver.find_elements(By.CSS_SELECTOR, "[data-testid='open-threads']")
    chat_threads.pop(0)
    for chat_thread in chat_threads:
        # Get message from the second paragraph with class "text-gray-400"
        message_element = locate_element(chat_thread, by_css="p.text-gray-400.text-sm")
        message = message_element.text
        # Get timestamp from the second paragraph with class "text-gray-500"
        timestamp_element = locate_element(chat_thread, by_css="p.text-gray-500.text-xs")
        timestamp = timestamp_element.text

        # If message is longer than 20 chars, '...' appears at the end, remove it
        if len(message) > 20:
            message = message[:-3]

        # Print the extracted information for each chat thread
        print(f"Message: {message}")
        print(f"Timestamp: {timestamp}")
        print("-" * 30)

        if message in msg and "a few seconds ago" in timestamp:
            print("Message sent successfully")
            return message
    print("Message not sent")
    return None

def check_receive(driver: webdriver, sent_message: str, sent_user: str) -> bool:
    '''
    This function checks the chat thread for a message from a specific user with a specific text
    '''
    chat_threads = driver.find_elements(By.CSS_SELECTOR, "[data-testid='open-threads']")
    chat_threads.pop(0)
    for chat_thread in chat_threads:
        # Get username from the first paragraph with class "text-white"
        username_element = locate_element(chat_thread, by_css="p.text-white.text-sm")
        username = username_element.text

        # Get message from the second paragraph with class "text-gray-400"
        message_element = locate_element(chat_thread, by_css="p.text-gray-400.text-sm")
        message = message_element.text

        # Get timestamp from the second paragraph with class "text-gray-500"
        timestamp_element = locate_element(chat_thread, by_css="p.text-gray-500.text-xs")
        timestamp = timestamp_element.text

        # If message is longer than 20 chars, '...' appears at the end, remove it
        if len(message) > 20:
            message = message[:-3]

        # Print the extracted information for each chat thread
        print(f"Username: {username}")
        print(f"Message: {message}")
        print(f"Timestamp: {timestamp}")
        print("-" * 30)

        if username == sent_user and message in sent_message and "a few seconds ago" in timestamp:
            print("Message received successfully")
            chat_thread.click()
            return True
    print("Message not received")
    return False

def personal_chat(driver: webdriver) -> None:
    '''
    This function tests the chat between 2 users functionality
    '''
    # Login with one of our test users
    temp_username = random.choice(usernames)
    print(f"Logging in with username: {temp_username}")
    login(driver, temp_username)

    goto_chat_page(driver)

    # Select a chat thread
    username = select_a_chat_thread(driver, temp_username)
    assert username is not None, "Chat thread not found"

    # Send a message in the chat thread
    sent_message = send_a_message(driver, "Hello, how are you?")
    assert sent_message is not None, "Message not sent"

    # Logout
    driver.get(SITE_NAME)
    logout(driver)

    # Login with the other user
    print(f"Logging in with username: {username}")
    login(driver, username)
    goto_chat_page(driver)

    # Check if the message is received
    assert check_receive(driver, sent_message, temp_username), "Message not received"

    # Reply back to the message
    sent_message = send_a_message(driver, "I am fine, thank you!")
    assert sent_message is not None, "Message not sent"

    # Logout
    driver.get(SITE_NAME)
    logout(driver)

    # Login with the other user
    print(f"Logging in with username: {temp_username}")
    login(driver, temp_username)
    goto_chat_page(driver)

    # Check if the message is received
    assert check_receive(driver, sent_message, username), "Reply not received"

def create_group_chat(driver: webdriver, user2: str, user3: str, grpname: str) -> bool:
    '''
    This function creates a group chat with 3 users
    '''

    # Click on the add chat button
    locate_element(driver, by_id=ADD_CHAT).click()
    print(f"Creating a group chat with users: {user2}, {user3}")
    input_field = locate_element(driver, by_id=CHAT_SEARCHBAR_INPUT)
    input_field.click()
    input_field.clear()
    send_keys_slowly(input_field, user2)
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=CHAT_SEARCHBAR_USER).click()
    thread.sleep(DELAY_TIME)
    input_field = locate_element(driver, by_id=CHAT_SEARCHBAR_INPUT)
    input_field.click()
    input_field.clear()
    send_keys_slowly(input_field, user3)
    thread.sleep(DELAY_TIME)
    locate_element(driver, by_id=CHAT_SEARCHBAR_USER).click()
    thread.sleep(DELAY_TIME)
    input_field = locate_element(driver, by_id=CHAT_GROUP_INPUT)
    input_field.send_keys(grpname)
    locate_element(driver, by_id=CHAT_CREATE_CHAT).click()
    thread.sleep(DELAY_TIME)
    # Check that it has been created
    chat_threads = driver.find_elements(By.CSS_SELECTOR, "[data-testid='open-threads']")
    chat_threads.pop(0)
    for chat_thread in chat_threads:
        # Get username from the first paragraph with class "text-white"
        groupname_element = locate_element(chat_thread, by_css="p.text-white.text-sm")
        groupname = groupname_element.text

        # Get timestamp from the second paragraph with class "text-gray-500"
        timestamp_element = locate_element(chat_thread, by_css="p.text-gray-500.text-xs")
        timestamp = timestamp_element.text

        # Print the extracted information for each chat thread
        print(f"Groupname/Username: {groupname}")
        print(f"Timestamp: {timestamp}")
        print("-" * 30)

        if groupname == grpname and "a few seconds ago" in timestamp:
            print("Group chat created successfully")
            chat_thread.click()
            return True
    print("Group chat not created")
    return False
    
def group_chat(driver: webdriver) -> None:
    '''
    This function tests the group chat functionality
    '''

    user1 = random.choice(usernames)
    user2 = random.choice(usernames)
    while user1 == user2:
        user2 = random.choice(usernames)
    user3 = random.choice(usernames)
    while user3 == user2 or user3 == user1:
        user3 = random.choice(usernames)
    
    print(f"Logging in with username: {user1}")
    login(driver, user1)

    goto_chat_page(driver)

    # Create a group chat with user2 and user3
    group_name = 'Discord1'
    assert create_group_chat(driver, user2, user3, group_name), "Group chat not created"

    # Send a message in the group chat
    sent_message = send_a_message(driver, "Hello, how are you?")
    assert sent_message is not None, "Message not sent"

    # Logout
    driver.get(SITE_NAME)
    logout(driver)

    # Login with the user2
    print(f"Logging in with username: {user2}")
    login(driver, user2)
    goto_chat_page(driver)

    # Check if the message is received
    assert check_receive(driver, sent_message, group_name), "Message not received"

    # Reply back to the message
    sent_message = send_a_message(driver, "I am fine, thank you!")
    assert sent_message is not None, "Message not sent"

    # Logout
    driver.get(SITE_NAME)
    logout(driver)

    # Login with the user3
    print(f"Logging in with username: {user3}")
    login(driver, user3)
    goto_chat_page(driver)

    # Check if the message is received
    assert check_receive(driver, sent_message, group_name), "Reply not received"

    # Reply back to the message
    sent_message = send_a_message(driver, "I am glad you are both fine!")
    assert sent_message is not None, "Message not sent"

    # Logout
    driver.get(SITE_NAME)
    logout(driver)

    # Login with the user1
    print(f"Logging in with username: {user1}")
    login(driver, user1)
    goto_chat_page(driver)

    # Check if the message is received
    assert check_receive(driver, sent_message, group_name), "Reply not received"

    print("Group chat functionality is working fine")


def chats(driver: webdriver) -> None:
    '''
    This is the main function of testing the chats functionality
    '''

    # Logout if already logged in
    logout(driver)

    personal_chat(driver)

    # group_chat(driver)

    print("Chatting functionality is working fine")
