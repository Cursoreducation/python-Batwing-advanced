import requests
#
# 1. Create tests for class Calculator (functions_to_test.py)
#     a. Using unittest lib
#     b. Using pytest lib
# 2.* Create tests for class Employee (employee.py) and mock response from "https://company.com"


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

    def monthly_schedule(self, month):
        response = requests.get("http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'