import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
MY_LAT = 14.689622
MY_LONG = 121.117744

def is_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True

def night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    if hour_now <= sunset or hour_now > sunrise:
        return True

if is_near() and night_time():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Makes the connection secure
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="jeongyoo03@gmail.com",
                            msg="Subject:ISS\n\nLook up")




