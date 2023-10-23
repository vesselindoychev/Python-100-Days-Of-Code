import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

website_url = 'https://www.python.org'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(website_url)

dates = driver.find_elements(By.CSS_SELECTOR, value='.medium-widget.event-widget.last .shrubbery .menu li time')
events = driver.find_elements(By.CSS_SELECTOR, value='.medium-widget.event-widget.last .shrubbery .menu li a')

dates_list = []
events_list = []
upcoming_events = {}
for tag in dates:
    date = tag.get_attribute('datetime').split('T')[0]
    dates_list.append(date)

for tag2 in events:
    event_name = tag2.text
    events_list.append(event_name)


for i in range(len(dates_list)):
    upcoming_events[i] = {
        'time': dates_list[i],
        'name': events_list[i]
    }

print(upcoming_events)

driver.quit()
