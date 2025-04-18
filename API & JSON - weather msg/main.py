import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
API_KEY = os.environ["KEY"]

parameters = {
    "lat": 14.692639,
    "lon": 121.120920,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    code = hour_data["weather"][0]["id"]
    if int(code) < 700:
        message = "It will rain today in your city, don't forget bring an umbrella when going outside!"
        will_rain = True
    else:
        message = "Today will be sunny in your city, have a pleasant day outside!"
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls() #Makes the connection secure
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="jeongyoo03@gmail.com",
                            msg=f"Subject:Weather\n\n{message}")

