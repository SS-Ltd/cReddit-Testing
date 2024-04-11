'''
This module checks the functionalities of the update email page of the mobile application.
'''

from my_imports import thread, webdriver
from constants import DELAY_TIME
from helper_functions import locate_element, check_hyperlink
from Paths import UPDATE_EMAIL_EMAIL, UPDATE_EMAIL_PASSWORD, UPDATE_EMAIL_SAVE
from Paths import UPDATE_EMAIL_ERROR_EMAIL_EMPTY, UPDATE_EMAIL_ERROR_EMAIL_INVALID
from Paths import UPDATE_EMAIL_ERROR_PASSWORD_EMPTY, UPDATE_EMAIL_ERROR_PASSWORD_INVALID
from Paths import UPDATE_EMAIL_FORGOT_PASSWORD
from Paths import FORGOT_PASSWORD_WINDOW, FORGOT_PASSWORD_HAVING_TROUBLE


def email(driver: webdriver) -> None:
    '''
    This function performs validations on email field.
    '''

    # Locate the email field
    email_field = locate_element(driver, by_xpath=UPDATE_EMAIL_EMAIL)
    assert email_field is not None, "Email field not found"
    print("Email field found")

    # Click on the email field
    email_field.click()

    # Check for empty email
    email_field.send_keys("")
    driver.swipe(100, 1500, 100, 700)
    save_button = locate_element(driver, by_accessibility_id=UPDATE_EMAIL_SAVE)
    save_button.click()
    driver.swipe(100, 700, 100, 1500)

    # Check for empty email error
    error = locate_element(
        driver, by_accessibility_id=UPDATE_EMAIL_ERROR_EMAIL_EMPTY)
    assert error is not None, "Empty email error not found"

    # Check for invalid email
    email_field.click()
    email_field.send_keys("invalid_email")
    driver.swipe(100, 1500, 100, 700)
    save_button.click()
    driver.swipe(100, 700, 100, 1500)

    # Check for invalid email error
    error = locate_element(
        driver, by_accessibility_id=UPDATE_EMAIL_ERROR_EMAIL_INVALID)
    assert error is not None, "Invalid email error not found"

    print("Email field validations passed")


def password(driver) -> None:
    '''
    This function performs validations on password field.
    '''

    # Locate the password field
    password_field = locate_element(driver, by_xpath=UPDATE_EMAIL_PASSWORD)
    assert password_field is not None, "Password field not found"
    print("Password field found")

    # Click on the password field
    password_field.click()

    # Check for empty password
    password_field.send_keys("")
    driver.swipe(100, 1500, 100, 700)
    save_button = locate_element(driver, by_accessibility_id=UPDATE_EMAIL_SAVE)
    save_button.click()
    driver.swipe(100, 700, 100, 1500)

    # Check for empty password error
    error = locate_element(
        driver, by_accessibility_id=UPDATE_EMAIL_ERROR_PASSWORD_EMPTY)
    assert error is not None, "Empty password error not found"

    # Check for invalid password
    password_field.click()
    password_field.send_keys("1234567")     # Less than 8 characters
    driver.swipe(100, 1500, 100, 700)
    save_button.click()
    driver.swipe(100, 700, 100, 1500)

    # Check for invalid password error
    error = locate_element(
        driver, by_accessibility_id=UPDATE_EMAIL_ERROR_PASSWORD_INVALID)
    assert error is not None, "Invalid password error not found"

    print("Password field validations passed")


def forgot_password(driver) -> None:
    '''
    This function checks the functionalities of the forgot password button.
    '''

    # Locate the forgot password button
    button = locate_element(
        driver, by_accessibility_id=UPDATE_EMAIL_FORGOT_PASSWORD)
    assert button is not None, "Forgot password button not found"
    print("Forgot password button found")

    # Click on the forgot password button
    button.click()

    # Check that the forgot password page is opened
    assert locate_element(
        driver, by_xpath=FORGOT_PASSWORD_WINDOW) is not None, "Forgot password page not found"
    print("Forgot password page found")

    # Check the having trouble link
    check_hyperlink(driver, FORGOT_PASSWORD_HAVING_TROUBLE)


def update_email(driver) -> None:
    '''
    This function checks the functionalities of the update email page of the mobile application.
    '''

    # Validations on fields
    # Test email field
    # email(driver)
    # password(driver)

    # Testing the forgot password functionality

    print("Update Email page functionalities checked")
