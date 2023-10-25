import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)


tinder_url = 'https://tinder.com'

EMAIL = os.environ['FACEBOOK_EMAIL']
PASSWORD = os.environ['FACEBOOK_PASSWORD']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=tinder_url)

time.sleep(2)
a_tag = driver.find_element(By.XPATH, '//*[@id="s1166637769"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
a_tag.click()

time.sleep(2)
login_link = driver.find_element(By.XPATH, '//*[@id="s-561743307"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
login_link.send_keys(Keys.ENTER)

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

allow_cookies_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[2]')
allow_cookies_btn.send_keys(Keys.ENTER)

time.sleep(2)
email_input = driver.find_element(By.ID, value='email')
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.ID, value='pass')
password_input.send_keys(PASSWORD)

facebook_login_btn = driver.find_element(By.NAME, value='login')
facebook_login_btn.click()


#
# facebook_login_link = driver.find_element(By.XPATH, value='//*[@id="s-561743307"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
# print(facebook_login_link.get_attribute('aria-label'))
# facebook_login_link.click()
