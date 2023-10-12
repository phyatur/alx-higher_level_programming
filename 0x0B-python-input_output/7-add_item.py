#!/usr/bin/python3
"""
A 7-add_item module

Contains functions that adds all arguments to a Python list,
and then save them to a file
"""
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
my_list = load_from_json_file(filename)
for arg in argv[1:]:
    my_list.append(arg)
save_to_json_file(my_list, filename)
