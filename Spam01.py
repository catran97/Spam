# -*- coding: utf-8 -*-
#spamgondola@gmail.com Спамер
#gondola2000

#ykfgodnew@gmail.com Ярик
#artur.tikhonov.97@mail.ru Артур
#sanya.barckov@yandex.ru Саня
#goodmorningsam66@gmail.com Жека

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import io

def sendMail(messagetext):
    sender = "spamgondola@gmail.com"
    password = "gondola2000"
    recipient = "goodmorningsam66@gmail.com"
    subject = "TEST MESSAGE"
    text = MIMEText(messagetext, "plain", "utf-8")
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(sender, password)
    message = "Subject: {}\n\n{}".format(subject, text)
    smtp_server.sendmail(sender, recipient, message)
    smtp_server.close()

mail_body = 'message.txt'
with open(mail_body , encoding="utf8") as file:
    messagetext = file.read()
sendMail(messagetext)



