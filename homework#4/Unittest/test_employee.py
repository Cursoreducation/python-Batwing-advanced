import unittest
from unittest.mock import patch
from employee import Employee

class TestForClasses(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee("yura","tsap", 100)

    def test_email(self):
        self.assertEqual(f"{self.emp1.first}.{self.emp1.last}@email.com", self.emp1.email, msg=None)

    def test_fullname(self):
        self.assertEqual(f'{self.emp1.first} {self.emp1.last}', self.emp1.fullname, msg=None)

    def test_aplly_raise(self):
        self.assertEqual(Employee.raise_amt * self.emp1.pay, 105, msg=None)

    def test_aplly_raise2(self):
        self.assertEqual(self.emp1.apply_raise(), 105)