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
SETTINGS_CONTENT_POLICY = 'Content Policy'
SETTINGS_PRIVACY_POLICY = 'Privacy Policy'
SETTINGS_USER_AGREEMENT = 'User Agreement'
SETTINGS_HELP_CENTER = 'Help Center'
SETTINGS_VISIT_REDDIT_MOBILE = 'Visit r/redditmobile'
