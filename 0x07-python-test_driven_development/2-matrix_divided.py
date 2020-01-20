#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
Matrix must be a list of lists of integers or floats
Otherwise raise a TypeError.
Each row of the matrix must be of the same size
Otherwise raise a TypeError
div must be a number (integer or float)
Otherwise raise a TypeError
div can’t be equal to 0
Otherwise raise a ZeroDivisionError
All elements of the matrix should be divided by div
Rounded to 2 decimal places
Returns a new matrix
"""


def matrix_divided(matrix, div):
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")
    copy = 0
    for x in matrix:
        if copy != 0 and len(x) != copy:
            raise TypeError('Each row of the matrix must have the same size')
        lrow = []
        for row in matrix:
            lrow.append(len(row))
        if not all(elem == lrow[0] for elem in lrow):
            raise TypeError("Each row of the matrix must have the same size")
            if type(y) != int and type(y) != float:
                raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError('Each row of the matrix must have the same size')
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrixdiv = [[round(x / div, 2) for x in row] for row in matrix]
    return matrixdiv

