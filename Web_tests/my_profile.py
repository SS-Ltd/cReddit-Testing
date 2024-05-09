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


def goto_subfeed(driver) -> None:
    '''
    This function tests the subfeed it is using
    '''
    
    saved = locate_element(driver, by_xpath=MY_PROFILE_SAVED)
    assert saved is not None, "saved subfeed not found"
    saved.click()
    print("Saved subfeed clicked")
    thread.sleep(DELAY_TIME)
    hidden = locate_element(driver, by_xpath=MY_PROFILE_HIDDEN)
    assert hidden is not None, "hidden subfeed not found"
    hidden.click()
    print("Hidden subfeed clicked")
    thread.sleep(DELAY_TIME)
    upvoted = locate_element(driver, by_xpath=MY_PROFILE_UPVOTED)
    assert upvoted is not None, "upvoted subfeed not found"
    upvoted.click()
    print("Upvoted subfeed clicked")
    thread.sleep(DELAY_TIME)
    downvoted = locate_element(driver, by_xpath=MY_PROFILE_DOWNVOTED)
    assert downvoted is not None, "downvoted subfeed not found"
    downvoted.click()
    print("Downvoted subfeed clicked")
    thread.sleep(DELAY_TIME)

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

def my_profile(driver) -> None:
    '''
    This function is supposed to test my Profile page.
    '''

    # Get a random post first
    post_url = random_post(driver)

    # Go to my profile page
    goto_myprofile(driver)
    print("Goto My Profile Page Successful!")

    # goto_subfeed(driver)
    # print("Goto Subfeeds successful")
    # test_overview(driver)

    # test_posts(driver)

    test_comments(driver)

    thread.sleep(DELAY_TIME)
