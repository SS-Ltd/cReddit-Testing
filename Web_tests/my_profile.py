'''
This Module is supposed to test my Profile page.
'''

from constants import DELAY_TIME, SITE_NAME
from my_imports import thread, By
from helper_functions import locate_element
from paths import MY_PROFILE_OVERVIEW, MY_PROFILE_POSTS, MY_PROFILE_COMMENTS
from paths import MY_PROFILE_SAVED, MY_PROFILE_HIDDEN
from paths import MY_PROFILE_UPVOTED, MY_PROFILE_DOWNVOTED
from paths import CREATE_POST_RANDOM_COMMUNITY, CREATE_POST_BODY

def goto_myprofile(driver) -> None:
    '''
    This function goes to the settings page from the homepage
    '''
    locate_element(driver, by_id="navbar_profile").click()

    locate_element(driver, by_id="profile_view").click()

    assert locate_element(driver, by_id='profile-header') is not None, 'Did not go to my profile page'

def test_overview(driver) -> None:
    '''
    This function tests the overview of the my profile page
    '''
    overview = locate_element(driver, by_xpath=MY_PROFILE_OVERVIEW)
    assert overview is not None, "Overview not found"
    overview.click()
    print("Overview clicked")
    thread.sleep(DELAY_TIME)

    # Check that the post is by this username
    text = locate_element(driver, by_xpath="//div[@id='overview']/div/div/div/p").text
    print(text)
    assert text in driver.current_url, "Not a post by this user"
    print("Post by this user")

def test_posts(driver) -> None:
    '''
    This function tests the posts of the my profile page
    '''

    # First create a post in a community with known text
    # Then go to my profile page
    # Then go to the posts subfeed
    # Then check if the post is there

    # Create a post
    redirect = locate_element(driver, by_xpath='//*[@id="view-profile"]/div/div[1]/div/main/div[3]/div/div/a')
    assert redirect is not None, "Redirect not found"
    redirect.click()
    thread.sleep(DELAY_TIME)

    # Check if the user is redirected to the create post page
    assert "submit" in driver.current_url, "Not in create post page"

    # Create a post
    # Choose a community to post in
    locate_element(driver, by_id='create_post_community_dropdown_button').click()
    thread.sleep(1)
    random = locate_element(driver, by_xpath=CREATE_POST_RANDOM_COMMUNITY)
    # random/div/h1[1].text
    text = locate_element(random, by_xpath='./div/h1[1]')
    print("Text = ", text)
    print(text.text)
    text = text.text
    random.click()
    thread.sleep(1)

    # Write the title of the post
    locate_element(driver, by_id='post_title').find_element(By.XPATH, './*').send_keys('Yarab yeb2a 4a88al')
    thread.sleep(1)

    locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div').send_keys('munich betewla3 ya reggalaaaaaaa')

    # Submit the post
    locate_element(driver, by_xpath='//*[@id="root"]/div/div[3]/div[1]/div[3]/div[3]/div').click()
    thread.sleep(DELAY_TIME)

    # Go to my profile page
    goto_myprofile(driver)

    # Go to the posts subfeed
    posts = locate_element(driver, by_xpath=MY_PROFILE_POSTS)
    assert posts is not None, "posts subfeed not found"
    posts.click()
    print("Posts subfeed clicked")
    thread.sleep(DELAY_TIME)

    # Check if the post is there
    post = locate_element(driver, by_xpath="//*[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('comment') + 1) = 'comment']")
    assert post is not None, "Post not found"
    # Check if it is indeed the same post
    print(post.text)
    # assert "Yarab yeb2a 4a88al" in post.text, "Post not found"

def test_comments(driver) -> None:
    '''
    This function tests the comments of the my profile page
    '''

    # Go to a certain post and comment there
    driver.get('https://creddit.tech/r/adasdasd/comments/663d0e0d8c0f4f2e53114667')
    thread.sleep(DELAY_TIME)

    text = locate_element(driver, by_id='add_comment')
    assert text is not None, "Add comment not found"
    text.click()
    text = locate_element(driver, by_id='comment_text')
    assert text is not None, "Comment text not found"
    text.send_keys("This is a comment")
    submit = locate_element(driver, by_id='submit_comment')
    assert submit is not None, "Submit comment not found"
    submit.click()
    thread.sleep(DELAY_TIME)

    goto_myprofile(driver)

    comments = locate_element(driver, by_xpath=MY_PROFILE_COMMENTS)
    assert comments is not None, "comments subfeed not found"
    comments.click()
    print("Comments subfeed clicked")
    thread.sleep(DELAY_TIME)

    text = locate_element(driver, by_xpath='//*[@id="comments"]/div[1]/div[2]/div[1]/p')
    assert text is not None, "Comment not found"
    print(text.text)
    assert "This is a comment" in text.text, "Comment not found"
    print("Comment found")

def test_saved(driver, post_url: str) -> None:
    '''
    This function checks the save posts functionality
    '''

    # Go to a certain post and save it
    driver.get(post_url)
    thread.sleep(DELAY_TIME)

    # Locate the menu button
    menu = locate_element(driver, by_xpath="//div[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('menu') + 1) = 'menu']")
    menu.click()
    print("Menu clicked")

    # Locate the save post button
    save_post = locate_element(driver, by_xpath="//div[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('menu_save') + 1) = 'menu_save']")
    save_post.click()
    print("Post saved")
    # Check that the post has been saved
    assert save_post.find_element(By.XPATH, './/p[contains(text(), "Unsave")]') is not None, "Post not saved"
    thread.sleep(DELAY_TIME)

    goto_myprofile(driver)

    saved = locate_element(driver, by_xpath=MY_PROFILE_SAVED)
    assert saved is not None, "saved subfeed not found"
    saved.click()
    print("Saved subfeed clicked")
    thread.sleep(DELAY_TIME)

    # Check if the post is there
    # Locate an element that contains mainfeed in its id
    post = locate_element(driver, by_xpath="//*[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('community') + 1) = 'community']")
    # Locate post/div/p and check that it is starts with "r/"
    post_a = locate_element(post, by_xpath=".//a/p")
    print(post_a.text)
    print(post_url)
    # assert post_a.text in post_url, "The post is incorrect"

def test_hidden(driver) -> None:
    '''
    This function tests the hidden functionality
    '''
    hidden = locate_element(driver, by_xpath=MY_PROFILE_HIDDEN)
    assert hidden is not None, "hidden subfeed not found"
    hidden.click()
    print("Hidden subfeed clicked")
    thread.sleep(DELAY_TIME)

    # Checks that there is an undo button
    undo = locate_element(driver, by_xpath="//*[starts-with(@id, 'undo-hide')]")
    assert undo is not None, "Undo button not found"
    print("Undo button found")
    undo.click()
    print("Undo button clicked")
    # Check that a post is now present
    post = locate_element(driver, by_xpath="//*[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('community') + 1) = 'community']")
    assert post is not None, "Post not found"
    print("Post found")

    print("Hidden subfeed test successful")

def test_upvoted(driver) -> None:
    '''
    This function tests the upvoted functionality
    '''
    upvoted = locate_element(driver, by_xpath=MY_PROFILE_UPVOTED)
    assert upvoted is not None, "upvoted subfeed not found"
    upvoted.click()
    print("Upvoted subfeed clicked")
    thread.sleep(DELAY_TIME)

    # Check that the upvote button is clicked
    upvote = locate_element(driver, by_xpath="//span[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('upvote') + 1) = 'upvote']")
    assert "hover:bg-opacity-30" in upvote.get_attribute("class"), "Upvote not clicked"

    print("Upvoted subfeed test successful")

    # goto_myprofile(driver)

def test_downvoted(driver) -> None:
    '''
    This function checks the downvoted functionality
    '''
    downvoted = locate_element(driver, by_xpath=MY_PROFILE_DOWNVOTED)
    assert downvoted is not None, "downvoted subfeed not found"
    downvoted.click()
    print("Downvoted subfeed clicked")
    thread.sleep(DELAY_TIME)

    # Check that the downvote button is clicked
    downvote = locate_element(driver, by_xpath="//span[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('downvote') + 1) = 'downvote']")
    assert "hover:bg-opacity-30" in downvote.get_attribute("class"), "Downvote css not changed"

    print("Downvoted subfeed test successful")

    # goto_myprofile(driver)

def random_post(driver) -> str:
    '''
    This function goes to a random post and returns the URL of that post to be used later
    '''
    # Click on a random post
    random = locate_element(driver, by_xpath="//*[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('comment') + 1) = 'comment']")
    random.click()
    print("Post clicked")
    thread.sleep(DELAY_TIME)

    # Check that you are indeed in a post page
    # Check if url contains the word 'comments'
    assert "comments" in driver.current_url, "Not in a post page"
    print("In a post page")

    return driver.current_url

def insert_picture(driver) -> None:
    '''
    This function takes you from my profile to settings to insert a picture
    '''

    redirect = locate_element(driver, by_xpath = "//div[@id='profile-header']/div/div/div/a")
    assert redirect is not None, "Redirect not found"
    redirect.click()
    thread.sleep(DELAY_TIME)

    # Check if the user is redirected to the settings page
    assert "settings" in driver.current_url, "Not in settings page"

    # Go back
    driver.back()

    redirect = locate_element(driver, by_xpath="//div[@id='right-sidebar']/div/div/div/div/a")
    assert redirect is not None, "Redirect not found"
    redirect.click()
    thread.sleep(DELAY_TIME)

    # Check if the user is redirected to the settings page
    assert "settings" in driver.current_url, "Not in settings page"

    # Go back
    driver.back()

def my_profile(driver) -> None:
    '''
    This function is supposed to test my Profile page.
    '''

    # Get a random post first
    # post_url = random_post(driver)

    # Go to my profile page
    goto_myprofile(driver)
    print("Goto My Profile Page Successful!")

    # goto_subfeed(driver)
    # print("Goto Subfeeds successful")
    # test_overview(driver)

    # test_posts(driver)

    # test_comments(driver, post_url)

    # test_saved(driver, post_url)

    # test_hidden(driver)

    # test_upvoted(driver)

    # test_downvoted(driver)

    # insert_picture(driver)

    locate_element(driver, by_xpath="//div[@id='right-sidebar']/div/div[2]/ul/li/div/span[2]/span/a/span/span").click()
    assert "settings" in driver.current_url, "Not in settings page"
    print("Redirect successful from right sidebar to settings page")
    driver.back()

    thread.sleep(DELAY_TIME)
