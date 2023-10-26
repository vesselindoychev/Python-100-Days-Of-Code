import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
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
tinder_login_btn = driver.find_element(By.XPATH,
                            '//*[@id="q-637390230"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
tinder_login_btn.click()

time.sleep(2)
login_with_facebook_btn = driver.find_element(By.XPATH,
                                 '//*[@id="q1929195990"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
login_with_facebook_btn.send_keys(Keys.ENTER)

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

time.sleep(6)
driver.switch_to.window(base_window)
print(driver.title)

tinder_cookie_btn = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/button')
tinder_cookie_btn.click()

time.sleep(3)
tinder_share_location_btn = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
tinder_share_location_btn.click()

time.sleep(3)
disable_notifications_btn = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]')
disable_notifications_btn.click()

time.sleep(2)
like_btn = driver.find_element(By.XPATH, '//*[@id="q-637390230"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
for i in range(100):
    time.sleep(3)
    try:
        like_btn.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.XPATH, '//*[@id="q-307019029"]/main/div/div[1]/div/div[4]/button')
            match_popup.click()
        except:
            reject_tinder_home_screen_btn = driver.find_element(By.XPATH, '//*[@id="q1929195990"]/main/div/div[2]/button[2]')
            reject_tinder_home_screen_btn.click()
            time.sleep(2)

    except:
        close_btn = driver.find_element(By.XPATH, '//*[@id="s-561743307"]/main/div/div[2]/button')
        close_btn.click()
        break
driver.quit()

driver.quit()
