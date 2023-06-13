#!/usr/bin/python3
""" Module that represents a Rectangle. """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class: a subclass of the BaseGeometry class"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Magic method prints a message"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
