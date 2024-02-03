# import smtplib

# my_email = "ilfedrigo.python.100days@gmail.com"
# password = "ioqr rpwy jwdu xzig"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#                         from_addr=my_email, 
#                         to_addrs="lucas.fedrigo@icloud.com", 
#                         msg="Subject:Hello\n\nThis is the body of my email"
#                         )
    
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1991, month=8, day=17, hour=4, minute=20)

print(date_of_birth)