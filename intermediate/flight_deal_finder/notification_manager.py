import os
from twilio.rest import Client

TWILIO_ACC_SID = os.environ['TWILIO_ACC_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
SENDER_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
RECEIVER_PHONE_NUMBER = os.environ['TWILIO_RECEIVER_PHONE_NUMBER']


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, text):
        message = self.client.messages.create(
            from_=SENDER_PHONE_NUMBER,
            body=text,
            to=RECEIVER_PHONE_NUMBER
        )
