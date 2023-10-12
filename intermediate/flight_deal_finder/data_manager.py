import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

class DataManager:
    def __init__(self):
        self.sheety_project_name = os.environ['SHEETY_PROJECT_NAME_FLIGHT']
        self.sheety_username = os.environ['SHEETY_USERNAME']
        self.sheety_name = os.environ['SHEETY_NAME']
        self.sheety_auth_token = os.environ['SHEETY_TOKEN']

        self.sheety_headers = {
            'Authorization': f'Bearer {self.sheety_auth_token}'
        }
        self.sheety_api_endpoint = f'https://api.sheety.co/{self.sheety_username}/{self.sheety_project_name}/{self.sheety_name}'