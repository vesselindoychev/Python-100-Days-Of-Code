import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv(verbose=True)

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option('detach', True)

CHROME_DRIVER_PATH = os.environ['CHROME_DRIVER_PATH2']
INSTAGRAM_EMAIL = os.environ['INSTAGRAM_EMAIL']
INSTAGRAM_PASSWORD = os.environ['INSTAGRAM_PASSWORD']


class InstaFollower:
    def __init__(self, chrome_driver_path):
        self.service = webdriver.ChromeService(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=CHROME_OPTIONS)

    def login(self):
        login_url = 'https://www.instagram.com/accounts/login/'
        self.driver.get(url=login_url)

        time.sleep(2)
        allow_cookies_btn = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        allow_cookies_btn.click()

        email_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

        email_input.send_keys(INSTAGRAM_EMAIL)
        password_input.send_keys(INSTAGRAM_PASSWORD)

        time.sleep(1)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()

    def find_followers(self):
        pass
    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
