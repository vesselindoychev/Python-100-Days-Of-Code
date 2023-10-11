import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(verbose=True)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
sender_phone_number = os.environ['TWILIO_PHONE_NUMBER']
receiver_phone_number = os.environ['RECEIVER_PHONE_NUMBER']
client = Client(account_sid, auth_token)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.environ['STOCK_API_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']

stock_url = 'https://www.alphavantage.co/query'
news_url = 'https://newsapi.org/v2/everything'

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}

news_parameters = {
    'q': COMPANY_NAME,
    'apiKey': NEWS_API_KEY
}

stock_response = requests.get(url=stock_url, params=stock_parameters)
stock_data = stock_response.json()['Time Series (Daily)']

news_response = requests.get(url=news_url, params=news_parameters)
news_data = news_response.json()

news_articles = news_data['articles'][:3]

text = ''

counter = 0

closed_prices = []

for k, v in stock_data.items():
    if counter == 2:
        break

    closed_prices.append(v['4. close'])
    counter += 1

yesterday_closing_price = float(closed_prices[0])
day_before_yesterday_closing_price = float(closed_prices[1])

difference = yesterday_closing_price - day_before_yesterday_closing_price

diff_percent = (difference / yesterday_closing_price) * 100
print(difference)
print(diff_percent)
up_down = None

if difference > 0:
    up_down = '▲'
else:
    up_down = '▼'

for article in news_articles:
    text = f"{STOCK_NAME}: {up_down}{round(diff_percent)}%\n" \
           f"Headline: {article['title']}. ({STOCK_NAME})?\n" \
           f"Brief: {article['description']}\n"

    message = client.messages.create(
        body=text,
        from_=sender_phone_number,
        to=receiver_phone_number
    )
