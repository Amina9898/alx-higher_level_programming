#!/usr/bin/python3
"""This module defines a function that writes into a file"""


def write_file(filename="", text=""):
    """
    function that writes a string to a
    text file (UTF8) and returns the number of characters written
    """
    f = open(filename, 'r+', encoding="utf-8")
    f.read()
    r = f.write(text)
    return r
