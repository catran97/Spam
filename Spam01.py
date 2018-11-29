# -*- coding: utf-8 -*-

import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from openpyxl import load_workbook

# Получение адреса и пароля отправителя, темы письма
try:
    config = open('config.cfg', encoding='utf-8-sig')
except IOError:
    print('# cannot find config.cgf!')
    exit(0)
else:
    print('> config loaded')
    with config:
        for index, line in enumerate(config):
            if index == 0:
                serv_mail = line
            elif index == 1:
                serv_pswrd = line
            elif index == 2:
                serv_header = line
                break


# Отправка письма
def sendMail(content, mail):
    try:
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', mail)
        if match == None:
            print('# email syntax error: ', mail)
        else:
            message = MIMEMultipart('alternative')
            message['Subject'] = serv_header
            message.add_header('Content-Type', 'text/html')
            text = MIMEText(content, 'html')
            message.attach(text)
            mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            mailserver.login(serv_mail, serv_pswrd)
            mailserver.sendmail(serv_mail, mail, message.as_string())
            mailserver.quit()
            print('> send to: ', mail)
    except NameError:
        print('# error reading config.cgf!')


# Получение списка писем
def getMails(content):
    try:
        ex_file = load_workbook('emails.xlsx')
    except IOError:
        print('# cannot find emails.xlsx!')
        exit(0)
    else:
        print('> emails loaded')
        print('ready')
        sheet = ex_file['email']
        column = sheet['D']
        for cell in column:
            if cell.value is None:
                continue
            else:
                mail = cell.value
                sendMail(content, mail)
                mail = ''


try:
    mail_body = open('message.html', encoding='utf8')
except IOError:
    print('# cannot find message.html!')
    exit(0)
else:
    print('> message loaded')
    with mail_body:
        content = mail_body.read()
        getMails(content)
