'''
This module is used to test the settings page of the Reddit website.
'''
from enum import Enum
from my_imports import TimeoutException, thread
from constants import DELAY_TIME, SITE_NAME
from write_to_files import write_to_all_files, report_fail, report_success
from helper_functions import locate_element
from Settings.account import account
from Settings.profile import profile
from Settings.privacy import privacy
from Settings.feed import feed
from Settings.notifications import notifications
from Settings.emails import emails


class Subpage(Enum):
    '''
    This class is used to define the different subpages of the settings page
    '''
    ACCOUNT = (0, "Account")
    PROFILE = (1, "Profile")
    SAFETY = (2, "Safety & Privacy")
    FEED = (3, "Feed Settings")
    NOTIFICATIONS = (4, "Notifications")
    EMAILS = (5, "Emails")


# Constant IDs to identify the subpages
SUBPAGES = {
    Subpage.ACCOUNT: 'setting-navbar-account-tab',
    Subpage.PROFILE: 'setting-navbar-profile-tab',
    Subpage.SAFETY: 'setting-navbar-safety & privacy-tab',
    Subpage.FEED: 'setting-navbar-feed settings-tab',
    Subpage.NOTIFICATIONS: 'setting-navbar-notifications-tab',
    Subpage.EMAILS: 'setting-navbar-emails-tab'
}

URLS = {
    Subpage.ACCOUNT: SITE_NAME + "settings/account",
    Subpage.PROFILE: SITE_NAME + "settings/profile",
    Subpage.SAFETY: SITE_NAME + "settings/privacy",
    Subpage.FEED: SITE_NAME + "settings/feed",
    Subpage.NOTIFICATIONS: SITE_NAME + "settings/notifications",
    Subpage.EMAILS: SITE_NAME + "settings/emails"
}

def goto_settings(driver) -> None:
    '''
    This function goes to the settings page from the homepage
    '''
    driver.get(SITE_NAME + "settings")
    locate_element(driver, by_id="navbar_profile").click()

    locate_element(driver, by_id="profile_settings").click()

    # Check if the settings page is loaded
    thread.sleep(DELAY_TIME)
    assert driver.current_url == SITE_NAME + "settings", 'Did not navigate to settings page'


def goto_subpage(driver, subpage: Subpage) -> None:
    '''
    This function goes to a specific subpage of the settings page

    '''
    driver.refresh()
    locate_element(driver, by_id=SUBPAGES[subpage]).click()

    # Wait for the page to load
    thread.sleep(DELAY_TIME)

    assert driver.current_url == URLS[subpage], 'Did not navigate to the subpage'

def settings(driver) -> None:
    '''
    This function test the settings page of the website
    '''

    goto_settings(driver)

    # Test each subpage of the settings page
    # Page 1: Account
    goto_subpage(driver, Subpage.ACCOUNT)
    account(driver)

    # Page 2: Profile
    goto_subpage(driver, Subpage.PROFILE)
    profile(driver)

    # Page 3: Safety & Privacy
    goto_subpage(driver, Subpage.SAFETY)
    privacy(driver)

    # Page 4: Feed Settings
    goto_subpage(driver, Subpage.FEED)
    feed(driver)

    # Page 5: Notifications
    goto_subpage(driver, Subpage.NOTIFICATIONS)
    notifications(driver)

    # Page 6: Emails
    goto_subpage(driver, Subpage.EMAILS)
    emails(driver)
