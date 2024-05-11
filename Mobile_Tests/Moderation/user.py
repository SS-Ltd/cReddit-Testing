'''
This Module tests the user management functionalities of the moderation tools of the mobile application.
'''

from my_imports import webdriver, thread
from constants import DELAY_TIME
from helper_functions import locate_element, end_text
from Paths import MOD_TOOLS_MODERATORS, MOD_TOOLS_APPROVED_USERS, MOD_TOOLS_MUTED_USERS, MOD_TOOLS_BANNED_USERS
# Import anything starting with MOD_MODERATORS from Paths.py
from Paths import MOD_MODERATORS_ALL, MOD_MODERATORS_EDITABLE, MOD_MODERATORS_ADD_MODERATOR
from Paths import MOD_MODERATORS_EDIT_MODERATOR, MOD_MODERATORS_EDIT_PERMISSIONS, MOD_MODERATORS_VIEW_PROFILE, MOD_MODERATORS_REMOVE_MODERATOR
from Paths import MOD_MODERATORS_ADD_MODERATOR_USERNAME, MOD_MODERATORS_ADD_MODERATOR_FULL_PERMISSIONS, MOD_MODERATORS_ADD_MODERATOR_ACCESS
from Paths import MOD_MODERATORS_ADD_MODERATOR_MAIL
from Paths import MOD_MODERATORS_ADD_MODERATOR_CONFIG
from Paths import MOD_MODERATORS_ADD_MODERATOR_POSTS
from Paths import MOD_MODERATORS_ADD_MODERATOR_FLAIR
from Paths import MOD_MODERATORS_ADD_MODERATOR_WIKI
from Paths import MOD_MODERATORS_ADD_MODERATOR_CHAT_CONFIG
from Paths import MOD_MODERATORS_ADD_MODERATOR_CHAT_OPERATOR
from Paths import MOD_MODERATORS_ADD_MODERATOR_INVITE
from Paths import MOD_MODERATORS_ADD_MODERATOR_CANCEL
from Paths import MOD_APPROVED_USERS_EDIT
from Paths import MOD_APPROVED_USERS_EDIT_PERMISSIONS
from Paths import MOD_APPROVED_USERS_VIEW_PROFILE
from Paths import MOD_APPROVED_USERS_REMOVE
from Paths import MOD_APPROVED_USERS_ADD_USER
from Paths import MOD_APPROVED_USERS_ADD_USER_USERNAME
from Paths import MOD_APPROVED_USERS_ADD_USER_ADD
from Paths import MOD_APPROVED_USERS_ADD_USER_CLOSE
from Paths import MOD_MUTED_USERS_INVITE
from Paths import MOD_BANNED_USERS
from Paths import MOD_BANNED_USERS_USERNAME
from Paths import MOD_BANNED_USERS_REASON
from Paths import MOD_BANNED_USERS_NOTE_MOD
from Paths import MOD_BANNED_USERS_DAYS
from Paths import MOD_BANNED_USERS_PERMANENT
from Paths import MOD_BANNED_USERS_NOTE_USER
from Paths import MOD_BANNED_USERS_BAN
from Paths import MOD_BANNED_USERS_CANCEL


def moderators(driver: webdriver) -> None:
    '''
    This function tests the moderators functionalities of the mobile application.
    '''
    # Click on the moderators
    locate_element(driver, by_accessibility_id=MOD_TOOLS_MODERATORS).click()
    thread.sleep(DELAY_TIME)
    print("Moderators clicked")

    # Click on the editable
    locate_element(driver, by_accessibility_id=MOD_MODERATORS_EDITABLE).click()
    print("Editable clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_EDIT_MODERATOR).click()
    print("Edit moderator clicked")
    locate_element(driver, by_accessibility_id=MOD_MODERATORS_EDIT_PERMISSIONS).click()
    print("Edit permissions clicked")
    locate_element(driver, by_accessibility_id=MOD_MODERATORS_VIEW_PROFILE).click()
    print("View profile clicked")
    locate_element(driver, by_accessibility_id=MOD_MODERATORS_REMOVE_MODERATOR).click()
    print("Remove moderator clicked")

    driver.back()

    # Click on the all tab
    locate_element(driver, by_accessibility_id=MOD_MODERATORS_ALL).click()
    print("All clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR).click()
    print("Add moderator clicked")
    username = locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_USERNAME)
    username.click()
    username.send_keys("username")
    end_text(driver)
    print("Username entered")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_FULL_PERMISSIONS).click()
    print("Full permissions clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_ACCESS).click()
    print("Access clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_MAIL).click()
    print("Mail clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_CONFIG).click()
    print("Config clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_POSTS).click()
    print("Posts clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_FLAIR).click()
    print("Flair clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_WIKI).click()
    print("Wiki clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_CHAT_CONFIG).click()
    print("Chat config clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_CHAT_OPERATOR).click()
    print("Chat operator clicked")
    locate_element(driver, by_accessibility_id=MOD_MODERATORS_ADD_MODERATOR_INVITE).click()
    print("Invite clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_CANCEL).click()
    print("Cancel clicked")

    print("Moderators functionalities checked")
    driver.back()

def approved_users(driver: webdriver) -> None:
    '''
    This function tests the approved users functionalities of the mobile application.
    '''
    # Click on the approved users
    locate_element(driver, by_accessibility_id=MOD_TOOLS_APPROVED_USERS).click()
    print("Approved users clicked")
    locate_element(driver, by_xpath=MOD_APPROVED_USERS_EDIT).click()
    print("Edit clicked")
    locate_element(driver, by_accessibility_id=MOD_APPROVED_USERS_EDIT_PERMISSIONS).click()
    print("Edit permissions clicked")
    locate_element(driver, by_accessibility_id=MOD_APPROVED_USERS_VIEW_PROFILE).click()
    print("View profile clicked")
    locate_element(driver, by_accessibility_id=MOD_APPROVED_USERS_REMOVE).click()
    print("Remove clicked")
    
    driver.back()

    locate_element(driver, by_xpath=MOD_APPROVED_USERS_ADD_USER).click()
    print("Add user clicked")
    username = locate_element(driver, by_xpath=MOD_APPROVED_USERS_ADD_USER_USERNAME)
    username.click()
    username.send_keys("username")
    end_text(driver)
    print("Username entered")
    locate_element(driver, by_accessibility_id=MOD_APPROVED_USERS_ADD_USER_ADD).click()
    print("Add clicked")
    locate_element(driver, by_xpath=MOD_APPROVED_USERS_ADD_USER_CLOSE).click()
    print("Close clicked")

    print("Approved users functionalities checked")
    driver.back()

def muted_users(driver: webdriver) -> None:
    '''
    This function tests the muted users functionalities of the mobile application.
    '''
    # Click on the muted users
    locate_element(driver, by_accessibility_id=MOD_TOOLS_MUTED_USERS).click()
    print("Muted users clicked")

    locate_element(driver, by_xpath=MOD_APPROVED_USERS_ADD_USER).click()
    print("Add user clicked")
    username = locate_element(driver, by_xpath=MOD_APPROVED_USERS_ADD_USER_USERNAME)
    username.click()
    username.send_keys("username")
    end_text(driver)
    print("Username entered")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_FULL_PERMISSIONS).click()
    print("Full permissions clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_ACCESS).click()
    print("Access clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_MAIL).click()
    print("Mail clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_CONFIG).click()
    print("Config clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_POSTS).click()
    print("Posts clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_FLAIR).click()
    print("Flair clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_WIKI).click()
    print("Wiki clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_CHAT_CONFIG).click()
    print("Chat config clicked")
    locate_element(driver, by_xpath=MOD_MODERATORS_ADD_MODERATOR_CHAT_OPERATOR).click()
    print("Chat operator clicked")
    locate_element(driver, by_accessibility_id=MOD_MUTED_USERS_INVITE).click()
    print("Invite clicked")
    locate_element(driver, by_xpath=MOD_APPROVED_USERS_ADD_USER_CLOSE).click()
    print("Close clicked")

    print("Muted users functionalities checked")

def banned_users(driver: webdriver) -> None:
    '''
    This function tests the banned users functionalities of the mobile application.
    '''
    # Click on the banned users
    locate_element(driver, by_accessibility_id=MOD_TOOLS_BANNED_USERS).click()
    print("Banned users clicked")

    locate_element(driver, by_xpath=MOD_BANNED_USERS).click()
    print("Banned clicked")
    username = locate_element(driver, by_xpath=MOD_BANNED_USERS_USERNAME)
    username.click()
    username.send_keys("username")
    end_text(driver)
    print("Username entered")
    reason = locate_element(driver, by_xpath=MOD_BANNED_USERS_REASON)
    reason.click()
    reason.send_keys("reason")
    end_text(driver)
    print("Reason entered")
    note_mod = locate_element(driver, by_xpath=MOD_BANNED_USERS_NOTE_MOD)
    note_mod.click()
    note_mod.send_keys("note mod")
    end_text(driver)
    print("Note mod entered")
    days = locate_element(driver, by_xpath=MOD_BANNED_USERS_DAYS)
    days.click()
    days.send_keys("7")
    end_text(driver)
    print("Days entered")
    permanent = locate_element(driver, by_xpath=MOD_BANNED_USERS_PERMANENT)
    permanent.click()
    print("Permanent clicked")
    note_user = locate_element(driver, by_xpath=MOD_BANNED_USERS_NOTE_USER)
    note_user.click()
    note_user.send_keys("note user")
    end_text(driver)
    print("Note user entered")
    locate_element(driver, by_accessibility_id=MOD_BANNED_USERS_BAN).click()
    print("Ban clicked")
    locate_element(driver, by_xpath=MOD_BANNED_USERS_CANCEL).click()
    print("Cancel clicked")

    print("Banned users functionalities checked")
    driver.back()


def user_management(driver: webdriver) -> None:
    '''
    This function tests the user management functionalities of the mobile application.
    '''

    # moderators(driver)

    # approved_users(driver)

    # muted_users(driver)

    banned_users(driver)

    print("User management functionalities checked")
