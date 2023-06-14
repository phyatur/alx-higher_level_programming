#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = matrix[:]
    length = len(matrix)
    for i in range(length):
        for j in range(len(matrix[i][:])):
            square[i][j] **= 2
    return square
