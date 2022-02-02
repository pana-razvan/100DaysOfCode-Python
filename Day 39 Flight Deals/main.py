from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

import pandas as pd

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# destinations_data = data_manager.get_destination_data()
#
# if destinations_data[0]["iataCode"] == "":
#     for city in destinations_data:
#         city["iataCode"] = flight_search.get_destination_code(city["city"])
#     data_manager.destination_data = destinations_data
#     data_manager.update_destination_codes()

with open("Flight Deals.csv", "r") as data:
    content = pd.read_csv(data)
    destinations = content.to_dict(orient="records")

for destination in destinations:
    cheapest_flight = flight_search.search_for_flights(destination["IATA Code"])
    if cheapest_flight is not None and cheapest_flight.conversion_EUR <= destination["Lowest Price EUR"]:
        notification_manager.send_notification(cheapest_flight)
