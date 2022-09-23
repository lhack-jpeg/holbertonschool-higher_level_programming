#!/usr/bin/python3
"""Divides a matrix by a specified number"""


def matrix_divided(matrix, div):
    """
    Function to divide a matrix by a number. Checks to see if
    the matrix is of type list of lists containing only integers
    or floats.
    """

    zero_div_err = "division by zero"
    div_number_err = "div must be a number"
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"
    len_err = 'Each row of the matrix must have the same size'
    if not type(div) in [int, float]:
        raise TypeError(div_number_err)
    if div == 0:
        raise ZeroDivisionError(zero_div_err)
    if not isinstance(matrix, list):
        raise TypeError(matrix_err)
    for array in matrix:
        if type(array) != list:
            raise TypeError(matrix_err)

    array_len = len(matrix[0])
    if array_len == 0:
        raise TypeError(matrix_err)
    for array in matrix:
        if len(array) != array_len:
            raise TypeError(len_err)
        for item in array:
            if type(item) not in [int, float]:
                raise TypeError(matrix_err)
    return [[round(x / div, 2) for x in row] for row in matrix]
