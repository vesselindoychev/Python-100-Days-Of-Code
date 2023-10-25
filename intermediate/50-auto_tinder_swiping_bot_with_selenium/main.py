from selenium import webdriver

tinder_url = 'https://tinder.com'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=tinder_url)

