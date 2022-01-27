import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "popescu.ionut.cel.mare@gmail.com"
MY_PASSWORD = "shl$p$CGl98Lv"

now = dt.datetime.now()


def send_letter(email, letter):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )


birthdays = pandas.read_csv("birthdays.csv")
birthdays = birthdays.to_dict(orient="records")
for record in birthdays:
    if record["day"] == now.day and record["month"] == now.month:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as random_letter:
            letter_text = random_letter.read()
            letter_text = letter_text.replace("[NAME]", record["name"])
        send_letter(record["email"], letter_text)
