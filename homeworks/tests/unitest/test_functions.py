import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(245, 5), 250)
        self.assertEqual(Calculator.add(-25, -10), -35)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(245, 5), 240)
        self.assertEqual(Calculator.subtract(-25, -10), -15)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(245, 5), 1225)
        self.assertEqual(Calculator.multiply(-25, -10), 250)

    def test_divide(self):
        self.assertRaises(ValueError, Calculator.divide, 245, 0)
        self.assertEqual(Calculator.divide(6, 2), 3)
