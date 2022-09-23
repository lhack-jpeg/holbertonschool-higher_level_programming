#!/usr/bin/python3
'''
Unit test module to check for largest int
'''

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Should be 4")

    def test_negative(self):
        self.assertEqual(max_integer([-999, -100, -101, -1]), -1,
                         "Should be -1")

    def test_all_same(self):
        self.assertEqual(max_integer([1, 1, 1, 1, 1, 1]), 1, "Should be 1")

    def test_right_type(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "Hello"])

    def test_func_no_args(self):
        self.assertIsNone(max_integer())

    def test_list_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_max_at_start(self):
        self.assertEqual(max_integer([100, 99, 1, 2]), 100, "Should be 100")

    def test_max_in_middle(self):
        self.assertEqual(max_integer([100, 99, 150, 1, 2]), 150,
                         "Should be 150")

    def test_list_of_one(self):
        self.assertEqual(max_integer([1]), 1, "should be 1")

    def test_list_one_neg(self):
        self.assertEqual(max_integer([-1]), -1, "should be -1")


if __name__ == '__main__':
    unittest.main()
