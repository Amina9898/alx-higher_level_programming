#!/usr/bin/python3
""" Module that represents a Rectangle. """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """ Square class: a subclass of the BaseGeometry class"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
