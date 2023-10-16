import os
import smtplib

import requests
from twilio.rest import Client

TWILIO_ACC_SID = os.environ['TWILIO_ACC_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
SENDER_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
RECEIVER_PHONE_NUMBER = os.environ['TWILIO_RECEIVER_PHONE_NUMBER']

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

SENDER_EMAIL = os.environ['SENDER_EMAIL']
PASSWORD = os.environ['PYTHON_MAIL_PASSWORD']


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, text):
        message = self.client.messages.create(
            from_=SENDER_PHONE_NUMBER,
            body=text,
            to=RECEIVER_PHONE_NUMBER
        )

    def get_all_users(self):
        response = requests.get(url=SHEETY_API_ENDPOINT, headers=SHEETY_HEADERS)
        result = response.json()['users']
        return result

    def send_email(self, text):
        data = self.get_all_users()

        for item in data:
            name = item['firstName']
            email = item['email']
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=SENDER_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=SENDER_EMAIL,
                    to_addrs=email,
                    msg=f'Subject:Low price alert!\n\n{text}'.encode('utf-8')
                )

