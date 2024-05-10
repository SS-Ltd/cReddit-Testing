"""
This module is used as the main function to test the functionality of a website Reddit clone.
"""

from chrome import chrome
# from firefox import firefox
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from write_to_files import delete_all_files_content,write_run_time_statistics
from home_page import home_page
from google_login import google_login
from Registration.sign_up import signup
from helper_functions import locate_element
from right_side_bar import test_right_side_bar
from search import search
from comments import comment
from Registration.login import login 
# Prepare the log files
delete_all_files_content()

# Prepare the driver
driver = chrome()
# driver = firefox()

# Navigate to the site
driver.get(SITE_NAME)
print(driver.title)

# Wait for the site to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
driver.maximize_window()
thread.sleep(DELAY_TIME)
# login(driver)
# Login
locate_element(driver, by_xpath='//*[@id="navbar_login_button"]').click()
locate_element(driver, by_xpath='//*[@id="login_username"]').send_keys("chat0")
locate_element(driver, by_xpath='//*[@id="login_password"]').send_keys("ABcd1234")
locate_element(driver, by_xpath='//*[@id="login_submit"]').click()
thread.sleep(DELAY_TIME)

# test_right_side_bar(driver)
# search(driver)
# Wait for the site to load
thread.sleep(DELAY_TIME)
# comment(driver)
#home_page(driver)
# login(driver)
#google_login(driver, "cReddit support center")

# write_run_time_statistics()
driver.quit()
