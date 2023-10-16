from data_manager import DataManager
from flight_search import FlightSearch
import requests
from datetime import datetime
from datetime import timedelta
from customer_data import CustomerService
from notification_manager import NotificationManager

notification_manager = NotificationManager()
data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]['iataCode'] == '':
    for item in sheet_data:
        item['iataCode'] = flight_search.get_destination_code(item['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

ORIGIN_CITY_CODE = 'LON'
tomorrow = datetime.now().date() + timedelta(days=1)
six_months_from_today = datetime.now().date() + timedelta(days=(6 * 30))

for destination in sheet_data:
    text = ''
    iataCode = destination['iataCode']
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        iataCode,
        from_time=tomorrow,
        to_time=six_months_from_today,
    )

    if flight is None:
        continue

    if int(flight.price) < int(destination['lowestPrice']):
        text += f'Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.'

        if flight.stop_overs > 0:
            text += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_email(text)
