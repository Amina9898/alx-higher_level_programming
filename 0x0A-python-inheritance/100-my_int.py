#!/usr/bin/python3
"""This module defimes MyInt clqass"""


class MyInt(int):
    """Subclass of int"""
    def __eq__(self, value):
        """inverted is equal method"""
        if value:
            return False
        return True

    def __ne__(self, value):
        """inverted not equal method"""
        if not value:
            return False
        return True
