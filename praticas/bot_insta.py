# BOT usando Selenium -  faz login no instagram

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from time import sleep

class InstagramBot:
    def __init__(self, username, password): 
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
    
    def login(self): 
        driver = self.driver
        driver.get('https://www.instagram.com')
        sleep(5)

        username_element = driver.find_element(By.NAME, 'username')
        username_element.clear()
        sleep(1)
        username_element.send_keys(self.username)
        sleep(1)
        password_element = driver.find_element(By.NAME, 'password')
        password_element.clear()
        password_element.send_keys(self.password)
        #password_element.send_keys(Keys.ENTER)

InstagramBot('kalebe', 'kalebe').login()