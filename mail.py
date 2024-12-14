
import smtplib
import datetime as dt

now = dt.datetime.now()
date = now.day
year = now.time()
print(date)
print(year)
score = input("enter you score :")
my_email = "adeebinamdar9@gmail.com"
password = "xnmx wrrf ssqp pyap"
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="sudubiradar0609@gmail.com", msg=f"Subject:qizzler app\n\n {date}// {year} your score for the quiz is :{score}")
connection.close()




