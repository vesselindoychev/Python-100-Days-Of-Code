import random
import pandas
import datetime as dt
import smtplib
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

random_letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

my_email = os.environ['EMAIL']
my_password = os.environ['PASSWORD']

now = dt.datetime.now()
current_month = now.month
current_date = now.day

b_day_data = pandas.read_csv('birthdays.csv')
b_day_data_dict = b_day_data.to_dict(orient='records')

for entry in b_day_data_dict:

    if entry['month'] == current_month and entry['day'] == current_date:
        name = entry['name']
        email = entry['email']
        year = entry['year']

        random_letter = random.choice(random_letters)

        with open(f'letter_templates/{random_letter}') as letter_file:
            letter = letter_file.read()

        with open('letter_templates/birthday_letter.txt', mode='w') as birthday_letter_file:
            letter_clone = letter
            birthday_letter_file.write(letter_clone.replace('[NAME]', f'{name}'))

        with open('letter_templates/birthday_letter.txt') as file:
            new_letter = file.read()
            print(new_letter)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday\n\n{new_letter}"
            )

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
