#!/bin/usr/env python

import smtplib

import schedule
import time

def job():
    schedule.every(10).minutes.do(job)
    mail =smtplib.SMTP('smtp.gmail.com',587)

    mail.ehlo()

    mail.starttls()

    mail.login('subhamkumarbhatt@gmail.com','password')

    mail.sendmail('subhamkumarbhatt@gmail.com',['harshitomar18@gmail.com','akshayy2013@gmail.com','aryamanvicky@gmail.com','subhamkumarbhatt@gmail.com'], 'Never get into fights with ugly people, they have nothing to lose.')

    mail.close()

schedule.every(5/60).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)

