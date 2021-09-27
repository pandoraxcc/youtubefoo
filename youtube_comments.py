from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

# Path to the execution file of webdriver
current_path = os.getcwd()
full_path = current_path + "\chromedriver.exe"


class ParserYoutube:
  
    def __init__(self, web_adress, full_path, comment_type = "neutral"):

        """
            Initialize fucntion:
            web_adress - target video
            full_path - adress to driver your executable
            TODO:
                comment_type - filter comments by emotional state
        """

        self.web_adress = web_adress
        self.comment_type = comment_type
        self.full_path = full_path
        self.browser = webdriver.Chrome(executable_path = self.full_path)

    
    def load_all_comments(self):

        """
        Load all comments first. XHR didn't seem to work, rendering via webdriver 
        """
        self.browser.get(web_adress)
        self.browser.maximize_window()
        time.sleep(4)
        
        try:
            comments = self.browser.find_element_by_xpath('//*[@id="comments"]')
        
        except NoSuchElementException:

            print("bad luck pal, next time. no comments")
            self.browser.quit()
        
        self.browser.execute_script("arguments[0].scrollIntoView();", comments)
        time.sleep(4)

        max_scroll = self.browser.execute_script("return document.documentElement.scrollHeight")
        
        
        while True:
            
            self.browser = execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_scroll = self.browser.execute_script("return document.documentElement.scrollHeight")

            if new_scroll == max_scroll:
                print("Got them. Loaded all comments. Starting scraping...")
                break

    def get_comments(self):
        
        """
        Saving all the comments on the page
        """

        try:

            comments = self.browser.find_elements_by_xpath('//*[@id="content-text"]')

        except NoSuchElementException:
            
            print("Oops, something went wrong. Can't grab comments. Quitting")
            self.browser.quit()
        
        return comments

    def get_user(self):

        """
        Single responsibility. Getting the author.
        """

        try:

            users = self.browser.find_elements_by_xpath('//*[@id="author-text"]')

        except NoSuchElementException:

            print("Oops, something went wrong. Can't grab comments. Quitting")
            self.browser.quit()
        
        return users

        
class ResultAnalyzer:
    
    def __init__(self, elements):
        self.elements = elements

    def count_elements(self):
        pass

# No comments
#https://www.youtube.com/watch?v=6JhVo2zS8hU


parser1 = ParserYoutube("https://www.youtube.com/watch?v=6JhVo2zS8hU", full_path)

parser1.load_all_comments()
comments_all = parser1.get_comments() 
users_all = parser1.get_user 
print(comments_all)


