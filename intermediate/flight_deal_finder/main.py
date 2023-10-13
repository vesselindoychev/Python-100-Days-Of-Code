# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import requests

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]['iataCode'] == '':
    for item in sheet_data:
        item['iataCode'] = flight_search.get_destination_code(item['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()