import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv(verbose=True)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.environ['STOCK_API_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']

stock_url = 'https://www.alphavantage.co/query'
news_url = 'https://newsapi.org/v2/everything'

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'IBM',
    # 'interval': '5min',
    'apikey': STOCK_API_KEY,
}

news_parameters = {
    'q': 'tesla',
    'from': '2023-09-10',
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API_KEY
}

stock_response = requests.get(url=stock_url, params=stock_parameters)
stock_data = stock_response.json()['Time Series (Daily)']
print(stock_data)

news_response = requests.get(url=news_url, params=news_parameters)
news_data = news_response.json()
print(news_data)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
