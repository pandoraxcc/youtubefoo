from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

print(os.getcwd())
class ParserYoutube:

    def __init__(self, web_adress, comment_type = "neutral"):
        # sending the adress of the web page 
        self.web_adress = web_adress
        self.comment_type = comment_type
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\Dmitrii\Desktop\scraping\chromedriver.exe')

    def scan_page_for_comments(self):
        no_comments = "Comments are turned off"
        
        try:
            self.browser.get(self.web_adress)
            comments = self.browser.find_element_by_css_selector("#guide").text
            
            if  no_comments in comments:
                self.browser.quit()
                return print("No comments on the page. Quitting")
            
            else:
                print("There are comments on the page")
                self.browser.quit()
        
        except Exception as e:
            print(f"failed to get {self.web_adress} \n")
            print(e)
            

        
    def scrape_all_comments(self):
        pass

    def get_user_id(self):
        pass


class ResultAnalyzer:
    
    def __init__(self, elements):
        self.elements = elements

    def count_elements(self):
        pass

test_1 = ParserYoutube("https://www.youtube.com/watch?v=6JhVo2zS8hU")
test_1.scan_page_for_comments()