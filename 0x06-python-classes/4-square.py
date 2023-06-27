#!/usr/bin/python3
""" defines a square based on size"""


class Square:
    """
    class square with private instance attribute size
    """

    def __init__(self, size=0):
        """
        Initializaation of square

        Args:
            size: size of side of square
        """
        self.__size = size

    @property
    def size(self):
        """
        find size
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Checks size value

        Args:
            value: value of size
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        area of square
        Returns:
            the area of the square
        """

        return self.__size ** 2
