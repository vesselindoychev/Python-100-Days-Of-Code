import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# service = Service(ChromeDriverManager().install())
tinder_url = 'https://tinder.com'

# chrome_driver_path = '/path/to/chromedriver'
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
#
# facebook_login_link = driver.find_element(By.XPATH, value='//*[@id="s-561743307"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
# print(facebook_login_link.get_attribute('aria-label'))
# facebook_login_link.click()
