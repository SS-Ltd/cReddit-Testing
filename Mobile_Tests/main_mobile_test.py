from appium import webdriver
import unittest
import time

class TestMobile(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "Android Emulator",
            "app": "x",
            "appPackage": "com.example.android.contactmanager",
            "appActivity": ".ContactManager"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        time.sleep(2)       