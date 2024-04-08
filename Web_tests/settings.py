'''
This module is used to test the settings page of the Reddit website.
'''
from enum import Enum
from my_imports import TimeoutException, thread
from constants import DELAY_TIME
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
    Subpage.ACCOUNT: "http://localhost:5173/settings/account",
    Subpage.PROFILE: "http://localhost:5173/settings/profile",
    Subpage.SAFETY: "http://localhost:5173/settings/privacy",
    Subpage.FEED: "http://localhost:5173/settings/feed",
    Subpage.NOTIFICATIONS: "http://localhost:5173/settings/notifications",
    Subpage.EMAILS: "http://localhost:5173/settings/emails"
}

def goto_settings(driver) -> None:
    '''
    This function goes to the settings page from the homepage
    '''
    driver.get("http://localhost:5173/settings")
    return
    try:
        locate_element(driver, by_id="navbar_profile").click()
        report_success(
            "The element with the ID 'navbar_profile' was found"
            + " [settings() -> goto_settings() -> profile button found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'navbar_profile' was not found"
            + " [settings() -> goto_settings() -> profile button not found]"
        )
        return

    thread.sleep(DELAY_TIME)

    try:
        locate_element(driver, by_id="profile_settings").click()
        report_success(
            "The element with the ID 'profile_settings' was found"
            + " [settings() -> goto_settings() -> settings button found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'profile_settings' was not found"
            + " [settings() -> goto_settings() -> settings button not found]"
        )
        return

    # Check if the settings page is loaded
    thread.sleep(DELAY_TIME)
    if driver.current_url == "http://localhost:5173/settings":
        report_success(
            "The settings page was loaded"
            + " [settings() -> goto_settings() -> settings page loaded]"
        )
    else:
        report_fail(
            "The settings page was not loaded"
            + " [settings() -> goto_settings() -> settings page not loaded]"
        )


def goto_subpage(driver, subpage: Subpage) -> None:
    '''
    This function goes to a specific subpage of the settings page

    '''
    driver.refresh()
    try:
        locate_element(driver, by_id=SUBPAGES[subpage]).click()
        report_success(
            "The " + subpage.value[1] + " subpage button was found"
            + " [settings() -> goto_subpage() -> " +
            subpage.value[1] + " button found]"
        )

        # Wait for the page to load
        thread.sleep(DELAY_TIME)

        if driver.current_url == URLS[subpage]:
            report_success(
                "The " + subpage.value[1] + " subpage was loaded"
                + " [settings() -> goto_subpage() -> " +
                subpage.value[1] + " page loaded]"
            )
        else:
            report_fail(
                "The " + subpage.value[1] + " subpage was not loaded"
                + " [settings() -> goto_subpage() -> " +
                subpage.value[1] + " page not loaded]"
            )
            return

    except TimeoutException:
        report_fail(
            "The " + subpage.value[1] + " subpage button was not found"
            + " [settings() -> goto_subpage() -> " +
            subpage.value[1] + " button not found]"
        )
        return

def settings(driver) -> None:
    '''
    This function test the settings page of the website
    '''
    write_to_all_files(
        "#################### Testing Settings Page ####################")
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

    write_to_all_files("Settings page test completed")
