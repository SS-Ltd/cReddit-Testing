'''
This file contains all the paths for the web tests.
'''
# Comments
COMMENT_CONTENT = ""
COMMENT_DOWNVOTE = "_downvote_comment"
COMMENT_UPVOTE = "upvote_comment"
COMMENT_REPLY = ""
COMMENT_OPTIONS = ""
COMMENT_USERNAME = ""
COMMENT_VOTES = '<span class="text-gray-300 text-sm">'
POST_COMMENTS = "_comment"
COMMENT_CREATE = "add_comment"
COMMENT_WRITE = "comment_text"
COMMENT_CANCEL = "cancel_comment"
COMMENT_COMMENT = "submit_comment"
COMMENT_EDIT = ""
COMMENT_SAVE = "_save"
COMMENT_GET_REPLY_NOTIFICATIONS =""
COMMENT_COPY_TEXT = ""
COMMENT_COLAPSE_THREAD = ""
COMMENT_REPORT = ""
COMMENT_BLOCK_ACCOUNT = ""
COMMENT_SHARE = "_share_comment"
COMMENT_UNSAVE = "_save"
COMMENT_DELETE = ""
# Right Side Bar
RIGHT_SIDE_BAR_CLEAR = "recent_posts_clear"
RIGHT_SIDE_BAR_COMMUNITY_NAME = "_community_recent"
RIGHT_SIDE_BAR_POST_TITLE = "_post_header"

# Profile Page
PROFILE_USERNAME = '//*[@id="root"]/div/div[3]/div/div[3]/div/div[1]/div[1]/div/p'                                  # xpath
PROFILE_MAINFEED_CATEGORY_DROPDOWN = 'mainfeed_category_dropdown'                                                   # id
PROFILE_MAINFEED_CATEGORY_HOT = 'mainfeed_category_hot'                                                             # id
PROFILE_MAINFEED_CATEGORY_NEW = 'mainfeed_category_new'                                                             # id
PROFILE_MAINFEED_CATEGORY_TOP = 'mainfeed_category_top'                                                             # id
PROFILE_FEED = 'profile-buttons-row'                                                                                # id
PROFILE_FIRST_COMMENT = '//*[@id="mainfeed"]/div[3]/div[1]/div/p[1]'                                                # xpath
PROFILE_FOLLOW = 'follow-btn-usercard'                                                                              # id
PROFILE_CHAT = 'chat-btn-usercard'                                                                                  # id
PROFILE_USER_DROPDOWN = 'users-drop-menu-down'                                                                      # id
PROFILE_USER_DROPDOWN_SHARE = '//*[@id="root"]/div/div[3]/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div[1]'   # xpath
PROFILE_USER_DROPDOWN_SEND = '//*[@id="root"]/div/div[3]/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div[2]'    # xpath
PROFILE_USER_DROPDOWN_BLOCK = '//*[@id="root"]/div/div[3]/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div[3]'   # xpath
PROFILE_USER_DROPDOWN_REPORT = '//*[@id="root"]/div/div[3]/div/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div[4]'  # xpath