'''
This file contains all the paths for the web tests.
'''
#ID = ID
#PID = Partial ID
#XPATH = Xpath

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

# Left Side Bar
LEFT_SIDE_BAR_HOME = "sidebar_home"                                                                                 # id
LEFT_SIDE_BAR_POPULAR = 'sidebar_popular'                                                                           # id
LEFT_SIDE_BAR_ALL = 'sidebar_all'                                                                                   # id
LEFT_SIDE_BAR_RECENT = 'sidebar_recent'                                                                             # id
LEFT_SIDE_BAR_RECENT_COMMUNITY = 'sidebar_recent_icon0'                                                             # id
LEFT_SIDE_BAR_RECENT_COMMUNITY_TEXT = '//*[@id="sidebar_recent_icon0"]/span[2]'                                     # xpath
LEFT_SIDE_BAR_COMMUNITY = 'sidebar_communities'                                                                     # id
LEFT_SIDE_BAR_CREATE_COMMUNITY = "(//button[@id='sidebar-create-community-icon'])[2]"                               # xpath
LEFT_SIDE_BAR_CREATE_COMMUNITY_CARD = 'community-card'                                                              # id
LEFT_SIDE_BAR_CREATE_COMMUNITY_ALREADY_EXISTS = '//*[@id="card-content"]/div[1]/p'                                  # xpath
LEFT_SIDE_BAR_COMMUNITY_RANDOM = "(//a[@id='sidebar_community_icon0'])[2]"                                          # xpath

# Other User Profile Page
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

# My Profile Page
MY_PROFILE_OVERVIEW = "//div[@id='view-profile']/div/div/div/main/div[2]/a/span/span/span"                    # xpath
MY_PROFILE_POSTS = "//div[@id='view-profile']/div/div/div/main/div[2]/a[2]/span/span/span"                    # xpath
MY_PROFILE_COMMENTS = "//div[@id='view-profile']/div/div/div/main/div[2]/a[3]/span/span/span"                 # xpath
MY_PROFILE_SAVED = "//div[@id='view-profile']/div/div/div/main/div[2]/a[4]/span/span/span"                    # xpath
MY_PROFILE_HIDDEN = "//div[@id='view-profile']/div/div/div/main/div[2]/a[5]/span/span/span"                   # xpath
MY_PROFILE_UPVOTED = "//div[@id='view-profile']/div/div/div/main/div[2]/a[6]/span/span/span"                  # xpath
MY_PROFILE_DOWNVOTED = "//div[@id='view-profile']/div/div/div/main/div[2]/a[7]/span/span/span"                # xpath

# Create Post
CREATE_POST_RANDOM_COMMUNITY = '//*[@id="create_post_community_dropdown_menu"]/ul[2]/li[1]/div'                     # xpath
CREATE_POST_BODY = '//*[@id="root"]/div/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div'               # xpath

# Settings
SETTINGS_PRIVACY_ADD_BLOCKED_USERS = '//*[@id="root"]/div/div[4]/div[3]/div/div[2]/div[1]/button'                   # xpath

# Searching
SEARCH_BAR = "navbar_searchbar_input"                                                                                #ID
SEARCH_POSTS = "posts_option"
SEARCH_COMMUNITIES = "communities_option"
SEARCH_COMMENTS = "comments_option"
SEARCH_PEOPLE = "people_option"
SEARCH_HASHTAGS = "hashtag_option"
SEARCH_SAFE = "ismature_switch_btn_search"
SEARCH_SORT_BY = "sort_options"
SEARCH_SORT_HOT = "search_hot"
SEARCH_SORT_NEW = "search_new"
SEARCH_SORT_TOP = "search_top"
SEARCH_FILTER_TIME = "sort_time"
SEARCH_FILTER_TIME_ALL_TIME = "search_all_time"
SEARCH_FILTER_TIME_YEAR = "search_past_year"
SEARCH_FILTER_TIME_MONTH = "search_past_month"
SEARCH_FILTER_TIME_WEEK = "search_past_week"
SEARCH_FILTER_TIME_TODAY = "search_past_24_hours"
SEARCH_FILTER_TIME_NOW = "search_past_hour"
SEARCH_CONTENT_MAP = "search_content_map"

# Chats
NAVBAR_CHAT = 'navbar_chat'                                                                                         # id
LANDING_CREATE_CHANNEL = 'landing-creat-channel'                                                                    # id
ADD_CHAT = 'add-chat'                                                                                               # id
CHAT_SEARCHBAR_INPUT = 'chat_searchbar_input'                                                                       # id
CHAT_GROUP_INPUT = 'chat_groupname_input'                                                                           # id
CHAT_SEARCHBAR_USER = 'search-user-row-0'                                                                           # id
CHAT_CREATE_CHAT = 'btn-creat-channel'                                                                              # id
CHAT_INPUT_TEXT = "//div[@id='root']/div/div[2]/div[2]/div/div[4]/div/div/div/div[2]"                               # xpath
CHAT_SEND_MESSAGE="#send-message-icon > path"                                                                       # CSS

# Moderation
MODERATION_TAB  = '//*[@id="root"]/div/div[3]/div/div[1]/div/div[4]/div/div'                                        # xpath
MOD_QUEUES      = 'mod_queues'                                                                                      # ID
MOD_QUEUES_REPORTED = '//*[@id="mod_content"]/div[1]/div[2]/div[1]'                                                 # xpath
MOD_QUEUES_EDITED = '//*[@id="mod_content"]/div[1]/div[2]/div[2]'                                                   # xpath
#MOD_QUEUES_DELETED = '//*[@id="mod_content"]/div[1]/div[2]/div[3]'                                                  # xpath
MOD_QUEUES_UNMODERATED = '//*[@id="mod_content"]/div[1]/div[2]/div[3]'                                              # xpaths
MOD_QUEUES_OPTIONS_LIST = "options_list"                                                                            # ID
MOD_USER_MANAGMENT = 'user_management'                                                                              # ID
MOD_USER_MANAGMENT_BANNED = 'user_management_Banned'                                                                # ID
MOD_USER_MANAGMENT_APPROVED = '//*[@id="mod_content"]/div[1]/div[2]/div[1]/div[2]/h1'                               # xpath
MOD_USER_MANAGMENT_MODERATORS = 'user_management_moderators'                                                        # ID
MOD_USER_MANAGMENT_BANNED_UNBAN = '//*[@id="mapped_mod_user_managemenet"]/div[1]/div/div[3]/button'                 # xpaths
MOD_USER_MANAGMENT_BANNED_EDIT = '//*[@id="mapped_mod_user_managemenet"]/div[1]/div/div[2]/button'                  # xpath
MOD_USER_MANAGMENT_BANNED_EDIT_REASON = '//*[@id="ban_modal_content"]/div[2]/select'                                # xpath
MOD_USER_MANAGMENT_BANNED_EDIT_NOTE ='//*[@id="ban_modal_content"]/div[2]/input'                                    # xpath
MOD_USER_MANAGMENT_BANNED_EDIT_DAYS = '//*[@id="ban_modal_content"]/div[2]/div[1]/input'                            # xpath
MOD_USER_MANAGMENT_BANNED_EDIT_PERMENANT ='//*[@id="ban_duration"]'                                             # xpath
MOD_USER_MANAGMENT_BANNED_EDIT_CANCEL = '//*[@id="ban_modal_content"]/div[2]/div[2]/div[1]'                         # xpath
MOD_USER_MANAGMENT_BANNED_EDIT_CONFIRM = '//*[@id="ban_modal_content"]/div[2]/div[2]/div[2]'                        # xpath
MOD_USER_MANAGMENT_BANNED_BAN_USER = 'ban_user'                                                                     # ID
MOD_USER_MANAGMENT_BANNED_BAN_USER_USER = 'username'                                                                # ID
MOD_USER_MANAGMENT_BANNED_BAN_USER_REASON = '//*[@id="ban_modal_content"]/div[2]/select'                            # xpath
MOD_USER_MANAGMENT_BANNED_BAN_USER_NOTE = 'modNote'                                                                 # ID
MOD_USER_MANAGMENT_BANNED_BAN_USER_DAYS = 'ban_duration_input'                                                      # ID
MOD_USER_MANAGMENT_BANNED_BAN_USER_PERMENANT = '//*[@id="ban_permenant"]'                                           # xpath
MOD_USER_MANAGMENT_BANNED_BAN_USER_CANCEL = 'cancel_ban'                                                            # ID
MOD_USER_MANAGMENT_BANNED_BAN_USER_CONFIRM = 'submit_ban'                                                           # ID
MOD_USER_MANAGMENT_APPROVE_USER = '//*[@id="approve_user"]/h1'                                                      # xpath
MOD_USER_MANAGMENT_APPROVE_USER_USERNAME = 'username'                                                               # ID
MOD_USER_MANAGMENT_APPROVE_USER_CANCEL = '//*[@id="approve_modal_content"]/div[2]/div/div[1]/h1'                    # xpath
MOD_USER_MANAGMENT_APPROVE_USER_APPROVE = '//*[@id="approve_modal_content"]/div[2]/div/div[2]/h1'                   # xpath
MOD_USER_MANAGMENT_APPROVED_REMOVE = '//*[@id="mapped_mod_user_managemenet"]/div[1]/div/div[2]/button'              # xpath
MOD_SCHEDULED_POST = 'scheduled_posts'                                                                              # ID
MOD_EXIT_MOD_TOOLS = 'exit_mod'                                                                                     # ID
MOD_MAPPED_MOD = 'mapped_mod'                                                                                       # ID
MOD_MAPPED_USERS = 'mapped_mod_user_managemenet'                                                                    # ID

# Messages
NOTIFICATIONS = 'navbar_bell'                                                                                       # id
MESSAGES = '//*[@id="root"]/div/div[1]/header/div/div[3]/div[2]/div[2]/div[2]/div[1]/a'                             # xpath
MESSAGES_ALL = '//*[@id="message"]/div[1]/div/div[2]/div/div/ul/li[1]'                                              # xpath
MESSAGES_UNREAD = '//*[@id="message"]/div[1]/div/div[2]/div/div/ul/li[2]'                                           # xpath
MESSAGES_UNREAD_ITEMS = 'unread'                                                                                    # id
MESSAGES_MESSAGES = '//*[@id="message"]/div[1]/div/div[2]/div/div/ul/li[3]'                                         # xpath
MESSAGES_MESSAGES_ITEMS = 'messages'                                                                                      # id
MESSAGES_POST_REPLIES = '//*[@id="message"]/div[1]/div/div[2]/div/div/ul/li[4]'                                     # xpath
MESSAGES_POST_REPLIES_ITEMS = 'post-replies'                                                                              # id
MESSAGES_USERNAME_MENTIONS = '//*[@id="message"]/div[1]/div/div[2]/div/div/ul/li[5]'                                # xpath
MESSAGES_USERNAME_MENTIONS_ITEMS = 'username-mentions'                                                                    # id
MESSAGES_INBOX_ITEMS = 'inbox'                                                                                      # id
MESSAGES_COMPOSE = '//*[@id="message"]/div[1]/div/div/div/ul/li[1]/a'                                               # xpath
MESSAGES_COMPOSE_USERNAME = '//*[@id="compose"]/div/div/form/div[1]/div/input'                                      # xpath
MESSAGES_COMPOSE_SUBJECT = '//*[@id="compose"]/div/div/form/div[2]/div/input'                                       # xpath
MESSAGES_COMPOSE_MESSAGE = '//*[@id="compose"]/div/div/form/div[3]/div/div/div/div[1]/textarea'                     # xpath
MESSAGES_COMPOSE_SEND = '//*[@id="compose"]/div/div/form/button'                                                    # xpath
MESSAGES_INBOX = '//*[@id="message"]/div[1]/div/div[1]/div/ul/li[2]/a'                                              # xpath
MESSAGES_SENT = '//*[@id="message"]/div[1]/div/div[1]/div/ul/li[3]/a'                                               # xpath
