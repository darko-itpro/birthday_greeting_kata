#!/usr/bin/env python 

from clean_classic import birthday_greeting as bg


def test_ok_dataset():
    dataset = ["John, Doe, 12/07/1999, him@home.com"]

    assert len(list(bg.employees_birthiday_extract(dataset, '12/07'))) == 1


def test_wrong_data_returns_no_value():
    dataset = ["John, Doe, 12/07/1999"]

    assert len(list(bg.employees_birthiday_extract(dataset, '12/07'))) == 0

    dataset = ["John, Doe, 12/07/1999, him@home.com, other"]

    assert len(list(bg.employees_birthiday_extract(dataset, '12/07'))) == 0


def test_no_current_birthday_returns_no_value():
    dataset = ["John, Doe, 12/07/1999, him@home.com"]

    assert len(list(bg.employees_birthiday_extract(dataset, '12/08'))) == 0

    dataset = ["John, Doe, 12/07/1999, him@home.com",
               "Jane, Doe, 12/08/1999, him@home.com"]

    assert len(list(bg.employees_birthiday_extract(dataset, '12/08'))) == 1


def test_returned_data_is_firstname_and_email():
    dataset = ["John, Doe, 12/07/1999, him@home.com"]

    first_data, second_data = next(bg.employees_birthiday_extract(dataset,
                                                                  '12/07'))

    assert first_data == 'John'
    assert second_data == 'him@home.com'


def test_incorrect_date_format_result_in_no_value():
    dataset = ["John, Doe, 12/7/1999, him@home.com"]

    assert len(list(bg.employees_birthiday_extract(dataset, '12/07'))) == 0
