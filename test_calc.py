import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_sum(self):
        result = calc.sum(num_1=5, num_2=10)
        self.assertEqual(result, 15)

    def test_substraction(self):
        result = calc.substraction(num_1=20, num_2=12)
        self.assertEqual(result, 8)

    def test_multiply(self):
        result = calc.multiply(num_1=10, num_2=100)
        self.assertEqual(result, 1000)

    def test_divide(self):
        result = calc.divide(num_1=100, num_2=2)
        self.assertEqual(result, 50)
        