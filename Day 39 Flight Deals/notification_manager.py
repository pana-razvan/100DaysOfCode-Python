import os
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.ACCOUNT_SID = os.getenv("TWILIO_SID")
        self.AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
        self.CLIENT = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

    def send_notification(self, flight):
        # self.CLIENT.messages.create(
        #     body=f"Found a cheap flight for you:\n"
        #          f"From: {flight.cityFrom}\n"
        #          f"To: {flight.cityTo}\n"
        #          f"Price: {flight.conversion_EUR} EUR / adult = {flight.conversion_EUR*2} for 2 adults\n"
        #          f"Departure Route Airports: {flight.route_outbound_flyFrom} -> {flight.route_outbound_flyTo}\n"
        #          f"Return Route Airports: {flight.route_inbound_flyFrom} -> {flight.route_inbound_flyTo}\n"
        #          f"Departure Date: {flight.route_outbound_local_departure}\n"
        #          f"Return Date: {flight.route_inbound_local_departure}\n"
        #          f"Seats Available: {flight.availability_seats}",
        #     from_='+19402603548',
        #     to='+40729745169'
        # )
        print(f"\nNotification sent:\n"
              f"Cheap flight from {flight.cityFrom} to {flight.cityTo}\n"
              f"Ticket price: {flight.conversion_EUR} €\n")






