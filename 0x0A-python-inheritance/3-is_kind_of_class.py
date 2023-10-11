#!/usr/bin/python3
""" A 3-is_kind_of_class that contains a function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ returns True if object is an instance of the specified class
        or if object is an instance of a class that inherited
        from the specified class """
    return isinstance(obj, a_class)
