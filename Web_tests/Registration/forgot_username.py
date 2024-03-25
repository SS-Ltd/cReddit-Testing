'''
This file contains the test cases for the forgot username page.
'''

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from my_imports import WebDriverWait, EC, By, TimeoutException, thread
from helper_functions import locate_element
from write_to_files import write_to_all_files, report_fail, report_success
from constants import DELAY_TIME
from Registration.menu_appear import forgot_username_menu_appeared

def email_textbox_forgot_username(driver):
    """
    This function tests the email textbox of the forgot password page
    """
    try:
        locate_element(driver, by_id="reset_username_email").click()
    except TimeoutException:
        report_fail(
            "The email textbox was not found"
            + "[forgot_password() -> email_textbox() -> username text box not found]"
        )
        return
    report_success(
        "The email textbox was found"
        + "[forgot_password() -> email_textbox() -> username text box found]"
    )

    try:
        locate_element(driver, by_id="reset_username_email_me").click()
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please fill out this field.")]'
        )
        assert len(users) > 0
    except (TimeoutException, AssertionError):
        report_fail(
            "The username 'please fill out this filed' did not appear"
            + "[forgot_password() -> email_textbox() ->"
            + " username text box Please enter a valid  appeared]"
        )
        return
    report_success(
        "The username 'please fill out this field' appeared"
        + "[forgot_password() -> email_textbox() -> username text box appeared]"
    )

    try:
        locate_element(driver, by_id="reset_username_email").send_keys("false")
        locate_element(driver, by_id="reset_username_email_me").click()
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please enter a valid")]'
        )
        assert len(users) > 0
    except (TimeoutException, AssertionError):
        report_fail(
            "The username 'please enter a valid email' Please enter a valid appeared"
            + "[forgot_password() -> email_textbox() ->"
            + " username text box Please enter a valid appeared]"
        )
        return
    report_success(
        "The username 'please enter a valid email' appeared"
        + "[forgot_password() -> email_textbox() -> username text box appeared]"
    )

    try:
        locate_element(driver, by_id="reset_username_email").clear()
        locate_element(driver, by_id="reset_username_email").send_keys(EMAIL)
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please enter a valid")]'
        )
        assert len(users) == 0
    except (TimeoutException, AssertionError):
        report_fail(
            "entered a valid username and did not get the expected result"
            + "[forgot_password() -> email_textbox() ->"
            + " username text box entered a valid username]"
        )
        return
    report_success(
        "entered a valid username and got the expected result"
        + "[forgot_password() -> email_textbox() -> username text box entered a valid username]"
    )


def forgot_username(driver) -> None:
    '''
    This function tests the forgot username functionality of the website
    @param driver: The driver to use
    '''
    email_textbox_forgot_username(driver)
    