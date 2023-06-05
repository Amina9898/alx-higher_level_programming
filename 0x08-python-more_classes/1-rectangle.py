#!/usr/bin/python3
"""This module defines a class rectangle."""


class Rectangle:
    """
    Represents a rectagle.
    """
    def __init__(self, width=0, height=0):
        """Initialises self method and private instance attributes
        width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property to retrieve width aka getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property to retrieve height aka height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
