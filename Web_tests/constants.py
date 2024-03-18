''' 
This file contains all the constants used in the project
'''
import os
from dotenv import load_dotenv
load_dotenv("../Web_Text_Files/credentials.env")

SUCCESS_FILE_PATH = "../Web_Text_Files/success_file.txt"
FAIL_FILE_PATH = "../Web_Text_Files/fail_file.txt"
COMBINED_FILE_PATH = "../Web_Text_Files/combined_file.txt"
LOG_FILE_PATH = "../Web_Text_Files/log_file.txt"
FIREFOX_DRIVER_PATH = "C:/geckodriver.exe"
FIREFOX_BINARY_PATH = "C:/Program Files/Mozilla Firefox/firefox.exe"
DELAY_TIME = 4
SITE_NAME = "https://creddit.tech?"
#SITE_NAME = "http://localhost:5173/"
EMAIL = str(os.getenv("EMAIL"))
PASSWORD = str(os.getenv("PASSWORD"))
# http://creddit.tech
