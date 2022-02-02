import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 94
HEIGHT_CM = 185
AGE = 35

APP_ID = "46c4850c"
API_KEY = "3875a81baf424e6fc38cbf868d6aebf9"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
# TODO 1. Print the exercise stats for a plain text input

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
params = {
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "query": exercise_text
}

# swam 2 miles and did 30 push-ups today

nutritionix_response = requests.post(url=exercise_endpoint, json=params, headers=HEADERS).json()

now = datetime.now()
body = {
    "workout": {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%X"),
        "exercise": nutritionix_response["exercises"][0]["name"].title(),
        "duration": nutritionix_response["exercises"][0]["duration_min"],
        "calories": nutritionix_response["exercises"][0]["nf_calories"]
    }
}

sheety_api = "https://api.sheety.co/9fed24b2ccf0fcc8b2d39580e9699352/dash'sWorkouts/workouts"
sheety_response = requests.post(url=sheety_api, json=body)
print(sheety_response.text)
