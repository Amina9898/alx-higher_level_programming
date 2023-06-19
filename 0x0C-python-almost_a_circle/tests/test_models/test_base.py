#!/usr/bin/python3
"""unittesting the base class"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    
    def test_default_id(self):
        b1 = Base()
        result = b1.id
        self.assertEqual(result, 1)

    def test_increment_id(self):
        b2 = Base()
        b3 = Base()
        result = b3.id
        self.assertEqual(result, 3)

    def test_custom_id(self):
        b4 = Base(6)
        result = b4.id
        self.assertEqual(result, 6)

    def test_multiple_objects(self):
        b5 = Base()
        b6 = Base()
        result = b6.id
        self.assertEqual(result, 5)
