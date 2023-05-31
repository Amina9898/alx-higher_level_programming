#!/usr/bin/python3
"""This module is to write a class object Square"""


class Square:
    """Represents Square"""
    def __init__(self, size=0):
        """Initialize self method and size attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method that returns the current square area"""
        return int(self.__size) * int(self.__size)
