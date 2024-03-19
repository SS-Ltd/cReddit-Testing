'''
This module is used to test the settings page of the Reddit website.
'''
from enum import Enum
from my_imports import WebDriverWait, EC, By, TimeoutException, thread
from pynput.keyboard import Key, Controller
from constants import DELAY_TIME
from write_to_files import write_to_all_files, report_fail, report_success


class Subpage(Enum):
    '''
    This class is used to define the different subpages of the settings page
    '''
    ACCOUNT = (0, "Account")
    PROFILE = (1, "Profile")
    SAFETY = (2, "Safety & Privacy")
    FEED = (3, "Feed Settings")
    NOTIFICATIONS = (4, "Notifications")
    EMAILS = (5, "Emails")


# Constant IDs to identify the subpages
SUBPAGES = {
    Subpage.ACCOUNT: 'setting-navbar-account-tab',
    Subpage.PROFILE: 'setting-navbar-profile-tab',
    Subpage.SAFETY: 'setting-navbar-safety & privacy-tab',
    Subpage.FEED: 'setting-navbar-feed settings-tab',
    Subpage.NOTIFICATIONS: 'setting-navbar-notifications-tab',
    Subpage.EMAILS: 'setting-navbar-emails-tab'
}

URLS = {
    Subpage.ACCOUNT: "http://localhost:5173/settings/account",
    Subpage.PROFILE: "http://localhost:5173/settings/profile",
    Subpage.SAFETY: "http://localhost:5173/settings/privacy",
    Subpage.FEED: "http://localhost:5173/settings/feed",
    Subpage.NOTIFICATIONS: "http://localhost:5173/settings/notifications",
    Subpage.EMAILS: "http://localhost:5173/settings/emails"
}


def check_popup_notification(driver) -> None:
    '''
    This function checks the popup notification that appears after changing
    '''
    # Check if pop-up is displayed
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[1]/div'))
        )
        report_success(
            "The changes pop-up was found"
            + " [settings() -> account_subpage() -> changes pop-up found]"
        )
    except TimeoutException:
        report_fail(
            "The changs pop-up was not found"
            + " [settings() -> account_subpage() -> changes pop-up not found]"
        )

def goto_settings(driver) -> None:
    '''
    This function goes to the settings page from the homepage
    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "navbar_profile"))).click()
        # EC.presence_of_element_located((By.ID, "expand-user-drawer-button"))).click()
        report_success(
            "The element with the ID 'navbar_profile' was found"
            + " [settings() -> goto_settings() -> profile button found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'navbar_profile' was not found"
            + " [settings() -> goto_settings() -> profile button not found]"
        )
        return

    thread.sleep(DELAY_TIME)

    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "profile_settings"))).click()
        # EC.presence_of_element_located((By.XPATH, '//*[@id="user-drawer-content"]/ul[3]/faceplate-tracker/li/a'))).click()
        report_success(
            "The element with the ID 'profile_settings' was found"
            + " [settings() -> goto_settings() -> settings button found]"
        )
    except TimeoutException:
        report_fail(
            "The element with the ID 'profile_settings' was not found"
            + " [settings() -> goto_settings() -> settings button not found]"
        )
        return

    # Check if the settings page is loaded
    thread.sleep(DELAY_TIME)
    if driver.current_url == "http://localhost:5173/settings":
        # if driver.current_url == "https://www.reddit.com/settings":
        report_success(
            "The settings page was loaded"
            + " [settings() -> goto_settings() -> settings page loaded]"
        )
    else:
        report_fail(
            "The settings page was not loaded"
            + " [settings() -> goto_settings() -> settings page not loaded]"
        )


def goto_subpage(driver, subpage: Subpage) -> None:
    '''
    This function goes to a specific subpage of the settings page

    '''
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, SUBPAGES[subpage]))
        ).click()
        report_success(
            "The " + subpage.value[1] + " subpage button was found"
            + " [settings() -> goto_subpage() -> " +
            subpage.value[1] + " button found]"
        )

        # Wait for the page to load
        thread.sleep(DELAY_TIME)

        # TOBEUPDATED!!!!!!!!!
        if driver.current_url == URLS[subpage]:
            report_success(
                "The " + subpage.value[1] + " subpage was loaded"
                + " [settings() -> goto_subpage() -> " +
                subpage.value[1] + " page loaded]"
            )
        else:
            report_fail(
                "The " + subpage.value[1] + " subpage was not loaded"
                + " [settings() -> goto_subpage() -> " +
                subpage.value[1] + " page not loaded]"
            )
            return

    except TimeoutException:
        report_fail(
            "The " + subpage.value[1] + " subpage button was not found"
            + " [settings() -> goto_subpage() -> " +
            subpage.value[1] + " button not found]"
        )
        return

# Tests on the Account Subpage


def account_subpage(driver) -> None:
    '''
    This function test the account subpage of the settings page
    '''

    write_to_all_files(
        "#################### Testing Account Subpage ####################")

    # Test the change email button
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "settings-change-email-button"))
        ).click()
        report_success(
            "The change email button was found"
            + " [settings() -> account_subpage() -> change email button found]"
        )
    except TimeoutException:
        report_fail(
            "The change email button was not found"
            + " [settings() -> account_subpage() -> change email button not found]"
        )

    check_popup_notification(driver)
    thread.sleep(DELAY_TIME)

    # Test the Gender dropdown list
    # First click the dropdown list
    try:
        gender_option = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[3]/div/div[2]/div[2]/div/a'))
        )
        gender_option.click()
        report_success(
            "The dropdown list was found"
            + " [settings() -> account_subpage() -> dropdown list found]"
        )
    except TimeoutException:
        report_fail(
            "The dropdown list was not found"
            + " [settings() -> account_subpage() -> dropdown list not found]"
        )
    thread.sleep(DELAY_TIME)
    # Then try to select a gender from the expanded dropdown list
    # First try the Man option
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, 'settings-simplemenu-gender-man'))
        ).click()
        report_success(
            "Man option was found"
            + " [settings() -> account_subpage() -> Man option found]"
        )
    except TimeoutException:
        report_fail(
            "Man option was not found"
            + " [settings() -> account_subpage() -> Man option not found]"
        )

    check_popup_notification(driver)

    # Check that the option on the outside is Man
    if gender_option.text == "Man":
        report_success(
            "Gender was changed"
            + " [settings() -> account_subpage() -> Gender changed]"
        )
    else:
        report_fail(
            "Gender was not changed"
            + " [settings() -> account_subpage() -> Gender not changed]"
        )

    thread.sleep(DELAY_TIME)

    # Test the change password button
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "settings-change-password-button"))
        ).click()
        report_success(
            "The change password button was found"
            + " [settings() -> account_subpage() -> change password button found]"
        )
    except TimeoutException:
        report_fail(
            "The change password button was not found"
            + " [settings() -> account_subpage() -> change password button not found]"
        )

    check_popup_notification(driver)
    thread.sleep(DELAY_TIME)

    # Test the country dropdown list
    # First click the dropdown list
    try:
        country_option = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[3]/div/div[4]/div[2]/div/a'))
        )
        country_option.click()
        report_success(
            "The dropdown list was found"
            + " [settings() -> account_subpage() -> dropdown list found]"
        )
    except TimeoutException:
        report_fail(
            "The dropdown list was not found"
            + " [settings() -> account_subpage() -> dropdown list not found]"
        )
    thread.sleep(DELAY_TIME)
    # Then try to select a country from the expanded dropdown list
    # First try the UK option
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, 'settings-simplemenu-country-uk'))
        ).click()
        report_success(
            "UK option was found"
            + " [settings() -> account_subpage() -> UK option found]"
        )
    except TimeoutException:
        report_fail(
            "UK option was not found"
            + " [settings() -> account_subpage() -> UK option not found]"
        )

    check_popup_notification(driver)

    # Check that the option on the outside is Egypt
    if country_option.text == "UK":
        report_success(
            "Country was changed"
            + " [settings() -> account_subpage() -> Country changed]"
        )
    else:
        report_fail(
            "Country was not changed"
            + " [settings() -> account_subpage() -> Country not changed]"
        )

    thread.sleep(DELAY_TIME)

    # Go To Connected Accounts
    # 1. Connect to twitter
    try:
        twitter = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "settings-connect-twitter-button"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", twitter)
        thread.sleep(DELAY_TIME)
        twitter.click()
        report_success(
            "The connect to twitter button was found"
            + " [settings() -> account_subpage() -> connect to twitter button found]"
        )
    except TimeoutException:
        report_fail(
            "The connect to twitter button was not found"
            + " [settings() -> account_subpage() -> connect to twitter button not found]"
        )

    thread.sleep(DELAY_TIME)

    # Disconnect from Apple
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "settings-disconnect-apple-button"))
        ).click()
        report_success(
            "The disconnect from apple button was found"
            + " [settings() -> account_subpage() -> disconnect from apple button found]"
        )
    except TimeoutException:
        report_fail(
            "The disconnect from apple button was not found"
            + " [settings() -> account_subpage() -> disconnect from apple button not found]"
        )

    # Connect to Google
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "settings-connect-google-button"))
        ).click()
        report_success(
            "The connect to google button was found"
            + " [settings() -> account_subpage() -> connect to google button found]"
        )
    except TimeoutException:
        report_fail(
            "The connect to google button was not found"
            + " [settings() -> account_subpage() -> connect to google button not found]"
        )

    thread.sleep(DELAY_TIME)

    # Delete Account
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "settings-delete-account-button"))
        ).click()
        report_success(
            "The delete account button was found"
            + " [settings() -> account_subpage() -> delete account button found]"
        )
    except TimeoutException:
        report_fail(
            "The delete account button was not found"
            + " [settings() -> account_subpage() -> delete account button not found]"
        )

def profile_subpage(driver) -> None:
    '''
    This function test the profile subpage of the settings page
    '''
    write_to_all_files(
        "#################### Testing Profile Subpage ####################")

    # Testing the Display Name (Optional) input field
    try:
        display_name = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "profile-display-name-input"))
        )
        display_name.clear()
        display_name.send_keys("Test Name")
        thread.sleep(DELAY_TIME)
        report_success(
            "The Display Name was found"
            + " [settings() -> profile_subpage() -> Display Name found]"
        )
    except TimeoutException:
        report_fail(
            "The Display Name was found"
            + " [settings() -> profile_subpage() -> Display Name found]"
        )

    # Check if the Display Name was changed
    if display_name.get_attribute('value') == "Test Name":
        report_success(
            "The Display Name was changed"
            + " [settings() -> profile_subpage() -> Display Name changed]"
        )
    else:
        report_fail(
            "The Display Name was not changed"
            + " [settings() -> profile_subpage() -> Display Name not changed]"
        )

    driver.execute_script("arguments[0].blur();", display_name)
    thread.sleep(DELAY_TIME)

    # About (optional) input field
    try:
        about = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "profile-about-input"))
        )
        about.clear()
        about.send_keys("Test About")
        thread.sleep(DELAY_TIME)
        report_success(
            "The About was found"
            + " [settings() -> profile_subpage() -> About found]"
        )
    except TimeoutException:
        report_fail(
            "The About was found"
            + " [settings() -> profile_subpage() -> About found]"
        )

    # Check if the About was changed
    if about.get_attribute('value') == "Test About":
        report_success(
            "The About was changed"
            + " [settings() -> profile_subpage() -> About changed]"
        )
    else:
        report_fail(
            "The About was not changed"
            + " [settings() -> profile_subpage() -> About not changed]"
        )

    driver.execute_script("arguments[0].blur();", about)
    thread.sleep(DELAY_TIME)

    # Check the social links
    # 1. Buy me a coffee
    try:
        buy_me_coffee = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "profile-added-social-link-buy_me_a_coffee"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", buy_me_coffee)
        thread.sleep(DELAY_TIME)
        driver.execute_script("arguments[0].click();", buy_me_coffee)
        report_success(
            "The Buy me a coffee button was found"
            + " [settings() -> profile_subpage() -> Buy me a coffee button found]"
        )
    except TimeoutException:
        report_fail(
            "The Buy me a coffee button was not found"
            + " [settings() -> profile_subpage() -> Buy me a coffee button not found]"
        )

    thread.sleep(DELAY_TIME)

    # 2. Twitter
    try:
        twitter = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "profile-added-social-link-twitter"))
        )
        driver.execute_script("arguments[0].click();", twitter)
        report_success(
            "The Twitter button was found"
            + " [settings() -> profile_subpage() -> Twitter button found]"
        )
    except TimeoutException:
        report_fail(
            "The Twitter button was found"
            + " [settings() -> profile_subpage() -> Twitter button found]"
        )

    thread.sleep(DELAY_TIME)

    # 3. Reddit
    try:
        reddit = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "profile-added-social-link-reddit"))
        )
        driver.execute_script("arguments[0].click();", reddit)
        report_success(
            "The Reddit button was found"
            + " [settings() -> profile_subpage() -> Reddit button found]"
        )
    except TimeoutException:
        report_fail(
            "The Reddit button was found"
            + " [settings() -> profile_subpage() -> Reddit button found]"
        )

    thread.sleep(DELAY_TIME)

    # 4. Discord
    try:
        discord = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "profile-added-social-link-discord"))
        )
        driver.execute_script("arguments[0].click();", discord)
        report_success(
            "The Discord button was found"
            + " [settings() -> profile_subpage() -> Discord button found]"
        )
    except TimeoutException:
        report_fail(
            "The Discord button was found"
            + " [settings() -> profile_subpage() -> Discord button found]"
        )

    thread.sleep(DELAY_TIME)

    # 5. Facebook
    try:
        facebook = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "profile-added-social-link-facebook"))
        )
        driver.execute_script("arguments[0].click();", facebook)
        report_success(
            "The Facebook button was found"
            + " [settings() -> profile_subpage() -> Facebook button found]"
        )
    except TimeoutException:
        report_fail(
            "The Facebook button was found"
            + " [settings() -> profile_subpage() -> Facebook button found]"
        )

    thread.sleep(DELAY_TIME)

    # Test the upload functionality
    try:
        upload_image = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "profile-image-upload-drag-and-drop"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", upload_image)
        thread.sleep(4)
        upload_image.click()
        thread.sleep(20)
        report_success(
            "The upload image was found"
            + " [settings() -> profile_subpage() -> upload image found]"
        )
    except TimeoutException:
        report_fail(
            "The upload image was found"
            + " [settings() -> profile_subpage() -> upload image found]"
        )

    keyboard = Controller()

    keyboard.type('C:\\Users\\abdal\\Pictures\\Screenshot 2024-03-19 195003.png')
    thread.sleep(DELAY_TIME)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    thread.sleep(DELAY_TIME)

    #  NSFW button
    try:
        nsfw = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[3]/div/div[9]/div[2]/label/div'))
        )
        # move to the element
        driver.execute_script("arguments[0].scrollIntoView();", nsfw)
        thread.sleep(DELAY_TIME)
        nsfw.click()
        report_success(
            "The NSFW button was found"
            + " [settings() -> profile_subpage() -> NSFW button found]"
        )
    except TimeoutException:
        report_fail(
            "The NSFW button was found"
            + " [settings() -> profile_subpage() -> NSFW button found]"
        )

    # Check if the popup notification is displayed
    thread.sleep(DELAY_TIME)
    check_popup_notification(driver)

    # Check the 'Allow people to follow you'
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[3]/div/div[10]/div[2]/label/div'))
        ).click()
        report_success(
            "The 'Allow people to follow you' button was found"
            + " [settings() -> profile_subpage() -> Allow people to follow you button found]"
        )
    except TimeoutException:
        report_fail(
            "The 'Allow people to follow you' button was found"
            + " [settings() -> profile_subpage() -> Allow people to follow you button found]"
        )

    # Check if the popup notification is displayed
    thread.sleep(DELAY_TIME)
    check_popup_notification(driver)

    # Check the 'Content Visibility' button
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[3]/div/div[11]/div[2]/label/div'))
        ).click()
        report_success(
            "The 'Content Visibility' button was found"
            + " [settings() -> profile_subpage() -> Content Visibility button found]"
        )
    except TimeoutException:
        report_fail(
            "The 'Content Visibility' button was found"
            + " [settings() -> profile_subpage() -> Content Visibility button found]"
        )

    # Check if the popup notification is displayed
    thread.sleep(DELAY_TIME)
    check_popup_notification(driver)

    # Check if 'Active in communities visibility' button
    try:
        WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[3]/div/div[12]/div[2]/label/div'))
        ).click()
        report_success(
            "The 'Active in communities visibility' button was found"
            + " [settings() -> profile_subpage() -> Active in communities visibility button found]"
        )
    except TimeoutException:
        report_fail(
            "The 'Active in communities visibility' button was found"
            + " [settings() -> profile_subpage() -> Active in communities visibility button found]"
        )

    # Check 'Clear history' button
    try:
        element = WebDriverWait(driver, DELAY_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[3]/div/div[13]/div[2]/button'))
        )
        driver.execute_script("arguments[0].click();", element)
        report_success(
            "The 'Clear history' button was found"
            + " [settings() -> profile_subpage() -> Clear history button found]"
        )
    except TimeoutException:
        report_fail(
            "The 'Clear history' button was found"
            + " [settings() -> profile_subpage() -> Clear history button found]"
        )

    # Check if the popup notification is displayed
    thread.sleep(DELAY_TIME)
    check_popup_notification(driver)

def settings(driver) -> None:
    '''
    This function test the settings page of the website
    '''

    write_to_all_files(
        "#################### Testing Settings Page ####################")
    goto_settings(driver)
    # thread.sleep(DELAY_TIME)

    # # Scroll down a little bit
    # driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    # driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    # driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    # driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    # driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    # thread.sleep(5)

    # Test each subpage of the settings page
    # Page 1: Account
    # goto_subpage(driver, Subpage.ACCOUNT)
    # thread.sleep(DELAY_TIME)
    # account_subpage(driver)
    # thread.sleep(DELAY_TIME)

    # Page 2: Profile
    goto_subpage(driver, Subpage.PROFILE)
    thread.sleep(DELAY_TIME)
    profile_subpage(driver)

    # Page 3: Safety & Privacy
    # goto_subpage(driver, Subpage.SAFETY)
    # thread.sleep(DELAY_TIME)

    # Page 4: Feed Settings
    # goto_subpage(driver, Subpage.FEED)
    # thread.sleep(DELAY_TIME)

    # Page 5: Notifications
    # goto_subpage(driver, Subpage.NOTIFICATIONS)
    # thread.sleep(DELAY_TIME)

    # Page 6: Emails
    # goto_subpage(driver, Subpage.EMAILS)
    # thread.sleep(DELAY_TIME)

    # write_to_all_files("Settings page test completed")
    # thread.sleep(DELAY_TIME)
