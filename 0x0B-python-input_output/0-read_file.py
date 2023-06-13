#!/usr/bin/python3
""" Moduke defines a function that reads files. """


def read_file(filename=""):
    """
    function that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    print(read_data, end="")
