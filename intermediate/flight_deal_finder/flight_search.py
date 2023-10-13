import os

import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

TEQUILA_KIWI_API_ENDPOINT = 'https://api.tequila.kiwi.com'

KIWI_API_KEY = os.environ['KIWI_API_KEY']
KIWI_HEADERS = {
    'apikey': KIWI_API_KEY,
}


class FlightSearch:
    def get_destination_code(self, city_name):
        location_api_endpoint = f'{TEQUILA_KIWI_API_ENDPOINT}/locations/query'
        query = {'term': city_name, 'location_types': 'city'}
        response = requests.get(url=location_api_endpoint, headers=KIWI_HEADERS, params=query)
        result = response.json()['locations']
        code = result[0]['code']
        return code
