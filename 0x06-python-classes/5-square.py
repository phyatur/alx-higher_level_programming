#!/usr/bin/python3

""" This module contains a Square class """

class Square:
    """ A square class """
    def __init__(self, size = 0):
        """
        Instantiation Method
        
        Args:
        size (int): the size of the square

        Exceptions:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
    def area(self):
        """
        This method returns the current square area
        
        Return:
        The current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ 
        This method retrieves the private instance attribute size 
        
        Return:
            size (int): the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the private instance attribute size 
        
        Exceptions:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ This method prints in stdout the square with the character # """            
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
            print()