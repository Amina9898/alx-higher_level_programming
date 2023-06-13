#!/usr/bin/python3
""" Module that represents a square. """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class: a subclass of the BaseGeometry class"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
