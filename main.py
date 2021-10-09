##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import pandas as pd
import datetime as dt
import random



my_email = "XXXX@gmail.com"
password = "XXXX"
data = pd.read_csv("birthdays.csv")
print(data)
# print(data.iloc[:,3:5])
# print(data[year])
now = dt.datetime.now()
print(now)

for row in data.iterrows():
    # print("printing row")
    # print(row)
    day = now.day
    month = now.month
    # print(month)
#     print("row", row[1])

#     # print(type(row))
    if row[1].day == day and row[1].month == month:
        letter_name = random.choice(['letter_1.txt', "letter_2.txt", "letter_3.txt"])
        with open(f"letter_templates/{letter_name}") as letter:
            template = letter.read()
            template = template.replace("[NAME]", row[1].his_name)
            print(template)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=row[1].email,
                                    msg=f"Subject:Happy Birthday \n\n{template}")


