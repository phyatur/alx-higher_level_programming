#!/usr/bin/python3


class Square:
    """
    class square with private instance attribute size
    """

    def __init__(self, size=0):
        """
        Args:
            size: size of side of square
        """
        self.__size = size

    @property
    def size(self):
        """
        find size
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

    def my_print(self):
        """
        prints square with character #
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("#" * self.__size)
        return
