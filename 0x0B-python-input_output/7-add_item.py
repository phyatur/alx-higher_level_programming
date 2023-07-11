#!/usr/bin/python3
""" add_item function """
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    the_list = load_from_json_file(filename)
except FileNotFoundError:
    the_list = []
for arg in argv[1:]:
    the_list.append(arg)
save_to_json_file(the_list, filename)
