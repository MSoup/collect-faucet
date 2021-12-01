from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

class Gitlab():
    def __init__(self):
        load_dotenv()
        try:
            self.GITLAB_URL = os.getenv("GITLAB_URL")
            self.USER = os.getenv("EMAIL")
            self.PW = os.getenv("PW")
        except:
            return "Could not get env variables to log in"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get(self.GITLAB_URL)

        user_form = self.driver.find_element(By.ID, 'user_login')
        pw_form = self.driver.find_element(By.ID, 'user_password')

        user_form.send_keys(self.USER)
        pw_form.send_keys(self.PW)
        pw_form.submit()