import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(verbose=True)

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

MY_GENDER = 'male'
MY_WEIGHT = 76
MY_HEIGHT = 179
MY_AGE = 20

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_input = input('Tell me which exercises you did: ')

post_request_body = {
    "query": exercise_input,
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

response = requests.post(url=exercise_endpoint, json=post_request_body, headers=headers)
result = response.json()
print(result)

current_date = datetime.now().strftime('%d/%m/%Y')
current_time = datetime.now().strftime('%H:%M:%S')

SHEETY_USERNAME = os.environ['SHEETY_USERNAME']
SHEETY_PROJECT_NAME = os.environ['SHEETY_PROJECT_NAME']
SHEETY_NAME = os.environ['SHEETY_NANME']
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']


sheety_endpoint = f'https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_NAME}'

# sheety_response = requests.get(url=sheety_endpoint)
# print(sheety_response.json())

sheety_headers = {
    'Authorization': f'Bearer {SHEETY_TOKEN}'
}
for exercise in result['exercises']:
    row_content = {
        'workout': {
            'date': current_date,
            'time': current_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    sheety_post_response = requests.post(url=sheety_endpoint, json=row_content, headers=sheety_headers)
    print(sheety_post_response.json())
