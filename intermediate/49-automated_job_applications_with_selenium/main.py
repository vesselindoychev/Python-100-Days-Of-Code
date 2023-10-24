import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

email = os.environ['LINKEDIN_EMAIL']
password = os.environ['LINKEDIN_PASSWORD']

linkedin_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3733302930&f_AL=true&geoId=105333783&keywords=python%20entry&location=Bulgaria&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=linkedin_url)

# time.sleep(2)
#
cookie_btns = driver.find_elements(By.CSS_SELECTOR, value='.artdeco-global-alert-action__wrapper button')
cookie_reject = cookie_btns[1]
cookie_reject.send_keys(Keys.ENTER)

# time.sleep(2)
nav_btns = driver.find_elements(By.CSS_SELECTOR, value='header nav div a')
sign_in_btn = nav_btns[1]
sign_in_btn.click()

# time.sleep(5)

email_input = driver.find_element(By.ID, value='username')
email_input.send_keys(email)

password_input = driver.find_element(By.ID, value='password')
password_input.send_keys(password)

confirm_sign_in_btn = driver.find_element(By.CSS_SELECTOR, value='.login__form_action_container button')
confirm_sign_in_btn.send_keys(Keys.ENTER)

time.sleep(5)
all_job_ads = driver.find_elements(By.CSS_SELECTOR, value='.job-card-container--clickable')
for job in all_job_ads:
    job.click()
    time.sleep(2)
    save_job_btn = driver.find_element(By.CLASS_NAME, value='jobs-save-button')
    save_job_btn.send_keys(Keys.ENTER)
