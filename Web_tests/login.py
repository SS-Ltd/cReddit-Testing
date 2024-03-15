"""
This module is used to test the login page of the website
"""

from my_imports import WebDriverWait, EC, By, TimeoutException, time as thread
from constants import DELAY_TIME
from write_to_files import write_to_all_files, report_fail, report_success

def goto_login(driver) -> None:
    """
    This function test the login window of the website
    """
    # Check login button
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "navbar_login-button"))
        ).click()
        report_success(
            "The element with the ID 'navbar_login_button' was found"
            + " [login() -> goto_login() -> login button found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'navbar_login_button' was not found"
            + " [login() -> goto_login() -> login button not found]"
        )
        return

    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "navbar_login_menu"))
        )
        report_success(
            "The Login Window appeared"
            + " [login() -> goto_login() -> login window appeared]"
        )
    except TimeoutException:
        report_fail(
            "The login window did not appear"
            + "[login() -> goto_login() -> login window did not appear]"
        )


def close_button(driver) -> None:
    """
    This function test the close button of the website
    """
    # Check close button
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "login_close"))
        ).click()
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
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "navbar_login_menu"))
        )
        report_fail(
            "The close button did not work"
            + "[login() -> close_button() -> close button failed]"
        )
    except TimeoutException:
        report_success(
            "The close button worked"
            + "[login() -> close_button() -> close button passed]"
        )

def login(driver):
    """
    This function test the login page of the website
    """

    write_to_all_files("#################### Testing Login Page ####################")
    goto_login(driver)
    thread.sleep(DELAY_TIME)

    # Check user agreement
    # Check Privacy Policy
    # Check continue with Google
    # Check continue with Apple might not get implmented
    # Check Username text box
    # Check Password text box
    # Check Log in button
    # Check Forgot username
    # Check Forgot password
    # Check Sign up

    # Check close button
    close_button(driver)
    thread.sleep(DELAY_TIME)
    write_to_all_files("############################################################")
