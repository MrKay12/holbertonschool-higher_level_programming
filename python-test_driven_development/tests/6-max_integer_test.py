#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [45]
        self.assertEqual(max_integer(one_element), 45)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.23, 4.69, -7.6875, 12.57, 8.3]
        self.assertEqual(max_integer(floats), 12.57)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.347, 17.5, -9, 1, 16]
        self.assertEqual(max_integer(ints_and_floats), 17.5)

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """Test a string."""
        string = "Bard"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Bard", "has", "meeps"]
        self.assertEqual(max_integer(strings), "meeps")

if __name__ == '__main__':
    unittest.main()
