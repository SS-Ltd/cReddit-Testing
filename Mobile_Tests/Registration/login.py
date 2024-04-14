'''
This module checks the functionalities of the login module of the mobile application.
'''

import datetime
from my_imports import thread
from constants import DELAY_TIME, EMAIL, PASSWORD_CREDDIT, EMAIL_SIGNUP, USERNAME, SEE_TIME
from Paths import (START_FORGOT_PASSWORD, RESET_PASSWORD_EMAIL_TEXTBOX, RESET_PASSWORD_BUTTON
                   , RESET_PASSWORD_RESEND, RESET_PASSWORD_OPEN_EMAIL_APP, RESET_PASSWORD_HELP_BUTTON
                   , RESET_PASSWORD_CLOSE_TAB_BUTTON, CONTINUE_WITH_GOOGLE_EMAIL,START_COUNTINUE_WITH_GOOGLE
                   , HOME_PAGE_TABS_HOME,SIGNUP_CONTINUE_WITH_GOOGLE,SIGNUP_EMAIL,SIGNUP_PASSWORD,SIGNUP_LOGIN
                   , SIGNUP_CONTINUE, START_SIGNUP,SIGNUP_USERNAME,SIGNUP_CONTINUE2,START_USERNAME,START_PASSWORD
                   , START_LOGIN, HOME_PAGE_TABS_HOME,SIGNUP_GENDER_MAN)
from helper_functions import locate_element, end_text
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

    continue_with_google_button = locate_element(driver, by_accessibility_id=SIGNUP_CONTINUE_WITH_GOOGLE)
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

def signup(driver, email:str = "Fake@email.no"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")) -> None:
    '''
    This function checks the functionalities of the signup module of the mobile application.
    '''
    signup_element = locate_element(driver, by_accessibility_id=START_SIGNUP)
    assert signup_element is not None, "signup button not found"
    signup_element.click()
    print("Clicked on the signup button")
    thread.sleep(SEE_TIME)
    ###########################go to login and come back to signup####################################
    # Click on the login button
    login_element = locate_element(driver, by_accessibility_id=SIGNUP_LOGIN)
    assert login_element is not None, "login button not found"
    login_element.click()
    print("Clicked on the login button")
    thread.sleep(SEE_TIME)
    # Click on the signup button
    signup_element = locate_element(driver, by_accessibility_id=START_SIGNUP)
    assert signup_element is not None, "signup button not found"
    signup_element.click()
    print("Clicked on the signup button")
    thread.sleep(SEE_TIME)
    ###########################end of go to login and come back to signup####################################

    ####################################senario############################################
    signup_email_field = locate_element(driver, by_id=SIGNUP_EMAIL)
    assert signup_email_field is not None, "signup email field not found"
    signup_email_field.click()
    thread.sleep(2)
    thread.sleep(SEE_TIME)
    signup_email_field.send_keys(email)
    print("Email entered")
    thread.sleep(SEE_TIME)
    signup_password_fields = locate_element(driver, by_id=SIGNUP_PASSWORD)
    assert signup_password_fields is not None, "signup password fields not found"
    signup_password_fields.click()
    thread.sleep(2)
    thread.sleep(SEE_TIME)
    signup_password_fields.send_keys("AAAAAAAa1")
    print("Password entered")
    end_text(driver)
    thread.sleep(SEE_TIME)
    signup_continue = locate_element(driver, by_accessibility_id=SIGNUP_CONTINUE)
    assert signup_continue is not None, "signup continue button not found"
    signup_continue.click()
    print("Signup continue button clicked")
    thread.sleep(SEE_TIME)
    username_field = locate_element(driver, by_id=SIGNUP_USERNAME)
    assert username_field is not None, "username field not found"
    username_field.click()
    thread.sleep(SEE_TIME)
    username = "FakeUsername" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    username_field.send_keys(username)
    print("Username is"+username)
    print("Username entered")
    end_text(driver)
    thread.sleep(SEE_TIME)
    signup_continue = locate_element(driver, by_accessibility_id=SIGNUP_CONTINUE2)
    assert signup_continue is not None, "signup continue button not found"
    signup_continue.click()
    print("Signup continue button clicked")
    thread.sleep(SEE_TIME)
    geneder_man = locate_element(driver, by_accessibility_id=SIGNUP_GENDER_MAN)
    assert geneder_man is not None, "signup man button not found"
    geneder_man.click()
    thread.sleep(10)
    home_tab = locate_element(driver, by_accessibility_id=HOME_PAGE_TABS_HOME)
    assert home_tab.is_displayed(), "Login was not successful"
    print("Login was successful")
    ####################################end of senario############################################

def login_wrong_password(driver) -> None:
    '''
    This function checks the functionalities of the login module of the mobile application.
    '''

    thread.sleep(DELAY_TIME)
    # Click on the login button
    username = locate_element(driver, by_xpath=START_USERNAME)
    username.click()
    thread.sleep(2)
    # username.clear()
    username.send_keys("Trevor11")

    password = locate_element(driver, by_xpath=START_PASSWORD)
    password.click()
    thread.sleep(2)
    # password.clear()
    password.send_keys("2")
    end_text(driver)

    login_element = locate_element(driver, by_accessibility_id=START_LOGIN)
    login_element.click()

    # Verify that the login was successful
    # Check the bottom tabs, one of them is an enough indication that the login was successful
    # Check the home tab (tab 1 of 5)
    home_tab = locate_element(driver, by_accessibility_id=HOME_PAGE_TABS_HOME)
    assert not home_tab.is_displayed(), "Login was successful"
    print("Login was not successful")

    # TEST FUNCTIONALITIES HERE
def login(driver) -> None:
    '''
    This function checks the functionalities of the login module of the mobile application.
    '''

    thread.sleep(DELAY_TIME)
    #login_continue_with_google(driver)
    #forgot_password(driver)
    #signup(driver, "husseinelhawary4@gmail.com")
    login_wrong_password(driver)
        # Check that another context has opened
    assert "WEBVIEW_chrome" in driver.contexts, "Content Policy page not found"
    print("Content Policy page found")
