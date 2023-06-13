#!/usr/bin/python3
"""Module represents a class"""


class BaseGeometry:
    """Class"""

    def area(self):
        """Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        if value is not an integer: raise a TypeError
        if value is less or equal to 0: raise a ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
