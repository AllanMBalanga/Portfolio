import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ["ID"]
APP_KEY = os.environ["KEY"]
USERNAME = os.environ["USER"]
PASSWORD = os.environ["PASSWORD"]
SHEETY_ENDPOINT = "https://api.sheety.co/d7f6716792047b5d0802b0c43273010e/copyOfMyWorkouts/workouts"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = 76
HEIGHT = 170
AGE = 22

now = datetime.now()
hour = now.strftime("%H:%M:%S")
today = now.strftime("%d/%m/%Y")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": input("What exercise/s did you do?"),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE

}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
data = response.json()
print(data)


for exercise in data["exercises"]:
    exercise_parameters = {
        "workout": {
            "date": today,
            "time": hour,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=exercise_parameters, auth=(USERNAME, PASSWORD))
