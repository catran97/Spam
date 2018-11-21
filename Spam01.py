# -*- coding: utf-8 -*-
#spamgondola@gmail.com Спамер
#gondola2000

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from openpyxl import load_workbook

sender = "spamgondola@gmail.com"
password ="gondola2000"

def sendMail(content, mail):
    message = MIMEMultipart('alternative')
    message['Subject'] = "Spamgondola test 3"
    message['From'] = sender
    message['To'] = mail
    message.add_header('Content-Type','text/html')
    text = MIMEText(content, 'html')
    message.attach(text)
    mailserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    mailserver.login(sender, password)
    mailserver.sendmail(message['From'], message['To'], message.as_string())
    mailserver.quit()

mail_body = 'message.html'
with open(mail_body , encoding="utf8") as file:
    content = file.read()

ex_file = load_workbook('emails.xlsx')
sheet = ex_file['email']
column = sheet['D']
for cell in column:
    if cell.value is None:
        continue
    else:
        mail=cell.value
        sendMail(content, mail)
        print('Send to: ', mail)
        mail=''