'''
This module contains all the xPaths and accessibility IDs for the mobile application.
'''
# RID = Resource ID
# XPATH = Xpath
# AID = Accessibility ID
# Starting page for the mobile application
START_USERNAME = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]'
START_PASSWORD = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]'
START_SIGNUP = 'Sign Up'
START_LOGIN = 'Continue'
START_COUNTINUE_WITH_GOOGLE = 'Continue with Google'
START_FORGOT_PASSWORD = 'Forgot Password?'
#reset password for the mobile application
RESET_PASSWORD_EMAIL_TEXTBOX = '//android.widget.EditText'
RESET_PASSWORD_BUTTON = 'Reset Password'
RESET_PASSWORD_RESEND = 'Resend'
RESET_PASSWORD_OPEN_EMAIL_APP = "Open email app"
RESET_PASSWORD_HELP_BUTTON = "Help"
RESET_PASSWORD_CLOSE_TAB_BUTTON = "Close tab"
# login continue with google
CONTINUE_WITH_GOOGLE_EMAIL = '(//android.widget.LinearLayout[@resource-id="com.google.android.gms:id/container"])[1]'
# signup 
SIGNUP_EMAIL = 'signup_email_field'                     #RID
SIGNUP_PASSWORD = 'signup_password_fields'              #RID
SIGNUP_LOGIN = 'Log In'                                 #AID
SIGNUP_CONTINUE = 'Continue'                            #AID
#signup continue with google
SIGNUP_CONTINUE_WITH_GOOGLE = 'Continue with Google'    #AID
# Home page
# Custom Navigation Bar
NAVIGATION_BAR_HOME = 'Home\nTab 1 of 5'                 #AID
NAVIGATION_BAR_COMMUNITIES = 'Communities Tab 2 of 5'   #AID
NAVIGATION_BAR_CREATE_POST = 'Create\nTab 3 of 5'       #AID
NAVIGATION_BAR_CHAT = 'Chat Tab 4 of 5'                 #AID
NAVIGATION_BAR_INBOX = 'Inbox Tab 5 of 5'               #AID

# Profile Icon
HOME_PAGE_PROFILE_ICON = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[4]'

# Within Profile Window
PROFILE_WINDOW_PROFILE = 'My Profile'
PROFILE_WINDOW_CREATE_COMMUNITY = 'Create a Community'
PROFILE_WINDOW_SAVED = 'Saved'
PROFILE_WINDOW_HISTORY = 'History'
PROFILE_WINDOW_SETTINGS = 'Settings'
PROFILE_SETTINGS = 'Settings'

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

# profile page
PROFILE_PAGE_EDIT_PROFILE = 'Edit'              #AID
PROFILE_PAGE_POSTS = 'Posts'                    #AID
PROFILE_PAGE_COMMENTS = 'Comments'              #AID
PROFILE_PAGE_ABOUT = 'About'                    #AID
PROFILE_PAGE_SHARE = 'profile share'            #RID
PROFILE_PAGE_SEARCH = 'profile search'          #RID
PROFILE_PAGE_MENU = 'profile menu'              #RID        #Might not work

# about user popup/Profile card
CREATE_YOUR_OWN_AVATAR = 'Create Your Own Avatar'           #AID        #not in project scope
ABOUT_USER_VIEW_PROFILE = 'View Profile'                    #AID
ABOUT_USER_SEND_MESSAGE = 'Send Message'                    #AID
ABOUT_USER_BLOCK_ACCOUNT = 'Block Account'                  #AID
#subreddit page
SUBREDDIT_PAGE_JOIN = 'Join'                                #AID
SUBREDDIT_PAGE_LEAVE = 'Joined'                             #AID
SUBREDDIT_PAGE_SORT_HOT = 'Hot'                             #AID
SUBREDDIT_PAGE_SORT_NEW = 'New'                             #AID
SUBREDDIT_PAGE_SORT_TOP = 'Top'                             #AID
SUBREDDIT_PAGE_SORT_OPTIONS = 'subreddit sorting options'   #RID    #Might not work
SUBREDDIT_PAGE_SEARCH = 'search subreddit'                  #RID    #Might not work
SUBREDDIT_PAGE_SHARE = 'share subreddit'                    #RID    #Might not work
SUBREDDIT_PAGE_OPTIONS = 'subreddit options'                #RID    #Might not work
#TOP COMMUNITIES
TOP_COMMUNITIES_JOIN_LEAVE = 'join or disjoin subreddit'
#CREATE COMMUNITY
CREATE_COMMUNITY_NAME = 'Community Name'#RID
CREATE_COMMUNITY_TYPE = 'Community Type'#RID
CREATE_COMMUNITY_TYPE_PUBLIC = 'Public Anyone can view, post, and comment to this community.'#AID
CREATE_COMMUNITY_TYPE_RESTRICTED = 'Restricted Anyone can view this community, but only approved users can post.'#AID
CREATE_COMMUNITY_TYPE_PRIVATE = 'Private Only approved users can view and submit to this community.'#AID
CREATE_COMMUNITY_18   = '18+ Community' #RID
CREATE_COMMUNITY_BUTTON = 'Create Community'#AID
CREATE_COMMUNITY_BACK = 'Back'          #AID
# posts all resource IDS except stated
POST_UPVOTE      = 'post upvote'        #RID
POST_VOTES       = 'post votes'         #RID        # Might not work
POST_DOWNVOTE    = 'post downvote'      #RID
POST_COMMENTS    = 'post comment'       #RID
POST_USERNAME    = 'post username'      #RID        # POST USERNAME and POST SUBREDDIT together form the some reason
POST_SUBREDDIT   = 'post subreddit'     #RID        # Might not work
POST_TITLE       = 'post title'         #RID
POST_SHARE       = 'post share'         #RID
# Create Post

# Comments all resource IDS
COMMENT_UPVOTE   = 'comment upvote'     #RID
COMMENT_VOTES    = 'comment votes'      #RID        # Might not work
COMMENT_DOWNVOTE = 'comment downvote'   #RID
COMMENT_OPTIONS  = 'comment options'    #RID
COMMENT_REPLY    = 'comment reply'      #RID
COMMENT_USERNAME = 'comment username'   #RID
COMMENT_CONTENT  = 'comment content'    #RID


# Create Post
CREATE_POST_TITLE = 'Create Post Title'                                                     #RID
CREATE_POST_NEXT = 'Next'                                                                   #AID
CREATE_POST_POST_TO = 'Post to'                                                             #AID
CREATE_POST_ADD_TAGS = 'Add tags & flair'                                                   #AID
CREATE_POST_POST = 'Post'                                                                   #AID
CREATE_POST_BODY = 'Create Post Body'                                                       #RID
CREATE_POST_ADD_LINK = 'add link'                                                           #AID
CREATE_POST_LINK_BODY = 'Insert Link'                                                       #RID
CREATE_POST_ADD_IMAGE = 'add image'                                                         #AID
CREATE_POST_IMAGE = 'com.google.android.providers.media.module:id/icon_thumbnail'           #RID
CREATE_POST_ADD_POLL = 'add poll'                                                           #AID
CREATE_POST_DURATION_POLL = 'Poll ends in 2 Day'                                            #AID
CREATE_POST_DURATION_POLL_5 = '5 Day'                                                       #AID
CREATE_POST_DURATION_POLL_NEW = 'Poll ends in 5 Day'                                        #AID
CREATE_POST_POLL_OPTION_1 = 'Option 1'                                                      #RID
CREATE_POST_POLL_OPTION_2 = 'Option 2'                                                      #RID
CREATE_POST_POLL_ADD_OPTION = 'Add option'                                                  #AID
CREATE_POST_POLL_OPTION_3 = 'Option 3'                                                      #RID
CREATE_POST_CLOSE_POLL_3 = 'close option 3'                                                 #AID
