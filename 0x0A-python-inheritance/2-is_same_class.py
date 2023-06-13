#!/usr/bin/python3
"""Module defines a is_same_class functiom"""

def is_same_class(obj, a_class):
    """
    function that returns True
    if the object is exactly an instance of
    the specified class ; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    if not isinstance(obj, a_class):
        return False
