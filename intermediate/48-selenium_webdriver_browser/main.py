from selenium import webdriver
from selenium.webdriver.common.by import By

product_url = 'https://www.amazon.com/Nike-Romaleos-Training-White-Black/dp/B01FZ3H4TQ/ref=sr_1_13?crid=RWB8BXT454CN&keywords=adidas%2Bpowerlift%2Bshoes&qid=1697802294&sprefix=adidas%2Bpowerlift%2Bshoe%2Caps%2C186&sr=8-13&th=1&psc=1'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(product_url)

price_dollars = driver.find_element(By.CLASS_NAME, value='a-price-whole')
price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
print(f"The price is {price_dollars.text}.{price_cents.text}")
#
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR, value='.doc-widget a')

bug_link = driver.find_element(By.XPATH, value='//*[@id="bylineInfo"]')
print(bug_link.text)
# driver.close()
driver.quit()