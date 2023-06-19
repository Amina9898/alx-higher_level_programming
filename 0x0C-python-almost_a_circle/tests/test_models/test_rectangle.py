#!/usr/bin/python3
"""This module is to test the Rectangle class"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases class"""
    def setUp(self):
        """Test class"""
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_set_height(self):
        """Test height setter"""
        self.rectangle.height = 8
        self.assertEqual(self.rectangle.height, 8)

    def test_set_width(self):
        """Test width setter"""
        self.rectangle.width = 9
        self.assertEqual(self.rectangle.width, 9)

    def test_get_width(self):
        """Test width gettter"""
        self.assertEqual(self.rectangle.width, 5)

    def test_get_height(self):
        """Test height getter"""
        self.assertEqual(self.rectangle.height, 10)

    def test_get_x(self):
        self.assertEqual(self.rectangle.x, 2)

    def test_set_x(self):
        self.rectangle.x = 4
        self.assertEqual(self.rectangle.x, 4)

    def test_get_y(self):
        self.assertEqual(self.rectangle.y, 3)

    def test_set_y(self):
        self.rectangle.y = 6
        self.assertEqual(self.rectangle.y, 6)

    def test_id(self):
        self.assertEqual(self.rectangle.id, 1)

if __name__ == '__main__':
    unittest.main()
