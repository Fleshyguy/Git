import unittest
from calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(10, calc.add(7, 3))

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(15, calc.subtract(30, 15))

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(81, calc.multiply(9, 9))

    def test_divide(self):
        calc = Calculator()
        self.assertEqual(20, calc.divide(100, 5))


if __name__ == '__main__':
    unittest.main()
