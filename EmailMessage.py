import os
import smtplib
import ssl
import time
from datetime import date, timedelta
import datetime
import calendar

logFile = open("logs.txt", "a")

employees = ["alina.wuethrich", "beat.haenger", "benjamin.brodwolf", "benji.oser", "carl.kuesters", "christina.dasilva", "dominik.erni", "gabriel.brodmann", "joshua.brehm", "gerd-emmanuel.nandzik", "joel.muller", "julian.henz", "marc.baur", "mario.hammel", "martin.lüpold", "meredit.sommer", "michael.hunziker", "nadia.kramer", "niki.stohler", "pascal.andermatt", "sibylle.tanner", "simon.fankhauser", "simon.spruengli"]
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "youengineering.test@gmail.com"  # Enter your address
password = "123456yE"
message = """\
Subject: Monatsende Hakuna Erinnnerung
Monatsende

Denkt bitte daran bis heute Abend eure Stunden in Hakuna vollständig zu erfassen. 
Merci vielmals und allne ä hübsche Tag :D  Sibylle"""


today = datetime.date.today()

def check_last_day():
    last = today.replace(day=calendar.monthrange(today.year, today.month)[1])
    if calendar.day_name[last.weekday()] == "Saturday":
        last = last + timedelta(days=-1)
        return last
    elif calendar.day_name[last.weekday()] == "Sunday":
        last = last + timedelta(days=-2)
        return last
    else:
        return last

def message_send_function():

    if today == check_last_day():

        for employee in employees:
            receiver_email = employee + "@youengineering.ch"
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)

                server.sendmail(sender_email, receiver_email, message.encode('utf-8', 'ignore'))


            logFile.write("Email successfully to " + receiver_email + " send")
            logFile.write("\n")
    logFile.write("---------------------------------------------------------------------------------------------")
    logFile.write("\n")
    logFile.close()


message_send_function()
