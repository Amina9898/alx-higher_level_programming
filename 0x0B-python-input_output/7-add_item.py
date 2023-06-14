#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then save them to a file
"""


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv

args[0] = "7-add_item.py"

cmd_args = args[1:]

with open("add_item.json", 'w', encoding="utf-8")as f:
    f.write(json.dumps(cmd_args))

new_args = load_from_json_file("add_item.json")

save_to_json_file(new_args, "add_item.json")
