#!/usr/bin/python3
"""
A base module

Contains a class Base
"""


class Base:
    """ A base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the class """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb.objects
        else:
            self.id = id
