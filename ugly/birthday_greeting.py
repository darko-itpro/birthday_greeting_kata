#!/usr/bin/env python 

import datetime

FILE_PATH = 'asset/employee.txt'


def send_email(to, title, body):
    print('Sending email to', to)
    print('Title:', title)
    print('body:', body)
    print('-' * 20)


file = open(FILE_PATH)

file.readline()

for emp in file:
    emp_data = emp[:-1].split(', ')

    try:
        if emp_data[2][:5] == datetime.datetime.now().strftime('%d/%m'):
            send_email(emp_data[-1], 'Joyeux Anniversaire',
                       "Subject: Happy birthday!\n\nHappy birthday, dear " +
                       emp_data[0])

    except IndexError:
        print("Wrong data for", emp_data)

file.close()
