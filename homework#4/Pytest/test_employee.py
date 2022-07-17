from employee import Employee
import pytest
from classes import ClassForTest

el = Employee("yura", "tsap", 100)
def test_email():
    assert el.email == 'yura.tsap@email.com'

def test_fullname():
    assert el.fullname == 'yura tsap'

def test_apply_raise():
    assert el.pay*el.raise_amt == 105


def test_request(requests_mock):
    requests_mock.get(
        "https://company.com", text="data", status_code=200
    )
    classForTest = ClassForTest()
    assert classForTest.send_request().ok
    assert classForTest.send_request().status_code == 200