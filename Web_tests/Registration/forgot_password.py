"""
This file contains the test cases for the forgot password functionality.
"""

import sys
import os
from enum import Enum

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper_functions import locate_element, check_logged_in, check_logged_out
from my_imports import WebDriverWait, EC, By, TimeoutException, thread
from constants import DELAY_TIME, EMAIL, USERNAME
from write_to_files import write_to_all_files, report_fail, report_success
from selenium.webdriver.common.keys import Keys
from my_imports import thread
from google_login import google_login, search_for_email, delete_open_email
from Registration.menu_appear import forgot_password_menu_appeared,login_menu_appeared

def email_me_button_is_enabled(driver):
    """
    This function tests the email me button of the forgot password page
    """
    try:
        locate_element(driver, by_id="reset_password_email_me").is_enabled()
    except TimeoutException:
        report_fail(
            "The email me button was not found"
            + "[forgot_password() -> email me button not found]"
        )
        return
    report_success(
        "The email me button was found" + "[forgot_password() -> email me button found]"
    )


def username_textbox(driver):
    """
    This function tests the username textbox of the forgot password page
    """
    try:
        locate_element(driver, by_id="reset_password_username").click()
    except TimeoutException:
        report_fail(
            "The username textbox was not found"
            + "[forgot_password() -> username_textbox() -> username text box not found]"
        )
        return
    report_success(
        "The username textbox was found"
        + "[forgot_password() -> username_textbox() -> username text box found]"
    )

    try:
        locate_element(
            driver,
            by_xpath='//*[@id="root"]/div/div[1]/'
            + "header/div[3]/div/div/div[3]/div[2]/div",
        ).click()
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please fill out this field.")]'
        )
        assert len(users) > 0
    except (TimeoutException, AssertionError):
        report_fail(
            "The username 'please fill out this filed' did not appear"
            + "[forgot_password() -> username_textbox() -> "
            + "username text box Please enter a valid  appeared]"
        )
        return
    report_success(
        "The username 'please fill out this field' appeared"
        + "[forgot_password() -> username_textbox() -> username text box appeared]"
    )

    try:
        locate_element(driver, by_id="reset_password_username").clear()
        locate_element(driver, by_id="reset_password_username").send_keys(USERNAME)
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please enter a valid")]'
        )
        assert len(users) == 0
    except (TimeoutException, AssertionError):
        report_fail(
            "entered a valid username and did not get the expected result"
            + "[forgot_password() -> username_textbox() ->"
            + " username text box entered a valid username]"
        )
        return
    report_success(
        "entered a valid username and got the expected result"
        + "[forgot_password() -> username_textbox() -> username text box entered a valid username]"
    )


def email_textbox(driver):
    """
    This function tests the email textbox of the forgot password page
    """
    try:
        locate_element(driver, by_id="reset_password_email").click()
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
        locate_element(driver, by_id="reset_password_username").click()
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
        locate_element(driver, by_id="reset_password_email").send_keys("false")
        locate_element(driver, by_id="reset_password_username").click()
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
        locate_element(driver, by_id="reset_password_email").clear()
        locate_element(driver, by_id="reset_password_email").send_keys(EMAIL)
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


def senario_wrong_credentials(driver):
    '''
    This function tests the forgot password
    functionality of the website in case of wrong credentials
    '''
    try:
        locate_element(driver, by_id="reset_password_username").clear()
        locate_element(driver, by_id="reset_password_username").send_keys("false")
        locate_element(driver, by_id="reset_password_email").clear()
        locate_element(driver, by_id="reset_password_email").send_keys("false")
        locate_element(driver, by_id="reset_password_email_me").click()
    except TimeoutException:
        report_fail(
            "The forgot senario_wrong_credentials did not work"
            + "[forgot_password() -> senario_wrong_credentials() ->"
            + " forgot password senario_wrong_credentials did not work]"
        )
        return
    report_success(
        "The forgot password senario_wrong_credentials worked"
        + "[forgot_password() -> senario_wrong_credentials() ->"
        + " forgot password senario_wrong_credentials worked]"
    )

    google_login(driver)
    found = search_for_email(driver, "cReddit support cen.")
    if not found:
        report_success(
            "The email was not found"
            + "[forgot_password() -> senario_wrong_credentials() ->"
            + " forgot password email not found]"
        )
    else:
        report_fail(
            "The email was found"
            + "[forgot_password() -> senario_wrong_credentials() ->"
            + " forgot password email found]"
        )

    driver.close()
    try:
        driver.switch_to.window(driver.window_handles[0])
    except TimeoutException:
        report_fail(
            "The tab was not switched back to the original tab"
            + "[forgot_password() -> senario_correct_credentials() -> tab not switched back]"
        )
        return
    report_success(
        "The tab was switched back to the original tab"
        + "[forgot_password() -> senario_correct_credentials() -> tab switched back]"
    )

def senario_correct_credentials(driver):
    """
    This function tests the forgot password
    functionality of the website in case of correct credentials
    """
    try:
        locate_element(driver, by_id="reset_password_username").clear()
        locate_element(driver, by_id="reset_password_username").send_keys(USERNAME)
        locate_element(driver, by_id="reset_password_email").clear()
        locate_element(driver, by_id="reset_password_email").send_keys(EMAIL)
        locate_element(driver, by_id="reset_password_email_me").click()
    except TimeoutException:
        report_fail(
            "The forgot senario_correct_credentials did not work"
            + "[forgot_password() -> senario_correct_credentials() ->"
            + " forgot password senario_correct_credentials did not work]"
        )
        return
    report_success(
        "The forgot password senario_correct_credentials worked"
        + "[forgot_password() -> senario_correct_credentials() ->"
        + " forgot password senario_correct_credentials worked]"
    )

    google_login(driver)
    emailfound = search_for_email(driver, "cReddit support cen.")
    if emailfound:
        report_success(
            "The email was found"
            + "[forgot_password() -> senario_correct_credentials() ->"
            + " forgot password email found]"
        )
    else:
        report_fail(
            "The email was not found"
            + "[forgot_password() -> senario_correct_credentials() ->"
            + " forgot password email not found]"
        )
    try:
        locate_element(driver, by_xpath="//a[contains(@href, 'reset-password')]").click()
    except TimeoutException:
        report_fail(
            "The forgot password link was not found"
            + "[forgot_password() -> senario_correct_credentials() ->"
            + " forgot password link not found]"
        )
        return
    report_success(
        "The forgot password link was found"
        + "[forgot_password() -> senario_correct_credentials() ->"
        + " forgot password link found]"
    )

    try:
        # Check if new tab is opened
        WebDriverWait(driver, DELAY_TIME).until(EC.number_of_windows_to_be(3))
        report_success(
            "A new tab was opened"
            + "[forgot_password() -> senario_correct_credentials() -> new tab opened]"
        )

        # Wait for the new tab to load
        thread.sleep(DELAY_TIME)

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[2])

        print(driver.current_url)
        # Check that the url matches the user agreement
        expected_url = "reset-password"
        # TODO: change this to the correct url

        if expected_url in driver.current_url:
            report_success(
                "The url contains the "
                + expected_url
                + "[forgot_password() -> senario_correct_credentials()"
                + " -> url contains the expected url]"
            )
        else:
            report_fail(
                "The url does not contain the "
                + expected_url
                + "[forgot_password() -> senario_correct_credentials()"
                + " -> url does not contain the expected url]"
            )
    except TimeoutException:
        report_fail(
            "A new tab was not opened"
            + "[forgot_password() -> senario_correct_credentials() -> new tab not opened]"
        )
        return
    # TODO: should  test the page
    ######
    # Close the new tab
    driver.close()
    # Switch back to the original tab
    try:
        driver.switch_to.window(driver.window_handles[1])
    except TimeoutException:
        report_fail(
            "The tab was not switched back to the original tab"
            + "[forgot_password() -> senario_correct_credentials() -> tab not switched back]"
        )
        return
    report_success(
        "The tab was switched back to the original tab"
        + "[forgot_password() -> senario_correct_credentials() -> tab switched back]"
    )

    delete_open_email(driver)
    thread.sleep(DELAY_TIME)

    driver.close()
    try:
        driver.switch_to.window(driver.window_handles[0])
    except TimeoutException:
        report_fail(
            "The tab was not switched back to the original tab"
            + "[forgot_password() -> senario_correct_credentials() -> tab not switched back]"
        )
        return
    report_success(
        "The tab was switched back to the original tab"
        + "[forgot_password() -> senario_correct_credentials() -> tab switched back]"
    )

def check_back_to_login(driver):
    """
    This function tests the back to login button of the forgot password page
    """
    try:
        locate_element(driver, by_id="reset_password_back").click()
    except TimeoutException:
        report_fail(
            "The back to login button was not found"
            + "[forgot_password() -> check_back_to_login() -> back to login button not found]"
        )
        return
    report_success(
        "The back to login button was found"
        + "[forgot_password() -> check_back_to_login() -> back to login button found]"
    )

    if login_menu_appeared(driver):
        report_success(
            "The back to login button worked"
            + "[forgot_password() -> check_back_to_login() -> back to login button worked]"
        )
    else:
        report_fail(
            "The back to login button did not work"
            + "[forgot_password() -> check_back_to_login() -> back to login button did not work]"
        )


def forgot_password(driver):
    """
    This function tests the forgot password functionality of the website
    """
    write_to_all_files("#################### Forgot Password ####################")
    username_textbox(driver)
    email_textbox(driver)
    email_me_button_is_enabled(driver)
    #senario_wrong_credentials(driver)
    #senario_correct_credentials(driver)#carefull this fuction deletes the email
    check_back_to_login(driver)
    write_to_all_files("#################### End Forgot Password ####################")
