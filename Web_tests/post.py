'''
This module tests the posts functionality
'''

from my_imports import thread, By
from constants import DELAY_TIME
from helper_functions import locate_element

def post(driver) -> None:
    '''
    This function tests the post interactions
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

    # Locate the upvote button
    upvote = locate_element(driver, by_xpath="//span[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('upvote') + 1) = 'upvote']")
    print(upvote.get_attribute("class"))
    upvote.click()
    print(upvote.get_attribute("class"))
    print("Upvoted")
    thread.sleep(DELAY_TIME)

    # Refresh the page
    driver.refresh()

    # Check that the css of the upvote button has changed
    upvote = locate_element(driver, by_xpath="//span[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('upvote') + 1) = 'upvote']")
    assert "hover:bg-opacity-30" in upvote.get_attribute("class"), "Upvote css not changed"

    # Locate the downvote button
    downvote = locate_element(driver, by_xpath="//span[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('downvote') + 1) = 'downvote']")
    print(downvote.get_attribute("class"))
    downvote.click()
    print(downvote.get_attribute("class"))
    print("Downvoted")
    thread.sleep(DELAY_TIME)

    # Refresh the page
    driver.refresh()

    # Check that the css of the downvote button has changed
    downvote = locate_element(driver, by_xpath="//span[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('downvote') + 1) = 'downvote']")
    assert "hover:bg-opacity-30" in downvote.get_attribute("class"), "Downvote css not changed"

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

    # Refresh the page
    driver.refresh()

    # Check that the post has been saved
    menu = locate_element(driver, by_xpath="//div[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('menu') + 1) = 'menu']")
    menu.click()
    print("Menu clicked")
    save_post = locate_element(driver, by_xpath="//div[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('menu_save') + 1) = 'menu_save']")
    assert save_post.find_element(By.XPATH, './/p[contains(text(), "Unsave")]') is not None, "Post not saved"

    # Click on the hide post button
    hide_post = locate_element(driver, by_xpath="//div[starts-with(@id, 'mainfeed') and substring(@id, string-length(@id) - string-length('menu_hide') + 1) = 'menu_hide']")
    hide_post.click()
    print("Post hidden")
    thread.sleep(DELAY_TIME)
    # Check for undo hide button
    undo_hide = locate_element(driver, by_xpath="//button[starts-with(@id, 'undo-hide')]")
    assert undo_hide is not None, "Post not hidden"

    # Refresh the page
    driver.refresh()

    # Check that the post has been hidden
    undo_hide = locate_element(driver, by_xpath="//button[starts-with(@id, 'undo-hide')]")
    assert undo_hide is not None, "Post not hidden"
    undo_hide.click()
    print("Undo hide clicked")
    thread.sleep(DELAY_TIME)

    print("Post interactions successful")
