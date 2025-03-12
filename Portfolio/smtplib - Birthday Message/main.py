import smtplib
import datetime as date
import random
import pandas
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

now = date.datetime.now()
today = (now.month,now.day)

birthday = pandas.read_csv("birthday.csv")
birthday_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in birthday.iterrows()}
file = f"letter_{random.randint(1,3)}.txt"

if today in birthday_dict:
    birthday_person = birthday_dict[today]    #holds the whole row of the person with the BDay today
    with open(file) as letter:
        contents = letter.read()
        change = contents.replace("[NAME]", birthday_person["name"])    #replaces the [NAME] using the name column of birthday_person
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{change}")


