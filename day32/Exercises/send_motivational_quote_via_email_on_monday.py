# Import required modules
import datetime as dt
import smtplib
from random import choice


def send_email(sender, receiver, message, password_app):
    """
        Send an email using the provided parameters.

    Parameters:
        sender (str): The sender's email address.
        receiver (str): The recipient's email address.
        message (str): The content of the email message.
        password_app (str): The password or app-specific password for the sender's email account.

    Returns:
        None

    """
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=password_app)
        connection.sendmail(from_addr=sender, to_addrs=receiver, msg=message)


email, password_app = input("Your Gmail: "), input("Your Password App: ")

data = dt.datetime.now()  # Get the current date and time.

if data.weekday() == 1:  # Check if today is Monday (weekday 2).
    with open("./quotes.txt", 'r') as quotes:
        quote = choice(quotes.readlines())  # Select a random quote from the quotes file.

        # Send the selected quote as an email to the specified recipient.
        send_email(email, email, "Subject:Motivational Quote\n\n" + quote, password_app)