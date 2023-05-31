#!/usr/bin/python3
"""This module is to write a class object Square"""


class Square:
    """Represents Square"""
    def __init__(self, size=0):
        """Initialize self method and size attribute"""
        self.__size = size

    @property
    def size(self):
        """property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Preperty setter"""
        self.value = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """public instance methed that return square area"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """
        public instance methed that prints in stdout the square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__size != 0:
                    for i in range(self.__size):
                        print("#", end="")
                print()
