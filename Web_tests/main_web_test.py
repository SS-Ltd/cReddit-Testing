"""
This module is used as the main function to test the functionality of a website Reddit clone.
"""

from chrome import chrome
# from firefox import firefox
from constants import SITE_NAME
from my_imports import WebDriverWait, EC, By, thread
from write_to_files import delete_all_files_content
from home_page import home_page
from google_login import google_login
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
thread.sleep(2)

# Start all necessary tests
#home_page(driver)
login(driver)
#google_login(driver, "cReddit support center")
driver.quit()
