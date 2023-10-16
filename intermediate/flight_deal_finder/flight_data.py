from intermediate.flight_deal_finder.data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
notification_manager = NotificationManager()


class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                 return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def check_for_lowest_price(self):
        all_destinations = data_manager.get_destination_data()

        current_price = [item['lowestPrice'] for item in all_destinations if item['city'] == self.destination_city]

        if self.price < int(current_price[0]):
            text = f'Low price alert! Only £{self.price} to fly from {self.origin_city}-{self.origin_airport} to {self.destination_city}-{self.destination_airport}, '
            f'from {self.out_date} to {self.return_date}.'

            notification_manager.send_sms(text)
