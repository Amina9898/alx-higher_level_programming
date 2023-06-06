#!/usr/bin/python3
"""This is a module that defines a Rectangle class"""


class Rectangle:
    """Represents a class object."""
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0, print_symbol="#"):
        """
        Initializes a new Rectangle.

        Args
            width :The width of the new rectangle
            height: The height of the new rectangle
            print_symbol: building block
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = str(self.print_symbol)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            per = 0
        else:
            per = (self.__width + self.__height) * 2
        return per

    def __str__(self):
        """str to define a string representation of a rectangle"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
