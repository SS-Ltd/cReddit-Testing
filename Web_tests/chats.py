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

def check_chat_exists(driver: webdriver, chat_name=None, chat_message=None, chat_timestamp=None) -> bool:
    '''
    This function checks whether a chat exists inside the chat threads
    If a message or timestamp are provided, check that they match
    '''
    print(f"Checking if chat thread exists with name: {chat_name}, message: {chat_message}, timestamp: {chat_timestamp}")
    chat_threads = driver.find_elements(By.CSS_SELECTOR, "[data-testid='open-threads']")
    if len(chat_threads) == 1:
        return False
    chat_threads.pop(0)
    for chat_thread in chat_threads:
        # Get username from the first paragraph with class "text-white"
        username_element = locate_element(chat_thread, by_css="p.text-white.text-sm")
        username = username_element.text

        # If username is longer than 20 chars, '...' appears at the end, remove it
        if len(username) > 20:
            username = username[:-3]

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
        print("-" * 30)  # Separator for better readability

        if (chat_name is None or username in chat_name) and (chat_message is None or message in chat_message) and (chat_timestamp is None or timestamp in chat_timestamp):
            print("Chat thread found")
            chat_thread.click()
            return True
    print("Chat thread not found")
    return False

def select_a_chat_thread(driver: webdriver, user1: str, user2: str) -> str:
    '''
    This function selects a random chat thread, or creates one if none exist
    It returns the username of the selected chat thread
    '''
    print("User2 is : ", user2)
    if not check_chat_exists(driver, chat_name=user2):
        # Create a new chat thread with another user
        locate_element(driver, by_id=LANDING_CREATE_CHANNEL).click()
        print(f"Creating a chat with user: {user2}")
        input_field = locate_element(driver, by_id=CHAT_SEARCHBAR_INPUT)
        input_field.click()
        send_keys_slowly(input_field, user2)
        thread.sleep(DELAY_TIME)
        locate_element(driver, by_id=CHAT_SEARCHBAR_USER).click()
        locate_element(driver, by_id=CHAT_CREATE_CHAT).click()
        thread.sleep(DELAY_TIME)
    if check_chat_exists(driver, chat_name=user2):
        return user2
    print("Chat thread not found")
    return None

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
    if check_chat_exists(driver, chat_message=msg, chat_timestamp="a few seconds ago"):
        print("Message sent successfully")
        return msg
    print("Message not sent")
    return None

def check_receive(driver: webdriver, sent_message: str, sent_user: str) -> bool:
    '''
    This function checks the chat thread for a message from a specific user with a specific text
    '''
    if check_chat_exists(driver, chat_name=sent_user, chat_message=sent_message, chat_timestamp="a few seconds ago"):
        print("Message received successfully")
        return True
    print("Message not received")
    return False

def personal_chat(driver: webdriver) -> None:
    '''
    This function tests the chat between 2 users functionality
    '''
    # Login with one of our test users
    user1 = random.choice(usernames)
    print(f"Logging in with username: {user1}")
    login(driver, user1)

    goto_chat_page(driver)

    # Select a chat thread
    user2 = random.choice(usernames)
    while user1 == user2:
        user2 = random.choice(usernames)
    username = select_a_chat_thread(driver, user1, user2)
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
    assert check_receive(driver, sent_message, user1), "Message not received"

    # Reply back to the message
    sent_message = send_a_message(driver, "I am fine, thank you!")
    assert sent_message is not None, "Message not sent"

    # Logout
    driver.get(SITE_NAME)
    logout(driver)

    # Login with the other user
    print(f"Logging in with username: {user1}")
    login(driver, user1)
    goto_chat_page(driver)

    # Check if the message is received
    assert check_receive(driver, sent_message, username), "Reply not received"

    print("Personal chat functionality is working fine")


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
    
    if check_chat_exists(driver, chat_name=grpname, chat_timestamp="a few seconds ago"):
        print("Group chat created successfully")
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
    # Set the group name with Discord + the last 2 characters of each user
    group_name = "Discord" + user1[-2:] + user2[-2:] + user3[-2:]
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
    driver.get(SITE_NAME)
    logout(driver)

    personal_chat(driver)
    
    # Logout if already logged in
    driver.get(SITE_NAME)
    logout(driver)

    group_chat(driver)

    print("Chatting functionality is working fine")
