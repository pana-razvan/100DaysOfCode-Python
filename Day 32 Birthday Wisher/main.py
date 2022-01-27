import smtplib
import datetime as dt
import random

EMAIL = "<your email goes here>"
PASSWORD = "<your password goes here>"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as quotes:
        list_of_quotes = quotes.readlines()
        random_quote = random.choice(list_of_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="<your destination email goes here>",
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )
