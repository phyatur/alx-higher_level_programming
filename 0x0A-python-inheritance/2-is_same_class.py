#!/usr/bin/python3
""" A 2-is_same_class that contains a function is_same_class(obj, a_class) """


def is_same_class(obj, a_class):
    """ returns True if the object is an instance of the specified class """
    return type(obj) == a_class
