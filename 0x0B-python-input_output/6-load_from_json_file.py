#!/usr/bin/python3
"""
A 6-load_from_json_file module

contains a function that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an Object
    Args:
        filename: file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f)
