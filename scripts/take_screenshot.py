from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

# Navigate to url
driver.get("http://www.example.com")

# Returns and base64 encoded string into image
driver.set_window_size(1024, 768)
driver.save_screenshot('./image.png')

driver.quit()