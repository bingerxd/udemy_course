import smtplib
import datetime as dt
import random

my_email = "proszedzialaj37@gmail.com"
password = "evsbgvdamvylsnkw"
another_email = "proszedzialaj@yahoo.com"

now = dt.datetime.now()
day_of_the_week = now.weekday()

with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)

if day_of_the_week == 3:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
         connection.starttls()
         connection.login(user=my_email, password=password)
         connection.sendmail(
             from_addr=my_email,
             to_addrs=another_email,
             msg=f"Subject:Monday Motivation\n\n{quote}"
         )