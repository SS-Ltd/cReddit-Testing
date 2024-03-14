'''
This module is used to test the homepage and move to other connected modules.

'''
# Related third-party imports
import time as thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


def home_page(driver: webdriver.Chrome):
    '''
    This function test the homepage of the website
    '''
