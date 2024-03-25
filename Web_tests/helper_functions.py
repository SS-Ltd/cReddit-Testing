'''
This file contains all the helper functions used in the project
'''

from constants import DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread, TimeoutException
from write_to_files import report_fail


def locate_element(driver, *, by_id=None, by_xpath=None) -> WebDriverWait:
    '''
    This function is used to locate an element
    '''
    if by_id:
        return WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, by_id))
            )
    if by_xpath:
        return WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.XPATH, by_xpath))
            )
    return None

def check_popup_notification(driver) -> None:
    '''
    This function checks the popup notification that appears after changing
    '''
    # Check if pop-up is displayed
    thread.sleep(DELAY_TIME)
    popup = locate_element(driver, by_xpath='//*[contains(@id, "popup")]')
    assert popup is not None, report_fail("Popup not found")

def check_logged_in(driver) -> bool:
    '''
    This function tests if the user is logged in correctly
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located(
            (By.ID, "navbar_login_button")))
    except TimeoutException:
        return True
    return False

def check_logged_out(driver) -> bool:
    '''
    This function tests if the user is logged out correctly
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located(
            (By.ID, "navbar_logout_button")))
    except TimeoutException:
        return True
    return False
