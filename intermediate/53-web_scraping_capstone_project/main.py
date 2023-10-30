import time

from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

load_dotenv(verbose=True)

CHROME_PATH = os.environ['CHROME_PATH']
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option('detach', True)

USER_AGENT = os.environ['USER_AGENT']
ACCEPT_LANG = os.environ['ACCEPT_LANGUAGE']

EMAIL = os.environ['GOOGLE_EMAIL']
PASSWORD = os.environ['GOOGLE_PASSWORD']

HEADERS = {
    'User-Agent': USER_AGENT,
    'Accept-Language': ACCEPT_LANG
}

GOOGLE_FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSd8CjnWW9V1lQhQl7G1zVh4lG2UoT8xwCDHTZfqXQi6gvo8MQ/viewform?usp=sf_link'
RENT_PROPERTY_LINK = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"north"%3A37.876713742767606%2C"east"%3A-122.2850135703125%2C"south"%3A37.67372983716383%2C"west"%3A-122.5816444296875%7D%2C"isMapVisible"%3Afalse%2C"filterState"%3A%7B"price"%3A%7B"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A3000%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%2C"regionSelection"%3A%5B%7B"regionId"%3A20330%2C"regionType"%3A6%7D%5D%2C"mapZoom"%3A12%7D'

RESPONSE = requests.get(url=RENT_PROPERTY_LINK, headers=HEADERS)
WEBPAGE_TEXT = RESPONSE.text

PROPERTY_CLASS = 'ListItem-c11n-8-84-3__sc-10e22w8-0'


class FindProperty:
    def __init__(self, chrome_path):
        self.service = webdriver.ChromeService(executable_path=chrome_path)
        self.driver = webdriver.Chrome(options=CHROME_OPTIONS, service=self.service)
        self.soup = BeautifulSoup(WEBPAGE_TEXT, 'lxml')
        self.prices = []
        self.links = []
        self.addresses = []
        self.property_items = []

    def get_all_properties(self):
        li_items = self.soup.select(selector='.result-list-container ul li')

        for i in li_items:
            attributes = i.attrs
            if 'class' in attributes:
                if i.attrs['class'][0] == PROPERTY_CLASS:
                    self.property_items.append(i)

    def get_links_of_property_ads(self):
        main_url = 'https://www.zillow.com'
        all_property_a_tags = self.soup.find_all(name='a', class_='property-card-link')
        for prop_a in range(0, len(all_property_a_tags) - 1, 2):
            prop_link = all_property_a_tags[prop_a].get('href').split(':')[0]
            if prop_link == 'https':
                link = all_property_a_tags[prop_a].get('href')
            else:
                link = main_url + all_property_a_tags[prop_a].get('href')
            self.links.append(link)

    def get_all_property_prices(self):
        all_prices = self.soup.select('[data-test=property-card-price]')
        for p in all_prices:
            if '+' in p.text:
                price = p.text.split('+')
            else:
                price = p.text.split('/')
            self.prices.append(price[0])

    def get_all_property_addresses(self):
        all_addresses = self.soup.select('[data-test=property-card-addr]')
        for addr in all_addresses:
            if '|' in addr.text:
                address = addr.text.split('|')[1]
            else:
                address = addr.text
            self.addresses.append(address)

    def make_google_form(self):
        self.driver.get(GOOGLE_FORM_LINK)

        time.sleep(2)

        for i in range(len(self.prices)):
            if i != 0:
                send_another_answer_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                send_another_answer_btn.click()
                time.sleep(3)
            address_input = self.driver.find_element(By.XPATH,
                                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH,
                                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

            address_input.send_keys(self.addresses[i])
            price_input.send_keys(self.prices[i])
            link_input.send_keys(self.links[i])

            send_form_btn = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            send_form_btn.click()
            time.sleep(4)

        self.driver.quit()


find_property = FindProperty(CHROME_PATH)
find_property.get_all_properties()
find_property.get_links_of_property_ads()
find_property.get_all_property_prices()
find_property.get_all_property_addresses()
find_property.make_google_form()
