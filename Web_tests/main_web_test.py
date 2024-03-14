"""
This module is used as the main function to test the functionality of a website Reddit clone.
"""
import time as thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import home_page
from write_to_files import write_to_all_files
from constants import SITE_NAME, DELAY_TIME
from login import login
from write_to_files import delete_all_files_content

delete_all_files_content()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(SITE_NAME)
print(driver.title)
driver.maximize_window()
thread.sleep(DELAY_TIME)
login(driver)
#home_page.home_page(driver)


driver.quit()
