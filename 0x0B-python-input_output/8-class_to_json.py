#!/usr/bin/python3
"""
A 8-class_to_json module

COntains a function that returns the dictionary description
for JSON serialization of an object
"""


def class_to_json(obj):
    """a function that returns the dictionary description
    Args:
        obj: Object
    """
    return obj.__dict__
