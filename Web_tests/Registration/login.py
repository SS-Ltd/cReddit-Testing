"""
This module is used to test the login page of the website
"""

import sys
import os
from enum import Enum
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Registration.forgot_password import forgot_password
from Registration.logout import logout
from helper_functions import locate_element , check_logged_in, check_logged_out , element_dissapeared
from my_imports import WebDriverWait, EC, By, TimeoutException, thread 
from constants import DELAY_TIME,EMAIL, PASSWORD, USERNAME, SEE_TIME
from write_to_files import write_to_all_files, report_fail, report_success
from Registration.forgot_username import forgot_username
from selenium.webdriver.common.keys import Keys
from Registration.menu_appear import (login_menu_appeared, 
                                      sign_up_menu_appeared, 
                                      forgot_password_menu_appeared,
                                      forgot_username_menu_appeared
                                      )
from google_login import google_login
from globals import set_first_login, get_first_login

class Hyperlink(Enum):
    '''
    This class is used to test the hyperlinks of the website
    '''
    USER_AGREEMENT = "user_agreement"
    PRIVACY_POLICY = "privacy_policy"

def goto_login(driver) -> bool:
    """
    This function test the login window of the website
    """
    # Check login button
    try:
        locate_element(driver, by_id="navbar_login_button").click()
        report_success(
            "The element with the ID 'navbar_login_button' was found"
            + " [login() -> goto_login() -> login button found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'navbar_login_button' was not found"
            + " [login() -> goto_login() -> login button not found]"
        )
        return False
    # Check if the login menu appeared
    return login_menu_appeared(driver)



def hyper_links(driver, hyperlink: Hyperlink) -> None:
    '''
    This function test the user agreement hyperlink of the website
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, 'login_user_agreement'
                 if hyperlink == hyperlink.USER_AGREEMENT
                 else 'login_policy'))
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


def close_button_login(driver) -> None:
    """
    This function test the close button of the website
    """
    # Check close button
    try:
        locate_element(driver, by_id="login_close").click()
        report_success(
            "The element with the ID 'login_close' was found"
            + "[login() -> close_button() -> close button found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_close' was not found"
            + "[login() -> close_button() -> close button not found]"
        )
        return

    try:
        locate_element(driver, by_id="navbar_login_menu")
        report_fail(
            "The close button did not work"
            + "[login() -> close_button() -> close button failed]"
        )
    except TimeoutException:
        report_success(
            "The close button worked"
            + "[login() -> close_button() -> close button passed]"
        )

def check_login_with_google(driver) -> bool:
    """
    This function test the login with google of the website
    """

    try:
        locate_element(driver, by_id="login_oauth").click()
        report_success(
            "The element with the ID 'login_oauth' was found"
            + "[login() -> check_login_with_google() -> google login found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_oauth' was not found"
            + "[login() -> check_login_with_google() -> google login not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    driver.switch_to.window(driver.window_handles[-1])
    if not get_first_login():
        try:
            locate_element(driver, by_xpath="/html/body/div[1]/div[1]/div[2]/"
                           + "div/div/div[2]/div/div/div[1]/form/span/section/"
                           + "div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[2]"
                           ).click() #hope this won't crash TODO: fix this
            driver.switch_to.window(driver.window_handles[0])
            thread.sleep(DELAY_TIME)
            return check_logged_in(driver)
        except TimeoutException:
            pass

    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.title_contains("Sign in - Google Accounts")
        )
        report_success(
            "The title of the Gmail login page was found"
            + "[login() -> check_login_with_google() -> Gmail login Page found]"
        )
    except TimeoutException:
        report_fail(
            "The title of the Gmail login page was not found"
            + "[login() -> check_login_with_google() -> Gmail login Page not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    # Check if the email input is present
    try:
        locate_element(driver, by_id="identifierId").send_keys(EMAIL, Keys.ENTER)
        report_success(
            "The email input was found"
            + "[login() -> check_login_with_google() -> Email input found]"
        )
    except TimeoutException:
        report_fail(
            "The email input was not found"
            + "[login() -> check_login_with_google() -> Email input not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    thread.sleep(DELAY_TIME)
    # Check if the password input is present
    try:#this xpath is might not work
        locate_element(driver, by_xpath="/html/body/"+
                       "div[1]/div[1]/div[2]/c-wiz/div/"+
                       "div[2]/div/div/div[1]/form/span/"+
                       "section[2]/div/div/div[1]/div[1]/"+
                       "div/div/div/div/div[1]/div/div[1]/input"
                       ).send_keys(PASSWORD, Keys.ENTER)
        report_success(
            "The password input was found"
            + "[login() -> check_login_with_google() -> Password input found]"
        )
    except TimeoutException:
        report_fail(
            "The password input was not found"
            + "[login() -> check_login_with_google() -> Password input not found]"
        )
        return False

    thread.sleep(SEE_TIME)
    set_first_login(False)
    driver.switch_to.window(driver.window_handles[0])

    # Check if pop-up is displayed
    try:
        locate_element(driver, by_xpath='//*[contains(@id, "toast-success")]')
    except (TimeoutException, AssertionError):
        report_fail("Popup not found in google login"
                    +"[login() -> check_login_with_google() -> Popup not found]")
        return False
    report_success("Popup found in google login"
                   +"[login() -> check_login_with_google() -> Popup found]")
    thread.sleep(SEE_TIME)

    return True

def username_textbox(driver) -> bool:
    """
    This function test the username text box of the website and all its corner cases
    """
    # Check username text box when no text entered
    try:
        locate_element(driver, by_id="login_username").click()
        report_success(
            "The element with the ID 'login_username' was found and clicked"
            + "[login() -> username_textbox() -> username text box found and clicked]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_username' was not found and clicked"
            + "[login() -> username_textbox() -> username text box not found and clicked]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_xpath='//*[@id="navbar_login_menu"]/'
                       +'div[1]/div[1]/div[1]/h1').click()
        users = driver.find_elements(By.XPATH, '//*[contains(text(),'
                                     +' "Please fill out this field.")]')
        assert len(users) > 0

        report_success(
            "The username 'please fill out this filed' appeared"
            + "[login() -> username_textbox() -> username text box appeared]"
        )
    except (TimeoutException,AssertionError):
        report_fail(
            "The username 'please fill out this filed' did not appear"
            + "[login() -> username_textbox() -> username text box did not appear]"
        )
        return False
    thread.sleep(SEE_TIME)

    # Check username text box when text entered
    try:
        locate_element(driver, by_id="login_username").send_keys("test")
        report_success(
            "The element with the ID 'login_username' was found 'test' was entered"
            + "[login() -> username_textbox() -> username text box found and 'text' entered]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_username' was not found 'test' was not entered"
            + "[login() -> username_textbox() -> username"+
            "text box not found and 'text' not entered]"
        )
        return False
    thread.sleep(SEE_TIME)

    return True

def password_textbox(driver) -> bool:
    """
    This function test the password text box of the website and all its corner cases
    """
    # Check password text box when no text entered
    try:
        locate_element(driver, by_id="login_password").click()
        report_success(
            "The element with the ID 'login_password' was found and clicked"
            + "[login() -> password_textbox() -> password text box found and clicked]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_password' was not found and clicked"
            + "[login() -> password_textbox() -> password text box not found and clicked]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id='login_username').click()
        users = driver.find_elements(By.XPATH, '//*[contains(text(),'
                                     +' "Please fill out this field.")]')
        assert len(users) > 0

        report_success(
            "The password 'please fill out this filed' appeared"
            + "[login() -> password_textbox() -> password text box appeared]"
        )
    except (TimeoutException,AssertionError):
        report_fail(
            "The password 'please fill out this filed' did not appear"
            + "[login() -> password_textbox() -> password text box did not appear]"
        )
        return False
    thread.sleep(SEE_TIME)

    # Check password text box when text entered
    try:
        locate_element(driver, by_id="login_password").send_keys("test")
        report_success(
            "The element with the ID 'login_password' was found 'test' was entered"
            + "[login() -> password_textbox() -> password text box found and 'text' entered]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_password' was not found 'test' was not entered"
            + "[login() -> password_textbox() -> password"+
            "text box not found and 'text' not entered]"
        )
        return False
    thread.sleep(SEE_TIME)

    return True


def login_to_forgot_username(driver) -> bool:
    """
    This function test the login to forgot username of the website
    """
    # Check forgot username button
    try:
        locate_element(driver, by_id="forgot_username").click()
        report_success(
            "The element with the ID 'forgot_username' was found"
            + "[login() -> login_to_forgot_username() -> forgot username found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'forgot_username' was not found"
            + "[login() -> login_to_forgot_username() -> forgot username not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    # Check if the forgot username page is displayed
    return forgot_username_menu_appeared(driver)

def login_to_forgot_password(driver) -> bool:
    """
    This function test the login to forgot password of the website
    """
    # Check forgot password button
    try:
        locate_element(driver, by_id="forgot_pass").click()
        report_success(
            "The element with the ID 'forgot_pass' was found"
            + "[login() -> login_to_forgot_password() -> forgot password found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'forgot_pass' was not found"
            + "[login() -> login_to_forgot_password() -> forgot password not found]"
        )
        return
    thread.sleep(SEE_TIME)

    # Check if the forgot password page is displayed
    return forgot_password_menu_appeared(driver)

def login_to_sign_up(driver) -> bool:
    """
    This function test the login to sign up button of the website
    """
    # Check sign up button
    try:
        locate_element(driver, by_id="login_signup").click()
        report_success(
            "The element with the ID 'login_signup' was found"
            + "[login() -> login_to_sign_up() -> sign up found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_signup' was not found"
            + "[login() -> login_to_sign_up() -> sign up not found]"
        )
        return False

    # Check if the sign up page is displayed
    return sign_up_menu_appeared(driver)

def sign_up_to_login(driver) -> bool:
    """
    This function test the sign up to login button of the website
    """
    # Check login button
    try:
        locate_element(driver, by_id="signup_login").click()
        report_success(
            "The element with the ID 'signup_login' was found"
            + "[login() -> sign_up_to_login() -> login found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'signup_login' was not found"
            + "[login() -> sign_up_to_login() -> login not found]"
        )
        return False

    # Check if the login page is displayed
    return login_menu_appeared(driver)

def scenario_wrong_username(driver) -> bool:
    """
    This function tests entering a wrong username to the website
    """
    # Check wrong username
    try:
        locate_element(driver, by_id="login_username").clear()
        locate_element(driver, by_id="login_username").send_keys("wrong")
        report_success(
            "The element with the ID 'login_username' was found 'test' was entered"
            + "[login() -> scenario_wrong_username() -> wrong username found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_username' was not found 'test' was not entered"
            + "[login() -> scenario_wrong_username() -> wrong username not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id="login_password").send_keys(PASSWORD)
        report_success(
            "The element with the ID 'login_password' was found 'test' was entered"
            + "[login() -> scenario_wrong_username() -> wrong password found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_password' was not found 'test' was not entered"
            + "[login() -> scenario_wrong_username() -> wrong password not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id="login_submit").click()
        report_success(
            "The element with the ID 'login_submit' was found"
            + "[login() -> scenario_wrong_username() -> submit found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_submit' was not found"
            + "[login() -> scenario_wrong_username() -> submit not found]"
        )
        return False

    try:
        popup = locate_element(driver, by_xpath='//*[contains(@id, "login-toast-error")]')
        assert popup is not None, report_fail("Popup not found")
        report_success(
            "The element with the text 'Invalid username or password.' was found"
            + "[login() -> scenario_wrong_username() -> wrong username found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the text 'Invalid username or password.' was not found"
            + "[login() -> scenario_wrong_username() -> wrong username not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    return True

def scenario_wrong_password(driver) -> bool:
    """
    This function tests entering a wrong password to the website
    """
    # Check wrong password
    try:
        locate_element(driver, by_id="login_username").clear()
        locate_element(driver, by_id="login_username").send_keys(USERNAME)
        report_success(
            "The element with the ID 'login_username' was found 'test' was entered"
            + "[login() -> scenario_wrong_password() -> wrong username found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_username' was not found 'test' was not entered"
            + "[login() -> scenario_wrong_password() -> wrong username not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id="login_password").clear()
        locate_element(driver, by_id="login_password").send_keys("wrong")
        report_success(
            "The element with the ID 'login_password' was found 'test' was entered"
            + "[login() -> scenario_wrong_password() -> wrong password found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_password' was not found 'test' was not entered"
            + "[login() -> scenario_wrong_password() -> wrong password not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id="login_submit").click()
        report_success(
            "The element with the ID 'login_submit' was found"
            + "[login() -> scenario_wrong_password() -> submit found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_submit' was not found"
            + "[login() -> scenario_wrong_password() -> submit not found]"
        )
        return False

    try:
        popup = locate_element(driver, by_xpath='//*[contains(@id, "login-toast-error")]')
        assert popup is not None, report_fail("Popup not found")
        report_success(
            "The element with the text 'Invalid username or password.' was found"
            + "[login() -> scenario_wrong_password() -> wrong password found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the text 'Invalid username or password.' was not found"
            + "[login() -> scenario_wrong_password() -> wrong password not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    return True

def scenario_wrong_username_password(driver) -> bool:
    """
    This function tests entering a wrong username and password to the website
    """
    # Check wrong username and password
    try:
        locate_element(driver, by_id="login_username").clear()
        locate_element(driver, by_id="login_username").send_keys("wrong")
        report_success(
            "The element with the ID 'login_username' was found 'test' was entered"
            + "[login() -> scenario_wrong_username_password() -> wrong username found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_username' was not found 'test' was not entered"
            + "[login() -> scenario_wrong_username_password() -> wrong username not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id="login_password").clear()
        locate_element(driver, by_id="login_password").send_keys("wrong")
        report_success(
            "The element with the ID 'login_password' was found 'test' was entered"
            + "[login() -> scenario_wrong_username_password() -> wrong password found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_password' was not found 'test' was not entered"
            + "[login() -> scenario_wrong_username_password() -> wrong password not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id="login_submit").click()
        report_success(
            "The element with the ID 'login_submit' was found"
            + "[login() -> scenario_wrong_username_password() -> submit found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_submit' was not found"
            + "[login() -> scenario_wrong_username_password() -> submit not found]"
        )
        return False

    try:
        popup = locate_element(driver, by_xpath='//*[contains(@id, "login-toast-error")]')
        assert popup is not None, report_fail("Popup not found")
        report_success(
            "The element with the text 'Invalid username or password.' was found"
            + "[login() -> scenario_wrong_username_password() -> wrong username and password found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the text 'Invalid username or password.' was not found"
            + "[login() -> scenario_wrong_username_password() ->"
            + " wrong username and password not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    return True

def scenario_correct_username_password(driver) -> bool:
    """
    This function tests entering a correct username and password to the website
    """
    # Check correct username and password
    try:
        locate_element(driver, by_id="login_username").clear()
        locate_element(driver, by_id="login_username").send_keys(USERNAME)
        report_success(
            "The element with the ID 'login_username' was found 'test' was entered"
            + "[login() -> scenario_correct_username_password() -> correct username found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_username' was not found 'test' was not entered"
            + "[login() -> scenario_correct_username_password() -> correct username not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id="login_password").clear()
        locate_element(driver, by_id="login_password").send_keys(PASSWORD)
        report_success(
            "The element with the ID 'login_password' was found 'test' was entered"
            + "[login() -> scenario_correct_username_password() -> correct password found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_password' was not found 'test' was not entered"
            + "[login() -> scenario_correct_username_password() -> correct password not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id="login_submit").click()
        report_success(
            "The element with the ID 'login_submit' was found"
            + "[login() -> scenario_correct_username_password() -> submit found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'login_submit' was not found"
            + "[login() -> scenario_correct_username_password() -> submit not found]"
        )
        return False

    try:
        popup = locate_element(driver, by_xpath='//*[contains(@id, "login-toast-success")]')
        assert popup is not None, report_fail("Popup not found")
        report_success(
            "The element with the text 'Successfully logged in.' was found"
            + "[login() -> scenario_correct_username_password() ->"
            + " correct username and password found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the text 'Successfully logged in.' was not found"
            + "[login() -> scenario_correct_username_password() ->"
            + " correct username and password not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    return check_logged_in(driver)

def login(driver) -> bool:
    """
    This function test the login page of the website
    """

    write_to_all_files(
        "#################### Testing Login Page ####################")
    if not goto_login(driver):
        return False
    thread.sleep(SEE_TIME)
    ##############################################

    # Check user agreement
    hyper_links(driver, Hyperlink.USER_AGREEMENT)
    thread.sleep(SEE_TIME)

    # Check Privacy Policy
    hyper_links(driver, Hyperlink.PRIVACY_POLICY)
    thread.sleep(SEE_TIME)

    #close_button_login(driver)
    #check_logged_in(driver)
    #logout(driver)
    #check_logged_out(driver)
    #goto_login(driver)#remove this later
    # Check continue with Apple might not get implmented
    ##############################################

    #Check continue with Google
    if check_login_with_google(driver):
        if check_logged_in(driver):
            logout(driver)
        goto_login(driver)
    thread.sleep(SEE_TIME)

    # Check Username text box
    if not username_textbox(driver):
        return False
    thread.sleep(SEE_TIME)

    # Check Password text box
    if not password_textbox(driver):
        return False
    thread.sleep(SEE_TIME)


    # Check Forgot username
    if login_to_forgot_username(driver):
        forgot_username(driver)
    thread.sleep(SEE_TIME)

    # Check Forgot password
    if login_to_forgot_password(driver):
        forgot_password(driver)
    thread.sleep(SEE_TIME)

    # checks all scenarios of login
    if scenario_wrong_username(driver):
        element_dissapeared(driver, by_xpath='//*[contains(@id, "login-toast-error")]')
        if scenario_wrong_password(driver):
            element_dissapeared(driver, by_xpath='//*[contains(@id, "login-toast-error")]')
            if scenario_wrong_username_password(driver):
                element_dissapeared(driver, by_xpath='//*[contains(@id, "login-toast-error")]')
                if scenario_correct_username_password(driver):
                    if check_logged_in(driver):
                        logout(driver)
                    #goto_login(driver)

    # Check Sign up button
    if login_to_sign_up(driver):
        sign_up_to_login(driver)
    thread.sleep(SEE_TIME)
    # Check close button
    close_button_login(driver)

    thread.sleep(DELAY_TIME)
    write_to_all_files(
        "#################### Finished Testing Login Page ####################")
