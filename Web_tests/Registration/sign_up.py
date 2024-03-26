import sys
import os
from enum import Enum
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Registration.logout import logout
from helper_functions import locate_element , check_logged_in, check_logged_out
from my_imports import WebDriverWait, EC, By, TimeoutException, thread
from constants import DELAY_TIME, EMAIL, PASSWORD, SEE_TIME, EMAIL_SIGNUP , USERNAME
from write_to_files import write_to_all_files, report_fail, report_success
from selenium.webdriver.common.keys import Keys
from menu_appear import signup_menu_appeared, sign_up_menu_appeared_email, sign_up_menu_appeared_username
from globals import set_first_signup, get_first_signup

def goto_sign_up(driver) -> None:
    '''
    This function navigates to the sign up page
    @param driver: The driver to use
    '''
    try:
        locate_element(driver, by_id='navbar_signup_button').click()
        report_success(
            "The element with the link text 'Sign up' was found"
            + "[goto_sign_up() -> Sign up found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the link text 'Sign up' was not found"
            + "[goto_sign_up() -> Sign up not found]"
        )
        return

class Hyperlink(Enum):
    '''
    This class is used to test the hyperlinks of the website
    '''
    USER_AGREEMENT = "user_agreement"
    PRIVACY_POLICY = "privacy_policy"

def hyper_links(driver, hyperlink: Hyperlink , page_no:str) -> None:
    '''
    This function test the user agreement hyperlink of the website
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, 'signup'+page_no+'_user_agreement'
                 if hyperlink == hyperlink.USER_AGREEMENT
                 else 'signup'+page_no+'_policy'))
        ).click()
        # WebDriverWait(driver, DELAY_TIME).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "a.no-underline:nth-child(1)"))
        # ).click()
        report_success(
            "The element with the link text '" + hyperlink.name + "' was found"
            + "[signup() -> hyper_links() -> " + hyperlink.name + " found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the link text '" + hyperlink.name + "' was not found"
            + "[signup() -> hyper_links() -> " + hyperlink.name + " not found]"
        )
        return

    try:
        # Check if new tab is opened
        WebDriverWait(driver, DELAY_TIME).until(
            EC.number_of_windows_to_be(2)
        )
        report_success(
            "A new tab was opened"
            + "[signup() -> hyper_links() -> new tab opened]"
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
                + "[signup() -> hyper_links() -> " + hyperlink.name + " url matches]"
            )
        else:
            report_fail(
                "The url does not match the " + hyperlink.name
                + "[signup() -> hyper_links() -> " + hyperlink.name + " url does not match]"
            )
    except TimeoutException:
        report_fail(
            "A new tab was not opened"
            + "[signup() -> user_agreement() -> new tab not opened]"
        )
        return

    # Close the new tab
    driver.close()

    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])

def check_signup_with_google(driver) -> bool:
    """
    This function test the signup with google of the website
    """

    try:
        locate_element(driver, by_id="signup_oauth").click()
        report_success(
            "The element with the ID 'signup_oauth' was found"
            + "[signup() -> check_signup_with_google() -> google signup found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'signup_oauth' was not found"
            + "[signup() -> check_signup_with_google() -> google signup not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    driver.switch_to.window(driver.window_handles[-1])
    if not get_first_signup():
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
            "The title of the Gmail signup page was found"
            + "[signup() -> check_signup_with_google() -> Gmail signup Page found]"
        )
    except TimeoutException:
        report_fail(
            "The title of the Gmail signup page was not found"
            + "[signup() -> check_signup_with_google() -> Gmail signup Page not found]"
        )
        return False
    thread.sleep(SEE_TIME)

    # Check if the email input is present
    try:
        locate_element(driver, by_id="identifierId").send_keys(EMAIL, Keys.ENTER)
        report_success(
            "The email input was found"
            + "[signup() -> check_signup_with_google() -> Email input found]"
        )
    except TimeoutException:
        report_fail(
            "The email input was not found"
            + "[signup() -> check_signup_with_google() -> Email input not found]"
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
            + "[signup() -> check_signup_with_google() -> Password input found]"
        )
    except TimeoutException:
        report_fail(
            "The password input was not found"
            + "[signup() -> check_signup_with_google() -> Password input not found]"
        )
        return False

    thread.sleep(SEE_TIME)
    set_first_signup(False)
    driver.switch_to.window(driver.window_handles[0])

    # Check if pop-up is displayed
    try:
        locate_element(driver, by_xpath='//*[contains(@id, "toast-success")]')
    except (TimeoutException, AssertionError):
        report_fail("Popup not found in google signup"
                    +"[signup() -> check_signup_with_google() -> Popup not found]")
        return False
    report_success("Popup found in google signup"
                   +"[signup() -> check_signup_with_google() -> Popup found]")
    thread.sleep(SEE_TIME)

    return check_logged_in(driver)

def email_textbox_signup(driver)-> bool:
    """
    This function tests the email textbox of the forgot signup page
    """
    try:
        locate_element(driver, by_id="signup_email").click()
    except TimeoutException:
        report_fail(
            "The email textbox was not found"
            + "[signup() -> email_textbox() -> email text box not found]"
        )
        return False
    report_success(
        "The email textbox was found"
        + "[signup() -> email_textbox() -> email text box found]"
    )

    try:
        locate_element(driver, by_id="signup_email_continue").click()
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please fill out this field.")]'
        )
        assert len(users) > 0
    except (TimeoutException, AssertionError):
        report_fail(
            "The email 'please fill out this filed' did not appear"
            + "[signup() -> email_textbox() ->"
            + " email text box Please enter a valid  appeared]"
        )
        return False
    report_success(
        "The email 'please fill out this field' appeared"
        + "[signup() -> email_textbox() -> email text box appeared]"
    )

    try:
        locate_element(driver, by_id="signup_email").send_keys("false")
        locate_element(driver, by_id="signup_email_continue").click()
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please enter a valid")]'
        )
        assert len(users) > 0
    except (TimeoutException, AssertionError):
        report_fail(
            "The email 'please enter a valid email' Please enter a valid appeared"
            + "[signup() -> email_textbox() ->"
            + " email text box Please enter a valid appeared]"
        )
        return False
    report_success(
        "The email 'please enter a valid email' appeared"
        + "[signup() -> email_textbox() -> email text box appeared]"
    )

    try:
        locate_element(driver, by_id="signup_email").clear()
        locate_element(driver, by_id="signup_email_continue").send_keys(EMAIL_SIGNUP)
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please enter a valid")]'
        )
        assert len(users) == 0
    except (TimeoutException, AssertionError):
        report_fail(
            "entered a valid email and did not get the expected result"
            + "[signup() -> email_textbox() ->"
            + " email text box entered a valid email]"
        )
        return False
    report_success(
        "entered a valid email and got the expected result"
        + "[signup() -> email_textbox() -> email text box entered a valid email]"
    )

    return True

def continue_button_email_signup(driver) -> bool:
    """
    This function tests the continue button of the signup email page 
    """
    try:
        locate_element(driver, by_id="signup_email_continue").click()
    except TimeoutException:
        report_fail(
            "The continue button was not found"
            + "[signup() -> continue_button() -> continue button not found]"
        )
        return False
    report_success(
        "The continue button was found"
        + "[signup() -> continue_button() -> continue button found]"
    )

    if sign_up_menu_appeared_username(driver):
        return True
    return False


def submit_button_signup(driver) -> bool:
    """
    This function tests the submit button of the signup email page 
    """
    try:
        locate_element(driver, by_id="signup_submit").click()
    except TimeoutException:
        report_fail(
            "The submit button was not found"
            + "[signup() -> submit_button_signup() -> submit button not found]"
        )
        return False
    report_success(
        "The submit button was found"
        + "[signup() -> submit_button_signup() -> submit button found]"
    )

    return check_logged_in(driver)

def username_textbox_signup(driver) -> bool:
    """
    This function tests the username textbox of the forgot password page
    """
    try:
        locate_element(driver, by_id="signup_username").click()
    except TimeoutException:
        report_fail(
            "The username textbox was not found"
            + "[signup() -> username_textbox() -> username text box not found]"
        )
        return False
    report_success(
        "The username textbox was found"
        + "[signup() -> username_textbox() -> username text box found]"
    )

    try:
        locate_element(driver,by_id="signup_password").click()
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please fill out this field.")]'
        )
        assert len(users) > 0
    except (TimeoutException, AssertionError):
        report_fail(
            "The username 'please fill out this filed' did not appear"
            + "[signup() -> username_textbox() -> "
            + "username text box Please enter a valid  appeared]"
        )
        return False
    report_success(
        "The username 'please fill out this field' appeared"
        + "[signup() -> username_textbox() -> username text box appeared]"
    )

    try:
        locate_element(driver, by_id="signup_username").clear()
        locate_element(driver, by_id="signup_username").send_keys(USERNAME)
        users = driver.find_elements(
            By.XPATH, "//*[contains(text()," + ' "Please enter a valid")]'
        )
        assert len(users) == 0
    except (TimeoutException, AssertionError):
        report_fail(
            "entered a valid username and did not get the expected result"
            + "[signup() -> username_textbox() ->"
            + " username text box entered a valid username]"
        )
        return False
    report_success(
        "entered a valid username and got the expected result"
        + "[signup() -> username_textbox() -> username text box entered a valid username]"
    )
    return True

def password_textbox_signup(driver) -> bool:
    """
    This function test the password text box of the website and all its corner cases
    """
    # Check password text box when no text entered
    try:
        locate_element(driver, by_id="signup_password").click()
        report_success(
            "The element with the ID 'signup_password' was found and clicked"
            + "[signup() -> password_textbox_signup() -> password text box found and clicked]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'signup_password' was not found and clicked"
            + "[signup() -> password_textbox_signup() -> password text box not found and clicked]"
        )
        return False
    thread.sleep(SEE_TIME)

    try:
        locate_element(driver, by_id='signup_username').click()
        users = driver.find_elements(By.XPATH, '//*[contains(text(),'
                                     +' "Please lengthen this")]')
        assert len(users) > 0

        report_success(
            "The password 'please fill out this filed' appeared"
            + "[signup() -> password_textbox_signup() -> password text box appeared]"
        )
    except (TimeoutException,AssertionError):
        report_fail(
            "The password 'please fill out this filed' did not appear"
            + "[signup() -> password_textbox_signup() -> password text box did not appear]"
        )
        return False
    thread.sleep(SEE_TIME)

    # Check password text box when text entered
    try:
        locate_element(driver, by_id="signup_password").send_keys("test")
        report_success(
            "The element with the ID 'signup_password' was found 'test' was entered"
            + "[signup() -> password_textbox_signup() ->"
            + " password text box found and 'text' entered]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'signup_password' was not found 'test' was not entered"
            + "[signup() -> password_textbox_signup() -> password"+
            "text box not found and 'text' not entered]"
        )
        return False
    thread.sleep(SEE_TIME)

    return True


def gender_drop_down(driver)->bool:
    '''
    This function tests the gender functionality
    '''
    dropdown = locate_element(
        driver, by_id='gender_dropdown_button')
    assert dropdown is not None, report_fail(
        "Gender Dropdown not found")
    dropdown.click()
    thread.sleep(DELAY_TIME)

    # Choose a random element from the dropdown
    random = locate_element(
        driver, by_id='gender_man')
    assert random is not None, report_fail("Random Element not found")
    report_success("Random Element found")
    random_text = random.text
    random.click()

    dropdown = locate_element(
        driver,by_id='gender_dropdown_button')
    assert dropdown is not None, report_fail(
        "Gender Dropdown not found")
    assert dropdown.text == random_text, report_fail(
        "Gender Dropdown not working")
    report_success("Gender Dropdown working")
    return True

def close_button_signup_email_signup(driver, page_id : str) -> bool:
    """
    This function test the close button of the website
    """
    # Check close button
    try:
        locate_element(driver, by_id=page_id).click()
        report_success(
            "The element with the ID 'signup1_close' was found"
            + "[signup() -> close_button_signup_email_signup_email() -> close button found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'signup_close' was not found"
            + "[signup() -> close_button_signup_email_signup_email() -> close button not found]"
        )
        return

    try:
        locate_element(driver, by_id="navbar_signup_button")
        report_fail(
            "The close button did not work"
            + "[signup() -> close_button_signup_email_signup_email() -> close button failed]"
        )
    except TimeoutException:
        report_success(
            "The close button worked"
            + "[signup() -> close_button_signup_email_signup_email() -> close button passed]"
        )


def signup(driver) -> None:
    '''
    This function tests the sign up functionality of the website
    @param driver: The driver to use
    '''
    goto_sign_up(driver)
    thread.sleep(SEE_TIME)

    # Check user agreement
    hyper_links(driver, Hyperlink.USER_AGREEMENT,"")
    thread.sleep(SEE_TIME)

    # Check Privacy Policy
    hyper_links(driver, Hyperlink.PRIVACY_POLICY,"")
    thread.sleep(SEE_TIME)

    check_signup_with_google(driver)
    thread.sleep(SEE_TIME)

    if check_logged_in():
        logout(driver)
        goto_sign_up(driver)
        thread.sleep(SEE_TIME)

    if not email_textbox_signup(driver):
        return False
    thread.sleep(SEE_TIME)

    if not continue_button_email_signup(driver):
        return False

    hyper_links(driver, Hyperlink.USER_AGREEMENT,"2")
    thread.sleep(SEE_TIME)

    # Check Privacy Policy
    hyper_links(driver, Hyperlink.PRIVACY_POLICY,"2")
    thread.sleep(SEE_TIME)

    if not username_textbox_signup(driver):
        return False
    thread.sleep(SEE_TIME)

    if not password_textbox_signup(driver):
        return False
    thread.sleep(SEE_TIME)

    if not gender_drop_down(driver):
        return False
    thread.sleep(SEE_TIME)

    if not submit_button_signup(driver):
        return False
    thread.sleep(SEE_TIME)

    if check_logged_in(driver):
        logout(driver)
    thread.sleep(SEE_TIME)


    return True
