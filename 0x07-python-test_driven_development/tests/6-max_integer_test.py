#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test for '6-max_integer.py'
    """

    def test_normal(self):
        """ Testing if it works """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 3, 4, 2]), 10)

    def test_negative(self):
        """ Testing negatives """
        self.assertEqual(max_integer([-1, -2, -2]), -1)
        self.assertEqual(max_integer([-10, -3, -4]), -3)

    def test_float(self):
        """ Testing floats """
        self.assertEqual(max_integer([1.5, 2.9, 3.66]), 3.66)
        self.assertEqual(max_integer([10.90, 9.67 , 8.5]), 10.90)

    def test_stringd(self):
        """ Testing Strings """
        self.assertEqual(max_integer(['python', 'zen', 'of']), 'zen')

    def test_empty(self):
        """ Testing empty list """
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__': 
    unittest.main()
