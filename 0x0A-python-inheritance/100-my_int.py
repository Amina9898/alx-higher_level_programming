#!/usr/bin/python3
"""This module defimes MyInt clqass"""


class MyInt(int):
    """Subclass of int"""
    def __eq__(self, value):
        """inverted is equal method"""
        return super().__ne__(value)

    def __ne__(self, value):
        """inverted not equal method"""
        return super().__eq__(value)
