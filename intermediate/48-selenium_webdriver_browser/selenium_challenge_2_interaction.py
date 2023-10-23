from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://en.wikipedia.org/wiki/Main_Page'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)

articles_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')

print(articles_count.text)
# articles_count.click()

# view_source = driver.find_element(By.LINK_TEXT, value='View source')
# view_source.click()

# search = driver.find_element(By.NAME, value='search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)


# driver.quit()