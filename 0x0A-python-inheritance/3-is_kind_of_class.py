#!/usr/bin/python3
""" Module defines is_kind_of_class() function"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False

    args:
        obj: object to test
        a_class: the class to test against
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
