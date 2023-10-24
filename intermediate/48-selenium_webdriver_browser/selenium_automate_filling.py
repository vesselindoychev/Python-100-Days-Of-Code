from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'http://secure-retreat-92358.herokuapp.com'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)

first_name_input = driver.find_element(By.NAME, value='fName')
last_name_input = driver.find_element(By.NAME, value='lName')
email_input = driver.find_element(By.NAME, value='email')
button = driver.find_element(By.TAG_NAME, value='button')

first_name_input.send_keys('Ivan')
last_name_input.send_keys('Ivanov')
email_input.send_keys('ivanivanov123@abv.bg')
button.send_keys(Keys.ENTER)