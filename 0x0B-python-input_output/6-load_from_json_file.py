#!/usr/bin/python3
"""This module defines load_from_json_file function"""


import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a “JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        jdata = f.read()
        obj = json.loads(jdata)
        return obj
