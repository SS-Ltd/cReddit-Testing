'''
This module checks the functionalities of the login module of the mobile application.
'''

from my_imports import thread
from constants import DELAY_TIME, EMAIL, PASSWORD_CREDDIT, EMAIL_SIGNUP, USERNAME, SEE_TIME
from Paths import (START_FORGOT_PASSWORD, RESET_PASSWORD_EMAIL_TEXTBOX, RESET_PASSWORD_BUTTON
                   , RESET_PASSWORD_RESEND, RESET_PASSWORD_OPEN_EMAIL_APP, RESET_PASSWORD_HELP_BUTTON
                   , RESET_PASSWORD_CLOSE_TAB_BUTTON, CONTINUE_WITH_GOOGLE_EMAIL,START_COUNTINUE_WITH_GOOGLE
                   , HOME_PAGE_TABS_HOME)
from helper_functions import locate_element
def forgot_password(driver) -> None:
    '''
    This function checks the functionalities of the forgot password module of the mobile application.
    '''

    ####################################################forgot password########################################################
    # Click on the forgot password button
    forgot_password_element = locate_element(driver, by_accessibility_id=START_FORGOT_PASSWORD)
    assert forgot_password_element is not None, "forgot password button not found"

    print("Before Clicking")
    print(driver.contexts)
    print(driver.context)


    forgot_password_element.click()
    print("Clicked on the forgot password button")
    reset_password_email_textbox = locate_element(driver, by_xpath=RESET_PASSWORD_EMAIL_TEXTBOX)
    assert reset_password_email_textbox is not None, "Reset password email textbox not found"
    print(driver.contexts)
    print(driver.context)

    #correct email address to send the reset password email to
    reset_password_email_textbox.click()
    thread.sleep(2)
    reset_password_email_textbox.send_keys(EMAIL)
    print("Email entered")
    thread.sleep(SEE_TIME)
    reset_password_button = locate_element(driver, by_accessibility_id=RESET_PASSWORD_BUTTON)
    assert reset_password_button is not None, "Reset password button not found"
    reset_password_button.click()
    print("Reset password button clicked")
    thread.sleep(SEE_TIME)
    thread.sleep(6)
    reset_password_resend = locate_element(driver, by_accessibility_id=RESET_PASSWORD_RESEND)
    assert reset_password_resend is not None, "Reset password resend button not found"
    reset_password_resend.click()
    print("Reset password resend button clicked")
    thread.sleep(SEE_TIME)
    reset_password_help_button = locate_element(
        driver, by_accessibility_id=RESET_PASSWORD_HELP_BUTTON)
    assert reset_password_help_button is not None, "Reset password help button not found"
    reset_password_help_button.click()
    print("Reset password help button clicked")
    thread.sleep(SEE_TIME)
    reset_password_close_tab_button = locate_element(
        driver, by_accessibility_id=RESET_PASSWORD_CLOSE_TAB_BUTTON)
    assert reset_password_close_tab_button is not None, "Reset password close tab button not found"
    reset_password_close_tab_button.click()
    print("Reset password close tab button clicked")
    thread.sleep(SEE_TIME)

    reset_password_open_email_app = locate_element(
        driver, by_accessibility_id=RESET_PASSWORD_OPEN_EMAIL_APP)
    assert reset_password_open_email_app is not None,"Reset password open email app button not found"
    reset_password_open_email_app.click()
    print("Reset password open email app button clicked")
    thread.sleep(SEE_TIME)
    #TODO: Add the code to check the email and reset the password



    ####################################################end of forgot password########################################################

def login_continue_with_google(driver) -> None:
    '''
    This function checks the functionalities of the continue with google module of the mobile application.
    '''

    continue_with_google_button = locate_element(driver, by_accessibility_id=START_COUNTINUE_WITH_GOOGLE)
    assert continue_with_google_button is not None, "Continue with google button not found"
    continue_with_google_button.click()
    print("Continue with google button clicked")
    thread.sleep(SEE_TIME)
    continue_with_google_email = locate_element(driver, by_xpath=CONTINUE_WITH_GOOGLE_EMAIL)
    assert continue_with_google_email is not None, "Continue with google email not found"
    continue_with_google_email.click()
    print("Continue with google email clicked")
    thread.sleep(SEE_TIME)
    thread.sleep(10)
    home_tab = locate_element(driver, by_accessibility_id=HOME_PAGE_TABS_HOME)
    assert home_tab.is_displayed(), "Login was not successful"
    print("Login was successful")
def signup_continue_with_google(driver) -> None:
    '''
    This function checks the functionalities of the continue with google module of the mobile application.
    '''

    continue_with_google_button = locate_element(driver, by_accessibility_id=SIGNUP_COUNTINUE_WITH_GOOGLE)
    assert continue_with_google_button is not None, "Continue with google button not found"
    continue_with_google_button.click()
    print("Continue with google button clicked")
    thread.sleep(SEE_TIME)
    continue_with_google_email = locate_element(driver, by_xpath=CONTINUE_WITH_GOOGLE_EMAIL)
    assert continue_with_google_email is not None, "Continue with google email not found"
    continue_with_google_email.click()
    print("Continue with google email clicked")
    thread.sleep(SEE_TIME)
    thread.sleep(10)
    home_tab = locate_element(driver, by_accessibility_id=HOME_PAGE_TABS_HOME)
    assert home_tab.is_displayed(), "Login was not successful"
    print("Login was successful")

#def signup(driver) -> None:

def login(driver) -> None:
    '''
    This function checks the functionalities of the login module of the mobile application.
    '''

    thread.sleep(DELAY_TIME)
    login_continue_with_google(driver)
    #forgot_password(driver)


        # Check that another context has opened
    assert "WEBVIEW_chrome" in driver.contexts, "Content Policy page not found"
    print("Content Policy page found")
