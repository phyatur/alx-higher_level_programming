#!/usr/bin/python3
""" A square class definition """


class Square:
    """ A square class with private attribute size

    Args:
        size: size of square

    """


    def __init__(self, size=0):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")


    def area(self):
        """ Area of a square

        Returns:
            the current square area 
        """
        return self.__size * self.__size

 
    @property
    def size(self):
        """ Size of square

        Returns:
            size of square
        """
        return self.__size


    @size.setter
    def size(self, value):
        """ Set size of square

        Args:
            value: value to set for size 
        """
        if type(value) is int:
            if value < 0:
