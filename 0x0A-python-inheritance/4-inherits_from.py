#!/usr/bin/python3
""" Module defines inherits_from() function"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False

    args:
        obj: object to test
        a_class: the class to test against
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
