'''
This module is used to test the settings page of the Reddit website.
'''

from my_imports import WebDriverWait, EC, By, TimeoutException, thread
from constants import DELAY_TIME
from write_to_files import write_to_all_files, report_fail, report_success

def goto_settings(driver) -> None:
    '''
    This function goes to the settings page from the homepage
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "navbar_profile"))).click()
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
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "profile_settings"))).click()
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

def settings(driver) -> None:
    '''
    This function test the settings page of the website
    '''

    write_to_all_files(
        "#################### Testing Settings Page ####################")
    goto_settings(driver)
    thread.sleep(DELAY_TIME)
