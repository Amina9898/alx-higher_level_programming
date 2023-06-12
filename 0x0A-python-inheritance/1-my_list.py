#!/usr/bin/python3
"""This module defines the print_sorted() function"""

class MyList(list):
    """Defines MyList class that inherits from list class"""
    def __init__(self):
        """Initialise self"""
        list.__init__(self)

    def print_sorted(self):
        """
        Public instance method that prints the list,
        but sorted (ascending sort)
        """
        listt = sorted(self)
        print(listt)

