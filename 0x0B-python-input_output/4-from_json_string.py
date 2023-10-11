#!/usr/bin/python3
"""
Module 4-from_json_string

contains a function that returns an object from a JSON string
"""
import json


def from_json_string(my_str):
    """A function that returns an object from a JSON string
    Args:
        my_str: json strinf
    Return:
        a python object
    """
    return json.loads(my_str)
