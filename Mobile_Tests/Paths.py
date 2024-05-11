'''
This module contains all the xPaths and accessibility IDs for the mobile application.
'''
# RID = Resource ID
# XPATH = Xpath
# AID = Accessibility ID
# end of text button
ALLOW_NOTIFICATIONS = 'com.android.permissioncontroller:id/permission_allow_button'     #RID
# Starting page for the mobile application
START_USERNAME = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]'
START_PASSWORD = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]'
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
SIGNUP_USERNAME = 'signup_username_field'               #RID
SIGNUP_CONTINUE2 = 'Continue'                           #AID#might need to update this
SIGNUP_GENDER_MAN = 'Man'                               #AID
#signup continue with google
SIGNUP_CONTINUE_WITH_GOOGLE = 'Continue with Google'    #AID

# Home page
SEARCH_ICON = 'Open search'                                 #RID
SEARCH_TEXT = 'search text'                                 #RID
SEARCH_SEARCH_FOR = 'Search for'                            #AID
SEARCH_RESULT = 'join or disjoin subreddit'                 #RID
SEARCH_COMMUNNITY = 'Communities\nTab 2 of 5'               #AID

# Custom Navigation Bar
NAVIGATION_BAR_HOME = 'Home\nTab 1 of 5'                #AID
NAVIGATION_BAR_COMMUNITIES = 'Communities Tab 2 of 5'   #AID
NAVIGATION_BAR_CREATE_POST = 'Create\nTab 3 of 5'       #AID
NAVIGATION_BAR_CHAT = 'Chat Tab 4 of 5'                 #AID
NAVIGATION_BAR_INBOX = 'Inbox Tab 5 of 5'               #AID

# Profile Icon
HOME_PAGE_PROFILE_ICON = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[4]'

# Within Profile Window
PROFILE_WINDOW_PROFILE = 'My Profile'
PROFILE_WINDOW_CREATE_COMMUNITY = 'Create a Community'  #AID
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
PROFILE_PAGE_BACK = 'Back'                      #AID
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
CREATE_COMMUNITY_TYPE_PRIVATE = 'Private\nOnly approved users can view and submit to this community.'
CREATE_COMMUNITY_TYPE_PRIVATE_DESC = 'Only approved users can view and submit to this community.'   #AID
CREATE_COMMUNITY_18   = '18+ Community' #RID
CREATE_COMMUNITY_BUTTON = 'Create Community'#AID
CREATE_COMMUNITY_BACK = 'Back'          #AID
CREATE_COMMUNITY_ALREADY_EXISTS = 'Subreddit already exists'    #AID
# posts all resource IDS except stated
POST_UPVOTE      = 'post upvote'                #RID
POST_VOTES       = 'post votes'                 #RID        # Might not work
POST_DOWNVOTE    = 'post downvote'              #RID
POST_COMMENTS    = 'post comment'               #RID
POST_USERNAME    = 'post username'              #RID        # POST USERNAME and POST SUBREDDIT together form the some reason
POST_SUBREDDIT   = 'post subreddit'             #RID        # Might not work
POST_TITLE       = 'post title'                 #RID
POST_SHARE       = 'post share'                 #RID
POST_MODERATOR   = 'moderator post settings'    #RID
# moderator post Card
POST_MOD_APPROVE_POST         = 'Approve post'  #RID
POST_MOD_REMOVE_POST          = 'Remove post'   #RID
POST_MOD_REMOVE_AS_SPAM       = 'Remove as spam'#RID
POST_MOD_LOCK_COMMENTS        = 'Lock comments' #RID
POST_MOD_STICKY_POST          = 'Sticky post'   #RID out of scope for project
POST_MOD_MARK_AS_SPOILER      = 'Mark as spoiler'#RID
POST_MOD_MARK_AS_NSFW         = 'Mark as NSFW'   #RID
POST_MOD_ADJUST_CROUD_CONTROL = 'Adjust Croud Control' #RID out of scope for project

# Comments all resource IDS
COMMENT_UPVOTE   = 'comment upvote'             #RID
COMMENT_VOTES    = 'comment votes'              #RID        # Might not work
COMMENT_DOWNVOTE = 'comment downvote'           #RID
COMMENT_OPTIONS  = 'comment options'            #RID
COMMENT_REPLY    = 'comment reply'              #RID
COMMENT_USERNAME = 'comment username'           #RID
COMMENT_CONTENT  = 'comment content'            #RID
COMMENT_CREATE   = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View'             #XPath
COMMENT_WRITE    = '//android.widget.EditText'
COMMENT_POST = 'Post'                   #AID
#AIDS
COMMENT_EDIT    = 'Edit comment'                            #AID
COMMENT_SHARE   = 'Share'                                   #AID
COMMENT_SAVE    = 'Save'                                    #AID
COMMENT_UNSAVE  = 'Unsave'                                  #AID
COMMENT_GET_REPLY_NOTIFICATIONS = 'Get reply notifications' #AID
COMMENT_COPY_TEXT = 'Copy text'                             #AID
COMMENT_COLAPSE_THREAD = 'Collapse thread'                  #AID
COMMENT_BLOCK_ACCOUNT = 'Block account'                     #AID
COMMENT_REPORT  = 'Report'                                  #AID
COMMENT_DELETE  = 'Delete comment'                          #AID


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

# Moderation
COMMUNITY_MOD_TOOLS = 'Mod Tools'                                                           #AID
# Moderator Tools
# General
MOD_TOOLS_MOD_LOG = 'Mod log'                                    #AID
MOD_TOOLS_INSIGHTS = 'Insights'                                  #AID
MOD_TOOLS_COMMUNITY_ICON = 'Community icon'                      #AID
MOD_TOOLS_DESCRIPTION = 'Description'                            #AID
MOD_TOOLS_WELCOME_MESSAGE = 'Welcome message'                    #AID
MOD_TOOLS_TOPICS = 'Topics'                                      #AID
MOD_TOOLS_COMMUNITY_TYPE = 'Community type'                      #AID
MOD_TOOLS_POST_TYPE = 'Post type'                                #AID
MOD_TOOLS_LOCATION = 'Location'                                  #AID
# Content & Regulations
MOD_TOOLS_QUEUES = 'Queues'                                      #AID
MOD_TOOLS_RULES = 'Rules'                                        #AID
MOD_TOOLS_SCHEDULED_POSTS = 'Scheduled posts'                    #AID
# User Management
MOD_TOOLS_MODERATORS = 'Moderators'                              #AID
MOD_TOOLS_APPROVED_USERS = 'Approved users'                      #AID
MOD_TOOLS_MUTED_USERS = 'Muted users'                            #AID
MOD_TOOLS_BANNED_USERS = 'Banned users'                          #AID

# Moderator Tools -> General -> Description
MOD_TOOLS_DESCRIPTION_EDIT = '//android.widget.EditText'         #XPath
MOD_TOOLS_DESCRIPTION_SAVE = 'Save'                              #AID

# Moderator Tools -> General -> Community Type
MOD_TOOLS_COMMUNITY_TYPE_SEEKBAR = 'android.widget.SeekBar'      #classname
MOD_TOOLS_COMMUNITY_TYPE_PUBLIC = 'Public'                       #AID
MOD_TOOLS_COMMUNITY_TYPE_RESTRICTED = 'Restricted'               #AID
MOD_TOOLS_COMMUNITY_TYPE_PRIVATE = 'Private'                     #AID
MOD_TOOLS_COMMUNITY_TYPE_SWITCH = 'android.widget.Switch'        #classname
MOD_TOOLS_COMMUNITY_TYPE_SAVE = 'Save'                           #AID

# Moderator Tools -> General -> Post Type
MOD_TOOLS_POST_TYPE_OPTIONS_ANY = 'Post type options\nChoose the types of posts you allow in your community\nAny'                                                                                               #AID
MOD_TOOLS_POST_TYPE_OPTIONS_LINK = 'Post type options\nChoose the types of posts you allow in your community\nLink'                                                                                             #AID
MOD_TOOLS_POST_TYPE_OPTIONS_TEXT = 'Post type options\nChoose the types of posts you allow in your community\nText'                                                                                             #AID
MOD_TOOLS_POST_TYPE_SAVE = 'Save'                                                                                                                                                                               #AID
OPTION_ANY = 'Any\nAllow text, link, image, and video posts'                                                                                                                                                    #AID
OPTION_LINK = 'Link only\nOnly allow link posts'                                                                                                                                                                     #AID
OPTION_TEXT = 'Text only\nOnly allow text posts'                                                                                                                                                                     #AID
IMAGE_POSTS = 'Image posts\nAllow images uploaded directly to Reddit as well as links to popular image hosting sites such as lmgur'                                                                             #AID
IMAGE_SWITCH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Switch[1]'    #XPath
VIDEO_POSTS = 'Video posts\nAllow videos uploaded directly to Reddit'                                                                                                                                           #AID
VIDEO_SWITCH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Switch[2]'    #XPath
POLL_POSTS = 'Poll posts\nAllow poll posts in your community'                                                                                                                                                   #AID
POLL_SWITCH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Switch[3]'     #XPath
POLL_ONLY_SWITCH = 'android.widget.Switch'                                                                                                                                                                      #classname

# Moderator Tools -> General -> Location
LOCATION_TEXT = 'android.widget.EditText'                                                                                                                                                                       #classname
LOCATION_HEADER = 'Adding a location helps your community show up in search results and recommendations and helps local redditors find it easier.'                                                              #AID
LOCATION_SAVE = 'save'                                                                                                                                                                                          #AID

# Moderator Tools -> Content & Regulations -> Queues
QUEUES_COMMUNITY = 'Community'
QUEUES_NEEDS_REVIEW = 'Needs Review'
QUEUES_POSTS_AND_COMMENTS = 'Posts and Comments'
QUEUES_SORT = 'sort'
QUEUES_GOTO_COMMUNITY = 'Go to community page'
QUEUES_REVIEW_NEEDS_REVIEW = 'Needs Review'
QUEUES_REVIEW_REMOVED = 'Removed'
QUEUES_REVIEW_REPORTED = 'Reported'
QUEUES_REVIEW_EDITED = 'Edited'
QUEUES_REVIEW_UNMODERATED = 'Unmoderated'
QUEUES_PAC_POSTS_AND_COMMENTS = 'Posts and Comments'
QUEUES_PAC_POSTS_ONLY = 'Posts Only'
QUEUES_PAC_COMMENTS_ONLY = 'Comments Only'

# Moderator Tools -> Content & Regulations -> Rules
RULES_ADD_RULE = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]'
RULES_EDIT_RULE = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[3]'
RULES_DONE_EDITING = 'Done'
RULES_DELETE_RULE = '//android.view.View[@content-desc="1\nBalbus cibus altus comburo."]/android.widget.Button'
RULES_RULE = '//android.view.View[@content-desc="1\nBalbus cibus altus comburo."]'
RULES_ADD_RULE_TITLE = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]'
RULES_ADD_RULE_DESCRIPTION = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]'
RULES_ADD_RULE_REPORT = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]'
RULES_ADD_RULE_PAC = 'Posts and comments'
RULES_ADD_RULE_CO = 'Only comments'
RULES_ADD_RULE_PO = 'Only posts'
RULES_ADD_RULE_SAVE = 'Save'

# Moderator Tools -> Content & Regulations -> Scheduled Posts
SCHEDULED_POSTS_SCHEDULE = 'Schedule post'
SCHEDULED_POSTS_MORE_OPTIONS = 'more options'
SCHEDULED_POSTS_CALENDAR = 'Post Settings\ncalender\nSchedule Post\nschedule post'
SCHEDULED_POSTS_SCHEDULE_POST = 'Schedule'
SCHEDULED_POSTS_TITLE = 'Create Post Title'

# Moderator Tools -> User Management -> Moderators
MOD_MODERATORS_ALL = 'All\nTab 1 of 2'
MOD_MODERATORS_EDITABLE = 'Editable\nTab 2 of 2'
MOD_MODERATORS_ADD_MODERATOR = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]'
MOD_MODERATORS_EDIT_MODERATOR = '(//android.view.View[@content-desc="cake"])[1]/android.widget.Button'
MOD_MODERATORS_EDIT_PERMISSIONS = 'Edit permissions'
MOD_MODERATORS_VIEW_PROFILE = 'View profile'
MOD_MODERATORS_REMOVE_MODERATOR = 'Remove'
MOD_MODERATORS_ADD_MODERATOR_USERNAME = '//android.widget.EditText'
MOD_MODERATORS_ADD_MODERATOR_FULL_PERMISSIONS = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[1]'
MOD_MODERATORS_ADD_MODERATOR_ACCESS = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[2]'
MOD_MODERATORS_ADD_MODERATOR_MAIL = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[3]'
MOD_MODERATORS_ADD_MODERATOR_CONFIG = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[4]'
MOD_MODERATORS_ADD_MODERATOR_POSTS = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[5]'
MOD_MODERATORS_ADD_MODERATOR_FLAIR = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[6]'
MOD_MODERATORS_ADD_MODERATOR_WIKI = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[7]'
MOD_MODERATORS_ADD_MODERATOR_CHAT_CONFIG = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[8]'
MOD_MODERATORS_ADD_MODERATOR_CHAT_OPERATOR = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[9]'
MOD_MODERATORS_ADD_MODERATOR_INVITE = 'Invite'
MOD_MODERATORS_ADD_MODERATOR_CANCEL = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'

# Moderator Tools -> User Management -> Approved Users
MOD_APPROVED_USERS_EDIT = '(//android.view.View[@content-desc="cake"])[1]/android.widget.Button'
MOD_APPROVED_USERS_EDIT_PERMISSIONS = 'Edit permissions'
MOD_APPROVED_USERS_VIEW_PROFILE = 'View profile'
MOD_APPROVED_USERS_REMOVE = 'Remove'
MOD_APPROVED_USERS_ADD_USER = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]'
MOD_APPROVED_USERS_ADD_USER_USERNAME = '//android.widget.EditText'
MOD_APPROVED_USERS_ADD_USER_ADD = 'Add'
MOD_APPROVED_USERS_ADD_USER_CLOSE = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'
