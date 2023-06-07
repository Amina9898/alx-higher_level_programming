#!/usr/bin/python3
"""This module defines the say_ny_name function"""


def say_my_name(first_name, last_name=""):
    """
    This is a function that prints My name is <first name> <last name>
    args:
        first_name: first string
        last_name: second string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
