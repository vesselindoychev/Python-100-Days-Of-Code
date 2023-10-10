import os

import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)
api_key = os.environ['API_KEY']
long = 42.144920
lat = 24.750320

# url = 'https://api.openweathermap.org/data/3.0/onecall?lat=42.144920&lon=24.750320&exclude={part}&appid=b196d8430a9e47db7320d7760ffed531'
url = 'https://api.openweathermap.org/data/3.0/onecall'
# url = 'https://api.openweathermap.org/data/2.5/weather'

weather_params = {
    'lat': lat,
    'lon': long,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url=url, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_data_by_hours = weather_data['hourly']
print(weather_data_by_hours)

is_bad_condition = False
for hourly_data in range(0, 12):
    weather = weather_data_by_hours[hourly_data]['weather']
    weather_id = weather[0]['id']
    if int(weather_id) < 700:
        is_bad_condition = True
    print(weather_id)

if is_bad_condition:
    print('Bring an umbrella')
print(weather_data)

