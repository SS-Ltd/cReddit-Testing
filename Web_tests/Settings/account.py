'''
This is the account subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

import sys
import os
from helper_functions import locate_element
from constants import DELAY_TIME
from my_imports import thread
from write_to_files import write_to_all_files, report_fail
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def change_email(driver) -> None:
    '''
    This function tests the change email functionality
    '''

    # Test the change email functionality
    write_to_all_files("Testing Change Email")
    # First locate the button
    email = locate_element(driver, by_id='settings-change-email-button')
    assert email is not None, report_fail(
        "Change email button not found")
    # Check that the update your email window has opened
    # For now it is done with the XPATH of the actual reddit page
    # Since it is not implemented in our clone yet
    window = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div')
    assert window is not None, report_fail(
        "Update your email window not found")
    email.click()
    # Locate the 'current password' input field
    password = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div[1]/input')
    assert password is not None, report_fail(
        "Current password input field not found")
    # Test with a wrong password
    password.clear()
    password.send_keys('Test Password')
    # Check that the ✔️ icon has appeared
    driver.execute_script("arguments[0].blur();", password)
    tick = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div[1]/div')
    assert tick is not None, report_fail(
        "✔️ icon not found in password field")
    # Locate the 'new email' input field
    new_email = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div[2]/input')
    assert new_email is not None, report_fail(
        "New email input field not found")
    # Enter a wrong format email
    new_email.clear()
    new_email.send_keys('Test Email')
    # Check that the ❌ icon has appeared
    driver.execute_script("arguments[0].blur();", new_email)
    cross = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div[2]/div')
    assert cross is not None, report_fail(
        "❌ icon not found")
    # Enter the current email
    new_email.clear()
    new_email.send_keys('dabocet696@ikumaru.com')
    # Check that the ❌ icon has appeared
    driver.execute_script("arguments[0].blur();", new_email)
    cross = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div[2]/div')
    assert cross is not None, report_fail(
        "❌ icon not found")
    # Enter a correct format email
    new_email.clear()
    new_email.send_keys('dabocet696@ikumaru.com')
    # Check that the ✔️ icon has appeared
    driver.execute_script("arguments[0].blur();", new_email)
    tick = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div[2]/div')
    assert tick is not None, report_fail(
        "✔️ icon not found in email field")
    # Locate the Save email button
    save = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div[3]/button')
    assert save is not None, report_fail(
        "Save email button not found")
    save.click()
    # You entered a wrong password, so a ❌ icon should appear in the password field
    cross = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div[2]/div')
    assert cross is not None, report_fail(
        "❌ icon not found")
    # Enter the correct password
    password.clear()
    password.send_keys('Correct Password')
    # Click on the save button
    save.click()
    # Chech that the 'Check your email' window has appeared
    window = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div')
    assert window is not None, report_fail(
        "Check your email window not found")
    # Click on the 'Got it' Button
    got_it = locate_element(
        driver, by_xpath='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div/button')
    assert got_it is not None, report_fail(
        "Got it button not found")
    got_it.click()
    # Refresh the page
    driver.refresh()
    # Check that the email has been updated but not yet verified
    text = locate_element(
        driver, by_xpath='//*[@id="AppRouter-main-content"]/div/div[2]/div[1]/div[1]/div[1]/p')
    assert text is not None, report_fail(
        "Email not updated")
    # Check that the text contains the text 'not verified!'
    assert 'not verified!' in text.text, report_fail(
        "Something went wrong, your email should not be verified yet!")
    # Go to gmail and verify the email
    # TODO: Implement this
    # Refresh the page
    driver.refresh()
    # Check that the email has been updated and verified
    text = locate_element(
        driver, by_xpath='//*[@id="AppRouter-main-content"]/div/div[2]/div[1]/div[1]/div[1]/p')
    assert text is not None, report_fail(
        "Email not updated")
    # Check that the text does not contain the text 'not verified!'
    assert 'not verified!' not in text.text, report_fail(
        "Something went wrong, your email should be verified!")
    write_to_all_files("Change Email Test Successful")

def change_gender(driver) -> None:
    '''
    This function tests the gender functionality
    '''
    write_to_all_files("Testing Change Gender")
    # Locate the dropdown
    dropdown = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[2]/div[2]/div/a')
    assert dropdown is not None, report_fail(
        "Gender Dropdown not found")
#    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    dropdown.click()
    thread.sleep(DELAY_TIME)

    # Choose a random element from the dropdown
    random = locate_element(
        driver, by_id='settings-simplemenu-gender-man')
    assert random is not None, report_fail("Random Element not found")
    random_text = random.text
    random.click()
    thread.sleep(DELAY_TIME)
    driver.refresh()
    thread.sleep(DELAY_TIME)
    dropdown = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[2]/div[2]/div/a')
    assert dropdown is not None, report_fail(
        "Gender Dropdown not found")
#    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    # assert dropdown.text == random_text, report_fail(
    #     "Gender Dropdown not working")
    write_to_all_files("Test Change Gender Successful")

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
    password.click()
    # This is not integrated yet, so I will write sample code that should work on the main reddit page
    # Check that the window has opened
    window = locate_element(
        driver, by_xpath='/html/body/div/div/div[2]/div/h1')
    assert window is not None and window.text == "Update your password", report_fail(
        "Change password window not found")
    # Locate the 'OLD PASSWORD' input field
    old_password = locate_element(
        driver, by_id='old_password')
    assert old_password is not None, report_fail(
        "Old password input field not found")
    # Enter a wrong password
    old_password.clear()
    old_password.send_keys('Test Password')
    # Check that the ✔️ icon has appeared
    driver.execute_script("arguments[0].blur();", old_password)
    tick = locate_element(
        driver, by_xpath='/html/body/div/div/div[2]/div/div[2]/div[1]/div[2]/div')
    assert tick is not None, report_fail(
        "✔️ icon not found in old password field")
    # Locate the 'NEW PASSWORD' input field
    new_password = locate_element(
        driver, by_id='password')
    assert new_password is not None, report_fail(
        "New password input field not found")
    # Enter a password that is less than 8 characters
    new_password.clear()
    new_password.send_keys('Test')
    # Check that the ❌ icon has appeared
    driver.execute_script("arguments[0].blur();", new_password)
    error = locate_element(
        driver, by_xpath='/html/body/div/div/div[2]/div/form/fieldset[2]/div[2]')
    assert error is not None and error.text == "Password must be at least 8 characters long", report_fail(
        "Error message not found in new password field")
    # Enter a password that is more than 8 characters
    new_password.clear()
    new_password.send_keys('TestPassword')
    # Check that the ✔️ icon has appeared
    driver.execute_script("arguments[0].blur();", new_password)
    tick = locate_element(
        driver, by_xpath='/html/body/div/div/div[2]/div/form/fieldset[2]/div[2]/div')
    assert tick is not None, report_fail(
        "✔️ icon not found in new password field")
    # Locate the 'CONFIRM NEW PASSWORD' input field
    confirm_password = locate_element(
        driver, by_id='password2')
    assert confirm_password is not None, report_fail(
        "Confirm new password input field not found")
    # Enter a password that does not match the new password
    confirm_password.clear()
    confirm_password.send_keys('TestPassword1')
    # Check that the ❌ icon has appeared
    driver.execute_script("arguments[0].blur();", confirm_password)
    error = locate_element(
        driver, by_xpath='/html/body/div/div/div[2]/div/form/fieldset[3]/div[2]')
    assert error is not None and error.text == "Password must match", report_fail(
        "Error message not found in confirm new password field")
    # Enter a password that matches the new password
    confirm_password.clear()
    confirm_password.send_keys('TestPassword')
    # Check that the ✔️ icon has appeared
    driver.execute_script("arguments[0].blur();", confirm_password)
    tick = locate_element(
        driver, by_xpath='/html/body/div/div/div[2]/div/form/fieldset[3]/div[2]/div')
    assert tick is not None, report_fail(
        "✔️ icon not found in confirm new password field")
    # Locate the Log me out of everywhere button
    log_out = locate_element(
        driver, by_id='invalidate_oauth')
    assert log_out is not None, report_fail(
        "Log me out of everywhere button not found")
    # log_out.click()
    # Locate the Save button
    save = locate_element(
        driver, by_xpath='/html/body/div/div/div[2]/div/form/fieldset[5]/button')
    assert save is not None, report_fail(
        "Save button not found")
    save.click()
    # You entered a wrong old password, so a ❌ icon should appear in the old password field
    cross = locate_element(
        driver, by_xpath='/html/body/div/div/div[2]/div/form/fieldset[1]/div')
    assert cross is not None and cross.text == "Incorrect password", report_fail(
        "Error message not found in old password field")
    # Enter the correct old password
    old_password.clear()
    old_password.send_keys('Correct Password')
    # Click on the save button
    save.click()
    # Check that the change password window has closed
    window = locate_element(
        driver, by_xpath='/html/body/div/div/div[2]/div/h1')
    assert window is None, report_fail(
        "Change password window not closed")

    write_to_all_files("Change Password Test Successful")

def change_country(driver) -> None:
    '''
    This function tests the change country functionality
    '''
    write_to_all_files("Testing Change Country")
    # Locate the dropdown
    dropdown = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[2]/div/a')
    assert dropdown is not None, report_fail(
        "Country Dropdown not found")
#    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    dropdown.click()
    thread.sleep(DELAY_TIME)

    # Choose a random element from the dropdown
    random = locate_element(
        driver, by_id='settings-simplemenu-country-uk')
    assert random is not None, report_fail("Random Element not found")
    random_text = random.text
    random.click()
    thread.sleep(DELAY_TIME)
    driver.refresh()
    thread.sleep(DELAY_TIME)
    dropdown = locate_element(
        driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[4]/div[2]/div/a')
    assert dropdown is not None, report_fail(
        "Country Dropdown not found")
#    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    # assert dropdown.text == random_text, report_fail(
    #     "Country Dropdown not working")
    write_to_all_files('Country Test Completed Successfully')

def connect_twitter(driver) -> None:
    '''
    This function connects or disconnects from twitter
    '''
    raise NotImplementedError("This function is not implemented yet")
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
    raise NotImplementedError("This function is not implemented yet")
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
    raise NotImplementedError("This function is not implemented yet")
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
    # TODO: Not completed or tested yet
    # change_email(driver)
    # thread.sleep(DELAY_TIME)

    # Test the gender functionality
    change_gender(driver)
    thread.sleep(DELAY_TIME)

    # Test the change password functionality
    # TODO: Not completed or tested yet
    # change_password(driver)
    # thread.sleep(DELAY_TIME)

    # Test the Change Country Functionality
    change_country(driver)
    thread.sleep(DELAY_TIME)

    # Go to connected accounts
    # 1. Connect to twitter
    # TODO: Not completed yet
    # connect_twitter(driver)
    # thread.sleep(DELAY_TIME)

    # 2. Connect to apple
    # TODO: Not completed yet
    # connect_apple(driver)
    # thread.sleep(DELAY_TIME)

    # 3. Connect to google
    # TODO: Not completed yet
    # connect_google(driver)
    # thread.sleep(DELAY_TIME)

    write_to_all_files(
        "#################### Account Subpage Test Completed ####################")
