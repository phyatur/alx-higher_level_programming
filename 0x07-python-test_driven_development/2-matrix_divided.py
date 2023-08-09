#!/usr/bin/python3

"""
Module 2-matrix_divided.py
Contains one function,  matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.


    Args:
        mattix: a list of ingeters or floats
        div: divisor


    Returns:
        a new matrix
    """
    
    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    size_check = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of '
                    'integers/floats')
        if size_check == 0:
            size_check = len(row)
        elif size_check != len(row):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(num / div, 2) for num in row] for row in matrix]
