import pandas
import datetime as dt
import random
import smtplib

dataframe = pandas.read_csv("./res/birthdays.csv")
now = dt.datetime.now()


def get_random_letter():
    random_letter = random.randint(1, 3)
    with open(f"./res/letter_templates/letter_{random_letter}.txt") as random_letter:
        return ''.join(random_letter.readlines())


def send_email(to, email, message):
    def custom_message(name):
        nonlocal message
        message = message.replace("[NAME]", name)

    def send():
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login("ahmadalqaisi219@gmail.com", "nanirwbzjgwfdvdx")
            connection.sendmail(from_addr="ahmadalqaisi219@gmail.com", to_addrs=email,
                                msg="Subject:Happy birthday\n\n" + message)

    custom_message(to)
    send()


for (index, row) in dataframe.iterrows():
    if now.month == row.month and now.day == row.day:
        send_email(to=row["name"], email=row.email, message=get_random_letter())
