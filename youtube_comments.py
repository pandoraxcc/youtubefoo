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
        
        
   def load_all_comments(self):

          self.browser.get(self.web_adress)
          self.browser.maximize_window()
          time.sleep(3)
          # We need to locate the comment sector in order to render it
          target_section = self.browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments')
          self.browser.execute_script("arguments[0].scrollIntoView();", target_section)
          time.sleep(4)

          # Check if the comments are off:
          try:
              is_off_path = self.browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-message-renderer/yt-formatted-string[1]/span').text
              for x in range(5):
                  print("\n")
                  print("\n")
                  print("Comments are off. closing the windows")
              self.browser.quit()
          except NoSuchElementException:
              pass
        
  def scroll_down(self):
          # Get scroll height.
          max_height = self.browser.execute_script("return document.body.scrollHeight")

          while True:

              # Scroll down to the bottom.
              self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
              max_height = self.browser.execute_script("return document.documentElement.scrollHeight")
              # Wait to load the page.
              time.sleep(2)

              # Calculate new scroll height and compare with last scroll height.
              new_height = self.browser.execute_script("return document.documentElement.scrollHeight")

              if new_height == max_height:
                  break

              max_height = new_height

    def get_all_comments(self):
        
        comments_lst = []
        #comments = self.browser.find_elements_by_xpath('//*[@id="content-text"]')
        comments = self.browser.find_elements_by_css_selector("#content-text")
        for comment in comments:
            comments_lst.append(comment.text)
            print(comment.text)
            #print("\n")
        #print(len(comments))
        
        return comments_lst

   def get_user_ids(self):

        user_prof = []
        user_chn = []
        users = self.browser.find_elements_by_css_selector('#author-text > span')
        for user in users:
            user_prof.append(user.text)
            #print(user.text)

        users_channel = self.browser.find_elements_by_css_selector('#author-text')
        for channel in users_channel:
            user_chn.append(channel.get_attribute('href'))
            print(channel.get_attribute('href'))

        
        return user_prof, user_chn


    def save_data(self):

        profile_names, urls_final = self.get_user_ids()
        comments_final = self.get_all_comments()
        rows_final = zip(profile_names, urls_final, comments_final)

        return rows_final
      
      
      
    def write_csv_report(self):

        header_row = ['profile_names', 'profile_url', 'comments']
        rows_final = self.save_data()
        

        with open('results_youtube.csv', 'w', encoding = 'utf-8', newline='') as f:
            writer = csv.writer(f)
            # write the header
            writer.writerow(header_row)
            # write multiple rows
            writer.writerows(rows_final)

            
parser1 = ParserYoutube("https://www.youtube.com/watch?v=eK0pO79YkvY", full_path)
parser1.load_all_comments()
parser1.scroll_down()
parser1.save_data()
parser1.write_csv_report()
            
            
