# youtube comments parser

Scrapes comments from youtube page, user ids, names and channel ids. Saves results in csv. In order to make it work, install selenium library for your python. After that, check the chrome browser version, and download the chrome webdriver https://chromedriver.chromium.org/downloads

Include the path to the webdriver inside of the script, suggested that you move it to the same directory as the script. 

The version of the webdriver must be at least the same as your browser version or higher. 


This tool is just a demo showcase of the webdriver and selenium, showing that it can dynamically load elements on the full JS dependent website - Youtube. Now, that's not the most efficient way of getting yotuube data - API is much faster and cleaner. Hence, if for some reason you want to do it that way ( without using google enviroment and account ) - that's one of the possible solutions. In the same way other dynamic websites could be scraped, if you were not able to get the data through JS requests.
