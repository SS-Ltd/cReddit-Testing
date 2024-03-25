'''
This module is used to navigate to the google Gmail and log in to the account 
'''

from my_imports import WebDriverWait, EC, By, TimeoutException , thread
from write_to_files import write_to_all_files, report_fail, report_success
from constants import EMAIL, PASSWORD ,DELAY_TIME
from globals import set_first_login, get_first_login


def search_for_email(driver, text :str) -> bool:
    '''
    This function searches for an email in the Gmail inbox
    if the email is found it clicks on it
    @param driver: The driver to use
    @param Text: The text to search for
    @return: True if the email was found, False otherwise
    '''
    a = driver.find_elements(By.XPATH, "//*[@class='yW']/span")
    for i in a:
        if i.text == text:
            i.click()
            return True
    return False

def delete_open_email(driver) -> None:
    '''
    This function deletes the email that is open
    @param driver: The driver to use
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id=":4"]/div[2]/div[1]/div/div[2]/div[3]'))).click()
    except TimeoutException:
        report_fail("The delete button was not found"
            + "[google_login() -> delete_open_email() -> Delete button not found]")
        return
    report_success("The delete button was found"
        + "[google_login() -> delete_open_email() -> Delete button found]")

def goto_google(driver) -> None:
    '''
    This function navigates to google Gmail
    @param driver: The driver to use
    '''
    driver.execute_script("window.open('https://www.google.com/gmail/about/', '_blank')")
    driver.switch_to.window(driver.window_handles[1])
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.title_contains("Gmail"))
    except TimeoutException:
        report_fail("The title of the Gmail page was not found"
            + "[google_login() -> goto_google() -> Gmail Page not found]")
        return
    report_success("The title of the Gmail page was found"
        + "[google_login() -> goto_google() -> Gmail Page found]")

def click_google_sign_in(driver) -> None:
    '''
    This function clicks the sign in button
    @param driver: The driver to use
    '''
    try:
        WebDriverWait(driver,DELAY_TIME).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/header/div/div/div/a[2]"))).click()
    except TimeoutException:
        report_fail("The sign in button was not found"
            + "[google_login() -> Sign in button not found]")
        return
    report_success("The sign in button was found"
        + "[google_login() -> Sign in button found]")

def enter_email_google(driver) -> None:
    '''
    This function enters the email to the email input
    @param driver: The driver to use
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located(
            (By.ID, "identifierId"))).send_keys(EMAIL)
    except TimeoutException:
        report_fail("The email input was not found"
            + "[google_login() -> Email input not found]")
        return
    report_success("The email input was found"
        + "[google_login() -> Email input found]")

def email_next_click_google(driver) -> None:
    '''
    This function clicks the next button after entering the email
    @param driver: The driver to use
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located(
            (By.ID, "identifierNext"))).click()
    except TimeoutException:
        report_fail("The next button was not found"
            + "[google_login() -> Next button not found]")
        return
    report_success("The next button was found"
        + "[google_login() -> Next button found]")

def enter_password_google(driver) -> None:
    '''
    This function enters the password to the password input
    @param driver: The driver to use
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[1]/div[2]"
             +"/c-wiz/div/div[2]/div/div/div/form/span/"
             +"section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))
             ).send_keys(PASSWORD)
    except TimeoutException:
        try:
            WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div"
                 +"/c-wiz/div/div[2]/div/div[1]/div/form/span/"
                 +"section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))
                 ).send_keys(PASSWORD)
        except TimeoutException:
            report_fail("The password input was not found"
                        + "[google_login() -> Password input not found]")
            return
    report_success("The password input was found"
        + "[google_login() -> Password input found]")

def password_next_click_google(driver) -> None:
    '''
    This function clicks the next button after entering the password
    @param driver: The driver to use
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located(
            (By.ID, "passwordNext"))).click()
    except TimeoutException:
        report_fail("The next button was not found"
            + "[google_login() -> Next button not found]")
        return
    report_success("The next button was found"
        + "[google_login() -> Next button found]")

def continue_page_click_google(driver) -> None:
    '''
    after the password page,
      a continue page sometimes appears and this function clicks on "not now" to continue
    @param driver: The driver to use
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="yDmH0d"]/div[1]/div[1]/div[2]'
             +'/div/div/div[3]/div/div[2]/div/div/button/span'))).click()
    except TimeoutException:
        print("The Conitue page did not appear")
def go_to_inbox(driver) -> None:
    '''
    This function navigates to the inbox page
    @param driver: The driver to use
    '''
    driver.execute_script("window.open('https://mail.google.com/mail/u/0/#inbox', '_blank')")
    driver.switch_to.window(driver.window_handles[1])
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.title_contains("Inbox"))
    except TimeoutException:
        report_fail("The title of the Inbox page was not found"
            + "[google_login() -> Inbox Page not found]")
        return
    report_success("The title of the Inbox page was found"
        + "[google_login() -> Inbox Page found]")
    thread.sleep(DELAY_TIME)

def inbox_page_check_google(driver) -> None:
    '''
    This function checks if the inbox page was found
    @param driver: The driver to use
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(EC.title_contains("Inbox"))
    except TimeoutException:
        report_fail("The title of the Inbox page was not found"
            + "[google_login() -> Inbox Page not found]")
        return
    report_success("The title of the Inbox page was found"
        + "[google_login() -> Inbox Page found]")

def google_login(driver) -> None:
    '''
    This function navigates to google Gmail and logs in
    @param driver: The driver to use
    '''
    write_to_all_files("#################### Login To Gmail ####################")
    if get_first_login():
        goto_google(driver)
        click_google_sign_in(driver)
        enter_email_google(driver)
        email_next_click_google(driver)
        thread.sleep(DELAY_TIME)    #remove this line may lead to crashes
        enter_password_google(driver)
        password_next_click_google(driver)
        set_first_login(False)
        continue_page_click_google(driver)
    else:
        go_to_inbox(driver)
    inbox_page_check_google(driver)
    thread.sleep(DELAY_TIME)
    write_to_all_files("#################### Gmail Login Complete ####################")
