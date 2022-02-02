import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
VARIATION_VALUE_PERCENT = 5

STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock.json()
stock_data_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
day_before = float(stock_data_list[1]["4. close"])
yesterday = float(stock_data_list[0]["4. close"])
target_value = VARIATION_VALUE_PERCENT / 100 * yesterday
variation = abs(yesterday - day_before)


def up_or_down():
    if yesterday - day_before >= 0:
        return "▲"
    elif yesterday - day_before < 0:
        return "▼"


news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

news = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_data = news.json()

news_titles_list = [news for news in news_data["articles"][:3]]


if variation >= target_value:
    for news in news_titles_list:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
                             body=f"{STOCK}: {up_or_down()} {round(variation/yesterday*100,1)}%\n"
                                  f"Headline: {news['title']}\n"
                                  f"Link: {news['url']}",
                             from_='+19402603548',
                             to='+40729745169'
                         )
