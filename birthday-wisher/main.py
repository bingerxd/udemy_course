##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import datetime as dt
import random
import pandas

birthdays = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
today = (now.month, now.day)

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

my_email = "proszedzialaj37@gmail.com"
password = "evsbgvdamvylsnkw"


if today in birthdays_dict:
    person = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as data:
        letter = data.read()
        letter = letter.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
        from_addr=my_email,
        to_addrs=person["email"],
        msg=f"Subject:Happy Birthday\n\n{letter}"
        )



