import sys
import os
from enum import Enum
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Registration.forgot_password import forgot_password
from Registration.logout import logout
from helper_functions import locate_element , check_logged_in, check_logged_out
from my_imports import WebDriverWait, EC, By, TimeoutException, thread
from constants import DELAY_TIME
from write_to_files import write_to_all_files, report_fail, report_success
from constants import EMAIL, PASSWORD
from Registration.forgot_username import forgot_username
from selenium.webdriver.common.keys import Keys

class Hyperlink(Enum):
    '''
    This class is used to test the hyperlinks of the website
    '''
    USER_AGREEMENT = "user_agreement"
    PRIVACY_POLICY = "privacy_policy"

def hyper_links(driver, hyperlink: Hyperlink) -> None:
    '''
    This function test the user agreement hyperlink of the website
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, 'signup_user_agreement'
                 if hyperlink == hyperlink.USER_AGREEMENT
                 else 'signup_policy'))
        ).click()
        # WebDriverWait(driver, DELAY_TIME).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "a.no-underline:nth-child(1)"))
        # ).click()
        report_success(
            "The element with the link text '" + hyperlink.name + "' was found"
            + "[login() -> hyper_links() -> " + hyperlink.name + " found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the link text '" + hyperlink.name + "' was not found"
            + "[login() -> hyper_links() -> " + hyperlink.name + " not found]"
        )
        return

    try:
        # Check if new tab is opened
        WebDriverWait(driver, DELAY_TIME).until(
            EC.number_of_windows_to_be(2)
        )
        report_success(
            "A new tab was opened"
            + "[login() -> hyper_links() -> new tab opened]"
        )

        # Wait for the new tab to load
        thread.sleep(DELAY_TIME)

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[1])

        print(driver.current_url)
        # Check that the url matches the user agreement
        expected_url = ("https://www.redditinc.com/policies/user-agreement"
                if hyperlink == Hyperlink.USER_AGREEMENT
                else "https://www.reddit.com/policies/privacy-policy")

        if driver.current_url.startswith(expected_url):
            report_success(
                "The url matches the " + hyperlink.name
                + "[login() -> hyper_links() -> " + hyperlink.name + " url matches]"
            )
        else:
            report_fail(
                "The url does not match the " + hyperlink.name
                + "[login() -> hyper_links() -> " + hyperlink.name + " url does not match]"
            )
    except TimeoutException:
        report_fail(
            "A new tab was not opened"
            + "[login() -> user_agreement() -> new tab not opened]"
        )
        return

    # Close the new tab
    driver.close()

    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])

def sign_up(driver) -> None:
    '''
    This function tests the sign up functionality of the website
    @param driver: The driver to use
    '''
    # Check user agreement
    hyper_links(driver, Hyperlink.USER_AGREEMENT)
    # Check Privacy Policy
    hyper_links(driver, Hyperlink.PRIVACY_POLICY)
