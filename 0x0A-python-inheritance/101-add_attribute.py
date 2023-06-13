#!/usr/bin/python3
"""defines the add_attribute() function"""


def add_attribute(objec, attrib, value):
    """Add a new attribute to an object if it's possible"""
    if not hasattr(objec, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objec, attrib, value)
