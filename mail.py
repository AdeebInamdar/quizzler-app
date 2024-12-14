
import smtplib
import datetime as dt

now = dt.datetime.now()
date = now.day
year = now.time()
print(date)
print(year)
score = input("enter you score :")
my_email = "add your sending mail"
password = "create password for google app"
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="sender email", msg=f"Subject:qizzler app\n\n {date}// {year} your score for the quiz is :{score}")
connection.close()




