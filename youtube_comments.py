from selenium import webdriver
import time
import os
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

# Path to the execution file of webdriver
current_path = os.getcwd()
full_path = current_path + "\chromedriver.exe"


class ParserYoutube:
  
    def __init__(self, web_adress, full_path):

        """
            Initialize fucntion:
            web_adress - target video
            full_path - adress to driver your executable
            TODO:
            comment_type - filter comments by emotional state
        """

        self.web_adress = web_adress
        self.full_path = full_path
        self.browser = webdriver.Chrome(executable_path = self.full_path)
