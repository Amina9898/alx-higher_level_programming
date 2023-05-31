#!/usr/bin/bash
"""This is a module for a class Square that defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize self methed and private intance attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
