'''
This is the account subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

import sys
import os
from helper_functions import locate_element, check_popup_notification
from constants import DELAY_TIME
from my_imports import thread
from write_to_files import write_to_all_files, report_fail
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def change_email(driver) -> None:
    '''
    This function tests the change email functionality
    '''

    # Test the change email functionality
    # First locate the button
    email = locate_element(driver, by_id='settings-change-email-button')
    assert email is not None, report_fail(
        "Change email button not found")
    # Get the text field and input new data in it
    # Then click submit
    # Refresh the page to check if the data was saved
    # If the data was saved, the test was successful
    # If not, the test failed
    # Report the result
    write_to_all_files("Testing Change Email")
    email.click()
    # email_input = locate_element(driver, by_id='settings-email-input')
    # assert email_input is not None, report_fail("Email input not found")
    # email_input.clear()
    # email_input.send_keys('Test Email')
    # submit_button = locate_element(driver, by_id='settings-submit-button')
    # assert submit_button is not None, report_fail("Change email submit button not found")
    # submit_button.click()
    # driver.refresh()
    # email = locate_element(
        # driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[1]/div[1]/h6')
    # assert email_input.text == 'Test Email', report_fail(
        # "Change email test failed")
    # For now, just check if a popup has appeared
    check_popup_notification(driver)
    write_to_all_files("Change Email Test Successful")

def change_gender(driver) -> None:
    '''
    This function tests the gender functionality
    '''
    write_to_all_files("Testing Change Gender")
    gender_option = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[2]/div[2]/div/a')
    assert gender_option is not None, report_fail('Gender dropdown not found')
    # Check if the option is Man or Woman
    driver.execute_script("arguments[0].scrollIntoView();", gender_option)
    gender_option.click()
    if gender_option.text == 'Man':
        # Change to woman
        locate_element(driver, by_id='settings-simplemenu-gender-woman').click()
        thread.sleep(DELAY_TIME)
        # Refresh page to check if changes have taken effect
        driver.refresh()
        gender_option = locate_element(
            driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[2]/div[2]/div/a')
        assert gender_option is not None, report_fail('Gender dropdown not found')
        assert gender_option.text == 'Woman', report_fail(
            'Gender did not change')
    else:
        # Change to man
        locate_element(driver, by_id='settings-simplemenu-gender-man').click()
        thread.sleep(DELAY_TIME)
        # Refresh page to check if changes have taken effect
        driver.refresh()
        gender_option = locate_element(
            driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[2]/div[2]/div/a')
        assert gender_option is not None, report_fail('Gender dropdown not found')
        assert gender_option.text == 'Man', report_fail(
            'Gender did not change')
    write_to_all_files('Gender Test Completed Successfully')

def change_password(driver) -> None:
    '''
    This function tests the change password functionality
    '''
    write_to_all_files("Testing Change Password")
    # First locate the button
    password = locate_element(driver, by_id='settings-change-password-button')
    assert password is not None, report_fail(
        "Change password button not found")
    driver.execute_script("arguments[0].scrollIntoView();", password)
    # Get the text field and input new data in it
    # Then click submit
    # Refresh the page to check if the data was saved
    # If the data was saved, the test was successful
    # If not, the test failed
    # Report the result
    password.click()
    # password_input = locate_element(driver, by_id='settings-password-input')
    # assert password_input is not None, report_fail("Password input not found")
    # password_input.clear()
    # password_input.send_keys('Test Password')
    # submit_button = locate_element(driver, by_id='settings-submit-button')
    # assert submit_button is not None, report_fail(
    #     "Change password submit button not found")
    # submit_button.click()
    # driver.refresh()
    # password = locate_element(
    #     driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[3]/div[1]/h6')
    # assert password_input.text == 'Last update was today', report_fail(
    #     "Change password test failed")
    # For now, just check if a popup has appeared
    check_popup_notification(driver)
    write_to_all_files("Change Password Test Successful")

def change_country(driver) -> None:
    '''
    This function tests the change country functionality
    '''
    write_to_all_files("Testing Change Country")
    country = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[2]/div/a')
    assert country is not None, report_fail('Country dropdown not found')
    driver.execute_script("arguments[0].scrollIntoView();", country)
    country.click()
    # Select UK, refresh the page to see if changes have taken effect
    locate_element(driver, by_id='settings-simplemenu-country-uk').click()
    thread.sleep(DELAY_TIME)
    driver.refresh()
    country = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[2]/div/a')
    assert country is not None, report_fail('Country dropdown not found')
    assert country.text == 'UK', report_fail('Country did not change')
    write_to_all_files('Country Test Completed Successfully')

def connect_twitter(driver) -> None:
    '''
    This function connects or disconnects from twitter
    '''
    write_to_all_files("Testing Connect Twitter")
    twitter = locate_element(driver, by_id="settings-connect-twitter-button")
    assert twitter is not None, report_fail("Twitter button not found")
    driver.execute_script("arguments[0].scrollIntoView();", twitter)
    twitter.click()
    # For now, nothing happens
    write_to_all_files("Connect Twitter Test Successful")

def connect_apple(driver) -> None:
    '''
    This function connects or disconnects from apple
    '''
    write_to_all_files("Testing Connect Apple")
    apple = locate_element(driver, by_id="settings-connect-apple-button")
    assert apple is not None, report_fail("Apple button not found")
    driver.execute_script("arguments[0].scrollIntoView();", apple)
    apple.click()
    # For now, nothing happens
    write_to_all_files("Connect Apple Test Successful")

def connect_google(driver) -> None:
    '''
    This function connects or disconnects from google
    '''
    write_to_all_files("Testing Connect Google")
    google = locate_element(driver, by_id="settings-connect-google-button")
    assert google is not None, report_fail("Google button not found")
    driver.execute_script("arguments[0].scrollIntoView();", google)
    google.click()
    # For now, nothing happens
    write_to_all_files("Connect Google Test Successful")

def account(driver) -> None:
    '''
    This function tests the account subpage of the settings page
    '''

    write_to_all_files(
        "#################### Testing Account Subpage ####################")

    # Test the change email functionality
    change_email(driver)
    thread.sleep(DELAY_TIME)

    # Test the gender functionality
    change_gender(driver)
    thread.sleep(DELAY_TIME)

    # Test the change password functionality
    change_password(driver)
    thread.sleep(DELAY_TIME)

    # Test the Change Country Functionality
    change_country(driver)
    thread.sleep(DELAY_TIME)

    # Go to connected accounts
    # 1. Connect to twitter
    connect_twitter(driver)
    thread.sleep(DELAY_TIME)

    # 2. Connect to apple
    connect_apple(driver)
    thread.sleep(DELAY_TIME)

    # 3. Connect to google
    connect_google(driver)
    thread.sleep(DELAY_TIME)

    write_to_all_files(
        "#################### Account Subpage Test Completed ####################")
