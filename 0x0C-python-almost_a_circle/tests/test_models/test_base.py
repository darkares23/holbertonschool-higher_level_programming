#!/usr/bin/python3
"""
Module for unittests for the Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseClassCreation(unittest.TestCase):
    """Test class for Base class instantiation tests"""

    def test_id_positive(self):
        bo = Base(23)
        self.assertEqual(bo.id, 23)
        bo = Base(34)
        self.assertEqual(bo.id, 34)

    def test_id_negative(self):
        bo = Base(-4)
        self.assertEqual(bo.id, -4)
        bo = Base(-10)
        self.assertEqual(bo.id, -10)

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, 1)
        bo = Base(None)
        self.assertEqual(bo.id, 2)
