import unittest
from unittest.mock import patch
from functions_to_tests import Calculator


class TestForClasses(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator(2,2)
        self.calculator2 = Calculator(-1, 5)
        self.calculator3 = Calculator(0, 2)
        self.calculator4 = Calculator(-1, 0)
        self.calculator5 = Calculator(2, 2)
    def test_add(self):
        self.assertEqual(self.calculator.add(), 4)
        self.assertEqual(self.calculator2.add(), 4)
        self.assertEqual(self.calculator3.add(), 2)
        self.assertEqual(self.calculator4.add(), -1)
    #     self.assertEqual(Calculator.add(3,2), 5)
    #     self.assertEqual(Calculator.add(-1, 5), 4)
    #     self.assertEqual(Calculator.add(-1, -2), -3)
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(), 0)
        self.assertEqual(self.calculator2.subtract(), -6)
        self.assertEqual(self.calculator3.subtract(), -2)
        self.assertEqual(self.calculator4.subtract(), -1)
    #     self.assertEqual(Calculator.subtract(1,2), -1)
    #     self.assertEqual(Calculator.subtract(3,2), 1)
    #     self.assertEqual(Calculator.subtract(0, 2), -2)
    #     self.assertEqual(Calculator.subtract(-1, 0), -1)
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(), 4)
        self.assertEqual(self.calculator2.multiply(), -5)
        self.assertEqual(self.calculator3.multiply(), 0)
        self.assertEqual(self.calculator4.multiply(), 0)
    #     self.assertEqual(Calculator.multiply(1,2), 2)
    #     self.assertEqual(Calculator.multiply(3,2), 6)
    #     self.assertEqual(Calculator.multiply(0, 2), 0)
    #     self.assertEqual(Calculator.multiply(-1, 0), 0)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(), 1)
        self.assertEqual(self.calculator2.divide(), -0.2)
        self.assertEqual(self.calculator3.divide(), 0)
    #     self.assertEqual(self.calculator4.divide(), 0)
    #     self.assertEqual(Calculator.divide(1,2), 0.5)
    #     self.assertEqual(Calculator.divide(4,2), 2)
    #     self.assertEqual(Calculator.divide(0, 2), 0)
    #     self.assertRaises(ZeroDivisionError, Calculator.divide, 5, 0)
    #
    @patch("functions_to_tests.Calculator.multiply")
    def test_with_mock(self, mockMultiply):
        mockMultiply.return_value = 1
        self.assertEqual(self.calculator5.test_for_mock(), 11)