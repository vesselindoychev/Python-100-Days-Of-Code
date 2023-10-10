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
    'appid': api_key
}

response = requests.get(url=url, params=weather_params)
print(response.json())
