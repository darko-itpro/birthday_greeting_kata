#!/usr/bin/env python 

import unittest as ut
from python_fanatik import birthday_greeting as bg


class TestEmployeeDataExtract(ut.TestCase):

    def test_ok_dataset(self):
        dataset = ["John", "Doe", "12/07/1999", "him@home.com"]

        self.assertTrue(bg.is_employee_birthday(dataset, '12/07'))

    def test_wrong_data_returns_no_value(self):
        dataset = ["John", "him@home.com"]

        self.assertFalse(bg.is_employee_birthday(dataset, '12/07'))

    def test_no_current_birthday(self):
        dataset = ["John", "Doe", "12/07/1999", "him@home.com"]

        self.assertFalse(bg.is_employee_birthday(dataset, '12/08'))

    def test_incorrect_date_format_result_in_false(self):
        dataset = ["John, Doe, 12/7/1999, him@home.com"]

        self.assertFalse(bg.is_employee_birthday(dataset, '12/07'))


if __name__ == '__main__':
    pass
