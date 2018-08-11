#!/usr/bin/env python 

import datetime

GREETING_MESSAGE = """Subject: Happy birthday!

Happy birthday, dear {}!"""

FILE_PATH = 'asset/employee.txt'

TODAY = datetime.datetime.now().strftime('%d/%m')


def employees_birthday_extract(filename):
    with open(filename) as employee_file:
        employee_file.readline()

        for employee_line in employee_file:
            try:
                first_name, last_name, date_as_string, email\
                    = employee_line[:-1].split(', ')
            except ValueError:
                continue

            if date_as_string[:5] == TODAY:
                yield first_name, email


def send_email(to, title, body):
    print('Sending email to', to)
    print('Title:', title)
    print('body:', body)
    print('-' * 20)


for name, email in employees_birthday_extract(FILE_PATH):
    send_email(email, "Joyeux Anniversaire", GREETING_MESSAGE.format(name))
