#!/usr/bin/python3
""" A module that contains the lookup function """


def lookup(obj):
    """ returns list of available attributes and methods of an object """
    return dir(obj)
