import datetime as dt
import smtplib
import time
import requests
import sys
import importlib

# Add the parent directory to sys.path to enable import
sys.path.append("..")
sunset_sunrize = importlib.import_module("sunset-sunrise-challenge.main")

def notify():
    """
    Send a notification email when the ISS is visible during the night.

    :return: None
    """
    email = "dummy@gmail.com"  # replace it with your own.
    password = "12345678"      # replace it with your email app password

    # Establish a connection with the SMTP server
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    connection.starttls()

    # Log in to the email account
    connection.login(user=email, password=password)

    # Send the notification email
    connection.sendmail(from_addr=email, to_addrs=email,
                        msg="Subject:look up👆\n\nThe ISS is above you in the sky!".encode("utf-8"))
    connection.close()

def is_night(sunset, sunrise):
    """
    Check if it's currently night based on the sunset and sunrise times.

    :param sunset: The hour of sunset.
    :type sunset: int
    :param sunrise: The hour of sunrise.
    :type sunrise: int
    :return: True if it's night, False if it's day.
    :rtype: bool
    """
    current_hour = dt.datetime.now().hour
    return False if current_hour in range(sunset, sunrise + 1) else True

# Fetch the current ISS position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_lng = float(data["iss_position"]["longitude"])

# Get sunset and sunrise times for the specified location
sunset = sunset_sunrize.sunset(lat=sunset_sunrize.IRBID_LAT, lng=sunset_sunrize.IRBID_LONG, time_format=0)
sunrise = sunset_sunrize.sunrise(lat=sunset_sunrize.IRBID_LAT, lng=sunset_sunrize.IRBID_LONG, time_format=0)

# Continuous loop to monitor and notify
while True:
    time.sleep(60)  # Delay to avoid continuous processing

    # Check if it's night and ISS is nearby
    if is_night(sunset=sunset, sunrise=sunrise) and (abs(sunset_sunrize.IRBID_LAT - iss_lat) <= 5 and abs(
            sunset_sunrize.IRBID_LONG - iss_lng) <= 5):
        notify()
