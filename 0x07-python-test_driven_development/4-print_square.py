#!/usr/bin/python3

"""
Module 4-print_square.py
Contains one function, print_square(size)
"""


def print_square(size):
    """
    A function that prints a square with the character #
    

    Args:
        size: the size length of the square


    Returns:
        a square of #
    """
    
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        print('#' * size)
