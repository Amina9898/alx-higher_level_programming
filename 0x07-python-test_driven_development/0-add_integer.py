#!/usr/bin/python3
"""This module defines a function"""


def add_integer(a, b=98):
    """
    function that adds 2 integers.

    args:
    a: first int
    b: second int initialised to 98
    return: a+b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
