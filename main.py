# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import smtplib
import datetime as dt
import pandas as pd
import random
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


now=dt.datetime.now()
today_day=now.day
today_month=now.month

todayM_D=(today_month,today_day)


with open("birthdays.csv") as birthdays_file:
    birthdays = pd.read_csv(birthdays_file)


dict_birthdays =  {(row["month"],row["day"]):row for (index, row) in birthdays.iterrows()}

if todayM_D in dict_birthdays:

    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_template:
        letter_template = letter_template.read()
        letter_template=letter_template.replace("[NAME]",f"{dict_birthdays[todayM_D]['name']}")
        print(letter_template)
    #HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
    # if (today_month, today_day) in birthdays_dict:
    with smtplib.SMTP("smtp.gmail.com", 587) as user:
        user.starttls()
        user.login("MY_EMAIL", "MY_PASSWORD")
        user.sendmail(from_addr="MY_EMAIL",to_addrs=f"{dict_birthdays[todayM_D]['email']}"
                      ,msg=f"subject:happy birthday\n\n{letter_template}")
