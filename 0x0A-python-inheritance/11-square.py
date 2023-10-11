#!/usr/bin/python3
""" A 10-square module that contains a subclass Square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines class Square"""

    def __init__(self, size):
        """ initializes Square  and
        validates size with integer_validator """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ returns unofficial string representation of Square """
        return "[Square] {}/{}".format(self.__size, self.__size)
