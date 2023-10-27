import os
from dotenv import load_dotenv
from selenium import webdriver

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option('detach', True)

CHROME_DRIVER_PATH = os.environ['CHROME_DRIVER_PATH']
INSTAGRAM_EMAIL = os.environ['INSTAGRAM_EMAIL']
INSTAGRAM_PASSWORD = os.environ['INSTAGRAM_PASSWORD']

load_dotenv(verbose=True)


class InstaFollower:
    def __init__(self, chrome_driver_path):
        self.service = webdriver.ChromeService(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=CHROME_OPTIONS)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass
