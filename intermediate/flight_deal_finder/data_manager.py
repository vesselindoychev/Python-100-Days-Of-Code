import os
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

SHEETY_PROJECT_NAME = os.environ['SHEETY_PROJECT_NAME_FLIGHT']
SHEETY_USERNAME = os.environ['SHEETY_USERNAME']
SHEETY_NAME = os.environ['SHEETY_NAME']
SHEETY_AUTH_TOKEN = os.environ['SHEETY_AUTH_TOKEN']

SHEETY_HEADERS = {
    'Authorization': f'Bearer {SHEETY_AUTH_TOKEN}'
}
SHEETY_API_ENDPOINT = f'https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_NAME}'


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADERS)
        sheet_data = response.json()
        self.destination_data = sheet_data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for item in self.destination_data:
            request_body = {
                'price': {
                    'iataCode': item['iataCode']
                }
            }

            response = requests.put(url=f"{SHEETY_API_ENDPOINT}/{item['id']}", json=request_body,
                                    headers=SHEETY_HEADERS)
