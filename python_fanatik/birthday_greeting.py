#!/usr/bin/env python 

import datetime
import logging
from typing import Iterable, Optional

# last, first, 1982/10/08, email

GREETING_MESSAGE = """Subject: Happy birthday!

Happy birthday, dear {}!"""


def is_employee_birthday(employee_data,
                         birthday_on=datetime.datetime.now().strftime('%d/%m')):
    try:
        return employee_data[2][:5] == birthday_on
    except IndexError:
        logging.error("Unexpected data structure for [>%s<]"
                      % employee_data)

    return False


def send_email(to: str, title: str, body: str):
    print('Sending email to', to)
    print('Title:', title)
    print('body:', body)
    print('-' * 20)


if __name__ == '__main__':
    FILE_PATH = 'asset/employee.txt'

    with open(FILE_PATH) as employee_file:
        employee_file.readline()

        for first_name, last_name, birthday, email \
                in [employee_data
                    for employee_data in [employee.split(', ')
                                          for employee in employee_file]
                    if is_employee_birthday(employee_data)]:
            send_email(email, "Joyeux Anniversaire",
                       GREETING_MESSAGE.format(first_name))
