#!/usr/bin/python3
""" A 3-to_json_string module that contains to_json_string.py function """
import json


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an object """
    return json.dumps(my_obj)
