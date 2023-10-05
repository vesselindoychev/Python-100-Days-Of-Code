import random
import smtplib
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv(verbose=True)

week_days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

current_day = week_days[dt.datetime.now().weekday()]
print(current_day)

with open('quotes.txt') as quotes_file:
    quotes_list = quotes_file.readlines()
    quote = random.choice(quotes_list)

my_email = os.environ['EMAIL']
password = os.environ['PASSWORD']

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f'Subject:Happy {current_day}\n\n{quote}'
    )
