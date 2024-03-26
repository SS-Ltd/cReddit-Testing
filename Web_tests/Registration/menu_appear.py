'''
This file contains the functions that check if the registration menus appeared
'''
import sys
import os
from enum import Enum
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helper_functions import locate_element
from my_imports import TimeoutException, thread
from write_to_files import write_to_all_files, report_fail, report_success

def login_menu_appeared(driver) -> bool:
    '''
    This function checks if the login menu appeared
    @param driver: The driver to use
    @return: True if the login menu appeared, False otherwise
    '''
    try:
        locate_element(driver, by_id="navbar_login_menu")
        report_success(
            "The Login Window appeared"
            + " [menu_appear.py -> login_menu_appeared() -> login window appeared]"
        )
        return True
    except TimeoutException:
        report_fail(
            "The login window did not appear"
            + "[menu_appear.py -> login_menu_appeared() -> login window did not appear]"
        )
        return False

def sign_up_menu_appeared(driver) -> bool:
    '''
    This function checks if the sign up menu appeared
    @param driver: The driver to use
    @return: True if the sign up menu appeared, False otherwise
    '''
    try:
        locate_element(driver, by_id="navbar_signup_menu")
        report_success(
            "The Sign Up Window appeared"
            + " [menu_appear.py -> sign_up_menu_appeared() -> sign up window appeared]"
        )
        return True
    except TimeoutException:
        report_fail(
            "The sign up window did not appear"
            + "[menu_appear.py -> sign_up_menu_appeared() -> sign up window did not appear]"
        )
        return False

def forgot_password_menu_appeared(driver) -> bool:
    '''
    This function checks if the forgot password menu appeared
    @param driver: The driver to use
    @return: True if the forgot password menu appeared, False otherwise
    '''
    try:
        locate_element(driver, by_id="reset_password_username")
    except TimeoutException:
        report_fail(
            "The forgot password window did not appear"
            + "[menu_appear.py -> forgot_password_menu_appeared() ->"
            + " forgot password window did not appear]"
        )
        return False
    report_success(
        "The Forgot Password Window appeared"
        + " [menu_appear.py -> forgot_password_menu_appeared() -> forgot password window appeared]"
    )
    return True

def forgot_username_menu_appeared(driver) -> bool:
    '''
    This function checks if the forgot username menu appeared
    @param driver: The driver to use
    @return: True if the forgot username menu appeared, False otherwise
    '''
    try:
        locate_element(driver, by_id="reset_username_email")
    except TimeoutException:
        report_fail(
            "The forgot username window did not appear"
            + "[menu_appear.py -> forgot_username_menu_appeared() ->"
            + " forgot username window did not appear]"
        )
        return False
    report_success(
        "The Forgot Username Window appeared"
        + " [menu_appear.py -> forgot_username_menu_appeared() -> forgot username window appeared]"
    )
    return True
