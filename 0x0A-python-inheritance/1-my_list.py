#!/usr/bin/python3
""" A module of a class that inherits from list """


class MyList(list):
    """ defines MyList class"""

    def __init__(self):
        """ initializes a new object"""
        pass

    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
