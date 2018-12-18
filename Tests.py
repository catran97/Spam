import Spam01
import unittest
from openpyxl import load_workbook
from Spam01 import *

class TestsSpam01(unittest.TestCase):
    def test_input_file_excel(self):  # если все значения есть
        print("Проверка файла emails.xlsx")
        ex_file = load_workbook('emails.xlsx')
        sheet = ex_file['email']
        column = sheet['D']
        for cell in column:
            if cell.value is None:
                continue
            else:
                 mail = cell.value
            email = "goodmorningsam66@gmail.com"
            self.assertEqual(mail, email)

#Проверка почтовых адресов

    def test_mail(self): #если почта указана правильно
        print("Проверка работы шаблона")
        mail = "artur.tikhonov.97@mail.ru"
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', mail)
        self.assertIsNotNone(match, mail)
        mail = "sanya.barckov@yandex.ru"
        self.assertIsNotNone(match, mail)
        mail = "goodmorningsam66@gmail.com"
        self.assertIsNotNone(match, mail)

    def test_not_mail(self): #если почта указана не правильно
        print("Проверка работы шаблона")
        mail = "artur.tikhonov.97@mail.ruoop"
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', mail)
        self.assertIsNone(match)
        mail = "sanya.barckovyandex.ru"
        self.assertIsNone(match)
        mail = "goodmorningsam66@gmail,com"
        self.assertIsNone(match)


    def test_input_file(self): #если все значения есть
        print("Проверка файла config.cfg")
        config = open('config.cfg', encoding='utf-8-sig')
        with config:
           for index, line in enumerate(config):
             if index == 0:
                 serv_mail = line
                 self.assertEqual(line,"spamgondola@gmail.com\n")
             elif index == 1:
                serv_pswrd = line
                self.assertEqual(line, "gondola2000\n")
             elif index == 2:
                serv_header = line
                self.assertEqual(line, "Spamgondola test 01")

if __name__ == '__main__':
    unittest.main()



