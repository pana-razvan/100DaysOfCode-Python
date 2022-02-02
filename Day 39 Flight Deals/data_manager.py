import requests
import os


class DataManager:

    def __init__(self):
        self.ENDPOINT = os.getenv("SHEETY_ENDPOINT")
        self.HEADER = {"Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"}
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.ENDPOINT, headers=self.HEADER)
        print(response.raise_for_status())
        print(response.text)
        sheet_data = response.json()
        self.destination_data = sheet_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{os.getenv('SHEETY_ENDPOINT')}/{city['id']}",
                json=new_data
            )
