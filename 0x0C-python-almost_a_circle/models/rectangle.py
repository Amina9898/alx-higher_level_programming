#!/usr/bin/python3
"""Defines the rectangle class"""


from models.base import Base


class Rectangle(Base):
    """creates Rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be a > 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be a non-negative number.")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be a non-negative number.")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__y = value
