"""
This module is used to test the login page of the website
"""

from enum import Enum
from my_imports import WebDriverWait, EC, By, TimeoutException, thread
from constants import DELAY_TIME
from write_to_files import write_to_all_files, report_fail, report_success


class Hyperlink(Enum):
    '''
    This class is used to test the hyperlinks of the website
    '''
    USER_AGREEMENT = "user_agreement"
    PRIVACY_POLICY = "privacy_policy"


def goto_login(driver) -> None:
    """
    This function test the login window of the website
    """
    # Check login button
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "navbar_login_button"))
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


def hyper_links(driver, hyperlink: Hyperlink) -> None:
    '''
    This function test the user agreement hyperlink of the website
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="navbar_login_menu"]/div/div[2]/p/a[1]'
                 if hyperlink == hyperlink.USER_AGREEMENT
                 else '//*[@id="navbar_login_menu"]/div/div[2]/p/a[2]'))
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

    write_to_all_files(
        "#################### Testing Login Page ####################")
    goto_login(driver)
    thread.sleep(DELAY_TIME)

    # Check user agreement
    hyper_links(driver, Hyperlink.USER_AGREEMENT)
    thread.sleep(DELAY_TIME)
    # Check Privacy Policy
    hyper_links(driver, Hyperlink.PRIVACY_POLICY)
    thread.sleep(DELAY_TIME)
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
    write_to_all_files(
        "############################################################")
