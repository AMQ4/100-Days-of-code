import datetime as dt
import smtplib
import time

import requests
import sys
import importlib

sys.path.append("..")
sunset_sunrize = importlib.import_module("sunset-sunrise-challenge.main")


def notify():
    email = "dummy@gmail.com"  # replace it with your own.
    password = "12345678"      # replace it with your email app password
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=email,
                        msg="Subject:look up👆\n\nThe ISS is above you in the sky!".encode("utf-8"))
    connection.close()


def is_night(sunset, sunrise):
    return False if dt.datetime.now().hour in range(sunset, sunrise + 1) else True


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_lng = float(data["iss_position"]["longitude"])

sunset = sunset_sunrize.sunset(lat=sunset_sunrize.IRBID_LAT, lng=sunset_sunrize.IRBID_LONG, time_format=0)
sunrise = sunset_sunrize.sunrise(lat=sunset_sunrize.IRBID_LAT, lng=sunset_sunrize.IRBID_LONG, time_format=0)

while True:
    time.sleep(60)
    if is_night(sunset=sunset, sunrise=sunrise) and (abs(sunset_sunrize.IRBID_LAT - iss_lat) <= 5 and abs(
            sunset_sunrize.IRBID_LONG - iss_lng) <= 5):
        notify()