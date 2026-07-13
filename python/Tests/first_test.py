import unittest
from . import first


class TestCalculations(unittest.TestCase):
    def test_sum(self):
        calculation = first.calculations(8, 2)
        self.assertEqual(calculation.add(), 10, 'the sum is wrong')

    def test_sub(self):
        calculation = first.calculations(8,2)
        self.assertEqual(calculation.sub(), 6, "test case failed")

    def test_mul(self):
        calculation=first.calculations(8,2)
        self.assertEqual(calculation.multiply(), 16, "executed correctly")

    def test_divide(self):
        calculation = first.calculations(10, 2)
        self.assertEqual(calculation.divide(), 5)

        calculation = first.calculations(15, 3)
        self.assertEqual(calculation.divide(), 5)

        with self.assertRaises(ZeroDivisionError):
            first.calculations(10, 0).divide()