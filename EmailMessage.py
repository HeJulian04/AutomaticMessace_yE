import os
import smtplib
import ssl
import time
from datetime import date, timedelta
import datetime
import calendar

logFile = open("logs.txt", "a")

employees = ["julian.henz", "simon.spruengli"]
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "youengineering.test@gmail.com"  # Enter your address
password = "123456yE"
message = """\
Monatsende

Hiermit bitte ich euch eure Stunden zu erfassen."""


def message_send_function():
    today = datetime.date.today()

    last = today.replace(day=calendar.monthrange(today.year, today.month)[1])

    lastBusinessDay = last - timedelta(days=1 + last.weekday() - 5)

    if lastBusinessDay == today:

        logFile.write(lastBusinessDay.strftime("%d-%b-%Y"))
        logFile.write("\n")
        for employee in employees:
            receiver_email = employee + "@youengineering.ch"
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

            logFile.write("Email successfully to " + receiver_email + " send")
            logFile.write("\n")
    logFile.write("---------------------------------------------------------------------------------------------")
    logFile.write("\n")
    logFile.close()

message_send_function()



