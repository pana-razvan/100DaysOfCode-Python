import requests
from datetime import datetime
import smtplib
import time

# Bucharest
MY_LAT = 44.4268
MY_LONG = 26.1025
EMAIL = "popescu.ionut.cel.mare@gmail.com"
PASSWORD = "<password_goes_here>"


def iss_is_close_above():
    """Returns 'True' if ISS position is within +5 or -5 degrees of the_position or 'False' if otherwise"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_now_data = response.json()

    iss_lat = float(iss_now_data["iss_position"]["latitude"])
    iss_lng = float(iss_now_data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_lng <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset_hour or time_now.hour <= sunrise_hour:
        return True


while True:
    if iss_is_close_above() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=EMAIL,
                                msg=f"Subject:Look Up!\n\nThe ISS is now above you in the sky.\n"
                                    f"Time: {datetime.now().hour}:{datetime.now().minute}\n"
                                )
    time.sleep(60)
