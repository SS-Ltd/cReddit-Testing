'''
This module will contain the tests for the search functionality of the mobile app.
'''

from my_imports import webdriver, thread
from helper_functions import locate_element
from constants import DELAY_TIME
from Paths import SEARCH_ICON, SEARCH_BAR
from Paths import SEARCH_AUTOFILL_COMMUNITY, SEARCH_AUTOFILL_PEOPLE
from Paths import SEARCH_COMMUNITY_HEADER, SEARCH_PEOPLE_HEADER

def send_keys_slowly(element, text, delay=0.5):
    for character in text:
        element.send_keys(character)
        thread.sleep(delay)

def autofill(driver: webdriver) -> None:
    '''
    This function will test the autofill functionality of the search bar.
    '''
    # Locate the search bar.
    search_bar = locate_element(driver, by_id=SEARCH_BAR)
    search_bar.click()
    send_keys_slowly(search_bar, "cha")
    thread.sleep(DELAY_TIME)
    print("Search bar clicked")

    # Locate the autofilled community
    search_autofill_community = locate_element(driver, by_accessibility_id=SEARCH_AUTOFILL_COMMUNITY)
    search_autofill_community.click()
    print("Autofilled community clicked")

    # Locate the community header
    search_community_header = locate_element(driver, by_xpath=SEARCH_COMMUNITY_HEADER)
    print("Community header located")
    print(search_community_header.get_attribute('content-desc'))
    assert search_community_header.get_attribute('content-desc') == "r/Chat_Community0", "Community header text is not as expected"

    driver.back()

    # Locate the autofilled people
    search_autofill_people = locate_element(driver, by_accessibility_id=SEARCH_AUTOFILL_PEOPLE)
    search_autofill_people.click()
    print("Autofilled people clicked")

    # Locate the people header
    search_people_header = locate_element(driver, by_xpath=SEARCH_PEOPLE_HEADER)
    print("People header located")
    print(search_people_header.get_attribute('content-desc'))
    assert search_people_header.get_attribute('content-desc') == "chat13", "People header text is not as expected"

def restart(driver: webdriver, text: str) -> None:
    '''
    Restarts
    '''

    driver.back()

    # Locate the search icon
    search_icon = locate_element(driver, by_accessibility_id=SEARCH_ICON)
    search_icon.click()
    print("Search icon clicked")

    # Locate the search bar
    search_bar = locate_element(driver, by_id=SEARCH_BAR)
    search_bar.click()
    search_bar.clear()
    send_keys_slowly(search_bar, text)
    thread.sleep(DELAY_TIME)
    print("Search bar clicked")

    # Locate the search button that contains accessibility id starting with 'Search for'
    search_for = locate_element(driver, by_xpath="//android.widget.Button[starts-with(@content-desc, 'Search for')]")
    search_for.click()
    print("Search for button clicked")
    thread.sleep(DELAY_TIME)

def tabs(driver: webdriver) -> None:
    '''
    This function will test the tabs in the search functionality of the mobile app.
    '''

    # Locate the search bar.
    search_bar = locate_element(driver, by_id=SEARCH_BAR)
    search_bar.click()
    send_keys_slowly(search_bar, "sadasd")
    thread.sleep(DELAY_TIME)
    print("Search bar clicked")

    # Locate the search button that contains accessibility id starting with 'Search for'
    search_for = locate_element(driver, by_xpath="//android.widget.Button[starts-with(@content-desc, 'Search for')]")
    search_for.click()
    print("Search for button clicked")
    thread.sleep(DELAY_TIME)

    # Locate the post
    post = locate_element(driver, by_accessibility_id='r/null\nsadasd\n1 upvotes  \n1 comments')
    # post.click()
    assert post is not None, "Post not displayed"
    print("Post clicked")
    thread.sleep(DELAY_TIME)

    restart(driver, "cha")

    # Locate the community tab
    community = locate_element(driver, by_accessibility_id='Communities\nTab 2 of 5')
    community.click()
    print("Community tab clicked")

    # Locate the community in the search results
    community = locate_element(driver, by_accessibility_id='Chat_Community0\n1 members\njoin or disjoin subreddit')
    assert community is not None, "Community not displayed"
    print("Community displayed")
    thread.sleep(DELAY_TIME)

    restart(driver, "bagarrab 7aga")

    # Locate the comments tab
    comments = locate_element(driver, by_accessibility_id='Comments\nTab 3 of 5')
    comments.click()
    print("Comments tab clicked")

    # Sort by new
    locate_element(driver, by_accessibility_id='Sort').click()
    locate_element(driver, by_accessibility_id='New').click()

    # Locate the comment in the search results
    comment = locate_element(driver, by_accessibility_id='u/chat0\nbagarrab 7aga\n1 upvotes')
    assert comment is not None, "Comment not displayed"
    print("Comment displayed")
    thread.sleep(DELAY_TIME)

    restart(driver, "chat13")

    # Locate the people tab
    people = locate_element(driver, by_accessibility_id='People\nTab 4 of 5')
    people.click()
    print("People tab clicked")

    # Locate the people in the search results
    people = locate_element(driver, by_accessibility_id='u/chat13')
    assert people is not None, "People not displayed"
    print("People displayed")
    thread.sleep(DELAY_TIME)

    restart(driver, "bagarrab el #")

    # Locate the hashtag tab
    # Swipe left to locate the hashtag tab
    driver.swipe(1200, 370, 300, 300)
    hashtag = locate_element(driver, by_accessibility_id='Hashtags\nTab 5 of 5')
    hashtag.click()
    print("Hashtag tab clicked")

    # Locate the hashtag in the search results
    hashtag = locate_element(driver, by_xpath='//android.widget.ImageView')
    assert hashtag is not None, "Hashtag not displayed"
    print("Hashtag displayed")
    thread.sleep(DELAY_TIME)



def search(driver: webdriver) -> None:
    '''
    This function will test the search functionality of the mobile app.
    '''

    # Locate the search icon.
    search_icon = locate_element(driver, by_accessibility_id=SEARCH_ICON)
    search_icon.click()
    print("Search icon clicked")

    # Check the autofill functionality
    # autofill(driver)

    # Check the tabs
    tabs(driver)
    
    print("Search functionality passed")
