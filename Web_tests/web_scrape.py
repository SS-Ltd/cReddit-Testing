"""
This script is used to scrape the web for posts. 
"""

import json
from random import randrange as rand
from pynput.keyboard import Controller, Key
from selenium.webdriver.common.keys import Keys
import requests
from emoji import emojize
from my_imports import (
    WebDriverWait,
    EC,
    By,
    TimeoutException,
    thread,
    webdriver,
    ChromeDriverManager,
    ChromeService,
)
from selenium.webdriver import ActionChains
import shutil

def return_random_username():
    '''
    This function returns a random username
    '''
    x = rand(0, 10, 1)

    if x==0:
        return "RadiantSamurai"
    elif x==1:#fake2@email.com
        return "TheCursedOne"
    elif x==2:
        return "TheLastUchiha"
    elif x==3:
        return "lvl100MafiaBoss"
    elif x==4:
        return "lvl1Crook"
    elif x==5:
        return "NoManLeftBehind"
    elif x==6:
        return "LegendaryWarrior"
    elif x==7:
        return "UnmatchedProdigy"
    elif x==8:
        return "Herokiller123"
    elif x==9:
        return "TheRizzler"

def locate_element(driver, *, by_id=None, by_xpath=None, by_classname=None) -> WebDriverWait:
    '''
    This function is used to locate an element
    '''
    try:
        if by_id:
            return WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.ID, by_id))
                )
        if by_xpath:
            return WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, by_xpath))
                )
        if by_classname:
            return WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, by_classname))
                )
    except TimeoutException:
        return None
    return None


def write_to_file(data, file_path):
    """
    This function writes the data to the file
    :param data: the data to write to the file
    :param file_path: the path to the file
    :return: None
    """
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(data)
        file.write("\n")

def download_vid(driver,i)->str:
    '''
    This function downloads the video from the post
    '''
    vid = locate_element(driver, by_xpath='//*[contains(@id, "'+ POST_VIDEO_ID +'")]')
    child = vid.find_elements(By.XPATH, './/shreddit-async-loader/media-telemetry-observer/*')
    try:
        src = child[1].get_attribute('src')
    except Exception as e:
        src = child[0].get_attribute('src')

    response = requests.get(src , stream=True)
    with open(FOLDER_PATH + 'vid'+str(i)+'.mp4', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        return 'vid'+str(i)+'.mp4'

def download_img(driver,i)->str:
    '''
    This function downloads the image from the post
    '''
    img = locate_element(driver, by_xpath='//*[contains(@id, "'+ POST_IMAGE_ID +'")]')
    src = img.get_attribute('src')
    print(src)
    response = requests.get(src , stream=True)
    with open(FOLDER_PATH+'img'+str(i)+'.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        return 'img'+str(i)+'.png'

def random_login(driver):
    '''
    This function logs in with a random username
    '''
    driver.get("https://creddit.tech/")
    thread.sleep(5)
    if locate_element(driver, by_id="navbar_profile") is not None:
        logout(driver)
        driver.get("https://creddit.tech/")
    thread.sleep(7)
    locate_element(driver, by_id="navbar_login_button").click()
    username = return_random_username()
    password = PASSWORD
    locate_element(driver, by_id="login_username").clear()
    locate_element(driver, by_id="login_username").send_keys(username)
    locate_element(driver, by_id="login_password").clear()
    locate_element(driver, by_id="login_password").send_keys(password)
    locate_element(driver, by_id="login_submit").click()
    thread.sleep(4)

def logout(driver):
    '''
    This function logs out
    '''
    locate_element(driver, by_id="navbar_profile").click()
    thread.sleep(1)
    locate_element(driver, by_id="profile_logout").click()
    thread.sleep(1)

def choose_community(driver):
    '''
    This function chooses the community
    '''
    thread.sleep(1)
    community1 = locate_element(driver, by_xpath='//*[@id="create_post_community_dropdown_menu"]/ul[2]/li[1]/div')
    community2 = locate_element(driver, by_xpath='//*[@id="create_post_community_dropdown_menu"]/ul[2]/li[2]/div')
    community3 = locate_element(driver, by_xpath='//*[@id="create_post_community_dropdown_menu"]/ul[2]/li[3]/div')

    community1_name = community1.find_elements(By.TAG_NAME, 'h1')[0].text
    if SUBREDDIT_NAME in community1_name:
        community1.click()
        return

    community2_name = community2.find_elements(By.TAG_NAME, 'h1')[0].text
    if SUBREDDIT_NAME in community2_name:
        community2.click()
        return

    community3_name = community3.find_elements(By.TAG_NAME, 'h1')[0].text
    if SUBREDDIT_NAME in community3_name:
        community3.click()
        return

    print("Community not found")

def post_text(driver,post_title,post_text)->str:
    '''
    This function logs in with the given username
    '''
    random_login(driver)
    locate_element(driver, by_id='navbar_create_post').click()
    thread.sleep(3)
    locate_element(driver, by_id='create_post_community_dropdown_button').click()
    thread.sleep(1)
    choose_community(driver)
    title_element = locate_element(driver, by_id='post_title').find_element(By.XPATH, './*')
    send_non_bmp_characters(title_element,post_title)
    thread.sleep(1)
    text_element = locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div')
    send_non_bmp_characters(text_element,post_text)
    thread.sleep(1)
    locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div[1]/div[3]/div[3]/div').click()
    thread.sleep(3)
    WebDriverWait(driver, 700).until(EC.url_contains(SUBREDDIT_NAME))
    driverlink = driver.current_url
    thread.sleep(1)
    logout(driver)
    return driverlink

def remove_non_bmp_characters(text):
    return ''.join(c for c in text if c <= '\uffff')

def send_non_bmp_characters(text_element,text):
    '''
    This function sends non bmp characters to the text element
    '''
    escaped_text = json.dumps(text)[1:-1].replace("'", "\\'")
    driver.execute_script("arguments[0].innerHTML = '{}'".format(escaped_text),text_element)
    thread.sleep(1)
    text_element .send_keys('.')
    text_element .send_keys(Keys.BACKSPACE)

def post_photo(driver,post_title,postpath)->str:
    '''
    This function logs in with the given username
    '''
    random_login(driver)
    locate_element(driver, by_id='navbar_create_post').click()
    thread.sleep(3)
    locate_element(driver, by_id='create_post_community_dropdown_button').click()
    thread.sleep(1)
    choose_community(driver)
    thread.sleep(1)
    title_element = locate_element(driver, by_id='post_title').find_element(By.XPATH, './*')
    send_non_bmp_characters(title_element,post_title)
    thread.sleep(1)
    locate_element(driver, by_id='type_image').click()
    thread.sleep(1)
    locate_element(driver, by_id='post_drop_image').click()
    thread.sleep(3)
    keyboard = Controller()
    thread.sleep(1)

    keyboard.type(
        'C:\\Users\\husse\\OneDrive\\Desktop\\college\\Senior-1\\Semister_2\\Software\\Posts_scraped\\'+postpath)
    thread.sleep(3)
    keyboard.press(Key.enter)
    thread.sleep(1)
    keyboard.release(Key.enter)
    thread.sleep(1)
    locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div[1]/div[3]/div[3]/div').click()
    print("post Photo/Video being uploaded")
    WebDriverWait(driver, 700).until(EC.url_contains(SUBREDDIT_NAME))
    thread.sleep(3)
    driverlink = driver.current_url
    thread.sleep(1)
    logout(driver)
    return driverlink

def comment_on_post(driver,postlink,comment,commentscount):
    '''
    This function logs in with the given username
    '''
    for i in range(commentscount):
        random_login(driver)
        thread.sleep(5)
        driver.get(postlink)
        thread.sleep(7)
        locate_element(driver, by_id="add_comment").click()
        thread.sleep(2)
        locate_element(driver,by_xpath='//*[contains(@id, "_upvote")]'"").click()
        text_element = locate_element(driver, by_id="comment_text")
        send_non_bmp_characters(text_element,comment[i])
        thread.sleep(2)
        locate_element(driver, by_id="submit_comment").click()
        thread.sleep(2)
        logout(driver)

PASSWORD = "12345678Mm"
TIME = "1 D"
SUBREDDIT = "https://www.reddit.com/r/apexlegends/"
SUBREDDIT_NAME = "apexlegends"
POST_ID = "t3_"
POST_TITLE_ID = "post-title-t3_"
POST_TEXT_ID = "post-rtjson-content"
POST_COMMENTS_ID = "-comment-rtjson-content"
POST_IMAGE_ID = "post-image"
POST_VIDEO_ID = 'aspect-ratio'
VOTES_PATH = "faceplate-number"
TREE_DOTS_PATH = "shreddit-post-overflow-menu//div/faceplate-dropdown-menu/button"
MAX_NUM_POSTS = 200
FOLDER_PATH = "../../../../Posts_scraped/"
REDDIT_URL = "https://www.reddit.com"
SKIP = 2
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
thread.sleep(2)
driver.get(SUBREDDIT)
thread.sleep(5)

#sorting by new
#dropdowns = driver.find_element(By.XPATH ,"//shreddit-sort-dropdown[contains(.,'Open sort options')]")
#dropdowns.click()
#locate_element(driver, by_xpath="//a[contains(@href, '/r/"+SUBREDDIT_NAME+"/new/')]").click()

action = ActionChains(driver)
thread.sleep(5)


#expanding the page
driver.execute_script("window.scrollBy(0, 10000)")
thread.sleep(4)
#driver.execute_script("window.scrollBy(0, -10000)")
#thread.sleep(10)
#driver.execute_script("window.scrollBy(0, 10000000)")
#thread.sleep(5)
#driver.execute_script("window.scrollBy(0, 10000000)")
#thread.sleep(5)
#driver.execute_script("window.scrollBy(0, 10000000)")
#thread.sleep(5)
#driver.execute_script("window.scrollBy(0, 10000000)")
#thread.sleep(5)
#driver.execute_script("window.scrollBy(0, 10000000)")
#thread.sleep(5)
driver.execute_script("window.scrollBy(0, -5000000)")
thread.sleep(15)
#getting the posts links
get_source = driver.page_source
posts_url = [0]*MAX_NUM_POSTS
link = [0]*MAX_NUM_POSTS
search_post_link = '<a slot="full-post-link" class="absolute inset-0" href="'
for i in range(MAX_NUM_POSTS):
    posts_url[i] = get_source.find(search_post_link, posts_url[i-1]+1)
    if posts_url[i] == -1:
        print("posts =",i)
        break
    print(posts_url[i])
    temp = get_source[posts_url[i] + len(search_post_link):]
    link[i] = temp[:temp.find('"')]
    print(link[i])
empty = link.count(0)
print("Done with getting the links posts",MAX_NUM_POSTS-empty)
data = ""
thread.sleep(5)
# posts = []
# posts = driver.find_elements(By.XPATH, '//*[contains(@id, "'+ POST_ID +'")]')
# number_of_post = len(posts)
# number_of_post = min(MAX_NUM_POSTS,int(number_of_post/3))
i = SKIP-1
#looping through the posts and scraping the data from them then posting them to creddit
for j in range (MAX_NUM_POSTS):
    i += 1
    type = ""
    try:

        print(link[i])
        print(REDDIT_URL+link[i])
        driver.get(REDDIT_URL+link[i])
        thread.sleep(2)
        if driver.current_url != REDDIT_URL+link[i]:
            continue
    except Exception as e:
        continue
    data = "Post: "
    try:
        post_title= locate_element(driver, by_xpath='//*[contains(@id, "'+ POST_TITLE_ID +'")]').text
    except Exception as e:
        print(e)
        continue
    data += post_title
    data += " Post content: "
    if locate_element(driver, by_xpath='//*[contains(@id, "'+ POST_IMAGE_ID +'")]'):#if there is an image
        data += "Image: "
        image_path = download_img(driver,i)
        type = "image"
    elif locate_element(driver, by_xpath='//*[contains(@id, "'+ POST_VIDEO_ID +'")]'):#if there is a video
        data += "Video: "
        vid_path = download_vid(driver,i)
        type = "video"
    elif locate_element(driver, by_xpath='//*[contains(@id, "'+ POST_TEXT_ID +'")]'):#if there is text
        data += "Text: "
        post_body = locate_element(driver, by_xpath='//*[contains(@id, "'+ POST_TEXT_ID +'")]').text
        data += post_body
        type = "text"

    data += " comments: "
    comments = [""]*20
    commentelements = driver.find_elements(By.XPATH, '//*[contains(@id, "'+ POST_COMMENTS_ID +'")]')
    for k in range(min(rand(6,20),len(commentelements))):
        comments[k] = commentelements[k].text
        data += "[comment]" + str(k) +" "+ str(comments[k])
    write_to_file(data, FOLDER_PATH + "posts.txt")
    #thread.sleep(2000)
    try:
        #POST TO CREDDIT
        if type == "text":
            newlink = post_text(driver, post_title,post_body)
        elif type == "image":
            newlink = post_photo(driver, post_title,image_path)
        elif type == "video":
            newlink = post_photo(driver, post_title,vid_path)
        print("link is:")
        print(newlink)
   
        countempty = comments.count("")
        comment_on_post(driver,newlink,comments,len(comments)-countempty)
        for j in range(len(comments)):
            comments[j] = ""
    except Exception:
        continue

    print("Done with post",i)
    thread.sleep(7)
