import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = os.getenv("api_key")
api_end_point = os.getenv("api_end_point")

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

lat = 44.4268
lng = 26.1025

parameters = {
    "lat": lat,
    "lon": lng,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

data = requests.get(api_end_point, params=parameters)
data.raise_for_status()
weather_data = data.json()

will_rain = False

conditions_list = [item["weather"][0]["id"] for item in weather_data["hourly"][:12]]
for item in conditions_list:
    if item < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
                         body="It's going to rain today. Remember to bring an umbrella ☂️",
                         from_="+19402603548",
                         to="+40 729 745 169"
                     )
    print(message.status)
