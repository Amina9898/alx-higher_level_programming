#!/usr/bin/python3
"""This module defines the print_square function"""


def print_square(size):
    """
    function that prints a square with the character #

    args:
        size: size length of the square
            must be an integer or raises TypeError
            if < 0 raises ValueError
            if float raise TypeError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
