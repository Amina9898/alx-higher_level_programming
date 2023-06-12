#usr/bin/python3
"""This module works as a definition for the lookup function"""


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object
    """
    return list(dir(obj))
