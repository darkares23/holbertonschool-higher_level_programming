#!/usr/bin/python3
""" """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
	""" """
    def test_getter(self):
		""" """
        r1 = Square(5)
        self.assertEqual(r1.size, 5)
    def test_setter(self):
        """ """
		r1 = Square(5)
        r1.size = 8
        self.assertEqual(r1.size, 8)
    def test_string(self):
		""" """
        r1 = Square(3)
        with self.assertRaises(TypeError):
            r1.size = "Hi"
    def test_negative(self):
		""" """
        r1 = Square(6)
        with self.assertRaises(ValueError):
            r1.size = -5
    def test_zero(self):
		""" """
        r1 = Square(6)
        with self.assertRaises(ValueError):
            r1.size = 0
    def test_tupla(self):
		""" """
        r1 = Square(7)
        with self.assertRaises(TypeError):
            r1.size = (2, 8)
    def test_empty(self):
		""" """
        r1 = Square(7)
        with self.assertRaises(TypeError):
            r1.size = ""
    def test_none(self):
		""" """
        r1 = Square(5)
        with self.assertRaises(TypeError):
            r1.size = None
    def test_list(self):
		""" """
        r1 = Square(4)
        with self.assertRaises(TypeError):
            r1.size = [4, 7]
    def test_dict(self):
		""" """
        r1 = Square(5)
        with self.assertRaises(TypeError):
            r1.size = {"hi": 5, "world": 8}
    def test_width(self):
		""" """
        r1 = Square(5)
        r1.size = 6
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 6)

class TestUpdateMethod(unittest.TestCase):
    """Testcases for the square update method"""

    def test_update(self):
		""" """
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

            
if __name__ == "_main_":
   unittest.main()