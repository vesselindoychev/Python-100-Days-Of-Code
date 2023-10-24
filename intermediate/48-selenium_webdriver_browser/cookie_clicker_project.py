import time
from selenium import webdriver
from selenium.webdriver.common.by import By


cookie_game_url = 'https://orteil.dashnet.org/experiments/cookie'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url=cookie_game_url)

cookie = driver.find_element(By.ID, value='cookie')
products = driver.find_elements(By.CSS_SELECTOR, value='#store div')[0:8]
product_ids = [p.get_attribute('id') for p in products]

timeout = time.time() + 60 * 5
five_sec_window = time.time() + 5 * 1
while True:
    cookie.click()

    if time.time() > five_sec_window:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')[0: 8]
        item_prices = []

        for price in all_prices:
            cost = int(price.text.split(' - ')[1].replace(',', ''))
            item_prices.append(cost)

        cookie_upgrades = {}

        for i in range(len(item_prices)):
            cookie_upgrades[item_prices[i]] = product_ids[i]

        money = int(driver.find_element(By.ID, value='money').text.replace(',', ''))

        affordable_upgrades = {}

        for cost, id in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = id

        highest_price_upgrade = max(affordable_upgrades)
        print(highest_price_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_upgrade]

        driver.find_element(By.ID, value=to_purchase_id).click()

        five_sec_window = time.time() + 5 * 1

    if time.time() > timeout:
        cookies_per_sec = driver.find_element(By.ID, value='cps').text
        print(cookies_per_sec)
        break
