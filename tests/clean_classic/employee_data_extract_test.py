#!/usr/bin/env python 

import unittest as ut
from clean_classic import birthday_greeting as bg


class TestEmployeeDataExtract(ut.TestCase):

    def test_ok_dataset(self):
        dataset = ["John, Doe, 12/07/1999, him@home.com"]

        self.assertTrue(len(list(bg.employees_birthiday_extract(dataset,
                                                                '12/07'))) == 1)

    def test_wrong_data_returns_no_value(self):
        dataset = ["John, Doe, 12/07/1999"]

        self.assertTrue(len(list(bg.employees_birthiday_extract(dataset,
                                                                '12/07'))) == 0)

        dataset = ["John, Doe, 12/07/1999, him@home.com, other"]

        self.assertTrue(len(list(bg.employees_birthiday_extract(dataset,
                                                                '12/07'))) == 0)

    def test_no_current_birthday_returns_no_value(self):
        dataset = ["John, Doe, 12/07/1999, him@home.com"]

        self.assertTrue(len(list(bg.employees_birthiday_extract(dataset,
                                                                '12/08'))) == 0)

        dataset = ["John, Doe, 12/07/1999, him@home.com",
                   "Jane, Doe, 12/08/1999, him@home.com"]

        self.assertTrue(len(list(bg.employees_birthiday_extract(dataset,
                                                                '12/08'))) == 1)

    def test_returned_data_is_firstname_and_email(self):
        dataset = ["John, Doe, 12/07/1999, him@home.com"]

        first_data, second_data = next(bg.employees_birthiday_extract(dataset,
                                                                      '12/07'))

        self.assertEqual(first_data, 'John')
        self.assertEqual(second_data, 'him@home.com')

    def test_incorrect_date_format_result_in_no_value(self):
        dataset = ["John, Doe, 12/7/1999, him@home.com"]

        self.assertTrue(len(list(bg.employees_birthiday_extract(dataset,
                                                                '12/07'))) == 0)


if __name__ == '__main__':
    pass