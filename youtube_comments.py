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
        # sending the adress of the web page 
        self.web_adress = web_adress
        self.comment_type = comment_type
        self.full_path = full_path
        self.browser = webdriver.Chrome(executable_path = self.full_path)

    
    def scrape_all_comments(self):
        pass

    def get_user_id(self):
        pass


class ResultAnalyzer:
    
    def __init__(self, elements):
        self.elements = elements

    def count_elements(self):
        pass

# No comments
#https://www.youtube.com/watch?v=6JhVo2zS8hU

test_1 = ParserYoutube("https://www.youtube.com/watch?v=vyqSdJLVQgg", full_path)
test_1.scan_page_for_comments()