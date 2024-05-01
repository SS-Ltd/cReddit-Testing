'''
This is the profile subpage of the settings page.
This module contains all the necessary tests needed to test this subpage.
'''

import sys
import os
from helper_functions import locate_element, check_popup_notification, check_checkbox
from constants import DELAY_TIME
from pynput.keyboard import Controller, Key
from my_imports import thread, WebDriverWait, EC, By, TimeoutException
from write_to_files import write_to_all_files, report_fail
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_text_field(driver, *, by_id=None, by_xpath=None, length, field_name) -> None:
    '''
    This function checks the text field
    '''
    field = locate_element(driver, by_id=by_id, by_xpath=by_xpath)
    assert field is not None, report_fail(f"{field_name} input field not found")
#    driver.execute_script("arguments[0].scrollIntoView();", field)
    field.clear()
    # Limit is <length> characters, try to send more than <length> characters
    field.send_keys('a' * (length + 1))
    # Unfocus the text field
    driver.execute_script("arguments[0].blur();", field)
    check_popup_notification(driver)
    # Check if the text field has been limited to <length> characters
    assert field.get_attribute('value') == 'a' * length, report_fail(f"{field_name} input field does not limit characters")
    # Send actual data
    field.clear()
    field.send_keys('Test ' + field_name)
    # Unfocus the text field
    driver.execute_script("arguments[0].blur();", field)
    check_popup_notification(driver)
    # Check if the data was saved
    assert field.get_attribute('value') == 'Test ' + field_name, report_fail(f"{field_name} input field data not saved")

def display_name(driver) -> None:
    '''
    This function checks the Display Name Text Field
    '''
    check_text_field(driver, by_id='profile-display-name-input', length=30, field_name='Display Name')

def about(driver) -> None:
    '''
    This function checks the About Text Field
    '''
    check_text_field(driver, by_id='profile-about-input', length=100, field_name='About')

def social(driver) -> None:
    '''
    This function checks the social links functionalities
    '''
    raise NotImplementedError("Social Links functionality not implemented")

def UploadImage(driver) -> None:
    '''
    This function checks the Upload Image functionality
    '''
    # Test the upload functionality
    upload_image = locate_element(driver, by_id="settings_avatar_upload")
    assert upload_image is not None, report_fail("Upload Image button not found")
    driver.execute_script("arguments[0].scrollIntoView();", upload_image)
    upload_image.click()

    keyboard = Controller()

    thread.sleep(DELAY_TIME)

    keyboard.type(
        'C:\\Users\\abdal\\Pictures\\munich.jpg')
    thread.sleep(DELAY_TIME)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    check_popup_notification(driver)

def clear_history(driver) -> None:
    '''
    This function checks the Clear History functionality
    '''
    button = locate_element(driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[13]/div[2]/button')
    assert button is not None, report_fail("Clear History button not found")
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()
    # Does nothing on the main reddit page, so i'm not sure what to test here
    thread.sleep(DELAY_TIME)
    print("Tested Clear History")

def profile(driver) -> None:
    '''
    This function tests the profile subpage of the settings page
    '''

    # Test the Display Name (optional) functionality
    # display_name(driver)

    # Test the About (optional) functionality
    # about(driver)

    # Test the Social Links functionality
    # TODO: Implement the social links functionality
    # social(driver)
    # thread.sleep(DELAY_TIME)

    # Test the Upload Image functionality
    # UploadImage(driver)
    # thread.sleep(DELAY_TIME)

    # Test the NSFW checkbox functionality
    check_checkbox(driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[9]/div[2]/label/input', name='NSFW')
    thread.sleep(DELAY_TIME)

    # Test the Allow people to follow you checkbox functionality
    check_checkbox(driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[10]/div[2]/label/input', name='Allow people to follow you')
    thread.sleep(DELAY_TIME)

    # Test the Content Visibility checkbox functionality
    check_checkbox(driver, by_xpath='//*[@id="root"]/div/div[4]/div[3]/div/div[11]/div[2]/label/input', name='Content Visibility')
    thread.sleep(DELAY_TIME)

    # Test the Clear Button functionality
    clear_history(driver)
