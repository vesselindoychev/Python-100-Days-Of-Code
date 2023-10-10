import os
from twilio.rest import Client
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
sender_phone = os.environ['TWILIO_SENDER_PHONE']
receiver_phone = os.environ['TWILIO_RECEIVER_PHONE']

api_key = os.environ['API_KEY']
long = 42.144920
lat = 24.750320

url = 'https://api.openweathermap.org/data/3.0/onecall'

weather_params = {
    'lat': 45.516022,
    'lon': -122.681427,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url=url, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_data_by_hours = weather_data['hourly']

is_bad_condition = False

for hourly_data in range(0, 12):
    weather = weather_data_by_hours[hourly_data]['weather']
    weather_id = weather[0]['id']
    if int(weather_id) < 700:
        is_bad_condition = True

if is_bad_condition:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Don't forget to get an ☔",
        from_=sender_phone,
        to=receiver_phone
    )
    print(message.status)
    # print('It rains')
