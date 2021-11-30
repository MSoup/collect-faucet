import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# These options makes python not complain about errors about random Chromium settings
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Selenium should search for Chrome in my default path (where chrome normally gets installed)
driver = webdriver.Chrome(options=options)

driver.get('http://www.google.com/')

# Let the user actually see something!
time.sleep(2) 

search_box = driver.find_element(by="name", value='q')

search_box.send_keys('ChromeDriver')

search_box.submit()

# Let the user actually see something!
time.sleep(3) 

driver.quit()
