'''
This module contains all the xPaths and accessibility IDs for the mobile application.
'''

# Starting page for the mobile application
START_USERNAME = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]'
START_PASSWORD = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]'
START_LOGIN = 'Continue'
START_FORGOT_PASSWORD = 'Forgot Password?'
#reset password for the mobile application
RESET_PASSWORD_EMAIL_TEXTBOX = '//android.widget.EditText'
RESET_PASSWORD_BUTTON = 'Reset Password'
RESET_PASSWORD_RESEND = 'Resend'
RESET_PASSWORD_OPEN_EMAIL_APP = "Open email app"

# Home page

# Profile Icon
HOME_PAGE_PROFILE_ICON = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[4]'

# Within Profile Window
PROFILE_SETTINGS = 'Settings'

# Bottom tabs
HOME_PAGE_TABS_HOME = 'Home\nTab 1 of 5'

# Settings page
SETTINGS_ACCOUNT = '//android.widget.Button[@content-desc="Account Settings u/Claudine"]'
SETTINGS_CONTENT_POLICY = 'Content Policy'
SETTINGS_PRIVACY_POLICY = 'Privacy Policy'
SETTINGS_USER_AGREEMENT = 'User Agreement'
SETTINGS_HELP_CENTER = 'Help Center'
SETTINGS_VISIT_REDDIT_MOBILE = 'Visit r/redditmobile'

# Account settings page
ACCOUNT_UPDATE_EMAIL = '//android.widget.Button[@content-desc="Update email address\nGloria.Grady@hotmail.com"]'
ACCOUNT_UPDATE_PASSWORD = 'Change password'

# Update Email page
UPDATE_EMAIL_USERNAME = 'u/username'
UPDATE_EMAIL_EMAIL = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]'
UPDATE_EMAIL_PASSWORD = '//android.widget.ScrollView/android.widget.EditText[2]'
UPDATE_EMAIL_SAVE = 'Save'
UPDATE_EMAIL_CANCEL = 'Cancel'
UPDATE_EMAIL_FORGOT_PASSWORD = 'Forgot password?'
UPDATE_EMAIL_ERROR_EMAIL_EMPTY = 'Please enter an email address.'
UPDATE_EMAIL_ERROR_EMAIL_INVALID = 'Please enter a valid email address.'
UPDATE_EMAIL_ERROR_PASSWORD_EMPTY = 'Please enter your password'
UPDATE_EMAIL_ERROR_PASSWORD_INVALID = 'Password must be at least 8 characters long'

# Update Password page
UPDATE_PASSWORD_USERNAME = 'u/username'
UPDATE_PASSWORD_CURRENT_PASSWORD = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]'
UPDATE_PASSWORD_NEW_PASSWORD = '//android.widget.ScrollView/android.widget.EditText[2]'
UPDATE_PASSWORD_CONFIRM_PASSWORD = '//android.widget.ScrollView/android.widget.EditText[3]'
UPDATE_PASSWORD_SAVE = 'Save'
UPDATE_PASSWORD_FORGOT_PASSWORD = 'Forgot password?'


# Forgot Password page
FORGOT_PASSWORD_WINDOW = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View'
FORGOT_PASSWORD_HAVING_TROUBLE = 'Having Trouble?'
