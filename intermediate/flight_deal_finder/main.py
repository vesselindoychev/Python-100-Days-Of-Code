from data_manager import DataManager
from flight_search import FlightSearch
import requests
from datetime import datetime
from datetime import timedelta

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]['iataCode'] == '':
    for item in sheet_data:
        item['iataCode'] = flight_search.get_destination_code(item['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

ORIGIN_CITY_CODE = 'LGW'
tomorrow = datetime.now().date() + timedelta(days=1)
six_months_from_today = datetime.now().date() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_months_from_today,
    )
