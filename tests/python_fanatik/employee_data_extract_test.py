#!/usr/bin/env python 

from python_fanatik import birthday_greeting as bg


def test_ok_dataset():
    dataset = ["John", "Doe", "12/07/1999", "him@home.com"]

    assert bg.is_employee_birthday(dataset, '12/07')


def test_wrong_data_returns_no_value():
    dataset = ["John", "him@home.com"]

    assert bg.is_employee_birthday(dataset, '12/07') is False


def test_no_current_birthday():
    dataset = ["John", "Doe", "12/07/1999", "him@home.com"]

    assert bg.is_employee_birthday(dataset, '12/08') is False


def test_incorrect_date_format_result_in_false():
    dataset = ["John, Doe, 12/7/1999, him@home.com"]

    assert bg.is_employee_birthday(dataset, '12/07') is False
