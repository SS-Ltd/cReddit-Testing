'''
This module is used to test the logout functionality of the website
'''

from my_imports import WebDriverWait, EC, By, thread, TimeoutException
from write_to_files import report_fail, report_success
from constants import DELAY_TIME, SEE_TIME
from helper_functions import locate_element, check_logged_out

def logout(driver) -> None:
    '''
    This function tests the logout functionality of the website
    @param driver: The driver to use
    '''
    # Click the logout button
    try:
        locate_element(driver, by_id="navbar_profile").click()
    except TimeoutException:
        report_fail("The profile button was not found"
            + "[logout() -> Profile button not found]")
        return
    report_success("The profile button was found"
        + "[logout() -> Profile button found]")
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id="profile_logout").click()
    except TimeoutException:
        report_fail("The logout button was not found"
            + "[logout() -> Logout button not found]")
        return
    report_success("The logout button was found"
        + "[logout() -> Logout button found]")

    # Check if the user is logged out
    if check_logged_out(driver):
        report_success("The user was logged out successfully"
            + "[logout() -> User logged out]")
    else:
        report_fail("The user was not logged out successfully"
            + "[logout() -> User not logged out]")
