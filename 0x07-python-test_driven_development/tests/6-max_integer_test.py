#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class defines several test cases"""
    def test_max_integer(self):
        """Return max integer in a list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 8, 6]), 8)
        self.assertEqual(max_integer([7, 0, 6]), 7)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-1, -2, 0, -4]), 0)
        self.assertEqual(max_integer([-2, -5, -3, -4]), -2)

    def test_types(self):
        """Test types"""
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, [5, None, 6])
        self.assertRaises(TypeError, max_integer, [5, 7, 6], None)

    def test_empty_excess_input(self):
        """Test empty and excess input"""
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))
        self.assertRaises(TypeError, max_integer, [1, 2], [2, 9])


if __name__ == "__main__":
    unittest.main()
