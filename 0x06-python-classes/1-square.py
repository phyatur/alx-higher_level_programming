#!/usr/bin/python3
""" square based on size definition """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size):
        
        """
        Args:
            size: size of square
        """

        self.__size = size
