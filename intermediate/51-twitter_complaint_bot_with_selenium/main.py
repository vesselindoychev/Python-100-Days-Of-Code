import time

from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv(verbose=True)

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option('detach', True)

CHROME_DRIVER_PATH = os.environ['CHROME_DRIVER_PATH']

PROMISED_DOWNLOAD = os.environ['PROMISED_DOWNLOAD']
PROMISED_UPLOAD = os.environ['PROMISE_UPLOAD']
TWITTER_EMAIL = os.environ['TWITTER_EMAIL']
TWITTER_PASSWORD = os.environ['TWITTER_PASSWORD']


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.service = webdriver.ChromeService(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=CHROME_OPTIONS)
        self.upload = 0
        self.download = 0

    def get_internet_speed(self):
        url = 'https://www.speedtest.net'
        self.driver.get(url=url)

        time.sleep(2)
        accept_cookie_btn = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        accept_cookie_btn.click()

        time.sleep(1)
        go_btn = self.driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()

        time.sleep(43)
        self.download = self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.upload = self.driver.find_element(By.XPATH,
                                               '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(self.download)
        print(self.upload)

    def tweet_at_provider(self):
        twitter_url = 'https://twitter.com'
        self.driver.get(url=twitter_url)

        time.sleep(1)
        sign_in_button = self.driver.find_element(By.XPATH,
                                                  '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in_button.click()

        time.sleep(2)
        email_input = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

        email_input.send_keys(TWITTER_EMAIL)

        time.sleep(1)
        next_btn = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_btn.click()

        time.sleep(1)
        password_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)

        login_btn = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_btn.click()

        time.sleep(2)
        make_post_btn = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        make_post_btn.click()

        text_area = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div')
        text_area.send_keys(
            f'Hi Vivacom, why is my internet speed {self.download} download/{self.upload} upload when i pay for {PROMISED_DOWNLOAD} download/{PROMISED_UPLOAD} upload?')

        upload_post_btn = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
        upload_post_btn.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
