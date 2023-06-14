#!/usr/bin/python3
"""This module defines the save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        new = json.dumps(my_obj)
        f.write(new)
