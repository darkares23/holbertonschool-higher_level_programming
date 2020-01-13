#!/usr/bin/python3
"""
Divide matrix module
"""


def matrix_divided(matrix, div):
    """Function divides elements of a matrix"""

    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, type([])):
        raise TypeError(matrix_err)

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    for list in matrix:
        if len(list) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    for list in matrix:
        for item in list:
            if not isinstance(item, (float, int)):
                raise TypeError(matrix_err)
            if any([item == float('inf'), item == float('nan')]):
                raise TypeError(matrix_err)

    return([[round((item / div), 2) for item in row] for row in matrix])
