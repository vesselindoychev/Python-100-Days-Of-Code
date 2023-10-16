import os
from flight_data import FlightData
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

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime('%d/%m/%Y'),
            'date_to': to_time.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'GBP'
        }

        response = requests.get(url=f"{TEQUILA_KIWI_API_ENDPOINT}/v2/search", headers=KIWI_HEADERS, params=query)

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airport=data['route'][0]['flyTo'],
            out_date=data['route'][0]['local_departure'].split('T')[0],
            return_date=data['route'][1]['local_departure'].split('T')[0]
        )

        print(f"{flight_data.destination_city}: £{flight_data.price}")
        flight_data.check_for_lowest_price()
        return flight_data
