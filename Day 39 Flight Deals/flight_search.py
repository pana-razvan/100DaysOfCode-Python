import requests
import os
from datetime import datetime, timedelta
from flight_data import FlightData


class FlightSearch:

    def __init__(self):
        self.MY_CITY_CODE = "BUH"
        self.ENDPOINT = os.getenv('TEQUILA_ENDPOINT')
        self.HEADER = {"apikey": os.getenv('TEQUILA_API_KEY')}

    def get_destination_code(self, city_name):
        data = requests.get(
            url=f"{self.ENDPOINT}/locations/query",
            params={"term": city_name, "location_types": "city"},
            headers=self.HEADER
        ).json()
        return data["locations"][0]["code"]

    def search_for_flights(self, destination_city_code):
        params = {
            "fly_from": f"city:{self.MY_CITY_CODE}",
            "fly_to": f"city:{destination_city_code}",
            "dateFrom": f"{(datetime.now() + timedelta(days=1)).strftime('%d/%m/%Y')}",
            "dateTo": f"{(datetime.now() + timedelta(days=30*6)).strftime('%d/%m/%Y')}",
            "max_stopovers": 0,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 21,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "EUR"
        }
        response = requests.get(
            url=f"{self.ENDPOINT}/v2/search",
            params=params,
            headers=self.HEADER
        )
        response.raise_for_status()

        try:
            flight = FlightData(response.json()["data"][0])
        except IndexError:
            print(f"There are no flights available for {destination_city_code}")
            return None
        else:
            print(f"{flight.route_outbound_cityTo}: {flight.conversion_EUR} €")
            return flight
