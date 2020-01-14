#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class test for 6-max_interger.py """

    def test_max_integer_neg(self):
        """ test case for normal list of integers w/ negatives
        """
        test_list = [1, 2, 3, 8, 4, -40, -400, -12, 0]
        self.assertEqual(max_integer(test_list), 8)

    def test_max_integer_(self):
        """ test case for empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """test max_ordered
        """
        self.assertEqual(max_integer([23]), 23)

    def test_max_integer(self):
        """ test case for normal list of integers w/o negatives
        """
        test_list = [1, 2, 3, 8, 4]
        self.assertEqual(max_integer(test_list), 8)

    def test_max_same_number(self):
        """test max_ordered
        """
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_string_list(self):
        """test max_ordered
        """
        with self.assertRaises(TypeError):
            max_integer('hello', 'there')

    def test_string(self):
        """test max_ordered
        """
        self.assertEqual(max_integer("hello"), 'o')

    def test_return_none(self):
        """test max_ordered
        """
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        """test max_ordered
        """
        self.assertEqual(max_integer([.23, 23.43, 44.2]), 44.2)
    
    def test_max_begin(self):
        """test max_ordered
        """
        self.assertEqual(max_integer([50, 23, 44.2]), 50)

if __name__ == '__main__':
    unittest.main()
