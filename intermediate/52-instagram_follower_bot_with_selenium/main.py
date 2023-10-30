import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

load_dotenv(verbose=True)

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option('detach', True)

CHROME_DRIVER_PATH = os.environ['CHROME_DRIVER_PATH2']
INSTAGRAM_EMAIL = os.environ['INSTAGRAM_EMAIL']
INSTAGRAM_PASSWORD = os.environ['INSTAGRAM_PASSWORD']
ACCOUNT_TO_SEARCH = os.environ['SIMILAR_ACCOUNT']


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
        time.sleep(2)
        search_btn = self.driver.find_element(By.XPATH,
                                              '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a')
        search_btn.click()

        time.sleep(2)
        search_text_area = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/input')
        search_text_area.send_keys(ACCOUNT_TO_SEARCH)

        time.sleep(2)

        first_searched_user_link = self.driver.find_element(By.XPATH,
                                                            '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a')
        first_searched_user_link.click()

        time.sleep(3)
        view_followers_btn = self.driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        view_followers_btn.click()

        time.sleep(2)

    def follow(self):
        popup_window = self.driver.find_element(By.XPATH,
                                                '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        followers_list = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div')
        while True:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       popup_window)
            time.sleep(1)
            btns = followers_list.find_elements(By.TAG_NAME, value='button')
            follow_btns = [btn for btn in btns if btn.find_element(By.CSS_SELECTOR, value='div div').text == 'Follow']
            for btn in follow_btns:
                print(btn.text)
                btn.click()
                time.sleep(1)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
