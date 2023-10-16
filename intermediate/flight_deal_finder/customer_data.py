import os

import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

ENTRY_MESSAGE = "Welcome to Vesko's Flight Club\n" \
                "We find the best flight deals and email you."

SHEETY_USERNAME = os.environ['SHEETY_USERNAME']
SHEETY_PROJECT_NAME = os.environ['SHEETY_PROJECT_NAME_FLIGHT']
SHEETY_NAME = os.environ['SECOND_SHEETY_NAME']
SHEETY_AUTH_TOKEN = os.environ['SHEETY_AUTH_TOKEN']

SHEETY_API_ENDPOINT = f'https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_NAME}'
SHEETY_HEADERS = {
    'Authorization': f"Bearer {SHEETY_AUTH_TOKEN}"
}


class CustomerService:
    def __init__(self):
        self.first_name = input('What is your first name?\n')
        self.last_name = input('What is your last name?\n')
        self.email = input('What is your email?\n')
        self.retype_email = input('Type your email again.\n')

        if self.email == self.retype_email:
            print('You are in the club!')
            self.post_data()

    def post_data(self):
        request_body = {
            'user': {
                'firstName': self.first_name,
                'lastName': self.last_name,
                'email': self.email
            }
        }

        response = requests.post(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADERS, json=request_body)


# print(ENTRY_MESSAGE)
