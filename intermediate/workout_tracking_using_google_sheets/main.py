import os
import requests
from dotenv import load_dotenv

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
