# -*- coding: utf-8 -*-
#spamgondola@gmail.com Спамер
#gondola2000

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from openpyxl import load_workbook

#Получение адреса и пароля отправителя, темы письма
with open('config.cfg', encoding='utf-8-sig') as config:
    for index, line in enumerate(config):
        if index == 0:
            serv_mail = line
        elif index == 1:
            serv_pswrd = line
        elif index == 2:
            serv_header = line
            break

#Отправление письма
def sendMail(content, mail):
    message = MIMEMultipart('alternative')
    message['Subject'] = serv_header
    message.add_header('Content-Type','text/html')
    text = MIMEText(content, 'html')
    message.attach(text)
    mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mailserver.login(serv_mail, serv_pswrd)
    mailserver.sendmail(serv_mail, mail, message.as_string())
    mailserver.quit()

#Открытие файла письма
mail_body = 'message.html'
with open(mail_body , encoding='utf8') as file:
    content = file.read()

#Получение списка получателей
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