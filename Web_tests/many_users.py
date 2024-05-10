"""
This module is used as the main function to test the functionality of a website Reddit clone.
"""

email = 'yirawav345@mfyax.com'

from chrome import chrome
# from firefox import firefox
from constants import SITE_NAME, DELAY_TIME
from my_imports import WebDriverWait, EC, By, thread
from helper_functions import locate_element

# Prepare the driver
driver = chrome()
# driver = firefox()

# Navigate to the site
driver.get(SITE_NAME)
print(driver.title)

# Wait for the site to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
thread.sleep(DELAY_TIME)

for i in range(10, 20):
    # Generate a unique email
    # change any letter of email before the '@' character
    temp_email = email[:-15] + str(i) + email[-14:]
    print(temp_email)
    locate_element(driver, by_xpath='//*[@id="navbar_signup_button"]').click()
    locate_element(driver, by_xpath='//*[@id="signup_email"]').send_keys(temp_email)
    locate_element(driver, by_xpath='//*[@id="signup_email_continue"]').click()
    locate_element(driver, by_xpath='//*[@id="signup_username"]').send_keys('chat' + str(i))
    locate_element(driver, by_xpath='//*[@id="signup_password"]').send_keys('ABcd1234')
    locate_element(driver, by_xpath='//*[@id="gender_dropdown_button"]').click()
    locate_element(driver, by_xpath="//li[@id='gender_woman']/p").click()
    locate_element(driver, by_xpath='//*[@id="signup_submit"]').click()
    thread.sleep(DELAY_TIME)

    print("Logged In with username ", 'chat' + str(i))

    locate_element(driver, by_xpath='//*[@id="navbar_profile"]').click()
    locate_element(driver, by_xpath='//*[@id="profile_logout"]').click()
    thread.sleep(DELAY_TIME)

    print("Logged Out with username ", 'chat' + str(i))

# write_run_time_statistics()
driver.quit()
