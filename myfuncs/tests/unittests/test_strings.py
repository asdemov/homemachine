import unittest
from myfuncs.strfuncs.strings import *


class TestIsint(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(is_int(5), True)

    def test_negative_numbers(self):
        self.assertEqual(is_int(-3), True)

    def test_zero_numbers(self):
        self.assertEqual(is_int(0), True)

    def test_positive_real_numbers(self):
        self.assertEqual(is_int(0.56), False)

    def test_negative_real_numbers(self):
        self.assertEqual(is_int(-0.56), False)


if __name__ == '__main__':
    unittest.main()
