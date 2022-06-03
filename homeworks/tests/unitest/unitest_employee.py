import unittest
from employee import Employee
from mock import patch


class TestForClasses(unittest.TestCase):
    def setUp(self):
        self.employee_test = Employee("Tomas", "Yard", 30)

    def test_email(self):
        self.assertEqual(self.employee_test.email, 'Tomas.Yard@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee_test.fullname, 'Tomas Yard')

    def test_aplly_raise(self):
        self.employee_test.apply_raise()
        self.assertEqual(self.employee_test.pay, 31)
#

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.text = 'Good_work'
        self.assertEqual(self.employee_test.monthly_schedule('january'), 'Good_work')
