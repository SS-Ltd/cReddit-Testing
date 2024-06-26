'''
This file contains the test cases for the forgot username page.
'''

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from my_imports import WebDriverWait, EC, By, TimeoutException, thread
from helper_functions import locate_element
from write_to_files import write_to_all_files, report_fail, report_success
from constants import DELAY_TIME,EMAIL,USERNAME,SEE_TIME
from Registration.menu_appear import forgot_username_menu_appeared , login_menu_appeared
from google_login import google_login, search_for_email, delete_open_email

def email_textbox_forgot_username(driver):
    """
    This function tests the email textbox of the forgot username page
    """
    try:
        locate_element(driver, by_id="reset_username_email").click()
    except TimeoutException:
        report_fail(
            "The email textbox was not found"
            + "[forgot_username() -> email_textbox() -> email text box not found]"
        )
        return
    report_success(
        "The email textbox was found"
        + "[forgot_username() -> email_textbox() -> email text box found]"
    )

    try:
        locate_element(driver, by_id="reset_username_email_me").click()
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please fill out this field.")]'
        )
        assert len(users) > 0
    except (TimeoutException, AssertionError):
        report_fail(
            "The email 'please fill out this filed' did not appear"
            + "[forgot_username() -> email_textbox() ->"
            + " email text box Please enter a valid  appeared]"
        )
        return
    report_success(
        "The email 'please fill out this field' appeared"
        + "[forgot_username() -> email_textbox() -> email text box appeared]"
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
            "The email 'please enter a valid email' Please enter a valid appeared"
            + "[forgot_username() -> email_textbox() ->"
            + " email text box Please enter a valid appeared]"
        )
        return
    report_success(
        "The email 'please enter a valid email' appeared"
        + "[forgot_username() -> email_textbox() -> email text box appeared]"
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
            "entered a valid email and did not get the expected result"
            + "[forgot_username() -> email_textbox() ->"
            + " email text box entered a valid email]"
        )
        return
    report_success(
        "entered a valid email and got the expected result"
        + "[forgot_username() -> email_textbox() -> email text box entered a valid email]"
    )

def scenario_wrong_email(driver):
    '''
    This function tests the scenario when the email is wrong
    @param driver: The driver to use
    '''
    try:
        locate_element(driver, by_id="reset_username_email").clear()
        locate_element(driver, by_id="reset_username_email").send_keys("fakeemail@gmail.com")
        locate_element(driver, by_id="reset_username_email_me").click()
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Email Does not Exist")]'
        )
        assert len(users) > 0
    except (TimeoutException, AssertionError):
        report_fail(
            "The email 'Email Does not Exist' did not appear"
            + "[forgot_username() -> email_textbox() ->"
            + " email text box Email Does not Exist]"
        )
        return
    report_success(
        "The email 'Email Does not Exist' appeared"
        + "[forgot_username() -> email_textbox() -> email text box Email Does not Exist]"
    )
    
    google_login(driver)
    found = search_for_email(driver, "cReddit support cen.")
    if found:
        report_fail(
            "The email was found"
            + "[forgot_username() -> scenario_wrong_email() -> email found]"
        )
    else:
        report_success(
        "The email was not found"
        + "[forgot_username() -> scenario_wrong_email() -> email not found]"
        )

    driver.close()
    try:
        driver.switch_to.window(driver.window_handles[0])
    except TimeoutException:
        report_fail(
            "The window was not switched"
            + "[forgot_username() -> scenario_wrong_email() -> window not switched]"
        )
        return
    report_success(
        "The window was switched"
        + "[forgot_username() -> scenario_wrong_email() -> window switched]"
    )

def scenario_correct_email(driver):
    '''
    This function tests the scenario when the email is correct
    @param driver: The driver to use
    '''
    try:
        locate_element(driver, by_id="reset_username_email").clear()
        locate_element(driver, by_id="reset_username_email").send_keys(EMAIL)
        locate_element(driver, by_id="reset_username_email_me").click()
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Email Does not Exist")]'
        )
        assert len(users) == 0
    except (TimeoutException, AssertionError):
        report_fail(
            "The email 'Email Does not Exist' appeared"
            + "[forgot_username() -> scenario_correct_email() ->"
            + " email text box Email Does not Exist]"
        )
        return
    report_success(
        "The email 'Email Does not Exist' did not appear"
        + "[forgot_username() -> scenario_correct_email() -> email text box Email Does not Exist]"
    )
    google_login(driver)
    found = search_for_email(driver, "cReddit support cen.")
    if not found:
        report_fail(
            "The email was not found"
            + "[forgot_username() -> scenario_correct_email() -> email not found]"
        )
        return
    report_success(
        "The email was found"
        + "[forgot_username() -> scenario_correct_email() -> email found]"
    )
    try:

        users = driver.find_elements(
                By.XPATH, "//*[contains(text()," + USERNAME + '")]'
            )
        assert len(users) > 0
        report_success(
        "The username was found"
        + "[forgot_username() -> scenario_correct_email() -> username found]"
        )
        delete_open_email(driver)
        report_success(
            "The email was deleted"
            + "[forgot_username() -> scenario_correct_email() -> email deleted]"
        )
    except (TimeoutException, AssertionError):
        report_fail(
            "The username was not found"
            + "[forgot_username() -> scenario_correct_email() -> username found]"
        )

    driver.close()
    try:
        driver.switch_to.window(driver.window_handles[0])
    except TimeoutException:
        report_fail(
            "The window was not switched"
            + "[forgot_username() -> scenario_correct_email() -> window not switched]"
        )
        return
    report_success(
        "The window was switched"
        + "[forgot_username() -> scenario_correct_email() -> window switched]"
    )

def check_back_to_login(driver):
    '''
    This function tests the back to login button
    @param driver: The driver to use
    '''
    try:
        locate_element(driver, by_id="reset_username_back").click()
    except TimeoutException:
        report_fail(
            "The back to login button was not found"
            + "[forgot_username() -> check_back_to_login() -> back to login button not found]"
        )
        return
    report_success(
        "The back to login button was found"
        + "[forgot_username() -> check_back_to_login() -> back to login button found]"
    )
    login_menu_appeared(driver)



def forgot_username(driver) -> None:
    '''
    This function tests the forgot username functionality of the website
    @param driver: The driver to use
    '''
    write_to_all_files("#################### Forgot Username ####################")
    email_textbox_forgot_username(driver)
    thread.sleep(SEE_TIME)

    scenario_wrong_email(driver)
    thread.sleep(SEE_TIME)
    
    scenario_correct_email(driver)#carefull this fuction deletes the email
    thread.sleep(SEE_TIME)

    check_back_to_login(driver)
    thread.sleep(SEE_TIME)
    write_to_all_files("#################### end Forgot Username ####################")
