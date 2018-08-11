#!/usr/bin/env python 

import datetime
import logging
from typing import Iterable, Optional

GREETING_MESSAGE = """Subject: Happy birthday!

Happy birthday, dear {}!"""


def is_employee_birthday(employee_data,
                         birthday_on=datetime.datetime.now().strftime('%d/%m')):
    """
    Returns True or False if it's employee's birthday.

    :param employee_data: A sequence of elements in which the third should be a
    date containing at least DD/MM.
    :param birthday_on: string representation of a date. The format should match
    the `employee_data` date format. Optional, if missing, today's date in DD/MM
    format will be used.
    :return: True if the birthday date matches, False even if the data is
    corrupted.
    """
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
