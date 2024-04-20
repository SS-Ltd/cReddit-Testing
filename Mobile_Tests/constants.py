'''
This file contains all the constants that are used throughout the project.
'''
import os
from dotenv import load_dotenv
load_dotenv("../Web_Text_Files/.env")

DELAY_TIME = 5
SEE_TIME = 2
USERNAME = str(os.getenv("USERNAME1"))
EMAIL = str(os.getenv("EMAIL"))
#PASSWORD = str(os.getenv("PASSWORD"))
PASSWORD_CREDDIT = str(os.getenv("PASSWORD_CREDDIT"))
EMAIL_SIGNUP = str(os.getenv("EMAIL_SIGNUP"))
