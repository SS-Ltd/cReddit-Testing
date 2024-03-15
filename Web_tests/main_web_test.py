"""
This module is used as the main function to test the functionality of a website Reddit clone.
"""

from chrome import chrome
# from firefox import firefox
from constants import SITE_NAME
from my_imports import WebDriverWait, EC, By
from write_to_files import delete_all_files_content
from home_page import home_page

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

# Start all necessary tests
home_page(driver)

driver.quit()
