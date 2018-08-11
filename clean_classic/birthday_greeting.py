#!/usr/bin/env python 

import datetime
import logging

GREETING_MESSAGE = """Subject: Happy birthday!

Happy birthday, dear {}!"""


def employees_birthiday_extract(iterable,
                                birthday_on=datetime.datetime.now().strftime('%d/%m')):
    """
    Extracts data from an iterable of Strings following the structure
    `John, Doe, 07/08/1900, john.doe@gmail.com` if the date is today's date.

    This is basically an extract and filter function.

    :param iterable: Strings with the described data structure
    :param birthday_on: optional string for the birthday date formated DD/MM.
    Current date if omited.
    :return: a generator object returning tuples (name, email)
    """
    for employee_data in iterable:
        try:
            first_name, last_name, date_as_string, email\
                = employee_data.strip().split(', ')
        except ValueError:
            logging.error("Unexpected data structure for [>%s<]"
                          % employee_data)
            continue

        if date_as_string[:5] == birthday_on:
            yield first_name, email


def send_email(to: str, title: str, body: str):
    print('Sending email to', to)
    print('Title:', title)
    print('body:', body)
    print('-' * 20)


if __name__ == '__main__':
    FILE_PATH = 'asset/employee.txt'

    with open(FILE_PATH) as employee_file:
        employee_file.readline()

        for name, email in employees_birthiday_extract(employee_file):
            send_email(email, "Joyeux Anniversaire",
                       GREETING_MESSAGE.format(name))

