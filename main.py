import smtplib
import random
import datetime as dt

now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
day_of_week = now.weekday()

def send_email():

    with open ("quotes.txt", "r") as file:
        quotes = file.readlines()

    random_quote = random.randint(0, 102)
    daily_quote = quotes[random_quote]

    my_email = "ilfedrigo.python.100days@gmail.com"
    password = "ioqr rpwy jwdu xzig"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                            from_addr=my_email, 
                            to_addrs="lucas.fedrigo@icloud.com", 
                            msg=f"Subject:Motivational Quote of the Day\n\n{daily_quote}"
                            )

if day_of_week == 6:
    send_email()




    



# date_of_birth = dt.datetime(year=1991, month=8, day=17, hour=4, minute=20)

# print(day_of_week)