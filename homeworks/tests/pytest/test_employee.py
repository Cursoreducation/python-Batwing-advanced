import pytest

from employee import Employee

Test_Employee = Employee('Tom', 'York', 40)


def test_email():
    assert Test_Employee.email == 'Tom.York@email.com'
    assert Test_Employee.email != 'Tom@email.com'


def test_fullname():
    assert Test_Employee.fullname == 'Tom York'
    assert Test_Employee.fullname != 'TOmYork'
    assert Test_Employee.fullname in 'Hello is is Tom York'


def test_apply_raise():
    assert Test_Employee.pay == 40
    Test_Employee.apply_raise()
    assert Test_Employee.pay != 55
