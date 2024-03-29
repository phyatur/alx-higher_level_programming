#!/usr/bin/python3
"""
A 5-save_to_json_file module

contains a function that that writes an Object to a text file, using a JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation
    Args:
        my_obj: python onject
        filename: file
    Return:
        a text file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
